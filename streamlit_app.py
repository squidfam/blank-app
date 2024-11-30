import streamlit as st
import pandas as pd
import numpy as np
import sklearn

from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from pandas.api.types import infer_dtype

def run_AI(academic_interest,skills,location,year_of_study,major,GPA,languages,research_interest):
    
    url = "https://raw.githubusercontent.com/noahvezina26/student-extracurriculars/refs/heads/main/student_data.csv"

    # Load and preprocess training data
    df = pd.read_csv(url)

    # Drop unnecessary columns
    df.drop("StudentID", axis=1, inplace=True, errors="ignore")
    df.drop("Name", axis=1, inplace=True, errors="ignore")
    df.drop("ExtracurricularActivites", axis=1, inplace=True, errors="ignore")

    column_order = [
        "Location",
        "YearOfStudy",
        "Major",
        "GPA",
        "AcademicInterest",
        "ResearchInterests",
        "Skills",
        "Languages",
        "ClubMemberships",
    ]

    df = df[column_order]

    # Define feature types
    categorical_features = ["AcademicInterest", "Location", "YearOfStudy", "Major", "ResearchInterests"]
    multi_categorical_features = ["Skills", "Languages", "ClubMemberships"]

    # Initialize encoders
    mlb = sklearn.preprocessing.MultiLabelBinarizer()
    ohe = sklearn.preprocessing.OneHotEncoder(dtype=int, sparse_output=False)

    # Encode multi-categorical features
    for feature in multi_categorical_features:
        if infer_dtype(df[feature]) == "string":
            df[feature] = df[feature].str.split(", ")
        encoded = mlb.fit_transform(df[feature])
        encoded_df = pd.DataFrame(encoded, columns=mlb.classes_)
        df = pd.concat([df, encoded_df], axis=1)
        df.drop(feature, axis=1, inplace=True)
        if feature == "ClubMemberships":
            target = encoded_df

    # Encode other categorical features
    for feature in categorical_features:
        encoded = ohe.fit_transform(df[[feature]])
        encoded_df = pd.DataFrame(encoded, columns=ohe.get_feature_names_out([feature]))
        df = pd.concat([df, encoded_df], axis=1)
        df.drop(feature, axis=1, inplace=True)

    # Define features and target
    X = df[[feature for feature in df.columns if feature not in target.columns]]
    y = target

    # Train model with RandomizedSearchCV
    model = MultiOutputClassifier(RandomForestClassifier())
    param_dist = {
        'estimator__n_estimators': np.arange(100, 500, 50),
        'estimator__max_depth': [None, 10, 20, 30],
        'estimator__min_samples_split': [2, 5, 10],
        'estimator__min_samples_leaf': [1, 2, 4],
        'estimator__max_features': ['sqrt', 'log2']
    }
    random_search = RandomizedSearchCV(estimator=model, param_distributions=param_dist, n_iter=10, cv=3, random_state=42, n_jobs=-1, verbose=2, error_score="raise")
    random_search.fit(X, y)

    best_model = random_search.best_estimator_

    # Prepare the input data (user input)
    input_data = pd.DataFrame({
        "Location": [location],
        "YearOfStudy": [year_of_study],
        "Major": [major],
        "GPA": [GPA],
        "AcademicInterest": [academic_interest],
        "ResearchInterests": [research_interest],
        "Skills": [skills],  # Assuming `skills` is a comma-separated string
        "Languages": [languages],  # Assuming `languages` is a comma-separated string
    })

    # Encode the input data using the same encoding process
    for feature in multi_categorical_features:
        if infer_dtype(input_data[feature]) == "string":
            input_data[feature] = input_data[feature].str.split(", ")
        encoded = mlb.transform(input_data[feature])  # Use the fitted transformer
        encoded_df = pd.DataFrame(encoded, columns=mlb.classes_)
        input_data = pd.concat([input_data, encoded_df], axis=1)
        input_data.drop(feature, axis=1, inplace=True)

    for feature in categorical_features:
        encoded = ohe.transform(input_data[[feature]])  # Use the fitted transformer
        encoded_df = pd.DataFrame(encoded, columns=ohe.get_feature_names_out([feature]))
        input_data = pd.concat([input_data, encoded_df], axis=1)
        input_data.drop(feature, axis=1, inplace=True)

    # Ensure the input data has the same columns as the training data
    input_data = input_data[[col for col in X.columns]]

    # Make predictions
    y_pred = best_model.predict(input_data)

    return y_pred


start_count = 0

st.title("What club should you be in? (AI_Lab project)")

st.write(
    "Hello and welcome to Team 1's project!"
)

st.write("For more information on this project, check out our [Gituh repo](https://github.com/noahvezina26/student-clubs-ml)."
)

academic_interest = st.multiselect(
    "What are your academic interests?",
    ['Psychology','History','Computer Science','Biology','Mathematics','Physics'],
)

if len(academic_interest) > 1 or len(academic_interest) == 0:
    st.markdown(":red[Error: Please make sure you select one option]")
else:
    start_count += 1

skills = st.multiselect(
    "What are your skills?",
    ['Problem Solving','Leadership','Public Speaking','Data Analysis','Programming','Artistic'],
)

if len(skills) == 0:
    st.markdown(":red[Error: Please make sure you select one option]")
else:
    start_count += 1

location = st.multiselect(
    "Where do you live?",
    ['New York','Boston','Chicago','Houston','Los Angeles','San Francisco'],
)

if len(location) > 1 or len(location) == 0:
    st.markdown(":red[Error: Please make sure you select one option]")
else:
    start_count += 1

year_of_study = st.multiselect(
    "What is your current year of study?",
    ['Freshman','Graduate','Junior','Senior','Sophomore'],
)

if len(year_of_study) > 1 or len(year_of_study) == 0:
    st.markdown(":red[Error: Please make sure you select one option]")
else:
    start_count += 1

major = st.multiselect(
    "What is your Major?",
    ['Psychology','Physics','Biology','Computer Science','History','Mathematics'],
)

if len(major) > 1 or len(major) == 0:
    st.markdown(":red[Error: Please make sure you select one option]")
else:
    start_count += 1

GPA = st.slider(
    "What is your GPA?",
    2.0,
    4.0,
    2.0
)

start_count += 1

languages = st.multiselect(
    "What languages do you speak (english is assumed)?",
    ['Chinese','Japanese','Spanish','German','French'],
)
start_count += 1

if len(languages) == 0:
    st.markdown(":red[Error: Please make sure you select one option]")
else:
    start_count += 1

research_interest = st.multiselect(
    "what is your research interest?",
    ['Biomedical Engineering','Urban Planning','Nanotechnology','Space Exploration','Climate Change','Machine Learning','Cybersecurity','Environmental Sustainability','Bioinformatics','Social Sciences','Quantum Computing','Cognitive Psychology','Robotics','Blockchain Technology','Astrophysics','Educational Technology','Data Science','Artificial Intelligence','Renewable Energy','Human-Computer Interaction','Behavioral Economics','Healthcare Management','Political Science','Natural Language Processing','Sustainable Agriculture'],
)

if len(research_interest) > 1 or len(research_interest) == 0:
    st.markdown(":red[Error: Please make sure you select one option]")
else:
    start_count += 1

st.button("Reset", type="primary")
if st.button("Run AI") and start_count == 8:
    output = run_AI(academic_interest,skills,location,year_of_study,major,GPA,languages,research_interest)
elif start_count != 8:
    st.markdown(":red[Error: Please make sure you've inputted everything correctly!]")

st.write("You should go into", output)
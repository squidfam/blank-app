import streamlit as st

def run_AI(academic_interest,skills,location,year_of_study,major,GPA,languages,research_interest):
    pass

start_count = 0

st.title("What club should you be in? (AI_Lab project)")

st.write(
    "Hello and welcome to Team 1's project! Please select one choice per question unless otherwise specified."
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
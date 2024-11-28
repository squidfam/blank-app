import streamlit as st

start = False
st.title("What club should you be in? (AI_Lab project)")

st.write(
    "Hello and welcome to Team 1's project! Please select one choice per question unless otherwise specified."
)
st.write("For more information on this project, check out our [Gituh repos](https://github.com/noahvezina26/student-clubs-ml)."
)
academic_interest = st.multiselect(
    "what is your academic interest?",
    ['Psychology','History','Computer Science','Biology','Mathematics','Physics'],
)
if len(academic_interest) > 1 or len(academic_interest) == 0:
    start = False
    st.markdown(":red[error: Please make sure you select one option]")
start = True
skills = st.multiselect(
    "what are your skills?",
    ['Problem Solving','Leadership','Public Speaking','Data Analysis','Programming','Artistic'],
)
if len(skills) == 0:
    start = False
    st.markdown(":red[error: Please make sure you select one option]")
start = True
location = st.multiselect(
    "where do you live?",
    ['New York','Boston','Chicago','Houston','Los Angeles','San Francisco'],
)
if len(location) > 1 or len(location) == 0:
    start = False
    st.markdown(":red[error: Please make sure you select one option]")
start = True
year_of_study = st.multiselect(
    "what is your current year of study?",
    ['Freshman','Graduate','Junior','Senior','Sophomore'],
)
if len(year_of_study) > 1 or len(year_of_study) == 0:
    start = False
    st.markdown(":red[error: Please make sure you select one option]")
start = True
major = st.multiselect(
    "what is your Major?",
    ['Psychology','Physics','Biology','Computer Science','History','Mathematics'],
)
if len(major) > 1 or len(major) == 0:
    start = False
    st.markdown(":red[error: Please make sure you select one option]")
start = True
GPA = st.slider(
    "what is your GPA?",
    2.0,
    4.0,
    2.0
)

languages = st.multiselect(
    "what Languages do you speak (english is assumed)?",
    ['Chinese','Japanese','Spanish','German','French'],
)
if len(languages) == 0:
    start = False
    st.markdown(":red[error: Please make sure you select one option]")
start = True
research_interest = st.multiselect(
    "what is your research interest?",
    ['Biomedical Engineering','Urban Planning','Nanotechnology','Space Exploration','Climate Change','Machine Learning','Cybersecurity','Environmental Sustainability','Bioinformatics','Social Sciences','Quantum Computing','Cognitive Psychology','Robotics','Blockchain Technology','Astrophysics','Educational Technology','Data Science','Artificial Intelligence','Renewable Energy','Human-Computer Interaction','Behavioral Economics','Healthcare Management','Political Science','Natural Language Processing','Sustainable Agriculture'],
)
if len(research_interest) > 1 or len(research_interest) == 0:
    start = False
    st.markdown(":red[error: Please make sure you select one option]")
start = True
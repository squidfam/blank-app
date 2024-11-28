import streamlit as st

st.title("What club should you be in? (AI_Lab project)")

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
academic_interests = st.multiselect(
    "what is your academic interest?",
    ['Psychology','History','Computer Science','Biology','Mathematics','Physics'],
)

skills = st.multiselect(
    "what are your skills?",
    ['Problem Solving','Leadership','Public Speaking','Data Analysis','Programming','Artistic'],
)

location = st.multiselect(
    "where do you live?",
    ['New York','Boston','Chicago','Houston','Los Angeles','San Francisco'],
)

year_of_study = st.multiselect(
    "what is your current year of study?",
    ['Freshman','Graduate','Junior','Senior','Sophomore'],
)

major = st.multiselect(
    "what is your Major?",
    ['Psychology','Physics','Biology','Computer Science','History','Mathematics'],
)

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

research_interest = st.multiselect(
    "what is your research interest?",
    ['Biomedical Engineering','Urban Planning','Nanotechnology','Space Exploration','Climate Change','Machine Learning','Cybersecurity','Environmental Sustainability','Bioinformatics','Social Sciences','Quantum Computing','Cognitive Psychology','Robotics','Blockchain Technology','Astrophysics','Educational Technology','Data Science','Artificial Intelligence','Renewable Energy','Human-Computer Interaction','Behavioral Economics','Healthcare Management','Political Science','Natural Language Processing','Sustainable Agriculture'],
)
SKILLS={"python","sql","machine learning","deep learning","natural language processing","nlp","pandas","numpy","scikit-learn","tensorflow","pytorch","streamlit","tableau","power bi","excel","matplotlib","seaborn","statistics","data analysis","data visualization","eda","git","github","docker","aws","flask","django","react","javascript","html","css"}

def extract_skills(text):
    text=text.lower()
    return sorted([skill for skill in SKILLS if skill in text])

def find_skill_gaps(required_skills,candidate_skills):
    return sorted(set(required_skills)-set(candidate_skills))

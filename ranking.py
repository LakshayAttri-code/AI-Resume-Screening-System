import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(job_description,resumes):
    texts=[job_description]+[r["text"] for r in resumes]
    vectorizer=TfidfVectorizer(stop_words="english",ngram_range=(1,2))
    matrix=vectorizer.fit_transform(texts)
    scores=cosine_similarity(matrix[0:1],matrix[1:]).flatten()
    results=[]
    for resume,score in zip(resumes,scores):
        results.append({"name":resume["name"],"text":resume["text"],"match_score":score*100})
    return pd.DataFrame(results).sort_values("match_score",ascending=False).reset_index(drop=True)

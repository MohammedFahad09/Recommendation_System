import numpy as np
from sklearn.metrics.pairwise import linear_kernel

def recommend_similar(book_title, df, tfidf_matrix, title_to_index, top_n=5):
    
    if book_title not in title_to_index:
        return []
    
    idx = title_to_index[book_title]
    
    scores = linear_kernel(tfidf_matrix[idx], tfidf_matrix).flatten()
    
    top_indices = np.argpartition(scores, -50)[-50:]
    top_indices = sorted(top_indices, key=lambda i: scores[i], reverse=True)
    
    results = []
    
    for i in top_indices[1:top_n+1]:
        results.append({
            "title": df.iloc[i]["title"],
            "rating": float(df.iloc[i]["average_rating"])
        })
    
    return results
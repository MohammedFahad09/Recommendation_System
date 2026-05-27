def recommend_by_genre(df, user_genres, top_n=10):
    
    user_genres_set = set(user_genres.lower().split())
    
    filtered = df[df["genre"].apply(
        lambda x: len(user_genres_set & set(x.split())) > 0
    )].copy()
    
    if filtered.empty:
        return []
    
    filtered["match_score"] = filtered["genre"].apply(
        lambda x: len(user_genres_set & set(x.split()))
    )
    
    filtered = filtered.sort_values(
        by=["match_score", "average_rating", "ratings_count"],
        ascending=False
    )
    
    return filtered.head(top_n).to_dict(orient="records")
def recommend_from_image(input_data, model_data):
    
    from utils.ocr import extract_text
    from utils.matching import find_best_match
    from utils.recommender import recommend_similar
    
    # 🔹 handle both image and text
    if isinstance(input_data, str):
        text = input_data.lower()
    else:
        text = extract_text(input_data)
    
    matched_title = find_best_match(text, model_data["titles"])
    
    if not matched_title:
        return {"error": "No book detected"}
    
    recommendations = recommend_similar(
        matched_title,
        model_data["df"],
        model_data["tfidf_matrix"],
        model_data["title_to_index"]
    )
    
    return {
        "detected_book": matched_title,
        "recommendations": recommendations
    }







# from utils.ocr import extract_text
# from utils.matching import find_best_match
# from utils.recommender import recommend_similar

# def recommend_from_image(image, model_data):
    
#     text = extract_text(image)
    
#     matched_title = find_best_match(text, model_data["titles"])
    
#     if not matched_title:
#         return {"error": "No book detected"}
    
#     recommendations = recommend_similar(
#         matched_title,
#         model_data["df"],
#         model_data["tfidf_matrix"],
#         model_data["title_to_index"]
#     )
    
#     return {
#         "detected_book": matched_title,
#         "recommendations": recommendations
#     }
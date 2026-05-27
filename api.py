from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import pickle
from scipy.sparse import load_npz

from utils.genre_recommender import recommend_by_genre
from services.recommendation_service import recommend_from_image

app = FastAPI(title="Book Recommender API")


# ---------------- LOAD MODEL ---------------- #

def load_model():
    with open("model/metadata2.pkl", "rb") as f:
        data = pickle.load(f)
    
    tfidf_matrix = load_npz("model/tfidf2_matrix.npz")
    
    return {
        "df": data["df"],
        "titles": data["titles"],
        "title_to_index": data["title_to_index"],
        "tfidf_matrix": tfidf_matrix
    }

model = load_model()
df = model["df"]


# ---------------- REQUEST SCHEMA ---------------- #

class GenreRequest(BaseModel):
    genres: str


class TextRequest(BaseModel):
    text: str


# =====================================================
# 🎯 GENRE ENDPOINT
# =====================================================

@app.post("/recommend/genre")
def recommend_genre(req: GenreRequest):
    
    results = recommend_by_genre(df, req.genres)
    
    return {
        "input_genres": req.genres,
        "results": results
    }


# =====================================================
# 📸 IMAGE ENDPOINT
# =====================================================

@app.post("/recommend/image")
async def recommend_image(file: UploadFile = File(...)):
    
    result = recommend_from_image(file.file, model)
    
    return result


# =====================================================
# ✍️ TEXT (BACKUP)
# =====================================================

@app.post("/recommend/text")
def recommend_text(req: TextRequest):
    
    result = recommend_from_image(req.text, model)
    
    return result


# =====================================================
# ROOT
# =====================================================

@app.get("/")
def root():
    return {"message": "Book Recommender API is running 🚀"}
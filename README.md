# 📚 Image-Based Personalized Book Recommendation System

## Project Description

This project is an AI-powered Book Recommendation System that recommends books based on images uploaded by users.

The system extracts text from the uploaded image using OCR (Optical Character Recognition), identifies the closest matching book title, and recommends similar books using content-based filtering techniques.

The recommendation engine uses TF-IDF vectorization and similarity calculations to generate personalized suggestions.

This project aims to improve book discovery by providing intelligent recommendations from visual input instead of manual searching.

---

# 🛠 Technology Stack and Tools Used

## Backend
- Python
- FastAPI

## Machine Learning / Data Processing
- Scikit-learn
- Pandas
- NumPy
- SciPy

## Image Processing
- OCR (Tesseract OCR)
- Pillow (PIL)

## Model Files
- TF-IDF
- Sparse Matrix (.npz)
- Metadata (.pkl)

## Development Tools
- Jupyter Notebook
- VS Code
- GitHub

---

# ✨ Features and Functionalities Implemented

### 📷 Image Upload
Users can upload an image containing a book cover or book title.

### 🔍 OCR-Based Text Extraction
Extracts text from uploaded images.

### 📚 Intelligent Book Matching
Matches extracted text with existing book metadata.

### 🤖 Recommendation Engine
Generates recommendations using:
- TF-IDF Vectorization
- Cosine Similarity

### ⚡ Fast API Backend
Provides REST API endpoints for recommendations.

### 🧠 Metadata-Based Recommendation
Uses stored metadata and trained model files for efficient recommendations.

---

# 📂 Project Structure

```plaintext
book-recommender/
│
├── app.py
│
├── model/
│   ├── tfidf.pkl
│   ├── tfidf_matrix.npz
│   ├── metadata.pkl
│   ├── model_training.ipynb
│
├── utils/
│   ├── ocr.py
│   ├── matching.py
│   ├── recommender.py
│   ├── genre_recommender.py
│
├── services/
│   └── recommendation_service.py
│
├── data/
│
├── requirements.txt
└── README.md

Student Name:- Mohd fahad
Enrollment No. :- En23cs301629

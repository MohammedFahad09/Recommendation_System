
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# ---------------- UI ---------------- #

st.set_page_config(page_title="Book Recommendation", layout="wide")

st.title("📚 Image Book Recommendation System")
st.write("Interface for recommending books")

st.divider()

# ---------------- NAVIGATION ---------------- #

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Genre Recommendation", "Image Based Recommendation"]
)

# ---------------- HOME ---------------- #

if page == "Home":
    st.header("Welcome")

    st.write("""
    This system recommends books based on:

    - Book similarity
    - Genre preference
    - AI recommendation model
    """)

    st.image("https://images.unsplash.com/photo-1512820790803-83ca734da794")


# ---------------- GENRE ---------------- #

elif page == "Genre Recommendation":

    st.header("Recommend Books by Genre")

    user_genres = st.text_input(
        "Enter genres (e.g. fantasy mystery romance)"
    )

    if st.button("Get Recommendations"):

        if not user_genres:
            st.warning("Please enter at least one genre")

        else:
            with st.spinner("Finding books..."):

                try:
                    response = requests.post(
                        f"{API_URL}/recommend/genre",
                        json={"genres": user_genres}
                    )

                    if response.status_code == 200:
                        results = response.json()["results"]
                    else:
                        results = []

                except:
                    st.error("API not running")
                    results = []

            if not results:
                st.error("No books found")

            else:
                st.success("Top Recommendations:")

                for r in results:
                    st.markdown(f"""
                    **📖 {r['title']}**  
                    ⭐ Rating: {r['average_rating']}  
                    🔥 Popularity: {r['ratings_count']}  
                    🎯 Match Score: {r['match_score']}  
                    🏷️ Genres: {r['genre']}
                    """)
                    st.divider()


# ---------------- IMAGE ---------------- #

elif page == "Image Based Recommendation":

    st.header("Recommend from Book Image")

    uploaded_file = st.file_uploader(
        "Upload book image",
        type=["jpg", "jpeg", "png"]
    )

    st.write("OR")

    manual_text = st.text_input(
        "Enter book name manually (backup)"
    )

    if st.button("Detect & Recommend"):

        result = None

        # 🔹 IMAGE CASE
        if uploaded_file:
            with st.spinner("Processing image..."):

                try:
                    response = requests.post(
                        f"{API_URL}/recommend/image",
                        files={"file": uploaded_file}
                    )

                    if response.status_code == 200:
                        result = response.json()
                    else:
                        result = {"error": "API error"}

                except:
                    st.error("API not running")

        # 🔹 TEXT CASE (backup)
        elif manual_text:
            try:
                response = requests.post(
                    f"{API_URL}/recommend/text",
                    json={"text": manual_text}
                )

                if response.status_code == 200:
                    result = response.json()
                else:
                    result = {"error": "API error"}

            except:
                st.error("API not running")

        else:
            st.warning("Upload image or enter book name")

        # 🔹 SHOW RESULT
        if result:
            if "error" in result:
                st.error(result["error"])

            else:
                st.success(f"Detected Book: {result['detected_book']}")

                st.subheader("Recommended Books:")

                for r in result["recommendations"]:
                    st.write(f"📖 {r['title']} ⭐ {r['rating']}")
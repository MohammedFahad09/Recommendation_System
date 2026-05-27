# from rapidfuzz import process

# def find_best_match(query, titles):
#     match = process.extractOne(query, titles, score_cutoff=60)
#     return match[0] if match else None






# from rapidfuzz import process
# import re

# # remove common useless words
# STOPWORDS = {"the", "is", "of", "and", "to", "in", "a", "an", "on", "for"}

# def clean_words(text):
#     words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
#     return [w for w in words if w not in STOPWORDS and len(w) > 2]


# def generate_phrases(words, min_len=2, max_len=4):
#     phrases = []
    
#     for i in range(len(words)):
#         for j in range(i + min_len, min(i + max_len + 1, len(words))):
#             phrase = " ".join(words[i:j])
#             phrases.append(phrase)
    
#     return phrases


# def find_best_match(text, titles):
    
#     words = clean_words(text)
    
#     if not words:
#         return None
    
#     phrases = generate_phrases(words)
    
#     best_match = None
#     best_score = 0
    
#     for phrase in phrases:
#         match = process.extractOne(phrase, titles)
        
#         if match:
#             matched_title, score, _ = match
            
#             if score > best_score:
#                 best_score = score
#                 best_match = matched_title
    
#     # threshold to avoid garbage matches
#     if best_score < 60:
#         return None
    
#     return best_match






# from rapidfuzz import process
# import re

# STOPWORDS = {"the", "is", "of", "and", "to", "in", "a", "an", "on", "for"}

# def clean_words(text):
#     words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
#     return [w for w in words if w not in STOPWORDS and len(w) > 2]


# def find_best_match(text, titles):
    
#     words = clean_words(text)
    
#     if not words:
#         return None
    
#     # 🔥 limit words (important for speed)
#     words = words[:6]
    
#     # 🔥 create small phrases only
#     phrases = []
#     for i in range(len(words) - 1):
#         phrases.append(words[i] + " " + words[i+1])
    
#     best_match = None
#     best_score = 0
    
#     for phrase in phrases:
        
#         # 🔥 MUCH FASTER: limit results
#         matches = process.extract(
#             phrase,
#             titles,
#             limit=5   # only top 5 instead of full search
#         )
        
#         for matched_title, score, _ in matches:
#             if score > best_score:
#                 best_score = score
#                 best_match = matched_title
    
#     if best_score < 60:
#         return None
    
#     return best_match






from rapidfuzz import process
import re

STOPWORDS = {"the", "is", "of", "and", "to", "in", "a", "an", "on", "for"}

def clean_text(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    
    # remove stopwords + small words
    words = [w for w in words if w not in STOPWORDS and len(w) > 2]
    
    # 🔥 keep only first few important words
    words = words[:8]
    
    return " ".join(words)


def find_best_match(text, titles):
    
    query = clean_text(text)
    
    if not query:
        return None
    
    # 🔥 single fast match
    match = process.extractOne(query, titles, score_cutoff=60)
    
    return match[0] if match else None
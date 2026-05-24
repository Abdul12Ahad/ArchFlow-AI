from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def generate_embedding(text):

    embedding = embedding_model.encode(
    text,
    normalize_embeddings=True
    )

    return embedding.tolist()
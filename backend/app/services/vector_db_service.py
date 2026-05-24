import chromadb

# Persistent local DB
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="repository_chunks"
)


def store_chunk(chunk_id, embedding, metadata, document):

    print(f"Stored chunk: {chunk_id}")

    collection.add(
        ids=[chunk_id],
        embeddings=[embedding],
        metadatas=[metadata],
        documents=[document]
    )


def search_similar_chunks(query_embedding, top_k=5):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results

def get_collection_count():
    return collection.count()
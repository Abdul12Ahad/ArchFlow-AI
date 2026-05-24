from backend.app.services.embedding_service import generate_embedding
from backend.app.services.vector_db_service import search_similar_chunks
from backend.app.services.vector_db_service import get_collection_count

def retrieve_relevant_chunks(query, top_k=5):

    print("TOTAL CHUNKS:", get_collection_count())

    #Generating query embedding
    query_embedding = generate_embedding(query)

    #Searching ChromaDB for vector similarity
    results = search_similar_chunks(query_embedding, top_k)

    print(results)
    
    return results
from modules.embeddings.embedder import EmbeddingEngine
from modules.embeddings.store_faisis import FAISSStore

class Retriever:
    def __init__(self):
        self.embedder = EmbeddingEngine()
        self.store_faisis = FAISSStore()

    def retrieve(self, query: str, top_k: int = 5):
        """
        Returns top K similar chunks/questions using embeddings + FAISS. 
        """
        query_emb = self.embedder.get_embedding(query)
        results = self.store.search(query_emb, k = top_k)
        return results
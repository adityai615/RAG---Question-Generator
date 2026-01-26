from sentence_transformers import SentenceTransformer

class EmbeddingEngine:
    def __init__(self, model_name="sentence-transformers/all-mpnet-base-v2"):
        """
        Loads The Highest accurace embedding model
        MPNet gives 768-dimensional vectors and very high accuracy.
        """
        self.model = SentenceTransformer(model_name)

    def get_embedding(self, text: str):
        """
        returns embedding vector for a single text.
        """
        return self.model.encode(text, convert_to_numpy=True)

    def get_embeddings(self, texts:list):
        """
        returns embedding vectors for a list of text
        """

        return self.model.encode(texts, convert_to_numpy=True)

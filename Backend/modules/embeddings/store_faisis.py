import faiss
import numpy as np
import json
import os

class FAISSStore:
    def __init__(self, index_path="database/faiss_index.index", meta_path="database/metadata.json"):
        self.index_path = index_path
        self.meta_path = meta_path

        self.dimension = 768
        self.index = None
        self.metadata = []

        # Load If exists
        if os.path.exists(index_path):
            self.index = faiss.read_index(index_path)
        else:
            #create empty faiss index
            self.index = faiss.IndexFlatL2(self.dimension) 

        # load metadata (text of questions)
        if os.path.exists(meta_path):
            with open(meta_path, "r") as f:
                self.metadata = json.load(f)

    def add(self, embeddings:np.ndarray, texts: list):
        """
        Add embeddings + associated text to the faiss index
        """
        self.index.add(embeddings)
        
        #save metadata
        self.metadata.extend(texts)

        #persist
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "w") as f:
            json.dump(self.metadata, f)

    def search(self, query_embedding, k=5):
        """
        search top k similar search
        """        
        distances, indices = self.index.search(np.array([query_embedding]), k)

        results = []
        for idx in indices[0]:
            if idx < len(self.metadata):
                results.append(self.metadata[idx])

        return results

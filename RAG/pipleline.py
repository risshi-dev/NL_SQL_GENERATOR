import chromadb
from sentence_transformers import SentenceTransformer
import torch

class Embed:
    def __init__(self, data, database):
        self.__client   = chromadb.PersistentClient('../../asset')
        self.__document = data
        self.__initiate(database)
        self.__embed()
    
    def __initiate(self, database):
        self.__collections = self.__client.get_or_create_collection(f"user1_{database}_db")

    def __embed(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        indexing    = []
        _documents  = []
        self.__model= SentenceTransformer("BAAI/bge-large-en-v1.5", device=device)
        
        for table in self.__document:
            indexing.append(f"table_{table}_idx")
            _documents.append(self.__document[table])

        encoded_indexing = self.__model.encode(_documents, convert_to_tensor=True).tolist()

        self.__collections.add(
            embeddings=encoded_indexing,
            documents=_documents,
            ids=indexing
        )

    def query_schema(self, query):
        encoded_query = self.__model.encode([query]).tolist()
        result = self.__collections.query(
            query_embeddings=encoded_query,
            n_results=5
        )
        
        return result['documents'][0]
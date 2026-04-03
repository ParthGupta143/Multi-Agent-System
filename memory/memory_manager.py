import chromadb
import hashlib

class MemoryManager:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./memory/chroma_db")
        self.collection = self.client.get_or_create_collection(
            name="agent_memory"
        )
        print("✅ Memory Manager initialized!")

    def _generate_id(self, text: str) -> str:
        return hashlib.md5(text.encode()).hexdigest()

    def save(self, query: str, result: str):
        doc_id = self._generate_id(query)
        existing = self.collection.get(ids=[doc_id])
        if existing["ids"]:
            print(f"📝 Memory already exists, updating...")
            self.collection.update(
                ids=[doc_id],
                documents=[result],
                metadatas=[{"query": query}]
            )
        else:
            self.collection.add(
                ids=[doc_id],
                documents=[result],
                metadatas=[{"query": query}]
            )
            print(f"💾 Saved to memory!")

    def search(self, query: str, threshold: float = 0.7) -> str | None:
        if self.collection.count() == 0:
            return None
        results = self.collection.query(
            query_texts=[query],
            n_results=1
        )
        if not results["ids"][0]:
            return None
        distance = results["distances"][0][0]
        similarity = 1 - distance
        if similarity >= threshold:
            print(f"🧠 Memory HIT! Similarity: {similarity:.2f}")
            return results["documents"][0][0]
        print(f"🔍 No similar memory (similarity: {similarity:.2f})")
        return None
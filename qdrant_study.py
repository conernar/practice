# 建表
from qdrant_client import QdrantClient, models

client = QdrantClient(url = "http://localhost:6333")

client.create_collection(
    collection_name = "contract_clauses",
    vectors_config = {
        "dense": models.VectorParams(
            size = 1024,
            distance = models.Distance.COSINE,
        )
    },
    hnsw_config = models.HnswConfigDiff(m = 16, ef_construct = 128),
)
# 写入（vectors + payload）
client.upsert(
    collection_name = "contract_clauses",
    points = [
        models.PointStruct(
            id = 1,
            vector = {
                "dense": embedding
            }, # list[float], length 1024
            payload = {
                "text": "Either party may terminate this Agreement...",
                "clause_type": "termination",
                "doc_id": "msa_2024_acme",
                "section": "12.3",
            }
        ),
        # ...批量，别一个一个upsert（请求开销大）
    ],
)
# `embedding` 是先用BGE-M3跑出来的向量。（Qdrant客户端内置了FastEmbed interface，能直接生成）
# Query

query_vec = embed(query_text) # 同一个BGE—M3

hits = client.query_points(
    collection_name = "contract_clauses",
    query = query_vec,
    using = "dense",
    limit = 5,
    with_payload = True,
    search_params = models.search_params(hnsw_ef = 128),
).points

for h in hits:
    print(h.score, h.payload["section"], h.payload["text"][:60])

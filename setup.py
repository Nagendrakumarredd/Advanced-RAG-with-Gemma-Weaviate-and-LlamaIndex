from llama_index.core.retrievers import VectorIndexAutoRetriever
from llama_index.core.vector_stores.types import MetadataInfo, VectorStoreInfo
import openai
from llama_index.llms.openai import OpenAI
from kaggle_secrets import UserSecretsClient

# Define additional information about the metadata which the LLM can use to infer the metadata filters
vector_store_info = VectorStoreInfo(
    content_info="Names of the Kaggle competitions",
    metadata_info=[
        MetadataInfo(
            name="competition_title",
            type="str",
            description=("Name of the Kaggle competition.")
        )
    ],
)

# Get OpenAI API key form Kaggle secrets
user_secrets = UserSecretsClient()
openai.api_key = user_secrets.get_secret("OPENAI_API_KEY")

# Set up the VectorIndexAutoRetriever
retriever = VectorIndexAutoRetriever(
    index, 
    llm = OpenAI(model="gpt-4"),
    vector_store_info=vector_store_info,
    similarity_top_k = 4, 
    vector_store_query_mode="hybrid", 
    alpha=0.5,
    verbose=True
)







response = retriever.retrieve(sample_query)

for i in range(len(response)):
    print(f"\nChunk {i}:")
    print((response[i].text))
    print(response[i].metadata)

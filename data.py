!pip install -q -U keras-nlp
!pip install -q -U keras>3
!pip install -q -U llama_index
!pip install llama-index-embeddings-huggingface
!pip install weaviate-client
!pip install llama-index-vector-stores-weaviate
!pip install torch sentence-transformers


Step 1: Define Gemma as a Custom LLM
import keras
import keras_nlp
import os

gemma_lm = keras_nlp.models.GemmaCausalLM.from_preset("gemma_instruct_2b_en")

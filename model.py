Step 1: Define Gemma as a Custom LLM

from typing import Any

from llama_index.core.callbacks import CallbackManager
from llama_index.core.llms import (
    CustomLLM,
    CompletionResponse,
    CompletionResponseGen,
    LLMMetadata,
)
from llama_index.core.llms.callbacks import llm_completion_callback

class Gemma(CustomLLM):
    num_output: int = 512
    model_name: str = "Gemma"
    model: Any = None

    def __init__(self, model, num_output):
        super(Gemma, self).__init__()
        self.model = model
        self.num_output = num_output

    @property
    def metadata(self) -> LLMMetadata:
        """Get LLM metadata."""
        return LLMMetadata(
            num_output=self.num_output,
            model_name=self.model_name,
        )

    @llm_completion_callback()
    def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse:
        return CompletionResponse(text=self.model.generate(prompt, max_length=self.num_output))

    @llm_completion_callback()
    def stream_complete(self, prompt: str, **kwargs: Any) -> CompletionResponseGen:
        response = ""
        for token in self.model.generate(prompt, max_length=self.num_output):
            response += token
            yield CompletionResponse(text=response, delta=token)



Step 2: Define Embedding Model and LLM


from llama_index.core.settings import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

Settings.llm = Gemma(gemma_lm, 512)
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

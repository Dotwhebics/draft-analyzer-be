from civis_backend_policy_analyser.core.model import get_rag_chain

class DocumentSummarizer:
    def __init__(self, retriever, llm_model):
        self.rag_chain = get_rag_chain(retriever=retriever, llm_model=llm_model)

    def summarize(self, prompt):
        return self.rag_chain.run(prompt)

    def assess(self, prompts, expected_format_instructions=""):
        return {prompt: self.rag_chain.invoke(expected_format_instructions + prompt) for prompt in prompts}
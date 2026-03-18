# ==> through this method "hugging_face_local" we can directly download the model and can talk with it

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id = "meta-llama/Llama-3.1-8B-Instruct",   # repo_id
    task = 'text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("tell me the birth place of Lord Ram")

print(result.content)




# ==> it is not runing properly because our system doesn't get that much load 
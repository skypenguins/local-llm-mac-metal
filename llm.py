from llama_cpp import Llama

llm = Llama(
    model_path="model/yarn-llama-2-13b-64k.Q4_0.gguf",
    n_gqa=8,
    n_gpu_layers=1,
)
output = llm(
    "アジャイル開発において最も大切なことは、",
    max_tokens=512,
    stop=["\n"],
    echo=True,
)
print(output)

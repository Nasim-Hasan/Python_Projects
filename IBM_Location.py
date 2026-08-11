import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Dynamically select device (CUDA -> Apple Silicon MPS -> CPU)
if torch.cuda.is_available():
    device = "cuda"
    device_map = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
    device_map = None
else:
    device = "cpu"
    device_map = None

model_path = "ibm-granite/granite-3.1-8b-instruct" # Make sure to check correct repo name
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Pass device_map or map directly to device
model = AutoModelForCausalLM.from_pretrained(
    model_path, 
    device_map=device_map,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
)

if device_map is None:
    model.to(device)

model.eval()

chat = [
    { "role": "user", "content": "Please list one IBM Research laboratory located in the United States. You should only output its name and location." },
]
chat_formatted = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)

# Tokenize and move to designated device
input_tokens = tokenizer(chat_formatted, return_tensors="pt").to(device)

# Generate output tokens
output = model.generate(**input_tokens, max_new_tokens=100)

# Decode output tokens into text
output_text = tokenizer.batch_decode(output, skip_special_tokens=True)
print(output_text[0])
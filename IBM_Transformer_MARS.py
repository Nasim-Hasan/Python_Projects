import torch
from transformers import AutoTokenizer, pipeline

model_id = "ibm-granite/granite-3.3-2b-instruct"
use_cuda = torch.cuda.is_available()

tok = AutoTokenizer.from_pretrained(model_id)
if tok.pad_token is None:
    tok.pad_token = tok.eos_token

pipe = pipeline(
    "text-generation",
    model=model_id,
    tokenizer=tok,
    dtype=torch.float16 if use_cuda else torch.float32,
    device_map="auto" if use_cuda else None,
)

messages = [{"role": "user", "content": "What is the temperature of Mars?"}]
prompt = tok.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)

out = pipe(
    prompt,
    max_new_tokens=100,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    eos_token_id=tok.eos_token_id,
    pad_token_id=tok.pad_token_id,
)
# Slice off the prompt to keep only the answer
answer = out[0]["generated_text"][len(prompt):]
print(answer)
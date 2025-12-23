import torch
import os
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from peft import PeftModel

base_model_name = "Qwen/Qwen2.5-1.5B-Instruct"

adapter_path = "\slogen-1.5b-v1"

print(f"Loading base model: {base_model_name}...")
base_model = AutoModelForCausalLM.from_pretrained(
    base_model_name, 
    device_map="auto", 
    torch_dtype=torch.float16
)

print(f"Loading custom adapters from {adapter_path}...")
if not os.path.exists(os.path.join(adapter_path, "adapter_config.json")):
    print("❌ ERROR: adapter_config.json NOT found!")
    model = base_model
else:
    model = PeftModel.from_pretrained(base_model, adapter_path)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(base_model_name)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_slogan(product_name, keywords):
    user_message = f"Write a creative marketing slogan for {product_name}. Keywords: {keywords}"
    
    prompt = f"<|im_start|>user\n{user_message}<|im_end|>\n<|im_start|>assistant\n"

    result = generator(
        prompt, 
        max_new_tokens=40,
        temperature=0.75, 
        do_sample=True,
        repetition_penalty=1.1
    )
    
    full_text = result[0]['generated_text']
    slogan = full_text.split("<|im_start|>assistant\n")[-1].replace("<|im_end|>", "").strip()
    
    return slogan
import torch
import os
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from peft import PeftModel

base_model_name = "Qwen/Qwen2.5-1.5B-Instruct"
adapter_path = "./slogen-1.5b-v1" 

print(f"Loading base model: {base_model_name}...")
base_model = AutoModelForCausalLM.from_pretrained(
    base_model_name, 
    device_map="auto", 
    torch_dtype=torch.float16
)

print(f"Loading custom adapters from {adapter_path}...")
if not os.path.exists(os.path.join(adapter_path, "adapter_config.json")):
    print(f"❌ ERROR: adapter_config.json NOT found in {adapter_path}")
    model = base_model
else:
    model = PeftModel.from_pretrained(base_model, adapter_path)

tokenizer = AutoTokenizer.from_pretrained(base_model_name)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_slogan(product_name, keywords):
    slogans = []
    
    # SYSTEM PROMPT: Force creativity
    system_instruction = "You are a creative marketing expert. Write a short, punchy slogan."
    
    user_message = f"Write a catchy slogan for {product_name}. Keywords: {keywords}"
    prompt = f"<|im_start|>system\n{system_instruction}<|im_end|>\n<|im_start|>user\n{user_message}<|im_end|>\n<|im_start|>assistant\n"

    # GENERATE 3 TIMES
    for i in range(3):
        result = generator(
            prompt, 
            max_new_tokens=40,
            temperature=0.85,  # High temperature for variety
            do_sample=True,
            repetition_penalty=1.2,
            top_k=50
        )
        
        full_text = result[0]['generated_text']
        slogan_text = full_text.split("<|im_start|>assistant\n")[-1].replace("<|im_end|>", "").strip()
        
        # Remove quotes if the AI added them
        slogan_text = slogan_text.replace('"', '').replace("'", "")
        
        # Avoid duplicates (basic check)
        if slogan_text not in slogans:
            slogans.append(slogan_text)

    # If we somehow got less than 3 (due to duplicates), fill with a fallback
    while len(slogans) < 3:
        slogans.append(f"{product_name}: The smart choice.")

    return slogans
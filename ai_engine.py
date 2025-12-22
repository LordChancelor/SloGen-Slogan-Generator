from transformers import pipeline

# Initialize the text generation model
# We use distilgpt2 because it is lightweight and fast for web projects
generator = pipeline('text-generation', model='distilgpt2')

def generate_slogan(product_name, keywords):
    # Prompt Engineering: We guide the model to act like a copywriter
    prompt = f"Marketing slogan for {product_name} which is {keywords}:"
    
    # Generate the output
    result = generator(prompt, max_length=40, num_return_sequences=1, temperature=0.8)
    
    # Clean the result
    generated_text = result[0]['generated_text']
    
    # Remove the prompt from the output to show only the new creative part
    slogan = generated_text.replace(prompt, "").strip().split("\n")[0]
    
    # Fallback if model generates empty string
    if not slogan:
        return f"Experience the best {product_name}."
        
    return slogan
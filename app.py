from flask import Flask, render_template, request, jsonify
from ai_engine import generate_slogan

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        product_name = data.get('product_name')
        keywords = data.get('keywords')
        
        slogan_list = generate_slogan(product_name, keywords)
        
        # Return the list as 'slogans'
        return jsonify({'slogans': slogan_list})
    
    return render_template('index.html')

if __name__ == '__main__':
    # Hugging Face Spaces specifically requires port 7860 and host 0.0.0.0
    app.run(host='0.0.0.0', port=7860)
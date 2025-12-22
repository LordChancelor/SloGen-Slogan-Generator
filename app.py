from flask import Flask, render_template, request, jsonify
from ai_engine import generate_slogan

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    product = data.get('product')
    tags = data.get('keywords')

    if not product:
        return jsonify({'error': 'Product name is required'}), 400

    try:
        # Call our AI function
        slogan = generate_slogan(product, tags)
        return jsonify({'slogan': slogan})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
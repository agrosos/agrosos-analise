# app.py
from flask import Flask, request, jsonify
from PIL import Image
import io
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def analyze_image():
    try:
        if 'image' in request.files:
            # Se enviou arquivo direto
            file = request.files['image']
            image = Image.open(io.BytesIO(file.read()))
        elif 'image_url' in request.json:
            # Se enviou uma URL
            image_url = request.json['image_url']
            response = requests.get(image_url)
            image = Image.open(io.BytesIO(response.content))
        else:
            return jsonify({"erro": "Nenhuma imagem enviada."}), 400

        width, height = image.size

        if width > height:
            result = "Folha saudável (exemplo automático)"
        else:
            result = "Possível problema detectado"

        return jsonify({
            "resultado": result
        })
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/', methods=['POST'])
def analyze_image():
    try:
        file = request.files['image']
        image = Image.open(io.BytesIO(file.read()))

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

from flask import Flask, render_template, request, jsonify
from PIL import Image
import numpy as np
from keras.models import load_model

app = Flask(__name__)

model = load_model('/app/data/model1_catsVSdogs_10epoch.h5')

classes = {
    0: 'its a cat',
    1: 'its a dog'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        file = request.files['file']
        image = Image.open(file)
        image = image.resize((128, 128))
        image = np.expand_dims(image, axis=0)
        image = np.array(image)
        image = image / 255
        pred = model.predict([image])[0]
        pred_class = np.argmax(pred)
        sign = classes[pred_class]
        return jsonify({'result': sign})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

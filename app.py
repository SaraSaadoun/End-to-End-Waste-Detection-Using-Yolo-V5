import sys,os
from wasteDetection.pipeline.training_pipeline import TrainPipeline
from wasteDetection.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template,Response
from flask_cors import CORS, cross_origin
from wasteDetection.constant.application import APP_HOST, APP_PORT


app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "input_image.jpg"


@app.route('/train')
def train():
    train_pipeline = TrainPipeline()
    train_pipeline.run_pipeline()
    return "Training completed successfully."

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
    try:
        image = request.json['image']
        decodeImage(image, client_app.filename)


        os.system("cd yolov5/ && python detect.py --weights my_model.pt --img 416 --conf 0.5 --source ../data/input_image.jpg")

        opencodedbase64 = encodeImageIntoBase64("yolov5/runs/detect/exp/input_image.jpg")
        result = {"image": opencodedbase64.decode('utf-8')}
        os.system("rm -rf yolov5/runs")

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)

@app.route("/live", methods=['GET'])
@cross_origin()
def predict_live():
    try:
        os.system("cd yolov5/ && python detect.py --weights my_model.pt --img 416 --conf 0.5 --source 0")
        os.system("rm -rf yolov5/runs")
        return "Camera starting!!" 

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    


if __name__ == "__main__":
    client_app = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT, debug=True)
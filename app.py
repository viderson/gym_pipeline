from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods =['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            body_weight=float(request.form.get('body_weight')),
            mood=request.form.get('mood'),
            dchest=float(request.form.get('dchest')),
            arms=float(request.form.get('arms')),
            waist=float(request.form.get('waist')),
            legs=float(request.form.get('legs')),
            shoulders=float(request.form.get('shoulders')),
            training_duration_minutes=float(request.form.get('training_duration_minutes')),
            sleep_hours=float(request.form.get('sleep_hours')),
            stress_level=int(request.form.get('stress_level')),
            program_phase=request.form.get('program_phase'),
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])

if __name__=="__main__":
    app.run(host="0.0.0.0")        
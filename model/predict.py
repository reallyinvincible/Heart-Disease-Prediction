import argparse
import json
import os
import sys
import pickle
import sagemaker_containers
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

def input_fn(request_body, request_content_type):
    print("Request Body:", request_body)
    event = json.loads(request_body)
    age = int(event['age'])
    gender = int(event['gender'])
    chest_pain = int(event['chest_pain'])
    blood_pressure = int(event['blood_pressure'])
    cholestrol_level = int(event['cholesterol_level'])
    max_heart_rate = int(event['max_heart_rate'])
    return [[age, gender, chest_pain, blood_pressure, cholestrol_level, max_heart_rate]]

def model_fn(model_dir):
    print("Loading model.")
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    print("Done loading model.")
    return model

def predict_fn(input_data, model):
    output = model.predict(input_data)
    print("Output", output)
    return output

def output_fn(prediction, content_type):
    result = {}
    result['prediction'] = str(prediction[0])
    print("Prediction", prediction)
    print("Result", result)
    return json.dumps(result)

import sys
import pandas as pd
import os
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts","model.pkl")
            preprocesor_path = os.path.join("artifacts", "preprocesor.pkl")
            print("Before Loading")
            model = load_object(model_path)
            preprocesor = load_object(preprocesor_path)
            print("After Loading")
            data_scaled = preprocesor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e, sys)
class CustomData:
    class TrainingData:
    def __init__(self, body_weight: float, mood: str, dchest: float, arms: float, waist: float,
                 legs: float, shoulders: float, training_duration_minutes: float,
                 sleep_hours: float, stress_level: int, program_phase: str):

        self.body_weight = body_weight
        self.mood = mood
        self.dchest = dchest
        self.arms = arms
        self.waist = waist
        self.legs = legs
        self.shoulders = shoulders
        self.training_duration_minutes = training_duration_minutes
        self.sleep_hours = sleep_hours
        self.stress_level = stress_level
        self.program_phase = program_phase

    def get_data_as_data_frame(self):
        try:
            data_input = {
                "body_weight": [self.body_weight],
                "mood": [self.mood],
                "dchest": [self.dchest],
                "arms": [self.arms],
                "waist": [self.waist],
                "legs": [self.legs],
                "shoulders": [self.shoulders],
                "training_duration_minutes": [self.training_duration_minutes],
                "sleep_hours": [self.sleep_hours],
                "stress_level": [self.stress_level],
                "program_phase": [self.program_phase]
            }
            return pd.DataFrame(data_input)
        except Exception as e:
            raise CustomException(e, sys)












        "body_weight",
                "dchest",
                "arms",
                "waist",
                "legs",
                "shoulders",
                "training_duration_minutes",
                "sleep_hours",
                "stress_level"
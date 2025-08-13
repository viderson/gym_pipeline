import sys
import os
from dataclasses import dataclass

import numpy as np 
import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.inpute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception impo CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocesor_obj_file_path = os.path.join('artifacts', 'proprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        """
        This function is responsible for data transformation
        """
        try:
            numerical_columns = [
                "body_weight",
                "dchest",
                "arms",
                "waist",
                "legs",
                "shoulders",
                "training_duration_minutes",
                "sleep_hours",
                "stress_level"
                ]
            categorical_columns = [
                "program_phase",
                'mood'
            ]

            num_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy = "mean")),
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps = [
                    ("imputer", strategy="most_frequent"),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean = False))
                ]
            )

            logging.info(f"Numerical Columns: {numerical_columns}")
            logging.info(f"Categorical Columns: {categorical_columns}")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns)
                    ("cat_pipeline", cat_pipeline, categorical_columns)
                ]
            )
            
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            loggin.info("Read train and test data completed")
            loggin.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = 'volume'
            
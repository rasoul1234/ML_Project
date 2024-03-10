import pandas as pd
import sys
from dataclasses import dataclass
import numpy as np

# useing sklean libraries
from sklearn.compuse import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
import import os


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: os.path.join('artifact', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation = DataTransformationConfig()
        
        #  here I want to change the data to numaric
    def get_data_transformer_object(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_enthnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
                ]
            #  this is for numeric features
            num_pipeline = Pipeline(
                steps = [
                ("imputer", SimpleImputer(strategy = "median"))
                ("scaler", StandardScaler()) 
                ]
            # this is for categorical features
            cat_pipeline = Pipline
                
                
            )
            
        except:
            pass
        
        
 



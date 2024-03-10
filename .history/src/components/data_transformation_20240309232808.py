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
        '''
        This function is responsible for data transformation
        
        '''
        
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
                ])
            # this is for categorical features
            cat_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy = "most_frequent"))
                    ("one_hot_encoder", OneHotEncoder())
                    ("scaler", StandardScaler())
                ])
            
            logging.info(f"Numerical columns: {numerical_columns}") 
            logging.info(f"Categorical columns: {categorical_columns}") 
            
            # now lets combile num_piplene and cat_pipline
            preprocessor = ColumnTransformer([
                # here it means I want num_pipeline for numerical_colunms
                # 1: pipeline name   2: kind of pipeline   3: which columns
                ("num_pipeline", num_pipline, numerical_columns)
                # here it means I want num_pipeline for categorical_colunms
                ("cat_pipline", cat_pipeline, categorical_columns)
            ])
            return preprocessor
            
        except Exception as e:
            raise CustomException(e, sys)
            
        
        # now lets start our transormation function
        # I will get train_path and test_path from data ingestion
 def initiate_data_transformation(self, train_path, test_path):
     try:
         train_df = pd.read_csv(train_path)
         test_df  = pd.read_csv(test_path)
         
         logging.info("Read train and test data completed")
         logging.info("Obtaining preprocessing object")
         
        #  lets call here 
         preprocessor_obj = self.get_data_transformer_object()
         target_column_name = "math_score"
         numerical_columns = ["writing_score", "reading_score"]
         
         input_feature_train_df = train_df.drop(columns = [target_column_name], axis = 1)
     except:
         pass



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

class DataTransformationConfig:
    preprocessor_obj_file_path: os.path.join('artifact', 'preprocessor.pkl')
 



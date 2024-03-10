import os
import sys

import numpy as np
import pandas as pd
# dill is used to create picle file
import dill
from src.exception import CustomException

# I got this from data_transformation
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok = True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            
    except Exception as e:
        faise CustomException(e, sys)

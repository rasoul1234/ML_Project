# we use data_ingestion for train and test and store my dataset here. In breif this file is used for reading my dataset
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', 'train.csv')
    test_data_path: str=os.path.join('artifacts', 'test.csv')
    raw_data_path: str=os.path.join('artifacts', 'data.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
        def initiate_data_ingestion(self):
            logging.info("Engered the data ingestion method or component")
            
            try:
                
            except:
                raise e
            # end try
        
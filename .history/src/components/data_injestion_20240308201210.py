# we use data_ingestion for train and test and store my dataset here. In breif this file is used for reading my dataset
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split

import os
import sys

import numpy as np
import pandas as pd
if os.path.isfile('pyfile.txt'):
    # Comment: 
    os.remove('pyfile.txt')  # import os
# end del-file

from src.exception import CustomException

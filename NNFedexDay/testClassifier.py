
import tensorflow as tf
import pandas as pd


# constants
TEST_CSV_FILE_NAME = 'test_data.csv'
TRAIN_CSV_FILE_NAME = 'train_data.csv'

# read in the file with pandas and create data frame.

train_df = pd.read_csv(TRAIN_CSV_FILE_NAME)
test_df = pd.read_csv(TEST_CSV_FILE_NAME)

import os

# Absolute path to project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Full paths to CSVs
APP_TRAIN = os.path.join(PROJECT_ROOT, 'data', 'application_train.csv')
APP_TEST  = os.path.join(PROJECT_ROOT, 'data', 'application_test.csv')

artifcraft=os.path.join(PROJECT_ROOT,"artifacts")




print(APP_TRAIN,APP_TEST)
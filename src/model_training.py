import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import shap
import lightgbm as lgb
import os 
import json
import joblib
from verstack import LGBMTuner
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def json_load(path):
    dir_path = os.getcwd()
    json_path = os.path.join(dir_path, path)
    with open(json_path, "r") as file:
        json_file = json.load(file)
    return json_file


def txt_load(path):
    dir_path = os.getcwd()
    txt_path = os.path.join(dir_path, path)
    with open(txt_path, 'r') as file:
        list = [line.strip() for line in file]
    return list


def split_dataset(dataframe, variables, target, test_size):
    X = dataframe.loc[:, variables]
    y = dataframe.loc[:, [target]]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state=123) 
    return X_train, X_test, y_train, y_test


def lightgbm_training(X_train, y_train, hyperparameters):
    model = lgb.LGBMRegressor(**hyperparameters)
    model.fit(X_train, y_train)
    return model


def model_results(model, X_train, X_test, y_train, y_test):
    train_results = model.predict(X_train)
    test_results = model.predict(X_test)
    print('Model Results:')
    print('')
    print('RMSE train:', np.sqrt(mean_squared_error(y_train, train_results)))
    print('RMSE test:', np.sqrt(mean_squared_error(y_test, test_results)))
    print('')
    print('MAE train:', mean_absolute_error(y_train, train_results))
    print('MAE test:',  mean_absolute_error(y_test, test_results))
    print('')
    print('R2 train:', r2_score(y_train, train_results))
    print('R2 test:', r2_score(y_test, test_results))


def calculate_shap_values(model, X_train):
    # Create explainer object of Shapley
    explainer = shap.TreeExplainer(model)
    # Calculaate Shapley values for a datset (i.e., X_train)
    shap_values = explainer.shap_values(X_train)
    return explainer, shap_values


def save_model(model, path):
    model_path = os.getcwd() + '\models' + path
    joblib.dump(model, model_path)


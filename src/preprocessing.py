import pandas as pd 
import numpy as np
import json
import os


def load_data(data):
    dataframe = pd.read_csv(data, sep=";")
    return dataframe

def delete_outliers(dataframe):
    min_mileage = 0
    max_mileage = 500000
    dataframe = dataframe.loc[(dataframe['mileage'] >= min_mileage) & (dataframe['mileage'] <= max_mileage)]
    return dataframe

def strings_to_date(dataframe):
    for column in dataframe.columns:
        if 'registration' in column or 'sold' in column:
            if dataframe[column].dtype == 'object':
                try:
                    dataframe[column] = pd.to_datetime(dataframe[column], format='%d/%m/%Y')
                except ValueError:
                    continue
    return dataframe


def booleans_to_numeric(dataframe):
    for column in dataframe.columns:
        if dataframe[column].dtype == 'bool':
            try:
                dataframe[column] = dataframe[column].astype(int)
            except ValueError:
                continue
    return dataframe


def strings_to_numeric(dataframe):
    for column in dataframe.columns:
        if dataframe[column].dtype == 'object':
            try:
                dataframe[column] = pd.to_numeric(dataframe[column])
            except ValueError:
                continue
    return dataframe


def get_dummies(dataframe):
    for column in dataframe.columns:
        if dataframe[column].dtype == 'object':
            try:
                dummies = pd.get_dummies(dataframe[column])
                # dummies.columns = [i.replace(' ', '_').lower() for i in dummies.columns]
                dataframe = pd.concat([dataframe, dummies], axis = 1)
            except ValueError:
                continue
    return dataframe


def feature_engineering(dataframe):
    dataframe['antiquity'] = (dataframe['sold_at'] - dataframe['registration_date']).dt.days / 365.25
    # dataframe['mil/ant'] = dataframe['mileage'] / dataframe['antiquity']
    # dataframe['eng/ant'] = dataframe['engine_power'] / dataframe['antiquity']
    # dataframe['mil/eng'] = dataframe['mileage'] / dataframe['engine_power']


def get_train_data(data):
    df = load_data(data)
    df.drop(columns=['maker_key', 'model_key'], inplace=True)
    df_1 = delete_outliers(df)
    df_2 = strings_to_date(df_1)
    df_3 = booleans_to_numeric(df_2)
    df_4 = strings_to_numeric(df_3)
    feature_engineering(df_4)
    df_5 = get_dummies(df_4)
    return df_5


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

    min_price = 1000
    # max_price = 1000000
    dataframe = dataframe.loc[(dataframe['price'] >= min_price)]

    min_engine_power = 10
    dataframe = dataframe.loc[(dataframe['engine_power'] >= min_engine_power)]

    return dataframe

def strings_to_date(dataframe):
    for column in dataframe.columns:
        if 'registration' in column or 'sold' in column:
            if dataframe[column].dtype == 'object':
                try:
                    dataframe[column] = pd.to_datetime(dataframe[column], format='%m/%d/%Y')
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
    columns_tu_get_dummies = ['fuel', 'paint_color', 'car_type']
    for column in columns_tu_get_dummies:
        if dataframe[column].dtype == 'object':
            try:
                dummies = pd.get_dummies(dataframe[column])
                # dummies.columns = [i.replace(' ', '_').lower() for i in dummies.columns]
                dataframe = pd.concat([dataframe, dummies], axis = 1)
            except ValueError:
                continue
    return dataframe
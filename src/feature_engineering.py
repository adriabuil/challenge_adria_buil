import pandas as pd 
import numpy as np
import json

import os
import src.preprocessing


def get_antiquity(dataframe):
    dataframe['antiquity'] = (dataframe['sold_at'] - dataframe['registration_date']).dt.days / 365.25
    return dataframe

def get_avg_price_model_key(dataframe):
    dataframe_agg = dataframe.groupby(['model_key']).agg(avg_price=('price', 'mean')).reset_index()
    dataframe_merged = pd.merge(dataframe, dataframe_agg, on='model_key', how='left')
    dataframe_merged['avg_price'] = dataframe_merged['avg_price'].round(2)
    return dataframe_merged

def get_avg_mileage_model_key(dataframe):
    dataframe_agg = dataframe.groupby(['model_key']).agg(avg_mileage=('mileage', 'mean')).reset_index()
    dataframe_merged = pd.merge(dataframe, dataframe_agg, on='model_key', how='left')
    dataframe_merged['avg_mileage'] = dataframe_merged['avg_mileage'].round(2)
    return dataframe_merged

def get_avg_antiquity_model_key(dataframe):
    dataframe_agg = dataframe.groupby(['model_key']).agg(avg_antiquity=('antiquity', 'mean')).reset_index()
    dataframe_merged = pd.merge(dataframe, dataframe_agg, on='model_key', how='left')
    dataframe_merged['avg_antiquity'] = dataframe_merged['avg_antiquity'].round(2)
    return dataframe_merged

def get_relations(dataframe):
    dataframe['avg_price_per_milleage'] = (dataframe['avg_price'] / dataframe['avg_mileage']).round(4)
    dataframe['avg_price_per_antiquity'] = (dataframe['avg_price'] / dataframe['avg_antiquity']).round(4)
    dataframe['price_per_milleage'] = (dataframe['price'] / dataframe['mileage']).round(4)
    dataframe['price_per_antiquity'] = (dataframe['price'] / dataframe['antiquity']).round(4)
    return dataframe

def get_train_data(data):
    df = src.preprocessing.load_data(data)
    df_1 = src.preprocessing.delete_outliers(df)
    df_2 = src.preprocessing.strings_to_date(df_1)
    df_3 = src.preprocessing.booleans_to_numeric(df_2)
    df_4 = src.preprocessing.strings_to_numeric(df_3)
    df_5 = src.preprocessing.get_dummies(df_4)
    df_6 = get_antiquity(df_5)
    df_7 = get_avg_price_model_key(df_6)
    df_8 = get_avg_mileage_model_key(df_7)
    df_9 = get_avg_antiquity_model_key(df_8)
    df_10 = get_relations(df_9)
    df_10.drop(columns=['maker_key', 'model_key'], inplace=True)
    return df_10
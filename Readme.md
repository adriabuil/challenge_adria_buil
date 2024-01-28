# Challenge - Adrià Buil

## Description   
This project trains a Light GBM model using data_pricing_challenge.csv
To answer specifc questions of the challenge, different notebooks have been prepared.

---------------------------------------------------------------------------------------------------------------------------------------------------------

## How to run:

XXXXX

---------------------------------------------------------------------------------------------------------------------------------------------------------

## src

# preprocessing.py

This script is able to train a RNN using the original excel given.

	1) Get data from an excel file without formatting
	2) Transform the data into a pandas dataframe with the correct format (see preprocessing.py in /scripts for more details)
	3) Creates a GluonTS dataset from the pandas dataframe and uses it to train a deepAREstimator, a RNN designed to predict Time Series Data.
	4) Serializes the model traind and saves it in the "/model" folder in order to use it later.

# app.py

This script creates an API that is able to get POST request with the JSON format given and returns a dictionary with the predictions for each book.

	1) Initializes a Flask app in localhost port 5000.
	2) Get requests in JSON format and transform the data in a GluonTS dataset.
	3) Get the RNN trained and inference it with the dataset.
	4) Save the results in a dictionary and return them as a response to the API POST request.

---------------------------------------------------------------------------------------------------------------------------------------------------------


## utils

In the scripts folder we have 2 python files:

	1) preprocessing.py --> Includes most functions used to process the data in the app
	2) estimator.py --> Includes the functions used to train and inference the RNN and the construction of GluonTS datasets.


---------------------------------------------------------------------------------------------------------------------------------------------------------

## Notebooks

In this folder we can find 2 notebooks:

	1) EDA.ipynb --> Fast EDA used to understand the data and prepare some transformation before training the model
	2) rnn_training.ipynb --> Notebook that gets the data from the excel and trains a RNN, I used it to test different variations and epochs and optain results. 
				  I tested the model using the 3 last periods of the known dataset.







## Answer to Challenge questions

1) What are the most important characteristics and features that determine the selling price of a
used car?

Answer:

2) How does the estimated value of a car change over time?

Answer:

a. Does a relative change in selling price over time differ significantly with respect to any of
the car characteristics, e.g., color, price range or features?

Answer:

b. Are there any statistically significant seasonality patterns in pricing, e.g. certain car types
being more expensive in summer than winter?

Answer

3. Assume you need a car for a year (buy it now and sell in 1 year) and will drive approx. 10,000 miles during this time frame. You want to spend at least $20k.
What particular car from this data set would you buy (selling price has to be at least $20k at the moment of purchase) if you want to minimize the loss in absolute value in $ when you sell it. (Loss in value is $ defined as: Price at purchase – price after a year)

Answer:

4. Please share the out-of-sample accuracy metric for the model you used to answer the above questions.

Answer:

5. Feel free to share any other interesting insights worth mentioning.
En la prediccion simplemente tengo que seleccionar un coche... por eso no me afecta mucho el echo de que algunos estén por enciam la media...

Answer:
me quedo con el maximo y punto. lo que sí que es verdad, es que en un futuro deberiamos ver como tratar estos casos para que las predicciones sean mas robustas.
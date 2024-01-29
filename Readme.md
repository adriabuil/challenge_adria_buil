# Challenge - Adrià Buil

## Description   
This project trains a Light GBM model using data_pricing_challenge.csv data
To answer specifc questions of the challenge, different notebooks have been prepared.

---------------------------------------------------------------------------------------------------------------


## src

	1)	preprocessing.py:
	2) 	feature_engineering.py:
	3)	model_training.py:




--------------------------------------------------------------------------------------------------------------


## utils

	1)	model_hyperparameters.json:
	2)	model_variables.md:



---------------------------------------------------------------------------------------------------------------

## Notebooks

In this folder we can find 3 notebooks:
	1) 	eda.ipynb --> Fast EDA used to understand the data and prepare some transformation before training the model
	2) model_validation.ipynb --> Notebook that gets the data from the excel, applies preprocessing.py and feature_engineering.py data transformation and trains a LightGBM model using model_training.py.
		Used to test different models, stored at models folder.
	3) predictor.ipynb --> Notebook prepared to answer Question 3


---------------------------------------------------------------------------------------------------------------

## Answer to Challenge questions

1) What are the most important characteristics and features that determine the selling price of a
used car?

As seen in the feature importance matrix in Model Validation notebook, most importance features are Antiquity, Mileage and Engine Power, followed by AVG created variables and fetures 5 and 6.

2) How does the estimated value of a car change over time?

As expected:
    - Car price descreases with antiquity.
        - 2012, 2013 and 2014 are the years with more registred cars.
    - Car price decreases with mileage.
        - Mileage range mean is 140827, being the most common range from 120000 to 180000.
    - Car price increases with engine power.
        - Engine power mean is 129, being the most common range from 104 to 184.

- Most common fuel is diesel.
    - Petrol cars have a significant sales peak on May.

- Subdued colors (i.e., black, grey, brown and white) are the most sold, only blue can be compared to them.
    - Black and Blue suffer the most with summer arrival.
        
- Estate, Hatchback, Sedan and Suv are the most sold car types
    - Suv is more sold in summer



3. Assume you need a car for a year (buy it now and sell in 1 year) and will drive approx. 10,000 miles during this time frame. You want to spend at least $20k.
What particular car from this data set would you buy (selling price has to be at least $20k at the moment of purchase) if you want to minimize the loss in absolute value in $ when you sell it. (Loss in value is $ defined as: Price at purchase – price after a year)

Methodoly used is the following:
	1. Train a model with available data.
	2. Filter data by current price >= $20k.
	3. Add to available registers:
		mileage = mileage + 10,000
		antiquity = antiquity +1
	4. Predict price after 1 year and +10,000 miles.
	5. Calculate Loss in value = Current price - predicted price
	6. Maximize loss in value --> BMW	X4	53055	140	07/01/2015	diesel	black	suv	

4. Please share the out-of-sample accuracy metric for the model you used to answer the above questions.

RMSE train: 1772.7817363501013
RMSE test: 2665.9339652313533

MAE train: 1200.4274307275098
MAE test: 1753.9790611735534

R2 train: 0.9532210392321492
R2 test: 0.9095318245994384

5. Feel free to share any other interesting insights worth mentioning.

Point 3 is 


- En la prediccion simplemente tengo que seleccionar un coche... por eso no me afecta mucho el echo de que algunos estén por enciam la media...

- me quedo con el maximo y punto. lo que sí que es verdad, es que en un futuro deberiamos ver como tratar estos casos para que las predicciones sean mas robustas.
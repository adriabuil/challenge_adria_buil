# Challenge - Adrià Buil

## Description   
	This project trains a Light GBM model using data_pricing_challenge.csv data.
	To answer specifc questions of the challenge, different notebooks have been prepared.

---------------------------------------------------------------------------------------------------------------

### data
	Data available for the project (data_pricing_challenge.csv)

### models
	Different models tested can be stored in this folder (by now, only baseline and final ones).
	To improve the model registry, each model variables and hyperparamters should be also stored here.

### src
	Python scripts used in notebooks are available in this folder
	1)	preprocessing.py
	2) 	feature_engineering.py
	3)	model_training.py

### utils
	In this folder, final model variables and hyperparamters are available:
	1)	model_hyperparameters.json
	2)	model_variables.md

### notebooks
	In this folder we can find 3 notebooks:
	1) 	eda.ipynb --> Fast EDA used to understand the data and prepare some transformation before training the model
	2) 	model_validation.ipynb --> Notebook that gets the data from the excel, applies preprocessing.py and feature_engineering.py data transformation and trains a LightGBM model using model_training.py. 
	Used to test different models, stored at models folder.
	3) 	predictor.ipynb --> Notebook prepared to answer Question 3

### main.py
	This field could be used in the future, once model development stage is completed and model is ready to be automated.


---------------------------------------------------------------------------------------------------------------

## Answer to Challenge questions

1)	What are the most important characteristics and features that determine the selling price of a used car?

Answer:

	As seen in the feature importance matrix in Model Validation notebook, most importance features are Antiquity, Mileage and Engine Power, followed by AVG created variables and fetures 5 and 6.

2)	How does the estimated value of a car change over time?

Answer:
	
	As expected:
    -	Car price descreases with antiquity.
        -	2012, 2013 and 2014 are the years with more registred cars.
    -	Car price decreases with mileage.
        -	Mileage range mean is 140827, being the most common range from 120000 to 180000.
    -	Car price increases with engine power.
        -	Engine power mean is 129, being the most common range from 104 to 184.

	-	Most common fuel is diesel.
    	-	Petrol cars have a significant sales peak on May.

	-	Subdued colors (i.e., black, grey, brown and white) are the most sold, only blue can be compared to them.
		-	Black and Blue suffer the most with summer arrival.
			
	- 	Estate, Hatchback, Sedan and Suv are the most sold car types
		-	Suv is more sold in summer



3)	Assume you need a car for a year (buy it now and sell in 1 year) and will drive approx. 10,000 miles during this time frame. You want to spend at least $20k. What particular car from this data set would you buy (selling price has to be at least $20k at the moment of purchase) if you want to minimize the loss in absolute value in $ when you sell it. (Loss in value is $ defined as: Price at purchase – price after a year)

Answer:
	Methodoly used is the following:
		1)	Train a model with available data.
		2)	Filter data by current price >= $20k.
		3)	Add to available registers:
				mileage = mileage + 10,000
				antiquity = antiquity +1
		4)	Predict price after 1 year and +10,000 miles.
		5)	Calculate Loss in value = Current price - predicted price.
		6)	Maximize loss in value --> BMW; X4; 53055; 140; 07/01/2015; diesel; black; suv

	Loss in value for car selected is positive, which seems counter intuitive
	With available data for training, prediction of the model estimates that for the selected car, selling price after 1 year and 10000 miles will be higher than current one.


4)	Please share the out-of-sample accuracy metric for the model you used to answer the above questions.

Answer:
	RMSE train: 3377.922257434325 
	RMSE test: 2737.5692747365324

	MAE train: 1242.1251848822146 
	MAE test: 1728.8835849061243
	
	R2 train: 0.8716846816833517 
	R2 test: 0.8879549109382575


5)	Feel free to share any other interesting insights worth mentioning.

Answer:
	Predicted price adjusts correctly in general, but overestimations could lead to mistakes while minimizing loss of value.

	Business needs must be understood to adjust it. 

	If appliable, punish overestimations (pred_price > real_price) over subestimations (pred price < real price).

	Further steps to upgrade the model:
		Collect more data
		Define new variables (e.g., purchase price)
		Collect market trends


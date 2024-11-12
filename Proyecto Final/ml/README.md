# Machine Learning Models

## Files included:

- `README.md`: This file
- `preparation.ipynb`: Jupyter notebook with the code to prepare the data and assign the labels
- `models.ipynb`: Jupyter notebook with the code to train the models and dump them to disk in joblib format
- `restaurants.csv`: a CSV file containing the restaurant table data (ID,Name,Food Type,Details,Smoking Area,Price Range,City,State,Image)
- `waiters.csv`: a CSV file containing the waiter table data (ID,Name,Restaurant)
- `transactions.csv`: a CSV file containing the transaction table data (ID,Waiter,People,Total,Tip,Timestamp,Payment Method)
- `restaurants_with_metrics.csv`: a CSV file containing the restaurant table data with the metrics calculated in the preparation notebook
- `lr_model.joblib`: a joblib file containing the trained Linear Regression model
- `rf_model.joblib`: a joblib file containing the trained Random Forest model

## Python Version

- Python 3.13.0

## Libraries installed

- `pandas`
- `sci-kit learn`
- `plotly`
- `jupyterlab`
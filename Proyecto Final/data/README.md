# Creating the SQLit3 database

Files included:

- `restaurants.csv`: a CSV file containing the restaurant table data (ID,Name,Food Type,Details,Smoking Area,Price Range,City,State,Image)
- `waiters.csv`: a CSV file containing the waiter table data (ID,Name,Restaurant)
- `transactions.csv`: a CSV file containing the transaction table data (ID,Waiter,People,Total,Tip,Timestamp,Payment Method)
- `pictures.ipynb`: a Jupyter notebook containing the code to download the images from http://pexels.com, save them in the `images` folder and update the `restaurants.csv` file with the image path
- `fts_tables.sql`: a SQL script to create the FTS tables for the restaurant table
- `data.db`: the SQLite3 database file
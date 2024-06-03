# Stock Price Prediction System

The Stock Price Prediction System is a project designed to predict stock prices using machine learning techniques. It includes two main components: a model training script and a web application. The model training script uses historical stock data to train a Long Short-Term Memory (LSTM) neural network model, and the web application uses the trained model to make stock price predictions.

**File 1: stock_market_prediction.py - Training the Prediction Tool**

1. **Downloading Stock Price Data:**
   - Imagine you want to predict the price of Apple (AAPL) stock. This file uses a library called `yfinance` to download historical closing prices for AAPL from the internet. You can specify a date range to get data for a specific period.

2. **Preparing the Data for Prediction:**
   - Not all downloaded data might be perfect. There could be missing price information for some days. This file removes those missing bits using `dropna`.
   - Splitting the Data: Imagine having a practice test before an actual exam. Here, the data is split into two parts: training data (practice test) and testing data (actual exam). The model learns from the training data (80% of the data) and is evaluated on the testing data (20% of the data).
   - Scaling the Data: Prices can fluctuate wildly. This file uses a technique called MinMaxScaler to transform all price values between 0 and 1. This makes the data easier for the model to understand.
   - Creating Sequences: Stock prices are influenced by past trends. The file creates sequences of 100 past closing prices. For example, the model might see the closing prices for the last 100 days to predict the 101st day's price.

3. **Building a Stock Price Prediction Model:**
   - This is where the magic happens! The file builds a special kind of neural network called a Long Short-Term Memory (LSTM) model. Think of an LSTM model as a complex calculator that can learn from sequences of data.
   - The model has multiple LSTM layers that process the data sequences (100 past prices). These layers can identify short-term and long-term patterns in the data.
   - Dropout layers help prevent the model from overfitting, which means it becomes too reliant on the training data and performs poorly on unseen data.
   - Finally, a Dense layer translates the processed information from the LSTM layers into a single output, the predicted price.
   - The model is compiled with an optimizer (Adam) that helps it learn and adjust its predictions based on the training data. It also uses a loss function (mean squared error) to measure how different the model's predictions are from the actual closing prices.

4. **Making Predictions and Visualizing Results:**
   - Once trained, the model is tested on the unseen data (testing set). It predicts prices for the remaining days in the testing data.
   - Remember the scaling done earlier (0 to 1)? This file reverses that scaling to get the predicted prices back in their original units (like dollars).
   - The file then creates charts to compare the predicted prices with the actual closing prices. This helps us see how well the model performed.

5. **Saving the Trained Model:**
   - After training, the model is saved as a file. This way, you can use the same model later to predict prices for other stocks without retraining it from scratch.

**File 2: app.py - Building a User-Friendly Web App**

1. **Web App Interface:**
   - This file creates a web app using Streamlit, a framework for building data apps. The app has a user-friendly interface where you can enter a stock ticker symbol (e.g., AAPL), start date, and end date.

2. **Downloading and Preprocessing Data from User Input:**
   - Based on your input, the app fetches new historical data for that specific stock and date range using `yfinance`.
   - Similar to file 1, the app cleans and prepares the downloaded data for prediction.

3. **Using the Trained Model for Prediction on New Data:**
   - The app retrieves the pre-trained model (saved from file 1).
   - It uses the model to predict future prices for the stock you entered, considering the data for the specified date range.

4. **Visualization on the Web App:**
   - The app displays charts showing the predicted closing prices for the chosen stock. If available, it also shows the actual historical closing prices for comparison.

**Important Note:**

* Predicting stock prices is a complex task, and these models are not always accurate. The future price of a stock is influenced by many factors beyond historical data.
* This system is for educational purposes only and should not be used for making investment decisions. 

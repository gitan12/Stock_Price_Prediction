### README for Stock Market Prediction Application

#### Overview
This project involves building a stock market prediction application using historical stock data. The application predicts future stock prices using machine learning models and displays the predictions along with moving averages. The user can input a stock ticker and a date range to get the predicted stock prices and visualizations.

#### Prerequisites
Before running the application, ensure that you have the following Python packages installed. You can install them using the provided `requirement.txt` file.

#### Installation
1. **Clone the repository** (if applicable) or download the project files.
2. **Install the required packages**:
   ```sh
   pip install -r requirement.txt
   ```
   
   The `requirement.txt` file includes:
   - streamlit
   - pandas
   - numpy
   - matplotlib
   - yfinance
   - scikit-learn
   - keras
   - tensorflow

#### Files in the Project
1. **`app.py`**: The main application file to run the Streamlit web app.
2. **`Stock Market Prediction.ipynb`**: Jupyter Notebook containing the development and experimentation code for the prediction model.
3. **Images**: Two images showing the application interface and results.

#### Running the Application
To run the application, use the following command in your terminal:
```sh
streamlit run app.py
```

#### Detailed Explanation of the Files

**1. `app.py`**
- **Imports and Libraries**: The script imports necessary libraries including `streamlit`, `pandas`, `numpy`, `matplotlib.pyplot`, `yfinance`, `scikit-learn`, `keras`, and `tensorflow`.
- **User Input**: The user is prompted to input a stock ticker, start date, and end date.
- **Data Retrieval**: Historical stock data is fetched from Yahoo Finance using the `yfinance` library.
- **Data Processing**: The data is processed to calculate the 100-day and 200-day moving averages.
- **Model Training and Prediction**: A machine learning model is trained using the historical stock data. The script uses Keras and TensorFlow for building and training the model.
- **Visualization**: The results, including the moving averages and predicted stock prices, are plotted using `matplotlib` and displayed on the Streamlit app.

**2. `Stock Market Prediction.ipynb`**
- This notebook includes the detailed steps for data preprocessing, model training, and evaluation. It serves as a development and experimentation environment where different models and approaches can be tested before being integrated into the `app.py`.

**3. Images**
- These images show the interface and output of the Streamlit application.
   - **Image 1**: Shows the stock ticker input, date range input, a table of the latest stock prices, and a plot of the 100-day and 200-day moving averages.
   - ![WhatsApp Image 2024-06-03 at 1 30 35 PM](https://github.com/gitan12/Stock-Market-Prediction-/assets/152585363/be161d5b-e4f3-46b1-a79d-af2eebe02c77)

   - 
   - **Image 2**: Displays the model's predicted prices overlaid with the original prices to show the accuracy of the predictions.
   - ![WhatsApp Image 2024-06-03 at 1 30 15 PM](https://github.com/gitan12/Stock-Market-Prediction-/assets/152585363/325785ee-4404-4355-8d06-6e656bd7c809)


#### Steps to Use the Application
1. **Open Terminal**: Navigate to the project directory.
2. **Run the Application**: Execute the command `streamlit run app.py`.
3. **Input Parameters**: In the web interface, enter the stock ticker (e.g., `ADANIPORTS.NS`), start date, and end date.
4. **View Results**: The application will display the latest stock prices, moving averages, and predicted prices.

### Example Results
The following are screenshots of the application output:

- **Input Parameters and Moving Averages**
![Moving Averages](data:image/jpeg;base64,`file-xeLfG10NTTCTHMZQZiYGtjV3`)

- **Predicted Prices**
![Predicted Prices](data:image/jpeg;base64,`file-VWtz6CHsfE017K4jlV2780Th`)

These images demonstrate the application’s capability to fetch, process, and visualize stock market data effectively.

#### Conclusion
This application is a powerful tool for predicting stock prices using historical data and machine learning. By following the instructions in this README, users can set up and run the application to make their own stock market predictions.

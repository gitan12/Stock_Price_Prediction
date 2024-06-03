import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from keras.layers import Dense, Dropout, LSTM
from keras.models import Sequential
import time

st.title('Stock Price Prediction')

# Sidebar for user input
st.sidebar.header('User Input Parameters')

def user_input_features():
    stock = st.sidebar.text_input('Stock Ticker', 'TATASTEEL.NS')
    start_date = st.sidebar.date_input('Start Date', pd.to_datetime('2004-01-01'))
    end_date = st.sidebar.date_input('End Date', pd.to_datetime('2024-05-28'))
    return stock, start_date, end_date

stock, start_date, end_date = user_input_features()

# Fetching the data
data = yf.download(stock, start=start_date, end=end_date)

if data.empty:
    st.write("Invalid Stock Ticker or Date Range. Please try again.")
else:
    st.write(f'Showing data for: {stock}')
    st.write(data.tail())

    #  Adding Index No.
    data.reset_index(inplace=True)

    # Moving Averages
    st.subheader('100-Day and 200-Day Moving Averages')
    MA_100_days = data.Close.rolling(100).mean()
    MA_200_days = data.Close.rolling(200).mean()

    plt.figure(figsize=(10, 6))
    plt.plot(MA_100_days, 'r', label='100-Day MA')
    plt.plot(MA_200_days, 'b', label='200-Day MA')
    plt.plot(data.Close, 'g', label='Closing Price')
    plt.legend()
    st.pyplot(plt)

    # Data Preparation
    data.dropna(inplace=True)
    data_train = pd.DataFrame(data.Close[0: int(len(data)*0.80)])
    data_test = pd.DataFrame(data.Close[int(len(data)*0.80): len(data)])

    scaler = MinMaxScaler(feature_range=(0,1))
    data_train_scale = scaler.fit_transform(data_train)

    x_train = []
    y_train = []

    for i in range(100, data_train_scale.shape[0]):
        x_train.append(data_train_scale[i-100:i])
        y_train.append(data_train_scale[i,0])

    x_train, y_train = np.array(x_train), np.array(y_train)

    # Model Building
    model = Sequential()
    model.add(LSTM(units=50, activation='relu', return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=60, activation='relu', return_sequences=True))
    model.add(Dropout(0.3))
    model.add(LSTM(units=80, activation='relu', return_sequences=True))
    model.add(Dropout(0.4))
    model.add(LSTM(units=120, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(units=1))

    model.compile(optimizer='adam', loss='mean_squared_error')

    with st.spinner('Training the model...'):
        model.fit(x_train, y_train, epochs=50, batch_size=32, verbose=0)
        time.sleep(1)
    st.success('Model trained successfully!')

    pas_100_days = data_train.tail(100)
    data_test = pd.concat([pas_100_days, data_test], ignore_index=True)
    data_test_scale = scaler.fit_transform(data_test)

    x_test = []
    y_test = []

    for i in range(100, data_test_scale.shape[0]):
        x_test.append(data_test_scale[i-100:i])
        y_test.append(data_test_scale[i,0])
        
    x_test, y_test = np.array(x_test), np.array(y_test)
    y_predict = model.predict(x_test)

    scale = 1/scaler.scale_
    y_predict = y_predict * scale
    y_test = y_test * scale

    plt.figure(figsize=(10, 8))
    plt.plot(y_predict, 'r', label='Predicted Price')
    plt.plot(y_test, 'g', label='Original Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    st.pyplot(plt)

    model.save('Stock_Predictions_Model.keras')
    st.write('Model saved as "Stock_Predictions_Model.keras"')


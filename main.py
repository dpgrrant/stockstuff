from xgboost import XGBRegressor
import numpy as np
import pandas as pd


from pandas_datareader import data as pdr
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
# import yfinance
# import matplotlib.pyplot as plt
# import datetime
# import mplfinance as mpf


def main():

    # Extrating data
    data = pdr.get_data_yahoo(['AAPL'],'2010-3-01','2022-01-28')



    data = data[["Close"]].copy()
    data["returns"]=data.Close.pct_change()
    data["log_returns"]=np.log(1+data["returns"])
    
    data.dropna(inplace=True)
    
    X=data[["Close","log_returns"]].values
    scaler=MinMaxScaler(feature_range=(0,1)).fit(X)
    X_scaled=scaler.transform(X)
    # print(X_scaled)
    Y=[x[0] for x in X_scaled]
    
    # print(Y)
    
    split=int(len(X_scaled)*.8)
    
    X_train=X_scaled[:split]
    X_test=X_scaled[split:len(X_scaled)]
    Y_train=Y[:split]
    Y_test=Y[split:len(Y)]
    
    
    # print(Y_train[0],X_train[0])
    # print( len(X_train),len(Y_train))
    # print( len(X_test),len(Y_test))
    
    # Y_train=Y_train[1:]
    # Y_test=Y_test[1:]
    # X_train=X_train[:-1]
    # X_test=X_test[:-1]
    

    # print(Y_train[0])
    # print(X_train)
    
    # print( len(X_train),len(Y_train))
    # print( len(X_test),len(Y_test))
    
    
    assert len(X_train) == len(Y_train)
    assert len(X_test) == len(Y_test)
    
    
    
    
    

    # train, test= train_test_split(X_scaled,0.2)
    
    
    # print(xgb_predict(train,test[0,0]))
    
    # rmse,y,pred=validate(data,0.2)
    
    # print(rmse)
    # print(y)
    # print(pred)



def validate(data,perc):
    predictions=[]
    train,test = train_test_split(data, perc)
    history=[x for x in train]
    
    for i in range(len(test)):
        test_X,test_y=test[i,:-1],test[i,-1]
        
        pred=xgb_predict(history, test_X[0])
        
        predictions.append(pred)
        
        history.append(test[i])
        
    error=mean_squared_error(test[:,-1],predictions,squared=False)
    return error,test[:,-1],predictions



def xgb_predict(Xtrain,YTrain,val):
    train=np.array(train)
    
    Xnew, Ynew=train[:,:-1],train[:,-1]
    
    model=XGBRegressor(objective="reg:squarederror",n_estimamtors=1000)
    model.fit(Xnew,Ynew)
    
    val=np.array(val).reshape(1,-1)
    pred=model.predict(val)
    return pred[0]
    

def train_test_split(data,perc):
    split=int(len(data)*.8)
    
    train=data[:split]
    test=data[split:len(data)]
    
    return train,test



if __name__ == "__main__":
    main()    



# data["EMA9"]=data['AAPL'].ewm(span=9, adjust=False).mean()
# data["MA9"]=data['AAPL'].rolling(9).mean()
# data["MA50"]=data['AAPL'].rolling(50).mean()
# data["MA100"]=data['AAPL'].rolling(100).mean()
# data["MA200"]=data['AAPL'].rolling(200).mean()
# data["High"]=temp['High']
# data["Low"]=temp['Low']
# data["Volume"]=temp['Volume']
# data["Open"]= temp['Open']





# MA9=data['AAPL'].rolling(9).mean()
# EMA9=data['AAPL'].ewm(span=9, adjust=False).mean()
# MA21=data['AAPL'].rolling(21).mean()
# MA50=data['AAPL'].rolling(50).mean()
# MA100=data['AAPL'].rolling(100).mean()
# MA200=data['AAPL'].rolling(200).mean()




# plt.plot(data['AAPL'],label= 'Close')
# plt.plot(EMA9,label= 'EMA 9 days')
# plt.plot(MA100,label= 'MA 100 days')
# plt.legend(loc='best')
# plt.title('APPLE \nClose and Moving Averages')
# plt.show()






import argparse
import pandas as pd 
from split_data import split_data
from get_data import read_params
from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score as r2,mean_absolute_error as mae,mean_squared_error as rmse

def train_and_evaluate(config_path):
    
    config=read_params(config_path)
    processed_train_data=config['split_data']['train_path']
    processed_test_data=config['split_data']['test_path']

    train_data=pd.read_csv(processed_train_data,sep=',',encoding='utf-8')
    test_data=pd.read_csv(processed_test_data,sep=',',encoding='utf-8')
    std=StandardScaler()
    x_train_std=std.fit_transform(train_data.drop(columns='TARGET'))
    x_test_std=std.fit_transform(test_data.drop(columns='TARGET'))
    y_train=train_data['TARGET']
    y_test=test_data['TARGET']
    alpha=config['estimators']['ElasticNet']['params']['alpha']
    l1_ratio=config['estimators']['ElasticNet']['params']['l1_ratio']
    
    regr=ElasticNet(random_state=42,l1_ratio=l1_ratio,alpha=alpha)
    regr.fit(x_train_std,y_train) 
    y_pred=regr.predict(x_test_std)  
    print(f"root mean squared error : {(rmse(y_test,y_pred))}")
    print(f"mean absolute error : {(mae(test_data['TARGET'],y_pred))}")
    print(f"r2 score : {(r2(test_data['TARGET'],y_pred))}")
    print(f"coeffients : {regr.coef_}")
    print(f"intercept : {regr.intercept_}")







if __name__=="__main__":
    arg=argparse.ArgumentParser()
    arg.add_argument("--config",default="params.yaml")
    parsed_arg=arg.parse_args()
    train_and_evaluate(config_path=parsed_arg.config)
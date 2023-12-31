import argparse
import pandas as pd 
from load_data import load_and_save
from get_data import read_params
from sklearn.model_selection import train_test_split

def split_data(config_path):
    config=read_params(config_path)
    data_path=config['load_data']['raw_dataset_csv']
    #print(data_path)
    df=pd.read_csv(data_path,sep=',',encoding='utf-8')
    #print(df.head())
    new_cols=df.columns
    #print(new_cols)
    test_size=config['split_data']['test_size']
    random_state=config['base']['random_state']
    TARGET=config['base']['target_col']
    x=df.drop(columns=TARGET)
    y=df[TARGET]
    test_size=config['split_data']['test_size']
    random_state=config['base']['random_state']
    TARGET=config['base']['target_col']
    print(test_size,random_state,TARGET)
    x_train,x_test,y_train,y_test=train_test_split( x,y,
                                    test_size=test_size,random_state=random_state
                                     )
    train_data=pd.concat([x_train,y_train],axis=1)
    test_data=pd.concat([x_test,y_test],axis=1)
    processed_train_data=config['split_data']['train_path']
    processed_test_data=config['split_data']['test_path']
    #print(processed_train_data)
    train_data.to_csv(processed_train_data,sep=',',index=False,header=new_cols)
    test_data.to_csv(processed_test_data,sep=',',index=False,header=new_cols)




if __name__=="__main__":
    arg=argparse.ArgumentParser()
    arg.add_argument("--config",default="params.yaml")
    parsed_arg=arg.parse_args()
    split_data(config_path=parsed_arg.config)
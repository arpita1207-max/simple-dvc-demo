# read data frm data source
#save it in the raw/data for further process
import os
from get_data import read_params,get_data
import argparse
import pandas as pd 

def load_and_save(config_path):
    config=read_params(config_path)
    data_path=config["data_source"]["s3_source"]
    df=pd.read_csv(data_path,sep=',',encoding='utf-8')
    new_cols=[col.replace(" ","_") for col in df.columns]
    raw_data_path=config['load_data']['raw_dataset_csv']
    df.to_csv(raw_data_path,sep=",",index=False,header=new_cols)
    #print(new_cols)

if __name__=="__main__":
    arg=argparse.ArgumentParser()
    arg.add_argument("--config",default="params.yaml")
    parsed_arg=arg.parse_args()
    load_and_save(config_path=parsed_arg.config)
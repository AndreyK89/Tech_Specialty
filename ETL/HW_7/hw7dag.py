from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime, timedelta
import pendulum
import requests
import pandas as pd
from sqlalchemy import inspect,create_engine
from dateutil.relativedelta import relativedelta
from pandas.io import sql
import time
import matplotlib.pyplot as plt

def tab4b_to_graphic(**kwargs):
    con=create_engine("mysql://Airflow:1@localhost:33061/spark")
    df = pd.read_sql('SELECT * FROM tasketl4b', con)
    print(df)
    ax = plt.gca()
    ax.ticklabel_format(style='plain')
# bar plot
    df.plot(kind='line', 
            x='№', 
            y='долг', 
            color='blue', ax=ax, label = 'Долг')
    df.plot(kind='line', 
            x='№', 
            y='проценты', 
            color='red', ax=ax, label = 'Проценты')
    plt.title('Ежемесячный платеж 86 689 р.')
    plt.grid ( True )
    ax.set(xlabel='Месяц')
    plt.savefig('/home/andrey/tab4b_graphic.png')

###############################
def hw_7_get_temp(**kwargs):

    ti = kwargs['ti']

    city = "Tobolsk"

    api_key = "9e09ab59b55473a15edd2c94a4dba25c"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    payload = {}

    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    # ti.xcom_push(key='hw_7_open_weather', value=round(float(response.json()['main']['temp'])-273.15, 2)

    return round(float(response.json()['main']['temp'])-273.15, 2)

def temp_rec_sql(ti):

    temp = int(ti.xcom_pull(task_ids='hw_7_get_temperature_task'))
    
    con=create_engine("mysql://Airflow:1@localhost:33061/spark")
    
    columns = ['Время', 'Температура.C']
    
    df = pd.DataFrame(columns=columns)
    
    df.loc[ len(df.index )] = [pd.Timestamp.now(), temp]

    df.to_sql('temp_Tobolsk',con,schema='spark',if_exists='append',index=False)
  
with DAG(

        'hw_7_temp_Tobolsk',

        start_date=datetime(2024, 1, 1),

        catchup=False,

        tags=['homework_ETL'],

) as dag:

    hw_7_get_temperature_task = PythonOperator(

        task_id='hw_7_get_temperature_task',

        python_callable=hw_7_get_temp,

    )

    hw_7_add_temperature = PythonOperator(
    
        task_id='hw_7_add_temperature',
        
        python_callable=temp_rec_sql,
        
    )
    
    hw_7_task_graphic = PythonOperator(
    
        task_id='hw_7_draw_graphic',
        
        python_callable=tab4b_to_graphic,
        
    ) 


    hw_7_get_temperature_task >> hw_7_add_temperature
    hw_7_task_graphic
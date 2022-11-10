# more complex skeleton: https://github.com/stacktonic-com/apache-airflow-dag-example-template/blob/master/apache_airflow_2.x_starter_template.py
# libraries 
import json
import os
from datetime import datetime, timedelta

from airflow.decorators import dag, task
# airflow
from airflow.models import DAG, Variable
from airflow.operators.bash import BashOperator
# airflow operators
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup

#  dag settings
DAG_OWNER_NAME = 'Naima'
DAG_NAME = 'dag_skeleton' 
''' 
    name should be unique.
    you can have multiple dag versions by changing the dag name
    and adding v1, v2, v3, etc. to the end of the dag name '''
DAG_DESCRIPTION = 'example skeleton dag description'
DAG_START_DATE = days_ago(1)
'''
    DAG_START_DATE = datetime(2021, 1, 1)
    DAG_START_DATE = datetime.now()
    DAG_START_DATE = datetime.now() - timedelta(days=1)

'''
DAG_SCHEDULE_INTERVAL = '@daily' 
'''
    None = manual
    @once - run once
    @hourly - run once an hour
    @daily - run once a day
    @weekly - run once a week
    @monthly - run once a month
    @yearly - run once a year
    crons: '0 0 * * *' https://crontab.guru/
'''
DAG_CATCHUP = False # When set to true, DAG will start running from DAG_START_DATE instead of current date
DAG_PAUSED_UPON_CREATION = True # Defaults to False. When set to True, uploading a DAG for the first time, the DAG doesn't start directly 

# dag default arguments

default_args = {
    "owner": DAG_OWNER_NAME,
    "start_date": DAG_START_DATE,
    "depends_on_past": False,
    "email": ['naima@fakeemail.com'],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 2, # Max. number of retries before failing
    "retry_delay": timedelta(minutes=60) # Retry delay

}

# normal python function
def print_hello():
    print("Hello World")

# python function with parameters
def print_hello_with_params(name, age):
    print("Hello {} you are {} years old".format(name, age))



# instantiate dag
with DAG(   
    dag_id=DAG_NAME,
    default_args=default_args,
    description=DAG_DESCRIPTION,
    schedule_interval=DAG_SCHEDULE_INTERVAL,
    catchup=DAG_CATCHUP,
    is_paused_upon_creation=DAG_PAUSED_UPON_CREATION
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the first task!"
    )
    task2 = PythonOperator(
        task_id='second_task',
        python_callable=print_hello
    )
    task3 = PythonOperator(
        task_id='third_task',
        python_callable=print_hello_with_params,
        op_kwargs={'name': 'Naima', 'age': 25}
    )

    task4= BashOperator(
        task_id='fourth_task',
        bash_command="echo goodbye world, this is the last task!"
    )

    
    task1 >> task2 >> task3 >> task4

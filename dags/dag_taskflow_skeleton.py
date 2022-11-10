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
DAG_NAME = 'dag_taskflow_skeleton' 
''' 
    name should be unique.
    you can have multiple dag versions by changing the dag name
    and adding v1, v2, v3, etc. to the end of the dag name '''
DAG_DESCRIPTION = 'example taskflow skeleton dag description'
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



# instantiate dag
@dag(   
    dag_id=DAG_NAME,
    default_args=default_args,
    description=DAG_DESCRIPTION,
    schedule_interval=DAG_SCHEDULE_INTERVAL,
    catchup=DAG_CATCHUP,
    is_paused_upon_creation=DAG_PAUSED_UPON_CREATION
)
def dag_taskflow_skeleton(): # dag name
    @task 
    def get_list1():
        list1 = ['a', 'b', 'c']
        return list1
    
    @task
    def get_list2():
        list2 = ['a', 'd', 'c']
        return list2

    @task
    def compare_lists(list1, list2):
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                print(f"{list1[i]} does not match {list2[i]}")
    
    compare_lists(get_list1(), get_list2())

dag_taskflow_skeleton() # instantiate dag
    
    

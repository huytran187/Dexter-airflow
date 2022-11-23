# Trying to figure out where to begin or what api I want to utilize for this project. May use a weather api, maybe music, maybe add ML capabilities if I get that far
# import libraries will increase as the project goes on
from datetime import datetime, timedelta # airflow modules
from airflow import DAG
from airflow.operators.bash_operator import BashOperator 

# begin with calling the api 
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    # Start on 27th of June, 2020
    'start_date': datetime(2022, 11, 23),
    'email': ['tyler.dex@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    # In case of errors, do one retry
    'retries': 1,
    # Do the retry with 30 seconds delay after the error
    'retry_delay': timedelta(seconds=30),
    # Run once every 15 minutes
    'schedule_interval': '*/15 * * * *'
}

# then 
with DAG(    dag_id=’project_dag’,
    default_args=default_args,
    schedule_interval=None,
    tags=[‘my_dags’],
) as dag:    #Here we define our first task
    t1 = BashOperator(bash_command=”touch /home/Rex/jetbrains-toolbox-1.26.5.13419/Py/Dexter-airflow/my_bash_file.txt”, task_id=”create_file”)    #Here we define our second task
    t2 = BashOperator(bash_command=”mv /home/Rex/jetbrains-toolbox-1.26.5.13419/Py/Dexter-airflow/my_bash_file.txt ~/my_bash_file_changed.txt”, task_id=”change_file_name”)    # Configure T2 to be dependent on T1’s execution
    t1 >> t2


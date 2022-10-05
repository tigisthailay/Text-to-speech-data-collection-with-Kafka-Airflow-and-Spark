from curses import echo
from random import randint
from warnings import catch_warnings
from airflow import DAG
from airflow import PythonOperator ,  BranchPythonOperator
from airflow import BashOperator

from datetime import datetime

def _choose_best_model(ti):
    accuracies = ti.xcom_pull( task_ids=[
        'training_model_A',
        'training_model_B',
        'training_model_C']
                 )
    best_accuracy = max(accuracies)
    if (best_accuracy > 8):
        return 'accurate'
    return 'inaccurate'
        
def _training_model():
    return randint(1, 10)
with DAG("Dataengin", start_date= datetime(2022, 1, 1),
         schedule_interval= "@daily",catchup=False) as dag:
    training_model_A= PythonOperator( task_id="trainig_model_A" ,
        python_callable=_training_model
        )
    
    training_model_B= PythonOperator( task_id="trainig_model_B" ,
        python_callable=_training_model
        )
    
    training_model_C= PythonOperator( task_id="trainig_model_C" ,
        python_callable=_training_model
        )
    
    choose_best_model =BranchPythonOperator(
            task_id="choose_best_model",
            python_callable= _choose_best_model 
        )
    accurate = BashOperator(
            task_id= "accurate", 
            bash_command="echo 'accurate'"
        )
        
    inaccurate = BashOperator(
            task_id= "inaccurate", 
            bash_command="echo 'inaccurate'"
        )
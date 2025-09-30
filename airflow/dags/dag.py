from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

from data_ingestion.scraper import (
    get_application_list,
    get_game_information,
    get_game_review,
)


default_arguments = {
    "owner": "NJR202-02-22",

    "retries": 1,
    "retry_delay": timedelta(minutes=1),
    "depends_on_past": False,
    # "email": [""],
    # "email_on_failure": False,
    # "email_on_retry": False,
}


def step_1(**context):
    application_list = get_application_list()
    print(len(application_list))
    return application_list

def step_2(**context):
    application_list = context["task_instance"].xcom_pull(task_ids="step_1")
    
    for item in application_list[:25]:
        application_id = item.get("appid")
        get_game_information(application_id)

def split(k):
    



with DAG(
    dag_id="dag",
    default_args=default_arguments,
    description="",
    schedule_interval="0 * * * *",  # 每小時執行
    start_date=datetime(2025, 9, 30),
    catchup=False,
    tags=["steam"],
) as dag:
    
    start_task = DummyOperator(
        task_id="start"
    )

    step_1_task = PythonOperator(
        task_id="step_1",
        python_callable=step_1,
    )

    step_2_task = PythonOperator(
        task_id="step_2",
        python_callable=step_2,
    )

    # get_application_list_op = PythonOperator(
    #     task_id="get_application_list",
    #     python_callable=get_application_list,
    # )
    
    # get_game_information_op = PythonOperator(
    #     task_id="get_game_information",
    #     python_callable=get_game_information,
    #     # op_args=[],
    # )

    # get_game_review_op = PythonOperator(
    #     task_id="get_game_review",
    #     python_callable=get_game_review,
    # )

    end_task = DummyOperator(
        task_id="end"
    )

    start_task >> step_1_task >> step_2_task >> end_task
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


with DAG(dag_id='scrapy_dag',start_date=datetime(2023,5,23),
         schedule_interval='@daily',catchup=False) as dag:
    
    
    
    wanted_spider = BashOperator(
        task_id='run_wanted_spider',
        bash_command='cd ${AIRFLOW_HOME}/dags/wanted && pip install --no-cache-dir -r requirements.txt && scrapy crawl wanted',
    )

    saramin_spider = BashOperator(
        task_id='run_saramin_spider',
        bash_command='cd ${AIRFLOW_HOME}/dags/saramin && pip install --no-cache-dir -r requirements.txt && scrapy crawl saramin',
    )

wanted_spider >> saramin_spider

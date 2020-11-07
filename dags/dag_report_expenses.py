# Importing Airflow's features
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

# Importing Python code
from datetime import timedelta

from python.scraper import scrap_the_web
from python.processor import process_data
from python.mailer import send_email

# Setting DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': 'arturskrzeta@gmail.com',
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
	dag_id='FX_Rates_Expense_Report',
	default_args=default_args,
	schedule_interval='0 0 * * *',
)

# Setting Tasks
scraping = PythonOperator(
	task_id='scraping',
	python_callable=scrap_the_web,
	dag=dag
)

processing = PythonOperator(
	task_id='processing',
	python_callable=process_data,
	dag=dag
)


mailing = PythonOperator(
	task_id='mailing',
	python_callable=send_email,
	dag=dag
)

# Setting Dependencies
scraping >> processing >> mailing

if __name__ == "__main__":
    dag.cli()

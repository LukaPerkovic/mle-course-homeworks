from airflow.models import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.task_group import TaskGroup

from datetime import datetime


from scripts.preprocess_data import preprocess_data
from scripts.handle_data import store_data
from scripts.train_model import train_model
from scripts.retrain_model import retrain_model
from scripts.choose_best import choose_best
from scripts.serve_model import serve_model


default_args = {
	'owner': 'Luka Perkovic',
	'email_on_failure': False,
	'start_date': datetime.today()
}

with DAG(
	'ml_pipeline',
	description='Data processing pipeline written with PySpark',
	schedule_interval=None,
	default_args=default_args,
	catchup=False) as dag:

	# task 2
	preprocessing_data = PythonOperator(
		task_id='processing_data',
		python_callable=preprocess_data
		)

	# task 3
	storing_data = PythonOperator(
		task_id='storing_processed_data',
		python_callable=store_data
		)

	# task 4
	with TaskGroup('training_and_retraining_the_model') as training_model:

		# task 4.1
		training_model = PythonOperator(
			task_id='training_model',
			python_callable=train_model
			)

		# task 4.2
		retraining_model = PythonOperator(
			task_id='retraining_model',
			python_callable=retrain_model
			)

	# task 5
	choosing_best = PythonOperator(
		task_id='choosing_model',
		python_callable=choose_best
		)


	# task 6
	serving_model = PythonOperator(
		task_id='serving_model',
		python_callable=serve_model
		)



	preprocessing_data  >> storing_data >> training_model >> choosing_best >> serving_model

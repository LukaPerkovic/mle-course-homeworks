# MLOps Coursework
## Pipeline

### Airflow

#### Description:
One pipeline to handle complete process - From ingesting data to serving model.

Since there's no input stream of data available, we are using the same file for the whole process.
Retraining logic has been set up, but in order to avoid making duplicate data it is currently dropping and replacing the table in database. Key logic to change if we had real input stream of batch data is changing if_exists='replace' with if_exists='append'. This way we have new stream of data, and we are keeping up with retraining the model.

Pipepine steps:

- Task 1: Creates table for processed data (used for retraining model)
- Task 2: Preprocessing data (taking data_batch.csv file) and creating a transformed version in /data folder.
- Task 3: Picking up transformed version and storing it in table created in Task 1
- Task 4: Training model - Contains both training anew (from transformed .csv) and retraining (from postgres table). Both version of model are stored in /models folder
- Task 5: Accessing what is the best model per accuracy and placing it in /best_model directory
- Task 6: Picking up the best model and serving it via Airflow Logs for this specific task (serving_model)

#### Installation:

1. Clone the repository and navigate to /pipeline_hw
2. Run the command line  ```chmod -R 777 .```
2. There run the command:
```docker build . --tag extending_airflow:latest``` .
This step is needed in order to enable writing requirements.txt in Production environment, but as well to install JDK, Hadoop, and Spark dependencies needed for Pyspark.
3. Run the command: ```docker compose up``` .
This will initiate the containers and start the webserver on localhost:8080
4. If prompted for Airflow user/pass it will be: airflow/airflow
5. After finishing Airflow, run ```docker compose down```




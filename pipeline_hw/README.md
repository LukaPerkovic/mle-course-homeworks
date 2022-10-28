# MLOps Coursework
## Pipeline

### Airflow


TASK 1 - ETL pipeline:

- Fetch batches from the source
- Preprocess and transform the data
- Store the data for future steps

TASK 2 - Model Training pipeline:

- Split the data in train and test sets
- Perform k fold cross-validated training for hyper
- Store the experimental results
- Save the model

TASK 3 - Model Serving pipeline:

- Use the data from Task 1
- Use the model from Task 2
- Produce results


sudo chmod u=rwx,g=rwx,o=rwx logs
  sudo chmod -R a+rw data
  sudo chmod -R a+rw models
  sudo chmod -R a+rw best_model

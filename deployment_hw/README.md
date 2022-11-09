# MLOps Coursework
## Deployment

### Flask, Docker, Kubernetes


#### Model: Suicide Likelihood

Model that predicts suicide probabilty considering country of origin, gender and years.

#### Installation

There are two ways to deploy the app.
Via Docker and via Kubernetes. This installation instruction assumes that you already installed either/both correctly.

**Docker**

Two ways.

From Dockefile:
  Navigate to the folder containing Dockerfile and run:
  ```docker build . --tag lukaperkovic/suicide-api```
  
From Docker Hub:
  ```docker pull lukaperkovic/suicide-api:latest```

To run the container:
```docker run -p 5000:5000 lukaperkovic/suicide-api```

The API can be accessed: localhost:5000/predict
  
**Kubernetes**

First start the cluster.
For minikube is simple as ```minikube start```

To deploy
```kubectl create deployment suicide --image=lukaperkovic/suicide-api:latest```

To expose:
```kubectl expose deployment suicide --port 5000 --type=LoadBalancer --name suicide-service```


To find out what URL is the app available run: ```minikube service list```
And there find what is the URL of suicide-service.

The API can be accessed {Whatever host you found in previous result} + /predict
For example my URL was: http://192.168.49.2:32490/predict

### Use

API handles both single entries, but also multiple entries in the form of .csv file.

Depending on which way you elected (Docker or Kubernetes), address will vary. For these examples we will use localhost:5000

**Single record:**
After accessing the localhost:5000/predict you will see necessary boxes to fill which are pretty self-explanatory.
Submitting the request will display result with prediction. (Almost all are  below 1%, but difference between them can be pretty drastic)

NOTE: There are 100 countries in the database. To be sure, consult scripts/params.py. Choosing non-existing country or mistaking types will result in error.

**Multi record:**

For this you create a csv.

![image](https://user-images.githubusercontent.com/51373370/200920879-d648686a-7ebc-42c1-a5dc-02364f53ddc7.png)

Or if creating a csv in text file, make sure it's correct formatting. Also make sure to specify the correct path.
_(Easiest way is to have .csv file at same location where you're running command in terminal)_

To send a post request:
```curl --location --request POST 'http://localhost:5000/predict' --form 'data=example.csv' ```

Results will be in form of a list displayed in the terminal.
  

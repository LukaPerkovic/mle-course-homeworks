### Experiment tracking - MLFlow

Navigate to the folder this read-me file is in (exp_tracking_hw). <br/>
Experiments are preconfigured, and written down in docker-compose.yml file in the command line of client service. <br/>
To add more experiemnts follow the format: python train.py \<model\> \<parameter> \<outliers\> <br/>
Parameters:
- **Model** - Can be 'randomforest' or 'gradientboost'
- **Parameter** - If randomforest then integer for _n_estimators_ should be set; If gradientboost then float for _learning_rate_ should be set.
- **Outliers** - Can be 'exclude' or 'include' to remove or not remove outliers with Isolation Forest model

After editing the experiments, save and close the docker-compose.yml file.<br/>

To run the mlflow server, run in the terminal<br/>
```docker compose up```

After process is finished, open your browser to the localhost (127.0.0.1:5000) to see the results of the experiments in MLFlow.<br/>

To decontruct containers after done using, exit the server with Ctrl+C, and then enter next line in terminal:<br/>
```docker compose down```

## Prequistes 
- Use python3.9 or newer

------------------------------------
## Prerequistes
### Create Virtual Environment
```
python3 -m venv <FOLDER-NAME>
```
### Activate Virtual Environment
```
source <FOLDER-NAME>/bin/activate
```
### Install Python Packages
```
pip install -r requirements.txt
```
## Run app
```
python app.py
```

## To Do
- Configure app to use Aurora RDS instead of sqlite


## Deploying to Heroku
- Create an environment variable for NEW_RELIC_CONFIG_FILE in the project settings. (cli or UI)

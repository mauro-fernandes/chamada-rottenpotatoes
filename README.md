# Dependencies
`poetry` 
Ref. https://python-poetry.org

# Install Dependencies
    poetry install

# Run App
    poetry run flask --app app/webapp run

`or...`

    poetry shell
    flask --app app/webapp run


## Run Flask Shell
    poetry run flask --app app/webapp shell

## Run just "flask run" command (enviroment variable)

    poetry shell

`and..`

###### `$` Unix Bash (Linux, Mac, etc.): 
    export FLASK_APP=app.webapp  

    flask run
 
###### `>` Windows PowerShell:
    $env:FLASK_APP = "app.webapp"
    
    flask run




# Admin DB 
Ref. https://flask-migrate.readthedocs.io/en/latest/
## Create a initial migration repository

    poetry shell
    
    flask db init
    
    flask db migrate -m "Initial migration."
    
    flask db upgrade


###### `$` Unix Bash (Linux, Mac, etc.): 

    export FLASK_APP=app.webapp 
    
    flask seed movies
        
    flask seed users
     

###### `>` Windows PowerShell:

    $env:FLASK_APP = "app.webapp"

    flask seed movies

    flask seed users

## After updating the model
    flask db upgrade


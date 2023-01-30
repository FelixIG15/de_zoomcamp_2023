# Homework
## Question 1
Run this script on Bash
    ```
    $ ./script_1.sh
    ```
## Question 2
1.  Run this script on Bash
    
    ```
    $ ./script_2a.sh
    ```

2.  Run this command in python container
    
    ```
    $ pip list
    ```

## Postgres Setup for Question 3,4,5
1.  Create Network
    ```
    docker network create pg-network
    ```
2.  Run this command on the terminal to setup pgAdmin & postgres DB
    ```
    $ docker-compose up -d
    ```

3.  Run this script on the terminal to build container image
    ```
    $ ./docker_build.sh
    ```

4.  Ingest the data and load it to database
    ```
    $ ./load_data_to_db.sh
    ```

5. Open pgAdmin and connect to Database 

6. Run SQL Queries, see queries on .sql files in this directory.
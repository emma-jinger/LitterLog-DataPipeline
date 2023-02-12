# Cat Data Schema

Repository containing the cat data schema for data storage and visualization using sqlalchemy, alembic, and postgresql
# What does this program do?
It watches new csv files in `/var/nfs/cat_watcher_output` (produced by the CatWatcher program running in the Nano device).
When a new file is found, it loads the data to the database `metabase_catwatcher_db`, which is defined in `config.py`.
This program is setup to be a service running in the background, so it is always running on the server (`cat_tech_server`).
![cat_data_etl.png]()

# Building the Project from Source (Written on 20221108, tested to work in my existing virtual env dir)
**Before building, make sure:** 
- [The metabase service is set up](https://github.com/emma-jinger/Set-Up-a-Service-on-Ubuntu). The metabase unit file at `/etc/systemd/system/metabase.service` and the service env var file at `/etc/default/metabase` defines its setup. 
- The postgres database is set up with the target role, db, and pw.

## Set up a virtual env in the server (optional)
I create a virtual environment `cat_data_pipeline_venv`
## Cloning the Repo to the virtual env directory 
To download the code, navigate to a folder of your choosing on your machine
```
git clone https://github.com/emma-jinger/cat_data.git 
```

## Verify Database info
- `DATABASE_URL` in `config.py` should match database information in the Metabase service env var file `/etc/default/matabase`.
- Value of `sqlalchemy.url` in `CatDataSchema/alembic` should match the above `DATABASE_URL`.
 
## Build the data pipeline project from the directory cat_data (project root)
```
pip install -e . 
```
## Check data from metabase 
Go to the address `http://192.168.1.157:3000`

# Running the Docker Container (Written on 20221108, not tested after writing)

## Cloning the Repo
To download the code, navigate to a folder of your choosing on your machine
```
git clone https://github.com/emma-jinger/cat_data.git 
```
## Build the Docker Image
Build our docker image `cat_data_watcher:latest` by running: 
```
./build.sh
```
## Spin up the containers (metabase, postgres, nginx, and cat_data_watcher)
Before using docker compose to spin the containers up, modify `DATABASE_URL` in `CatDataSchema/config.py` and `sqlalchemy.url` in `CatDataSchema/alembic.ini` to match the `DATABASE_URL` in `prod-docker-compose.yml`: 
```postgresql+psycopg2://metabase_catwatcher_user:metabase_catwatcher_pw@db:5432/metabase_catwatcher_db```

Spin up the container with the commands: 
```
cd docker 
sudo docker compose up -f prod-docker-compose.yml
```
## Check the data on Metabase. 
Go to the browser using `http://192.168.1.157:3001`, you should be able to see cat data whenever there is a new file generated. 


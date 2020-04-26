# ASRG Platform

## Run the app

Use the `run` script in the root directory.


## Initial Setup

This project is using Python3, Flask, Docker (for the postgres development instance) and node.


### .env

This project is using a `.env` file with some config parameters. Make sure you have it in the root folder.

The `.env` file needs to use the following template:

```
POSTGRES_URL="127.0.0.1:5432"
POSTGRES_USER="asrg"
POSTGRES_PW="..."
POSTGRES_DB="platform"
SECRET_KEY="..."
```

Generate a secret key:

```bash
head -n 1 /dev/urandom | base64
```

### Docker

Pull the image.

`sudo docker pull postgres`

I created a script to run the container:

`./postgres`

To stop the instance, use:

`./stop`


### Install Python packages

First create a new virtual environment.

`python3 -m venv venv`

Source into the venv.

`source venv/bin/activate`

Install the requirements.

`pip install -r requirements.txt`

### Install node stuff

`npm i`

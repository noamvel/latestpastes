# Latest Pastes
Latest Pastes is a simple python3 web crawler that crawls the [pastebin.com](https://pastebin.com/) site and stores the most recent "pastes" into storage. 

## Requirements 
* python3 with latest version 3.7.4 installed.
```
python --version
```
If python3 is not installed -> [install python](https://www.python.org/downloads/)

* Clone this project to your desired directory:
```
git clone https://github.com/noamvel/latestpastes.git
```
If git is not installed -> [install git](https://git-scm.com/download)

## Installation
### As python environment 
* It is best to have an isolated python virtual environment.   
From project home directory 'latestpastes' run:
```
python -m venv env
source env/bin/activate
```
* Install project required packages:
```
pip install -r requirements.txt
```
* execute
```
python latestpastes.py
```

### As python docker image
* Make sure you have docker installed and running:
```
docker --version
docker ps
```
If docker is not installed  -> [install docker](https://docs.docker.com/install/)

* build docker image, from project home directory run:
```
docker build -t latestpastes .
```
* execute
```
docker run --name you_decide -v $(pwd):/lpapp latestpastes
```

## Usage

* log
```
latestpastes.log
```
* storage
```
Files - jobs/
TinyDB - db.json
```





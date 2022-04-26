## Description
The goal was to write an app to collect data in a container. Application takes adNetwork and date as input parameters. It then retrieves each report for these input parameters from the URLs provided in advertising_network.YAML and store it in a database. All retrieved reports are saved to the same table called “daily_report”.

Resources used in this project are listed below in the [Useful resources](#useful-resources) section.

## Main bits of the project
* Fetch operation for CSV from Ad network URLs
* Insert operation to database
* Unit tests - missing
* Integration tests - missing

## Structure of the project
```
.
├── advertising_network.yaml
├── collect_data
├── database
│   ├── db.py
│   ├── models.py
│   └── __pycache__
│       ├── db.cpython-38.pyc
│       └── models.cpython-38.pyc
├── docker-compose.yaml
├── Dockerfile
├── main.py
├── Makefile
├── postgres
├── README.md
├── requirements
├── sanity.requirements
└── tests
    ├── integration
    │   └── test_main.py
    └── unit
        ├── test_db.py
        ├── test_main.py
        └── test_models.py


```

## Requirements
To run the project and tests you will need
* [Python Programming language](https://www.python.org/)
* [Docker](https://www.docker.com/get-started)
* [Docker Compose](https://docs.docker.com/compose/install/)

## Examples
First, use the docker-compose file to run the app and database in containers.

```
docker-compose up
```

Connect to the application container.

```
docker exec -it collect_data /bin/bash
```

### Example 
For Fetch and Insert data to a database for SuperNetwork and the date 2017-09-15

```
python main.py -a SuperNetwork -d 2017-09-15
```

For parameters help execute the following command

```
python main.py -h
```

Output

```
usage: main.py [-h] -a {SuperNetwork,AdUmbrella} -d DATE

The application takes adNetwork and date as input parameters. It then retrieves each report for these input parameters from the URLs provided in the advertising_network.YAML file and stores it in a database.

optional arguments:
  -h, --help            show this help message and exit
  -a {SuperNetwork,AdUmbrella}, --adNetwork {SuperNetwork,AdUmbrella}
                        Choose between "SuperNetwork" or "AdUmbrella"
  -d DATE, --date DATE  Date in format "YYYY-MM-DD", Example: 2014-01-28
```


The application will search for particular Ad Network URLs in an advertising_network.YAML. 

Modify the advertising_network.YAML accordingly to add more Ad Networks and their URLs and follow particular form style in a file.

```
--
reports:
  SuperNetwork:
    - https://storage.googleapis.com/expertise-test/supernetwork/report/daily/2017-09-15.csv
    - https://storage.googleapis.com/expertise-test/supernetwork/report/daily/2017-09-16.csvwey

  AdUmbrella:
    - https://storage.googleapis.com/expertise-test/reporting/adumbrella/adumbrella-15_9_2017.csv
    - https://storage.googleapis.com/expertise-test/reporting/adumbrella/adumbrella-16_9_2017.csv
```

### Check database
To check if data was inserted into database follow next commands.

```
docker exec -it postgres_db /bin/bash
```

```
psql -U postgres
```

Now you are able to execute database commands.

`Ctrl+c` to Gracefully stop application

## Running application locally
In `database/models.py` uncomment `LOCAL_DB_URI` and comment `DATABASE_URI` on lines 6 and 8 respectively.

## Testing
Unit tests should be written to test every function within this application. For testing database connection and database insertions [mock](https://docs.python.org/3/library/unittest.mock.html) should be used.

Integrations test should check integrity and idempotency of application.

## Useful resources
* https://docs.python.org/3/library/argparse.html
* https://pyyaml.org/wiki/PyYAMLDocumentation
* https://pandas.pydata.org/pandas-docs/stable/
* https://docs.sqlalchemy.org/en/14/orm/

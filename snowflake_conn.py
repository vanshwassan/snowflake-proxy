import snowflake.connector
import config
import os
import api

conn = snowflake.connector.connect(
    user=config.USER,
    password=config.PASSWORD,
    account='rra02970',
    warehouse='COMPUTE_WH',
    database='COVID19',
    schema='public'
)

# Function connects to Snowflake and sends in a SQL Statement to get the Covid Cases in United States


def getCases():
    curs = conn.cursor()
    curs.execute(
        "SELECT CONFIRMED FROM JHU_DASHBOARD_COVID_19_GLOBAL WHERE COUNTRY_REGION = 'United States' AND PROVINCE_STATE = 'California' AND FIPS = '06000';")
    a = curs.fetchone()[0]

    covid = int(a)
    return covid

# Function to send custom SQL Query as a json body and returns the result

def sendSQL(sql):
    curs = conn.cursor()
    curs.execute(
        (sql)
        )
    data = curs.fetchone()[0]
    return data

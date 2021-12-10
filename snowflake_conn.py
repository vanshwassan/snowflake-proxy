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
        "SELECT SUM(CONFIRMED) FROM JHU_DASHBOARD_COVID_19_GLOBAL WHERE COUNTRY_REGION = 'United States' AND PROVINCE_STATE = 'California';")
    a = curs.fetchone()[0]

    # Dividing by 2 because the Snowflake SQL Query returns SUM(CONFIRMED) + Total Cases in the Dataset Table for some reason so just did this for now

    a = int(a)
    covid = a/2
    return covid

def sendSQL(sql):
    curs = conn.cursor()
    curs.execute(
        (sql)
        )
    data = curs.fetchone()[0]
    return data
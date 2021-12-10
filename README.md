# snowflake-proxy-host
#### A basic proxy API Client that uses Snowflake's Python Connector to get data from their database

------

`/get` GET request to get the total number of COVID-19 cases in California (Updated everyday).

`/post` POST request to send in an sql query in json body and get the response.

### Example:

    {
    "sql": "SELECT DEATHS FROM JHU_DASHBOARD_COVID_19_GLOBAL WHERE COUNTRY_REGION = 'United States' AND PROVINCE_STATE = 'California' AND FIPS = '06000';"
    }

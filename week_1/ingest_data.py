import argparse
import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse
import os
import wget

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = 'output.csv'
    
    # download the csv
    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'

    print("")
    print(f"fetching data from {url}")
    try:
        filename = wget.download(url=url, out=csv_name)
    except:
        os.system(f"wget {url} -O {csv_name}")
    print("")
    print("Download Finished")
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    df = next(df_iter)

    if 'lpep_pickup_datetime' in df.columns and 'lpep_dropoff_datetime' in df.columns:
        df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
        df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])

    #CREATE TABLE
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    df.to_sql(name=table_name, con=engine, if_exists='append')

    while True:
        try:
            t_start = time()

            df = next(df_iter)
            if 'lpep_pickup_datetime' in df.columns and 'lpep_dropoff_datetime' in df.columns:
                df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
                df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])

            df.to_sql(name=table_name, con=engine, if_exists='append')
            
            t_end = time()
            print("inserted another chunk, took %.3f second" % (t_end - t_start))
        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    # user, password, host, port, database name, table name, url of the csv
    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()
    main(args)

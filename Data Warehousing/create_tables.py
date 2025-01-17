import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    
    """
    Executes all drop table queries
    param cur: database cursor
    param conn: database connector
    
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    
    """
    Executes all create table queries
    param cur: database cursor
    param conn: database connector
    return:
    
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    
    """
    Defines configuration parser, imports credentials from dwh.cfg file and opens a conenction with the redshift cluster.
    Dropes the already existing tables and creates new tables again.
    
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
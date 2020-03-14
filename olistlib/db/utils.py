import os
import pdb
import pandas as pd
import sqlalchemy
from tqdm import tqdm

WORK_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(WORK_DIR, 'data')
DB_PATH  = os.path.join(DATA_DIR, 'olist.db')


def import_query(path, **kwargs):
    '''
    Realiza o import de uma query com vários argumentos de import
    '''
    with open(path, 'r', **kwargs) as file_query:
        query = file_query.read()
    return query


def connect_db():
    '''
    Função para conectar ao banco de dados local (sqlite)
    '''
    string_connection = 'sqlite:///{path}'.format(path=DB_PATH)
    connection = sqlalchemy.create_engine(string_connection)
    return connection


def exec_queries(queries, conn):
        for query in tqdm(queries.split(";")[:-1]):
            conn.execute(query)


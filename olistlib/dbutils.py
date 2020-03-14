import os
import pdb
import pandas as pd
import sqlalchemy
from tqdm import tqdm


def import_query(path, **kwargs):
    '''
    Realiza o import de uma query com vários argumentos de import
    '''
    with open(path, 'r', **kwargs) as file_query:
        query = file_query.read()
    return query


def connect_sqlite_db(path):
    '''
    Função para conectar a banco de dados sqlite local
    '''
    string_connection = 'sqlite:///{path}'.format(path=path)
    connection = sqlalchemy.create_engine(string_connection)
    return connection


def exec_queries(queries, conn):
        for query in tqdm(queries.split(";")[:-1]):
            conn.execute(query)


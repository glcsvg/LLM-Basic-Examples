import pandas as pd
from sqlalchemy import create_engine, MetaData,  Table, select

class DatabaseClass:
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///Spotify.db')
        self.connection = self.engine.connect()
        self.metadata = MetaData()
        self.musics = Table('musics', self.metadata, autoload_with=self.engine)


    def get_table(self):

        return self.musics

    def db_execute(self,query):

        ResultProxy = self.connection.execute(query)
        return ResultProxy



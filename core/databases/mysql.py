from .relational import Relational
from sqlalchemy import create_engine, MetaData
from urllib.parse import quote_plus

class MYSQL(Relational):
    def __init__(self, host, username, password, database):
        try:
            self._engine =  create_engine(f"mysql+pymysql://{quote_plus(username)}:{quote_plus(password)}@{host}/{database}", echo=False)
            self._metadata = MetaData()
            self._dialects = self._engine.dialect
            self._metadata.reflect(bind=self._engine)
        except Exception :
            raise Exception("Error connecting Database")
    def metaData(self):
        pass
    
    def cursor(self, *args, **kwargs):
        pass



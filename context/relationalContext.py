from core.databases.mysql import MYSQL
from .context import Context
from sqlalchemy.schema import CreateTable
from sqlalchemy import text

class MySqlContext(Context):
    def __init__(self, *args, **kwargs):
        self.database = MYSQL(*args, **kwargs)
    
    def get_schema_information(self):
        metadata = self.database._metadata
        dialect = self.database._dialects
        self._schema_output = {}

        if not metadata.tables:
            raise Exception("Empty")

        for table_name, table_obj in metadata.tables.items():
            create_table_stmt = CreateTable(table_obj).compile(dialect=dialect)
            schema_string = str(create_table_stmt).strip()
            self._schema_output[table_name] = schema_string.replace("\n\t", '')

    def query(self, query):
        res = []

        with self.database._engine.connect() as connection:
            result = connection.execute(text(query))
            connection.commit()
            for row in result:
                res.append(row)
        
        return res
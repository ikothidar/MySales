import sqlite3

from typing import List, Optional

class SQLite:
    """
    Class to do databse transactions.
    """
    def __init__(self, **kwargs) -> None:
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', 'test')
        self.db = sqlite3.connect(self.filename)
        self._db.row_factory = sqlite3.Row

    def get_data(
        self, 
        query: Optional[str] = None, 
        columns: Optional[List] = None, 
        condition: Optional[str] = None,
        order: Optional[str] = 'ASC',
    ) -> List:
        """
        Execute given query or from passed parametes.

        Args:
            query (Optional[str], optional): Defaults to None.
                Full query to execute directly.
            columns (Optional[List], optional): Defaults to None.
                List of columns to fetch.
            condition (Optional[str], optional): Defaults to None.
                any condition to filter out data.
            order (Optional[str], optional): Defaults to 'ASC'.
                order of the result data.

        Returns:
            List: query result in list format.
        """
        if not query:
            query = f'SELECT '

            if columns:
                query += ', '.join(columns)
            else:
                query += '*'

            query += f' FROM {self.table} '

            if condition:
                query += condition

            query += f'ORDER BY {order} '

        print(f'\nQuery to execute: {query}\n')
        try:
            result = self._db.execute(query)

            return result.fetchall()
        except Exception as ex:
            print(f'\nException occurred: {ex}\n')

    def insert(self, row: dict) -> str:
        """
        Method to insert data into database.

        Args:
            row (dict): Row to be inserted in database.

        Returns:
            result (str): The result of the function.
        """
        columns = '", "'.join(row.keys())
        values = '", "'.join(map(str, row.values()))

        query = (
            f'INSERT INTO {self.table} '
            f'("{columns}") '
            f'VALUES ("{values}")'
        )

        print(f'\nQuery to execute: {query}\n')

        try:
            result = self._db.execute(query)
            self._db.commit()
            return result
        except Exception as ex:
            print(f'\nException occurred: {ex}\n')

    @property
    def filename(self):
        return self._filename
    
    @filename.setter
    def filename(self, fn):
        self._filename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row

    @filename.deleter
    def filename(self):
        self.close()

    @property
    def table(self):
        return self._table
    
    @table.setter
    def table(self, t):
        self._table = t

    @table.deleter
    def table(self):
        self._db.close()
        del self._filename

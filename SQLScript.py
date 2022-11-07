class Database:
    def __init__(self, host, database, user):
        self.con = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=getpass.getpass(prompt="ENTER DB PASSWORD: \n")
        )

    def select(self, attribute, table, additionalData=None):
        """
        SQL Script to select information from a database

        EXAMPLE:
            sqlSelect("*", "producten", "ORDER BY naam DESC")

        :parameter attribute: attribute for the database
        :parameter table: table to select from
        :parameter additionalData: extra attributes
        :type attribute: str
        :type table: str
        :type additionalData: str
        :returns: list
        """
        cur = self.con.cursor()
        if additionalData is None:
            select = f"SELECT {attribute} FROM {table}"
        else:
            select = f"SELECT {attribute} FROM {table} {additionalData}"
        cur.execute(select)
        fetched_selects = cur.fetchall()
        cur.close()
        return fetched_selects

    def insert(self, table, column, values, additionalData=None, fetch=None):
        """
        SQL Script to insert items into a database.

        EXAMPLE:
            sqlInsert("artikel", "artnr, naam, adviesprijs", "460, 'Tandpasta', 1.65", "", True)

        :param table: table to select from
        :param column: columns to insert to
        :param values: values to insert in the columns
        :param additionalData: extra data, i.e. 'RETURNING'
        :param fetch: to fetch one line back, if desired True. default: None
        :type fetch: bool
        :rtype fetch=True: list
        """
        cur = self.con.cursor()
        if additionalData is None:
            insert = f"INSERT INTO {table} ({column}) VALUES ({values})"
        else:
            insert = f"INSERT INTO {table} ({column}) VALUES ({values}) {additionalData}"
        cur.execute(insert)
        if fetch:
            fetched = cur.fetchone()[0]
            self.con.commit()
            cur.close()
            return fetched
        else:
            self.con.commit()
            cur.close()

    def update(self, table, set, additionalData):
        """
        SQL Script to update items into a database.

        EXAMPLE:
            sqlUpdate("klant", "adres = 'Amersfoortse Weg 7'", "WHERE plaats = 'DOORN'")

        :param table: the table to update
        :param set: the values to set
        :param additionalData: additional data to update, for example WHERE ... = ...
        :type parameters: str
        """
        cur = self.con.cursor()
        update = f"UPDATE {table} SET {set} {additionalData}"
        cur.execute(update)
        self.con.commit()
        cur.close()

    def custom(self, query):
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        cur.close()

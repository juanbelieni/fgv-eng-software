import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect("db.sqlite")
        self.cursor = self.conn.cursor()

    def execute(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)

            if query.strip().upper().startswith("SELECT"):
                result = self.cursor.fetchall()
                return result
            else:
                self.conn.commit()
                result = self.cursor.fetchall()
                return result

        except sqlite3.Error:
            # TODO: better this error
            return None


db = DB()

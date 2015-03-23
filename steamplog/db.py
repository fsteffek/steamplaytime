import MySQLdb
import time
import sys


class steamplog_db(object):
    def __init__(self):
        self.conn = MySQLdb.connect(
                host="localhost",
                user="steam",
                db="steam",
                charset="utf8")
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def update_appnames(self, app_list):
        self.cursor.executemany(
            'REPLACE INTO app_names'
            '(app_id, name)'
            'VALUES (%s, %s)', app_list
            )
        self.conn.commit()

    def log_playtime(self, owned_games):
        """Insert playtime data into database"""
        time_in_unix = int(time.time())  # timestamp for db
        table = 'playtime_forever'
        for game in owned_games['games']:
            query = 'INSERT INTO ' + table
            query += ' ( appid, minutes_played, time_of_record ) VALUES ( '
            query += '%d, ' % game.get('appid', 0)
            query += '%d, ' % game.get(table, 0)
            query += '%d )' % time_in_unix
            self.cursor.execute(query)
        self.conn.commit()

    def app_ids_from_db(self):
        """Get the app id for each game in database and return as list"""
        query = 'SELECT DISTINCT appid FROM playtime_forever ORDER BY appid'
        self.cursor.execute(query)
        table = self.cursor.fetchall()  # returns a tuple of tuples
        return [row[0] for row in table]

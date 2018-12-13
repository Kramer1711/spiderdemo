import pymysql


class conn:
    host = 'localhost'
    port = 3306
    user = 'root'
    passwd = 'root'
    database = 'oschina_spider'

    conn = None

    def getCon(self):
        if self.conn is None:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd,
                                        database=self.database)
        return self.conn

    def close(self):
        self.conn.close()

    pass


cc = conn()
print(type(cc.getCon()))

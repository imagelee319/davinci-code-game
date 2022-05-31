import pymysql


class RecordDAO:
    def __init__(self):
        self.conn = None

    def connect(self):
        # DB connect
        self.conn = pymysql.connect(host='localhost', port=3306, user='davinci', password='1234', db='davincicode')

    def disconnect(self):
        # DB disconnect
        self.conn.close()

    def insertRecord(self, id, score):
        # DB에 게임기록 저장 (insert)
        self.connect()
        cur = self.conn.cursor()
        sql = 'insert into record values (%s, %s)'
        cur.execute(sql, (id, score))
        self.conn.commit()
        self.disconnect()


    def selectRanking(self):
        # TOP10 랭킹 조회
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from record order by score desc limit 10'
        cur.execute(sql)
        self.conn.commit()
        rows = cur.fetchall()
        self.disconnect()
        return rows
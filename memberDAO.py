import pymysql

class MemberDAO:
    def __init__(self):
        self.conn = None

    def connect(self):
        # DB connect
        self.conn = pymysql.connect(host='localhost', port=3306, user='davinci', password='1234', db='davincicode')

    def disconnect(self):
        # DB disconnect
        self.conn.close()


    def insertMember(self, id, pw):
        # DB에 새로운 멤버를 추가 (insert)
        self.connect()
        cur = self.conn.cursor()
        sql = 'insert into player(id,password) values(%s,%s)'
        cur.execute(sql, (id, pw))
        self.conn.commit()
        self.disconnect()


    def selectMember(self, id):
        # 해당 id를 가진 멤버 조회
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from player where id=%s'
        cur.execute(sql, id)
        self.conn.commit()
        row=cur.fetchone()
        self.disconnect()
        return row

    def checkId(self,id):
        # 일치하는 id 조회
        self.connect()
        cur = self.conn.cursor()
        sql = 'select id from player where id=%s'
        cur.execute(sql, id)
        self.conn.commit()
        rows=cur.fetchall()
        self.disconnect()
        return rows

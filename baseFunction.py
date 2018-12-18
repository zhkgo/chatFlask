# -*- coding: utf-8 -*-
import pymysql
import random
def checkUser(username,password):
	try:
		db=pymysql.connect(host='localhost',user='chatUser',password='111111',port=3306,charset='utf8')
		cursor=db.cursor()
		cursor.execute("use chatDB")
		sql="select * from userInfo where username='%s' and password='%s'"%(username,password)
		num=cursor.execute(sql)
		if num!=0:
			return 1
		else:
			return 0
	except Exception as e:
		print(e)
		return 0
	finally:
		db.close()

def addUser(username,password):
	try:
		db=pymysql.connect(host='localhost',user='chatUser',password='111111',port=3306,charset='utf8')
		cursor=db.cursor()
		cursor.execute("use chatDB")
		sql="select * from userInfo where username='%s' "%username
		num=cursor.execute(sql)
		if num!=0:
			return 0
		sql="insert into userInfo(username,password) values('%s','%s')"%(username,password)
		num=cursor.execute(sql)
		if num!=0:
			db.commit()
			return 1
		else:
			return 0	
	except Exception as e:
		print(e)
		return 0
	finally:
		db.close()


def getImg():
	k=random.randint(1,32)
	return "https://chat-1252419034.cos.ap-shanghai.myqcloud.com/images/p%s.jpeg"%k
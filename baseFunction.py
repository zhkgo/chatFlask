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
			return "loginSuccess"
		else:
			return "loginFail"
	except Exception as e:
		print(e)
		return "UnknownError"
	finally:
		db.close()
def changePassword(username,oldPassword,newPassword):
	try:
		db=pymysql.connect(host='localhost',user='chatUser',password='111111',port=3306,charset='utf8')
		cursor=db.cursor()
		cursor.execute("use chatDB")
		sql="select * from userInfo where username='%s'"%username
		num=cursor.excute(sql)
		if num==0:
			return "userNotExist"
		sql="select * from userInfo where username='%s' and password='%s'"%(username,oldPassword)
		num=cursor.excute(sql)
		if num==0:
			return "passwordError"
		sql="update userInfo set password='%s' where username='%s'"%(newPassword,username)
		cursor.execute(sql)
		db.commit()
		return "changeSuccess"		
	except Exception as e:
		print(e)
		return "UnknowError"
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
			return "userExist"
		sql="insert into userInfo(username,password) values('%s','%s')"%(username,password)
		num=cursor.execute(sql)
		if num!=0:
			db.commit()
			return "registerSuccess"
		else:
			return "UnknowError"	
	except Exception as e:
		print(e)
		return "UnknowError"
	finally:
		db.close()


def getImg():
	k=random.randint(1,31)
	return "https://chat-1252419034.cos.ap-shanghai.myqcloud.com/images/p%s.jpeg"%k
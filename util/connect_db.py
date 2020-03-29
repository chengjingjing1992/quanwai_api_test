#coding:utf-8
# import MySQLdb.cursors
from pymysql import cursors
import pymysql
import json
class OperationMysql:
	def __init__(self,con):
		if con == 'test':
			self.conn = pymysql.connect(
				host='101.132.186.98',
				port=9696,
				user='thN1YBei',
				passwd=None,
				charset='utf8',
				# cursorclass=MySQLdb.cursors.DictCursor
				cursorclass=cursors.DictCursor

			)

		if con == 'prod':
			self.conn = pymysql.connect(
				host='101.132.186.98',
				port=9696,
				user='Ce4NHyoQ',
				passwd=None,
				charset='utf8',
				# cursorclass=MySQLdb.cursors.DictCursor
				cursorclass=cursors.DictCursor

			)




		self.cur = self.conn.cursor()

	#查询一条数据
	def search_one(self,sql):
		self.cur.execute(sql)
		result = self.cur.fetchone()
		print(type(result))
		print("result===",result)
		# result = json.dumps(result)
		return result

if __name__ == '__main__':
	op_mysql = OperationMysql("prod")
	print(op_mysql.conn)
	res = op_mysql.search_one("select nickname from quanwai.Profile where id=196597")
	print(type(res))
	res
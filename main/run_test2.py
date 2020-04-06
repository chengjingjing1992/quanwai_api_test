#!/usr/bin/python
#coding:utf-8
# 888888

import sys
print("sys.path==",sys.path)
# sys.path.append("E:/www/ImoocInterface")
from base.runmethod import RunMethod
import json
from data.get_data import GetData
from util.common_util import CommonUtil
from util.connect_db import OperationMysql
from data.dependent_data import DependdentData
from util.send_email import SendEmail
import requests
from util.operation_header import OperationHeader
from util.operation_json import OperetionJson
sys.path.append(sys.path[0]+'\..')
print("sys.path==",sys.path)
class RunTest:
	def __init__(self,fileName,sheetid):

		self.run_method = RunMethod()
		self.data = GetData(fileName=fileName,sheetid=sheetid)
		self.com_util = CommonUtil()
		self.send_mai = SendEmail()

	#程序执行的
	def go_on_run(self):

		res = None
		pass_count = []
		fail_count = []
		#获取excel 文件的行数
		rows_count = self.data.get_case_lines()

		# 行数减1 即需要执行多少个用例
		for i in range(1,rows_count):
			# 判断该用例是否执行
			is_run = self.data.get_is_run(i)
			if is_run:

				url = self.data.get_request_domain(i) + self.data.get_request_path(i)

				method = self.data.get_request_method(i)
				header=self.data.get_request_header(i)
				params = self.data.get_requestParams(i)
				body=self.data.get_body(i)
				cookies_1=self.data.get_cookies(i)
				expectHTTPStatus=self.data.get_expectHttpStatus(i)

				if params != None :
					params=self.paramOrBodyFollowDB(params)


				if body != None:
					body=self.paramOrBodyFollowDB(body)


				depend_case = self.data.is_depend(i)
				if depend_case != None:
					# 所依赖的那条用例的数据对象
					self.depend_data = DependdentData(depend_case,fileName=fileName,sheetid=sheetid)
					#所依赖的那条用例的执行响应数据
					depend_response_data = self.depend_data.get_data_for_key(i)
					#获取依赖的key
					depend_key = self.data.get_depend_field(i)
					request_data=None

					if params != None:
						params[depend_key]= depend_response_data

					if body != None:
						body[depend_key]= depend_response_data

				cookies = {
					"_qt": "zux5fyt9957zw9wyvausndkexpv00002",
					"path": "/",
					"domain": ".confucius.mobi"
				}
				res=self.run_method.run_main(url,method,cookies=cookies_1,body=body,headers=header,params=params)

				if expectHTTPStatus != res.status_code:
					self.data.write_result(i, "fail")
					self.data.write_actualStatusCode(i,res.status_code)
					self.data.write_actualResponse(i, res.text)
					continue

				self.data.write_actualStatusCode(i, res.status_code)


				print("res.text==",res.text)

				needCheckDict=self.data.get_expcet_response(i)
				if needCheckDict !=None:
					needCheckDict=self.paramOrBodyFollowDB(needCheckDict)

				checkListStr=[]
				# 需要检查的字段集合
				checkListStr= [str(i) for i in self.getListFromDict(checkListStr,needCheckDict)]

				flag=True
				for st in checkListStr:
					if st not in res.text:
						flag=False
						self.data.write_result(i, "fail")
						self.data.write_actualResponse(i,res.text)
						fail_count.append(i)
						break

				if flag == True:
					self.data.write_result(i,"ok")
					self.data.write_actualResponse(i,"")
					pass_count.append(i)
		print("pass_count,fail_count===", pass_count, fail_count)




	# params  body 期望的response 字段的值从数据库中拿取
	def paramOrBodyFollowDB(self,dic_data):
		if isinstance(dic_data,dict):

			for p in dic_data:
				if str(dic_data[p]).startswith("sql_"):
					sql = str(dic_data[p])[4:]
					dic = operation_mysql.search_one(sql=sql)
					result_db = None
					for x in dic:
						result_db = dic[x]
						break
					dic_data[p] = result_db

			return dic_data
	# 递归获取 expectResponse 字段的 字典value值
	def getListFromDict(self,list, dic):
		for i in dic:
			if isinstance(dic[i], dict):
				self.getListFromDict(list, dic[i])
			else:
				list.append(dic[i])
		return list



if __name__ == '__main__':


	# 选择数据环境 线上/测试
	db_enviroment="test"
	# db_enviroment="prod"
	operation_mysql = OperationMysql(db_enviroment)





	# # 选择用例文件
	# # fileName='../dataconfig/case1.xls'
	# # fileName = '../dataconfig/confucius.xls'
	fileName = '../dataconfig/management.xls'
	# # fileName = '../dataconfig/yunying.xls'
	sheetid=0
	run = RunTest(fileName=fileName,sheetid=sheetid)
	run.go_on_run()


#coding:utf-8
from util.operation_excel import OperationExcel
from data import data_config
from util.operation_json import OperetionJson
from util.connect_db import OperationMysql
import json
class GetData:
	def __init__(self,fileName,sheetid):
		self.opera_excel = OperationExcel(file_name=fileName,sheet_id=sheetid)

	def throw_canNotBeNullException(self,row,cellValue,colName):
		if isinstance(cellValue,str) and cellValue.strip() == '' or cellValue == None:
			raise Exception("excel文件第{}行".format(row+1), str(colName) + "值不能为空")
		pass

	#去获取excel行数,就是我们的case个数
	def get_case_lines(self):
		return self.opera_excel.get_lines()

	#获取是否执行
	def get_is_run(self,row):
		flag = None
		col = int(data_config.get_run())
		run_model = self.opera_excel.get_cell_value(row,col)
		self.throw_canNotBeNullException(row=row, cellValue=run_model, colName="run_model")
		print('run_model==',run_model)
		if run_model == 'yes':
			flag = True
		else:
			flag = False
		return flag

	#是否携带header
	def is_header(self,row):
		col = int(data_config.get_header())
		header = self.opera_excel.get_cell_value(row,col)
		if header != '':
			return header
		else:
			return None

	def get_request_header(self,row):
		col = int(data_config.get_header())
		header = self.opera_excel.get_cell_value(row, col)
		if header.strip() == '':
			return None
		else:
			return json.loads(header)









	#获取请求方式
	def get_request_method(self,row):
		col = int(data_config.get_run_way())
		request_method = self.opera_excel.get_cell_value(row,col)
		self.throw_canNotBeNullException(row=row, cellValue=request_method, colName="request_method")
		return request_method

	#获取域名
	def get_request_domain(self,row):
		col = int(data_config.get_domain())
		domain = self.opera_excel.get_cell_value(row,col)
		self.throw_canNotBeNullException(row=row,cellValue=domain,colName="domain")
		return domain
	# 获取域名后面的虚拟目录path
	def get_request_path(self,row):
		col = int(data_config.get_path())
		path= self.opera_excel.get_cell_value(row,col)
		self.throw_canNotBeNullException(row=row, cellValue=path, colName="path")
		return path

	#获取请求数据
	def get_request_data(self,row):
		col = int(data_config.get_data())
		data = self.opera_excel.get_cell_value(row,col)
		if data == '':
			return None
		return data

	#通过获取关键字拿到data数据
	def get_data_for_json(self,row):
		opera_json = OperetionJson()
		id=self.get_request_data(row)
		request_data = opera_json.get_data(id=id)
		return request_data

	#获取预期结果
	def get_expcet_response(self,row):
		col = int(data_config.get_expectResponse())
		expectResponse = self.opera_excel.get_cell_value(row,col)
		self.throw_canNotBeNullException(row=row, cellValue=expectResponse, colName="expectResponse")


		return json.loads(expectResponse)

	#通过sql获取预期结果
	def get_expcet_data_for_mysql(self,row):
		op_mysql = OperationMysql()
		sql = self.get_expcet_data(row)
		res = op_mysql.search_one(sql)
		return res.decode('unicode-escape')

	def write_result(self,row,value):
		col = int(data_config.get_result())
		self.opera_excel.write_value(row,col,value)

	def write_actualResponse(self,row,value):
		col = int(data_config.get_ActualResponse())
		self.opera_excel.write_value(row,col,value)

	def write_actualStatusCode(self,row,value):
		col = int(data_config.get_ActualHTTPStatus())
		self.opera_excel.write_value(row,col,value)



	#获取依赖数据的key
	def get_depend_key(self,row):
		col = int(data_config.get_data_depend())
		depent_key = self.opera_excel.get_cell_value(row,col)
		if depent_key == "":
			return None
		else:
			return depent_key

	#判断是否有case依赖
	def is_depend(self,row):
		col = int(data_config.get_case_depend())
		depend_case_id = self.opera_excel.get_cell_value(row,col)
		if depend_case_id == "":
			return None
		else:
			return depend_case_id

	#获取数据依赖字段
	def get_depend_field(self,row):
		col = int(data_config.get_field_depend())
		data = self.opera_excel.get_cell_value(row,col)
		if data == "":
			return None
		else:
			return data


	def get_body(self,row):
		col=int(data_config.get_body())
		body=self.opera_excel.get_cell_value(row,col)
		if body == "":
			return None
		else:
			return json.loads(body)

	def get_cookies(self,row):
		col=int(data_config.get_cookie())
		cookies=self.opera_excel.get_cell_value(row,col)
		if cookies == "":
			return None
		else:
			return json.loads(cookies)

	def get_expectHttpStatus(self,row):
		col=int(data_config.get_ExpectHTTPStatus())
		expectHttpStatus=self.opera_excel.get_cell_value(row,col)
		self.throw_canNotBeNullException(row=row, cellValue=expectHttpStatus, colName="expectHttpStatus")
		if expectHttpStatus == "":
			return None
		else:
			return expectHttpStatus

	def get_requestParams(self,row):
		col=int(data_config.get_params())
		params=self.opera_excel.get_cell_value(row,col)
		if params == "":
			return None
		else:
			return json.loads(params)









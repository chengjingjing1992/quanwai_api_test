#coding:utf-8
import sys
import json
sys.path.append('E:/www/ImoocInterface/')
from util.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse
class DependdentData:
	def __init__(self,case_id,fileName,sheetid):
		self.case_id = case_id
		self.opera_excel = OperationExcel(file_name=fileName,sheet_id=sheetid)
		self.data = GetData(fileName=fileName,sheetid=sheetid)

	#通过case_id去获取该case_id的整行数据
	def get_case_line_data(self):
		rows_data = self.opera_excel.get_rows_data(self.case_id)
		return rows_data

	#执行依赖测试，获取结果
	def run_dependent(self):
		run_method = RunMethod()
		row_num  = self.opera_excel.get_row_num(self.case_id)
		print("row_num====",row_num)

		url = self.data.get_request_domain(row_num) + self.data.get_request_path(row_num)
		method = self.data.get_request_method(row_num)
		header = self.data.get_request_header(row_num)
		# request_data = self.data.get_data_for_json(row_num)
		params = self.data.get_requestParams(row_num)
		body = self.data.get_body(row_num)
		cookies_1 = self.data.get_cookies(row_num)
		res = run_method.run_main(url,method,cookies=cookies_1,body=body,headers=header,params=params)

		return json.loads(res.text)

	#根据依赖的key去获取执行依赖测试case的响应,然后返回
	def get_data_for_key(self,row):
		depend_data = self.data.get_depend_key(row)
		print("depend_data===",depend_data)
		response_data = self.run_dependent()
		print("response_data===",response_data)

		json_exe = parse(depend_data)
		madle = json_exe.find(response_data)
		list=[math.value for math in madle]
		print("list===",list)
		return list[0]

if __name__ == '__main__':
	order = {
		"data": {
			"_input_charset": "utf-8", 
			"body": "慕课网订单-1710141907182334", 
			"it_b_pay": "1d", 
			"notify_url": "http://order.imooc.com/pay/notifyalipay", 
			"out_trade_no": "1710141907182334", 
			"partner": "2088002966755334", 
			"payment_type": "1", 
			"seller_id": "yangyan01@tcl.com", 
			"service": "mobile.securitypay.pay", 
			"sign": "kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D", 
			"sign_type": "RSA", 
			"string": "_input_charset=utf-8&body=慕课网订单-1710141907182334&it_b_pay=1d&notify_url=http://order.imooc.com/pay/notifyalipay&out_trade_no=1710141907182334&partner=2088002966755334&payment_type=1&seller_id=yangyan01@tcl.com&service=mobile.securitypay.pay&subject=慕课网订单-1710141907182334&total_fee=299&sign=kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D&sign_type=RSA", 
			"subject": "慕课网订单-1710141907182334", 
			"total_fee": 299
			}, 
			"errorCode": 1000, 
			"errorDesc": "成功", 
			"status": 1, 
			"timestamp": 1507979239100
		}
	res = "data.out_trade_no"
	json_exe = parse(res)
	madle = json_exe.find(order)
	print ([math.value for math in madle][0])



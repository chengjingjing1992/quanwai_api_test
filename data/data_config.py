#coding:utf-8
class global_var:

	#case_id
	Id = '0'
	request_name = '1'
	domain = '2'
	path = '3'
	run = '4'
	request_way = '5'
	header = '6'
	case_depend = '7'
	data_depend = '8'
	field_depend = '9'
	data = '10'
	expectResponse = '11'
	result = '12'
	cookies = '13'
	body = '14'
	ExpectHTTPStatus = '15'
	ActualHTTPStatus = '16'
	ActualResponse = '17'


#获取caseid
def get_id():
	return global_var.Id

#获取domain
def get_domain():
	return global_var.domain

def get_path():
	return global_var.path

def get_run():
	return global_var.run

def get_run_way():
	return global_var.request_way

def get_header():
	return global_var.header

def get_case_depend():
	return global_var.case_depend

def get_data_depend():
	return global_var.data_depend

def get_field_depend():
	return global_var.field_depend

def get_data():
	return global_var.data

def get_params():
	return global_var.data

def get_expectResponse():
	return global_var.expectResponse

def get_result():
	return global_var.result


def get_cookie():
	return global_var.cookies

def get_body():
	return global_var.body

def get_ExpectHTTPStatus():
	return global_var.ExpectHTTPStatus

def get_ActualResponse():
	return global_var.ActualResponse

def get_ActualHTTPStatus():
	return global_var.ActualHTTPStatus


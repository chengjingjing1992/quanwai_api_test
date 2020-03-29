#coding:utf-8
import requests
import json

class RunMethod:


	def run_main(self,url, method, headers=None, cookies=None, params=None, body=None):
		print("method===",method)
		print(type(method))
		if method == 'GET':
			return requests.get(url, headers=headers, cookies=cookies, params=params)

		if method == 'DELETE':
			return requests.delete(url, headers=headers, cookies=cookies, params=params)

		if method == 'POST':
			return requests.post(url, headers=headers, params=params, cookies=cookies, json=body)

		if method == 'PUT':
			return requests.put(url, headers=headers, params=params, cookies=cookies, json=body)
		#return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

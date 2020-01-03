#coding:utf-8
import json

def get_config_file():
	file = "G:\\python\\config.json" 
	data = json.load(open(file))
	for key in data.keys():
		print('key: %s value: %s' % (key,data.get(key)))
		
if __name__ == '__main__':
	get_config_file()
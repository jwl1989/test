#coding:utf-8
import json
class icc():
	def __init__(self):
		print("init...")
	def get_config_file(self):
		try:
			file = "G:\\python\\config.json" 
			self.config_data = json.load(open(file))
			for key in config_data.keys():
				print('key: %s value: %s' % (key,config_data.get(key)))
			return self.config_data
		except Exception as e:
			print("ERROR is ",e)
			return False
			
	def start_app():
		if "sd" in self.config_data.keys():
			print("deploy app in sd")
			for app in self.config_data['sd']['app']
				
		if "dp" in self.config_data.keys():
			print("deploy app in dp")
		
if __name__ == '__main__':
	get_config_file()
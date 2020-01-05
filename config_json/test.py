#coding:utf-8
import json
class icc():
	def __init__(self):
		print("init...")
	def get_config_file(self):
		try:
			file = "G:\\python\\test\\config_json\\config.json" 
			self.config_data = json.load(open(file))
			for key in self.config_data.keys():
				print('key: %s value: %s' % (key,self.config_data.get(key)))
			return self.config_data
		except Exception as e:
			print("ERROR is ",e)
			return False
			
	def start_app(self):
		if "sd" in self.config_data.keys():
			print("deploy app in sd")
			for app in self.config_data['sd']['app']:
				if app == "PUB":
					for pub in app['PUB'].keys():
						p_info = app['PUB'][pub]
						print("start pub",p_info['topicname'],p_info['msgnum'],p_info['msgsize'],p_info['msgtime'],p_info['len'])
					print("start app PUB:")
		if "dp" in self.config_data.keys():
			print("deploy app in dp")
			app = self.config_data['dp']['app']
			for app_name in self.config_data['dp']['app']:
				if app_name == "PUB":
					#print("app['PUB'] is ",app['PUB'],"app is ",app)
					for pub in app['PUB'].keys():
						p_info = app['PUB'][pub]
						print("start pub",p_info['topicname'],p_info['msgnum'],p_info['msgsize'],p_info['msgtime'],p_info['len'])
					print("start app PUB:")
		
if __name__ == '__main__':
	i = icc()
	i.get_config_file()
	i.start_app()
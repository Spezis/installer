import ui
import requests
import json


class View(ui.View):
	def did_load(self):
		r = requests.get('https://raw.githubusercontent.com/jensholzberger/installer/master/apps.json')
		liste =json.loads(r.content.decode().strip('\n'))
		self.modules=liste['modules']
		self.programms=liste['programms']
		print([i for i in self.programms.values()])
		self.present('sheet')

	def select_category(self, sender):
		pass


v = ui.load_view()

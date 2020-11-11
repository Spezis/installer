import ui
import requests
import json


class View(ui.View):
	def did_load(self):
		installer_liste = requests.get('https://raw.githubusercontent.com/jensholzberger/installer/master/apps.json')
		print(installer_liste.content)
		self.present('sheet')

	def select_category(self, sender):
		pass


v = ui.load_view()

apps={'modules':{'peewee':['coleifer/peewee','peewee']},'programms':{'chat-app':'Speziwelt'}}

with open('apps.json', 'w') as fp:
	json.dump(apps, fp,indent=4)


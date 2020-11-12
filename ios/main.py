import ui
import requests
import json

BACKUP_LIST = '''{
    "modules": {
        "peewee": [
            "coleifer/peewee",
            ["peewee.py"]
        ]
    },
    "programms": {
        "chat-app": ["Speziwelt",[['desktop/main.py'],['ios/main.py']]],
        "musik": "Musikdatenbank"
    }
}'''


class View(ui.View):
	def did_load(self):
		r = requests.get('https://raw.githubusercontent.com/jensholzberger/installer/master/apps.json')
		liste = json.loads(r.content.decode().strip('\n'))
		self.modules = liste['modules']
		self.programms = liste['programms']
		list1 = [i[0] for i in self.programms.values()]
		self['tableview1'].data_source = ui.ListDataSource(items=list1)

		self['segmentedcontrol1'].action = self.select_category
		self.present('sheet')

	def select_category(self, sender):
		if sender.selected_index:
			liste = [i for i in self.modules.keys()]
			self['tableview1'].data_source = ui.ListDataSource(items=liste)
			self['tableview1'].reload()
		else:
			list1 = [i[0] for i in self.programms.values()]
			self['tableview1'].data_source = ui.ListDataSource(items=list1)
			self['tableview1'].reload()


v = ui.load_view()


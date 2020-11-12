import ui
import requests
import json
import sys
import os

BACKUP_LIST = '''{
    "modules": {
        "peewee": [
            "coleifer/peewee",
            ["peewee.py"]
        ]
    },
    "programms": {
        "chat-app": ["Speziwelt",[["desktop/main.py"],["ios/main.py"],["generelledateien"]]],
        "musik": ["Musikdatenbank",[["desktopdateien"],["iosdateien"],["generelledateien"]]]
    }
}'''


class View(ui.View):
	def did_load(self):
		try:
			r = requests.get(
				'https://raw.githubusercontent.com/jensholzberger/installer/master/apps.json'
			)
			liste = json.loads(r.content.decode().strip('\n'))
		except Exception:
			self[
				'errortext'].text = 'Paketliste konnte nicht geladen werden (kein Internet).'
			liste = json.loads(BACKUP_LIST.strip('\n'))
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

def check_version():
	try:
		r = requests.get('https://raw.githubusercontent.com/jensholzberger/installer/master/apps.json')
		liste = json.loads(r.content.decode().strip('\n'))
	except Exception:
		#update failed
		#->try running startup scripts
		try:
			import startup
		except ImportError:
			#expected during testing or no startup programm existing
			sys.exit(0)
		
print(__file__)
if __name__ == '__main__':
	#executed by user
	v = ui.load_view()
else:
	#autostart folder (check for updates and install overdue packets)
	check_version()


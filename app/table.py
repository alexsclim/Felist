from flask_table import Table, Col

class TeamTable(Table):
	classes = ['table', 'table-striped', 'table-bordered', 'table-hover']
	teamId = Col('teamId')
	name = Col('name')
	practiceCost = Col('practiceCost')
	adminId = Col('adminId')
	regionCity = Col('regionCity')
	regionProvince = Col('regionProvince')

class TeamItem(object):
	def __init__(self, teamId, name, practiceCost, adminId, regionCity, regionProvince):
		self.teamId = teamId
		self.name = name
		self.practiceCost = practiceCost
		self.adminId = adminId
		self.regionCity = regionCity
		self.regionProvince = regionProvince
from controllers.Manager import AlarmManager

data = {
	'id': 3232,
	'title': 'hds',
	'time': '12:00:00'
}
a = AlarmManager.getAll()
print(a)
from subprocess import Popen

data = {
	'title': 'teste',
	'hour': '14:31'
}


Popen(["pythonw", "controllers/WaitHour.pyw", data['title'], data['hour']], shell=False)
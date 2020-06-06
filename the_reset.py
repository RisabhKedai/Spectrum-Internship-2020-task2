import json 
#a function to reset the current onj
def reset():
	with open("data_files/currentobj.json",'r') as cf:
			l=json.load(cf)
	l['Name']=''
	l['username']=''
	l['Branch']=''
	l['pps']=0
	l['math']=0
	l['chem']=0
	l['RegID']=''
	with open("data_files/currentobj.json",'w') as cf:
			json.dump(l,cf)

import os
os.system('pip install requests')
os.system('clear')
import requests
repo_url = 'https://github.com/ghoghnosblack/ddos/blob/main/non.text'
response = requests.get(repo_url)
if response.status_code == 200:
    print("        You are welcome❕")
else:
    print("        The program stops‼️")
    exit()
password = input('Enter Your Password: ')
if password == 'AMIRreza':
	print('password :',password,'✅')
else:
	print('password :',password,'❌')
	exit()

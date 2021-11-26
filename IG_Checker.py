try:import time,random,os;from colorama import Fore;from requests import get,post
except ModuleNotFoundError:
	os.system('pip install requests')
	os.system('pip install colorama')
	os.system('pip uninstall colorama')
	os.system('pip install colorama')
global x2,j
x2='[🖤] @TweakPY'
j='''
[☑️] NEW USER:︎︎
'''
def without_list():
	count,done,error=0,0,0
	user=""
	lena=input('[?] Length: ')
	length=(int(lena))
	try:
		use_checkers = open('id_token.txt', "r").read().splitlines()
		ID=use_checkers[0]
		token=use_checkers[1]
	except:
		pass
		print('[!] No Token/id Detected ')
		chars="qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
		while True:
			for user in range(1):
				user=""
				for item in range(length):
					user+=random.choice(chars)
			send=get(f'https://www.instagram.com/{user}',headers={'accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8','cache-control': 'max-age=0','sec-ch-ua':'"Google Chrome";v="89","Chromium";v="89", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'})
			if send.status_code==404:
				print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
				done+=1
				count+=1
				try:post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {user}\n\n{x2}')
				except:pass
				with open('Available.txt', 'a') as x:
					tl='[] NEW USER -->  '
					x.write(tl+user+'\n')
			else:
				print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
				error+=1
				count+=1
def with_list():
	error,count,done=0,0,0
	file=open('user.txt', 'r')
	try:
		use_checkers=open('id_token.txt', "r").read().splitlines()
		ID=use_checkers[0]
		token=use_checkers[1]
	except:
		pass
		print('[!] No Token/id Detected ')
	while True:
		time.sleep(0.9)
		user=file.readline().split('\n')[0]
		send=get(f'https://www.instagram.com/{user}',headers={'accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8','cache-control': 'max-age=0','sec-ch-ua':'"Google Chrome";v="89","Chromium";v="89", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'})
		if send.status_code==404:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			done+=1
			count+=1
			try:post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {user}\n\n{x2}')
			except:pass
			with open('Available.txt', 'a') as x:
				tl='[] NEW USER -->  '
				x.write(tl+user+'\n')
		else:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			error+=1
			count+=1
print("""
██╗ ██████╗        ██████╗██╗  ██╗
██║██╔════╝       ██╔════╝██║  ██║
██║██║  ███╗█████╗██║     ███████║
██║██║   ██║╚════╝██║     ██╔══██║
██║╚██████╔╝      ╚██████╗██║  ██║
╚═╝ ╚═════╝        ╚═════╝╚═╝  ╚═╝
        By @TweakPY @vv1ck                                                  
""")			
T=int(input("1- Without List\n2- with list\n:"))
if T==1:without_list()
elif T==2:with_list()
else:exit('• None !')

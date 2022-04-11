#Coded By Shin Code
#My Friend : 
#Jenderal92 - h0d3_g4n - Moslem - Kiddenta - Naskleng45
#Blog : https://www.blog-gan.org
#BUY ME A COFFE :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614

import requests,re,random,sys,time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore

print("""

               __
              / _)
     _/\/\/\_/ /
   _|         /
 _|  (  | (  |
/__.-'|_|--|_|  
=============
FREE GETIPS | PYTHON CODE
Yt : Py  |  ICQ : https://icq.im/Shin403

""")

def IpS():
	Shinn = raw_input('Frist Page@ ~#: ')
	Codde = raw_input('Last Page@ ~#: ')
	try:
		Head={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36'}
		for page in range(int(Shinn), int(Codde)):
			UrlWebs = 'http://bitverzo.com/recent_ip?p='+str(page)
			Shin = requests.get(UrlWebs, headers=Head, timeout=15).content
			if 'Recent IP reviews' in Shin:
				Shine = re.findall('<a href="http://bitverzo.com/ip/(.*?)">', Shin)
				for xxx in Shine:
					Repshin = xxx.replace('http://bitverzo.com/ip/', '')
					print('[+]' + Fore.GREEN + Repshin + Fore.WHITE)
					open('SHIN_IP.txt', 'a').write(Repshin+'\n')
				else:
					print(Fore.RED + 'Coded By Shin_Code' + Fore.WHITE)
	except:
		pass
IpS()
			
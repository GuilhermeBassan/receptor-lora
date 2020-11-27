import sys
import glob
import serial
import datetime
import json

class Comm(object):

	#TODO: fazer com que faça a listagem de baud rate e config avançadas
	def listPorts(self,info=False):
		tag = datetime.datetime.now()
		print(f"Iniciando listagem das portas disponíveis...")
		if sys.platform.startswith('win'):
			ports = ['COM%s' % (i + 1) for i in range(256)]
		elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
			ports = glob.glob('/dev/tty[A-Za-z]*')
		elif sys.platform.startswith('darwin'):
			ports = glob.glob('/dev/tty.*')
		else:
			raise EnvironmentError('Unsupported platform')
		result = []
		for port in ports:
			try:
				s = serial.Serial(port)
				s.close()
				result.append(port)
			except Exception as e:
				print(f"{tag} - AVISO - Problema ao listar portas - {e}")
				pass
		return result

	def saveConfig(self,port,baud):
		self.port = port
		self.baud = baud
		tag = datetime.datetime.now()
		print(f"{tag} - EVENTO - Iniciando salvamento das configurações...")
		try:
			data = {"PORT" : self.port, "BAUD" : self.baud}
			with open("cfg.json", "w") as cfg_file:
				json.dump(data, cfg_file, indent=2)
			cfg_file.close()
			print(f"{tag} - EVENTO - Configurações salvas.")
			return 1
		except Exception as e:
			print(f"{tag} - AVISO - Erro ao salvar configurações - {e}")
			return 0
		#pass

	def loadConfig(self,info=False):
		tag = datetime.datetime.now()
		print(f"{tag} - EVENTO - Carregando arquivo de configurações...")
		try:
			cfg_file = open("cfg.json", "r")
			cfg_data = json.load(cfg_file)
			port = cfg_data["PORT"]
			baud = cfg_data["BAUD"]
			cfg_file.close()
		except Exception as e:
			print(f"{tag} - AVISO - {e}")
			return 0
		print(f"{tag} - EVENTO - Arquivo carregado, iniciando últimas configurações.")
		return port, baud
		#pass

	#TODO: criar função que mostra o pacote
	#      fazer opção de display avançado (bytes recebidos)
	def serialRx(self,info=False):
		pass

	#TODO: criar função que envia os dados
	def serialTx(self):
		pass

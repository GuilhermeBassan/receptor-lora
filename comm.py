import sys
import glob
import serial
import datetime
import json

class Comm(object):

	#TODO: migrar a função de listagem de portas
	#      fazer com que faça a listagem de baud rate e config avançadas
	def listPorts(self,info=False):
		pass

	#TODO: migrar a função de salvar configurações
	def saveConfig(self,port,baud):
		self.port = port
		self.baud = baud
		tag = datetime.datetime.now()
		try:
			data = {"PORT" : self.port, "BAUD" : self.baud}
			with open("cfg.json", "w") as cfg_file:
				json.dump(data, cfg_file, indent=2)
			cfg_file.close()
			return 1
		except Exception as e:
			print(f"{tag} - AVISO - {e}")
			return 0
		#pass

	#TODO: migrar a função que carrega configurações salvas
	#      fazer com que essa função inicie a porta serial
	def loadConfig(self,info=False):
		pass

	#TODO: criar função que mostra o pacote
	#      fazer opção de display avançado (bytes recebidos)
	def serialRx(self,info=False):
		pass

	#TODO: criar função que envia os dados
	def serialTx(self):
		pass

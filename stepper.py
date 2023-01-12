import machine
import time

class stepper():
	#Inicializacion del objeto
	def __init__(self, direction = 1, wtime = 1, a = 0, b = 4, c = 5, d = 16):
		self.step = 0									#Memoria de secuencia inicia en 0
		self.direction = direction						#Direccion, toma el valor del argumento al momento de la creacion del objeto
		self.wtime = wtime								#Lo mismo para el tiempo de espera
		self.a = machine.Pin(a, machine.Pin.OUT)		
		self.b = machine.Pin(b, machine.Pin.OUT)		#Inicializacion de los pines
		self.c = machine.Pin(c, machine.Pin.OUT)		
		self.d = machine.Pin(d, machine.Pin.OUT)		
	

	def Steps(self, steps):								#Funcion construida para facilitar el conteo de pasos completos
		for i in steps:
			self.Seq()


	def Seq(self):										#Funcion de seguimiento de secuencia
		time.sleep_us(int(self.wtime*500))
		if self.step == 0:
			self.a.value(0)
			self.b.value(1)
			self.c.value(1)
			self.d.value(0)
			if self.direction==1:
				self.step = 1
			else:
				self.step = 7
			print(self.step)
			

		elif self.step == 1:
			self.a.value(0)	
			self.b.value(1)
			self.c.value(1)
			self.d.value(1)
			if self.direction==1:
				self.step = 2
			else:
				self.step = 0
			print(self.step)
			

		elif self.step == 2:
			self.a.value(0)
			self.b.value(0)
			self.c.value(1)
			self.d.value(1)
			if self.direction==1:
				self.step = 3
			else:
				self.step = 1
			print(self.step)
			
				
		elif self.step == 3:
			self.a.value(1)
			self.b.value(0)
			self.c.value(1)
			self.d.value(1)
			if self.direction==1:
				self.step = 4
			else:
				self.step = 2
			print(self.step)
		
		elif self.step == 4:
			self.a.value(1)	
			self.b.value(0)
			self.c.value(0)
			self.d.value(1)
			if self.direction==1:
				self.step = 5
			else:
				self.step = 3
			print(self.step)
			

		elif self.step == 5:
			self.a.value(1)
			self.b.value(1)
			self.c.value(0)
			self.d.value(1)
			if self.direction==1:
				self.step = 6
			else:
				self.step = 4
			print(self.step)
			
				
		elif self.step == 6:
			self.a.value(1)
			self.b.value(1)
			self.c.value(0)
			self.d.value(0)
			if self.direction==1:
				self.step = 7
			else:
				self.step = 5
			print(self.step)
		
		elif self.step == 7:
			self.a.value(1)
			self.b.value(1)
			self.c.value(1)
			self.d.value(0)
			if self.direction==1:
				self.step = 0
			else:
				self.step = 6
			print(self.step)
			

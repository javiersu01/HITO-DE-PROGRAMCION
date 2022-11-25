class Usuario:
	def __init__(self,nombre,pais,edad,correo,numTarjeta,username,contraseña):
		self.nombre=nombre
		self.pais=pais
		self.edad=edad
		self.correo=correo
		self.numTarjeta=numTarjeta
		self.username=username
		self.contraseña=contraseña

def Registrar():
	wh=1
	while (wh==1):
		print('*******************************************')
		print('\nREGISTRO')
		print('\nTines que registrar  ')
	
		wh1=1
		while(wh1==1):
			error=0
			username=input('\nNombre de Usuario:')
			if(len(username)<6):
				print('\nEl nombre se usuario tiene menos de 6 caracteres')
			elif(len(username)>12):
				print('\nEl nombre de usuario tiene más de 12 caracteres')
			else:
				for x in range(len(username)):
					if(ord(username[x:x+1])<48 or ord(username[x:x+1])>122):
						if(ord(username[x:x+1])!=241 and ord(username[x:x+1])!=209):
							print('\nEL NOMBRE DE USUARIO SOLO DEBE TENER NUMERO Y LETRAS')
							error=1
							break
				if(error!=1):
					wh1=0
		wh1=1
		while(wh1==1):
			contador=0
			contraseña=input('\nContraseña:')
			if(len(contraseña)<6):
				print('\nLA CONTRASEÑA DEBE TENER, MINIMO, 6 CARACTERES')
			else:
					print('CONTRASEÑA VALIDA')
					wh1=0
		wh1=1
		print('************************************************************')
		print('\nEscribe tu información ')
		while(wh1==1):
			error=0
			nombre=input('Nombre:')
			for x in range(len(nombre)):
					if(ord(nombre[x:x+1])==32):
						print('ESCRIBE TU NOMBRE, SIN APELLIDOS')
						error=1
						break
			if(error!=1):
				wh1=0
		pais=input('pais:')
		wh1=1
		while(wh1==1):
			try:
				edad=int(input('Edad:'))
				wh1=0
			except ValueError:
				print('\nMETE UN NUMERO')
		wh1=1
		
		correo=input('Correo:')
			
		wh1=1
		while(wh1==1):
			try:
				numTarjeta=int(input('Número de tarjeta:'))
				wh1=0
			except ValueError:
				print('\nMETISTE UNA LETRA')
		wh1=1
		usuario=Usuario(nombre,pais,edad,correo,numTarjeta,username,contraseña)
		return usuario
def Ingresar(listaProductos):
	username=input('Nombre de usuario:')
	if(username in usuarios):
		contraseña=input('\nContraseña:')
		if(contraseña in usuarios2):
			carrito = Carrito({}, 0)
			comprando = True
			while(comprando):
				print('================')
				print('LISTA DE ARTICULOS.')
				for producto in listaProductos:
					producto.imprimirProducto()
					
				print('=====================')
				print('\n\nEscribe los datos requeridos.')
				clave = input('Ingresa la clave asociada a tu producto: ')
				encontrado = False
				for producto in listaProductos:
					if producto.clave == clave and producto.revisarInventario():
						print('El producto existe.')
						print('Quieres agregarlo a tu carrito? ')
						print('SI=1')
						print('NO=2')
						opcion = input('Opcion: ')
						if opcion == '1':
							carrito.agregar(producto, producto.getClave())
							producto.setClave(producto.inventario)
							producto.reducirInventario()
							carrito.setTotal(producto.precio)
						encontrado = True
						break
				if encontrado:
					carrito.imprimirCarrito()
				else:
					print('El articulo descrito no existe o se encuentra agotado.')
					print('Deceas revisar otro articulo? ')
				print('Seguir mirando= 1')
				print('Terminar carrito= 2')
				opcion = input('Opcion: ')
				if opcion == '1':
					comprando = True
				else:
					comprando = False
			if len(carrito.articulos) != 0:
				print('<=================>')
				print('PAGO DE ARTICULOS.')
				carrito.imprimirCarrito()
				confirmacion = input('Presiona 1 para confirmar la compra, cualquier otra entrada cancelara la compra: ')
				if confirmacion == '1':	
					continuar = True
					while(continuar):
						contraseña = input('Ingresa tu contraseña:')
						try:
							if usuarios2[contraseña]:
								print('El total de articulos esta siendo cargado')
								print('Compra confirmada, vuelva pronto.')
							else:
								print('Correo o contraseña no valida, prueba registrarte antes.')
						except KeyError:
							print('Error en la validacion, revisa los datos.')
							datos = input('Quieres volver a intentarlo (1 = SI, otra entrada = NO)? ')
							if datos != '1':
								continuar = False
				else:
					print('Se ha cancelado la compra.')

			else:
				print('Tu carrito esta vacio.')
		
	else:
		print('NOMBRE DE USUARIO NO ENCONTRADO')
class Producto:
	def __init__(self, tipo, color, precio, inventario, talla):
		self.precio = precio
		self.tipo = tipo
		self.color = color
		self.inventario = inventario
		self.talla = talla
		self.clave = self.tipo[0] + self.tipo[1] + str(inventario) + self.color[0]
	def revisarInventario(self):
		if self.inventario == 0:
			print('Actualmente no tenemos existenacias')
			return False
		else:
			print('Articulo en existencia')
			return True

	def reducirInventario(self):
		self.inventario -= 1 

	def getClave(self):
		return self.clave

	def setClave(self, inventario):
		self.clave = self.tipo[0] + self.tipo[1] + str(inventario) + self.color[0]

	def imprimirProducto(self):
		print('<======================>')
		print('Articulo: ' + self.tipo + '........' + str(self.precio))
		print('Color: ' + self.color)
		print('inventario: '+ str(self.inventario))
		print('CLAVE del producto: ' + self.clave)
class Carrito:

	def __init__(self, articulos, total):
		self.articulos = articulos
		self.total = total
	def agregar(self, articulo, clave):
		self.articulos[clave] = articulo
	def setTotal(self, importe):
		self.total += importe
	def getTotal(self): 
		return self.total
	def imprimirCarrito(self):
		print('\n\nArticulos en tu carrito.')
		for producto in self.articulos:
			self.articulos[producto].imprimirProducto()
			print('\n\nTotal ........... '+ str(self.getTotal()))
pantalonNegro = Producto('Vaquero', 'Rojo', 20, 5, 'GRANDE')
playeraRoja = Producto('Zapato', 'Azul', 30, 6, 'PEQUEÑA')
vestidoBlanco = Producto('Vestido', 'Amarillo', 80, 7, 'MEDIANA')

listaProductos = [pantalonNegro,playeraRoja,vestidoBlanco]
carrito = Carrito({}, 0)
wh = 1
usuarios={}
usuarios2={}
while(wh==1):
	print('M E N U\n1. Registrar\n2. Ingresar\n3. Envio pdf\n4. SMS movil\n5. Salir')
	opcion=input('Opcion:')

	if(opcion=='1'):
		Persona=Registrar()
		usuarios2[Persona.contraseña]=Persona
		usuarios[Persona.username]=usuarios2
		print('\nUSUARIO REGISTRADO')
	elif(opcion=='2'):
		Ingresar(listaProductos)
	elif(opcion=='5'):
		print('Gracias por compra')
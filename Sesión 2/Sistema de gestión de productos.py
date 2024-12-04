class producto:
  def __init__(self, nombre, precio, cantidad):
    self.nombre = nombre
    self.cantidad = cantidad
    self.precio = precio

class sigep:
  def __init__(self):
    self.producto = {}
  
  def agregar(self):
    nombre = input("Nombre del producto: ").strip()
    if nombre in self.producto:
      print("Este producto ya existe en inventario")
    else:
      cantidad = int(input("Que cantidad hay: "))
      precio = float(input("Cual es el precio del producto: "))                
      self.producto[nombre]  = producto(nombre, cantidad, precio)                          
      print(f"'{nombre}' agregado al inventario")
  
  def eliminar(self):
    nombre =input("Nombre del producto a elininar: ")
    if nombre in self.producto:
      del self.producto[nombre]
      print(f"'{nombre}' ha sido eliminado del inventario")
    else:
      print("El producto no existe.")
  
  def actualizar(self):
    nombre = input("Producto a actualizar: ")
    if nombre in self.producto:
      cantidadnueva = int(input("Cuanta cantidad del producto llego: "))
      precionuevo = float(input("Precio del producto: "))

      producto = self.producto[nombre]
      producto.cantidad += cantidadnueva
      producto.precio = precionuevo
      print(f"'{nombre}' ha sido actualizado")
    else:
      print("El producto no existe.")
  
  def agotado(self):
    print("Productos a agotarse")
    for nombre, producto in self.producto.items():
      if producto.cantidad < 5:
        print(f"- {nombre}: {producto.cantidad} unidades")
  

  def menu(self):
        while True:
            print("Menú SIGEP")
            print("1. Agregar producto")
            print("2. Eliminar producto")
            print("3. Actualizar producto")
            print("4. Mostrar productos por agotarse")
            print("5. Salir")
            respuesta = input("Elija una opción: ")

            if respuesta == "1":
                self.agregar()
            elif respuesta == "2":
                self.eliminar()
            elif respuesta == "3":
                self.actualizar()
            elif respuesta == "4":
                self.agotarse()
            elif respuesta == "5":
                print("Gracias por usar sigep.")
                break
            else:
                print("Esta opción no es valida")

sistema = sigep()
sistema.menu()

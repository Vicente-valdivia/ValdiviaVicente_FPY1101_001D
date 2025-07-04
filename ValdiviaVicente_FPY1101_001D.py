productos = {'8475HD': ['hp', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['hp', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
 'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
 'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0] 
 }

def StockMarca(marca):
    marca = marca.lower()
    total_stock = 0
    for codigo, datos in productos.items():
        if datos[0].lower() == marca:
            total_stock += stock.get(codigo, [0,0])[1]
    if total_stock > 0:
        print(f"El stock es: {total_stock}")
    else:
        print("No se encontraron productos para esa marca.")
    

    
def BusquedaPorPrecio(PrecioMinimo, PrecioMaximo):
    try:
        PrecioMinimo = float(input("Ingrese el precio minimo: "))
        if PrecioMinimo < 0:
            print("El precio no puede ser negativo.")
            return
        PrecioMaximo = float(input("Ingrese el precio maximo: "))
        if PrecioMaximo < 0:
            print("El precio no puede ser negativo.")
            return
        if PrecioMinimo > PrecioMaximo:
            print("El precio minimo no puede ser mayor que el maximo.")
            return

        encontrados = False
        print(f"Productos entre {PrecioMinimo} y {PrecioMaximo}:")
        for codigo, datos in productos.items():
            precio_producto = stock.get(codigo, [0,0])[0]
            if PrecioMinimo <= precio_producto <= PrecioMaximo:
                print(f"Código: {codigo}, Marca: {datos[0]}, Pantalla: {datos[1]}, RAM: {datos[2]}, Almacenamiento: {datos[3]}, Procesador: {datos[5]}, GPU: {datos[6]}, Precio: {precio_producto}, Stock: {stock[codigo][1]}")
                encontrados = True
        if not encontrados:
            print("No hay productos en ese rango de precios.")
    except ValueError:
        print("Debe ingresar valores numéricos!!")
        return

    
def ActualizarPrecio(modelo,p):
    if modelo in stock>=0:
        try:
            p = float(input("Ingrese el nuevo precio: "))
            if p < 0:
                print("El precio no puede ser negativo.")
                return
            ValidarCambioDePrecio= input("¿Desea confirmar el cambio de precio? (Si/No): ").lower()
            if ValidarCambioDePrecio != 'si':
                print("Cambio de precio cancelado.")
                return
            stock[modelo][0] = p
            print(f"El precio del producto {modelo} ha sido actualizado a {p}.")
        except ValueError:
            print("Debe ingresar un valor numérico para el precio.")
    else:
        print(f"El modelo {modelo} no existe!!")
        
def menu():
    while True:
        print("\nMenu de opciones:")
        print("1. Ver stock por marca")
        print("2. Buscar productos por rango de precio")
        print("3. Actualizar precio de un producto")
        print("4. Salir")
        print("--------------------------------")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            StockMarca(input("Ingrese la marca del producto: "))
        elif opcion == '2':
            BusquedaPorPrecio(0, 0)
        elif opcion == '3':
            ActualizarPrecio(input("Ingrese el modelo del producto: ").upper(), 0)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")
            
menu()    
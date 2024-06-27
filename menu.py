# FUNCIONES
def mostrar_menu():
    print("""
1. Registrar pedido
2. Listar los todos los pedidos
3. Imprimir hoja de ruta
4. Salir del programa
""")

# VARIABLES
pedido=list()

datos={"Cliente":[],
"Direccion":[],
"Sector":[],
"Cil. 5kg":[],
"Cil. 15kg":[],
"Cil. 45kg":[]}

flag1=True

# MAIN
while True:
    mostrar_menu()
    op=input(">")
    if op=="1":
        flag1=True
        while flag1:
            while True:
                cliente=input("\nIngrese nombre y apellido de cliente: ")
                if cliente=="":
                    print("No ingreso nada estupido baboso -Andy y Luis")
                else:
                    print("Correctamenete ingrasdo")
                    break
            while True:
                direccion=input("\nIngrese direccion: ")
                if direccion=="":
                    print("No ingreso nada estupido baboso -Andy y Luis")
                else:
                    print("Correctamenete ingrasdo")
                    break
            while True:
                sector=input("\nIngrese sector (Centro, Colina, Industrias): ")
                sector=sector.lower()
                if sector=="centro" or sector=="colina" or sector=="industrias":#estas secciones, cambios pequenos como estos no me gustan usar funciones quitan personalisacion
                    print("Correctamenete ingrasdo")
                    break
                else:
                    print("sector invalido")
            while True:
                
                try:
                    cil_5=int(input("\nCuantos cilindros de 5?"))
                except:#algo similar para el menu op1 pero con funciones???
                    print("Error")
                    continue
                
                if cil_5>=0:
                    print("guardado")
                    break
                else:
                    print("valor invalido")
            while True:
                
                try:
                    cil_15=int(input("\nCuantos cilindros de 15?"))
                except:#algo similar para el menu op1 pero con funciones???
                    print("Error")
                    continue
                
                if cil_15>=0:
                    print("guardado")
                    break
                else:
                    print("valor invalido")
            while True:
                
                try:
                    cil_45=int(input("\nCuantos cilindros de 45?"))
                except:#algo similar para el menu op1 pero con funciones???
                    print("Error")
                    continue
                
                if cil_45>=0:
                    print("guardado")
                    break
                else:
                    print("valor invalido")
            
            #confirmacion de datos a ingresar
            print(f"""
                \t*** DEASEA GUARDAR ESTOS DATOS? ***
                "Cliente":[{cliente}],
                "Direccion":[{direccion}],
                "Sector":[{sector}],
                "Cil. 5kg":[{cil_5}],
                "Cil. 15kg":[{cil_15}],
                "Cil. 45kg":[{cil_45}]
                """)
            while True:
                op=input("Confirme con un yes/no?")
                op=op.lower()
                if op == "yes" or op == "y":
                    datos["Cliente"].append(cliente)
                    datos["Direccion"].append(direccion)
                    datos["Sector"].append(sector)
                    datos["Cil. 5kg"].append(cil_5)
                    datos["Cil. 15kg"].append(cil_15)
                    datos["Cil. 45kg"].append(cil_45)
                    print("datos guardados")
                    flag1=False
                    break
                elif op == "no" or op == "n":
                    print("\nReingrese datos")
                    break
                else:
                    print("ingrese con un 'y' o 'n'")
                    
    if op=="2":
        print(datos)
import re

opcion = 0
while opcion != 11:

    
     print("Expresiones Regulares")
     print("1.Todas las palabras que tengan una longitud de 7 o más letras\n"
         +"2.Expresiones que NO finalicen con una vocal\n"
         +"3.Las palabras que inicien con “M” donde la segunda letra no sea vocal\n"
         +"4.Expresiones encerradas entre comillas\n"
         +"5.Ip’s\n"
         +"6.Horas\n"
         +"7.Telefonos\n"
         +"8.Correos electrónicos\n"
         +"9.Url’s\n"
         +"10.Código postal\n"
         +"11.Salir")
     opcion = int(input("Seleccione una opción: "))

     if opcion == 1:
         filename = "Ejemplo-prueba.txt"
         textFile = open(filename, "r")
         regex = "[A-Za-z]{7,}"
         reg = re.compile(regex)
         for line in textFile:
            lista = reg.findall(line)
            print(lista)
         textFile.close()
     elif opcion == 2:
          filename = "Ejemplo-prueba.txt"
          textFile = open(filename, "r")
          regex = "[A-Za-z]+"
          reg = re.compile(regex)
          for line in textFile:
               lista = reg.findall(line)
               regex = "[A-Za-z]+[^aeiou]$"
               for elemento in lista:
                    if re.search(regex, elemento):
                         print(elemento)
          textFile.close()
     elif opcion == 3:
          filename = "Ejemplo-prueba.txt"
          textFile = open(filename, "r")
          regex = "[M][^aeiou][A-Za-z]+"
          reg = re.compile(regex)
          for line in textFile:
               lista = reg.findall(line)
               print(lista)
          textFile.close()
     elif opcion == 4:
          filename = "Ejemplo-prueba.txt"
          textFile = open(filename, "r")
          regex = "(\".*?\"|\'.*?\')"
          reg = re.compile(regex)
          for line in textFile:
               lista = reg.findall(line)
               print(lista)
          textFile.close()
     elif opcion == 5:
          filename = "Ejemplo-prueba.txt"
          textFile = open(filename, "r")
          regex = "(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
          reg = re.compile(regex)
          for line in textFile:
               lista = reg.findall(line)
               print(lista)
          textFile.close()
     elif opcion == 6:
          filename = "Ejemplo-prueba.txt"
          textFile = open(filename, "r")
          regex = "((1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm])?)"
          reg = re.compile(regex)
          for line in textFile:
               lista = reg.findall(line)
               print(lista)
          textFile.close()
     elif opcion == 7:
          filename = "Ejemplo-prueba.txt"
          textFile = open(filename, "r")
          regex = "(\+?\d[2]|\(\+?\d[2]\))?(\d{8,12})"
          reg = re.compile(regex)
          for line in textFile:
               lista = reg.findall(line)
               print(lista)
          textFile.close()
     elif opcion == 8:
          filename = "Ejemplo-prueba.txt"
          textFile = open(filename, "r")
          regex = "([a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})+"
          reg = re.compile(regex)
          for line in textFile:
               lista = reg.findall(line)
               print(lista)
          textFile.close()
     elif opcion == 9:
          filename = "Ejemplo-prueba.txt"
          textFile = open(filename, "r")
          regex = "(?:(?:https?|http|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]"
          reg = re.compile(regex)
          for line in textFile:
               lista = reg.findall(line)
               print(lista)
          textFile.close()
     elif opcion == 10:
          filename = "Ejemplo-prueba.txt"
          textFile = open(filename, "r")
          regex = "(\d{5})"
          reg = re.compile(regex)
          for line in textFile:
               lista = reg.findall(line)
               print(lista)
          textFile.close()
     elif opcion == 11:
          print("Gracias por su visita")
     else:
        print("\nNo es una opción válida")


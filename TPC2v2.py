Naipe = ["C", "P", "O", "E"]
Numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, "D", "V", "R"]
Baralhos = 1000000

def Contar(s):
  Baralho = []
  global Baralhos
  
  for num in Numero:
    for naip in Naipe:
      Baralho.append(str(num) + naip)
  
  for z in Baralho:
    i = 0
    for a in s:
      if(z == a):
        i+= 1
    if(i<Baralhos):
      Baralhos = i
		
  print("Baralhos possiveis: ")  
  print(Baralhos)
  
A = ["1P", "1C", "1O", "2P", "2C", "2O", "2E", "3P", "3C", "3O", 
     "3E", "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", 
     "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", 
     "9E", "DP", "DC", "DO", "DE", "JP", "JC", "JO", "JE", "VP", "VC", 
     "VO", "VE", "RP", "RC", "RO", "RE", "1P", "1C", "1O", "1E", "2P", "2C", 
     "2O", "2E", "3P", "3C", "3O", "3E", "4P", "4C", "4O", "4E", "5P", "5C", 
     "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C", 
     "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", "JP", "JC", 
     "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE", "1P", "1C", 
     "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", "4P", "4C", 
     "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", 
     "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", 
     "DO", "DE", "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", 
     "RO", "RE"]

Contar(A)
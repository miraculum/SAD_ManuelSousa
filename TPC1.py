#criar uma função
def solution(S):
    Pesquerdo = ['(', '[', '{']
    Pdireito = [')', ']', '}']
    Z = []
    for c in S:
      for x in range(3):
        if (Z and c == Pdireito[x]):
          if c != Z[0]:
            return 0
        elif (c == Pdireito[x] and not Z):
          return 0
        elif (c == Pesquerdo[x]):
          Z.insert(0, Pdireito[Pesquerdo.index(c)])
          break
        elif Z:
          if (c == Z[0]):
            Z.pop(0)
            break
            
    if not Z:
      return 1
    else:
      return 0

#chamar a função
S = "{[()dasdasda()]}"
solution(S)
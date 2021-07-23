class Hash:
    def __init__(self, size):
        self.size = size
        self.values = [-1] * self.size
        self.keys = [None] * self.size
        self.step = 1

    def put(self, value):
        index = self.myHashFunc(value)

        if self.keys[index] == None:
            self.keys[index] = index
            self.values[index] = value

        else:
            newIndex = index + 1
            if newIndex < self.size :
              self.putColided(value, index+1)
            else:
              self.putColided(value, newIndex % self.size)

    def putColided(self, value, index):
        if self.keys[index] == None:
            self.keys[index] = index
            self.values[index] = value
            return
        else:
            newIndex = index + 1
            if newIndex < self.size :
              return self.putColided(value, newIndex)
            else:
              return self.putColided(value, newIndex % self.size)

    def remove(self, value):
        index = self.myHashFunc(value)

        if self.keys[index] != None:
            if self.values[index] == value:
              self.keys[index] = None
              self.values[index] = -2
              return
            else:
              newIndex = index + 1
              if newIndex < self.size:
                return self.removeColided(value, newIndex)
              else:
                return self.removeColided(value, newIndex % self.size)

    def removeColided(self, value, index):
      if self.values[index] == value:
        self.keys[index] = None
        self.values[index] = -2
        return
      else:
        newIndex = index + 1
        if newIndex < self.size:
          return self.removeColided(value, newIndex)
        else:
          return self.removeColided(value, newIndex % self.size)

    def myHashFunc(self, string):
        return len(string) % self.size



if __name__ == "__main__":

    tamanho = input()
    myHash = Hash(int(tamanho))

    continuar = True
    while(continuar):
        entradaOperacao = input()
        if(int(entradaOperacao) == -1):
            continuar = False
        else:
            entradaPalavra = input()
            if(int(entradaOperacao) == 0):
              myHash.put(entradaPalavra)
            elif(int(entradaOperacao) == 1):
              myHash.remove(entradaPalavra)

    for i in range(int(tamanho)):
        print(myHash.values[i])


"""
10
0
abcd
0
abdc
0
bacd
0
acbd
0
aeiu
0
ppbb
0
ttdd
0
mint
0
timn
1
ppbb
1
timn
-1
"""
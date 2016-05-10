class ingrediente:
    def __init__(self):
        self.amount=-1
        self.IngredientName=""
    def createname(self,name):
        self.IngredientName=name
    def checkstatus(self):
        print(self.IngredientName)
        print(self.amount)

class receitas:
    def __init__(self):
        #self.
        pass

arquivo=open("Lista_Ingredientes.txt","a")

def insert_in_file(x):
    ing=x.IngredientName
    qte=x.amount
    arquivo.write(ing+"\n")
    arquivo.write(str(qte)+"\n")

def Entering():
    print("Escreva Os ingredientes e suas quantidades")
    a=ingrediente()
    a.IngredientName=raw_input("Ingrediente:")
    a.amount=input("Quantidade:")
    insert_in_file(a)

Entering()



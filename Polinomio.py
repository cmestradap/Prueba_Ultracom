class Polinomio():
    def __init__(self):
        self.__grado=1
        self.__x = float                                           #variable
        self.__coeficiente = 1                                     #coeficiente que acompaña a la variable
        self.__polinomio = float

    def suma(self,valor):
        return self.__polinomio + valor

    def resta(self,valor):
        return self.__polinomio - valor

    def multiplicacion(self,valor):
        return self.__polinomio * valor

    def crear_polinomio(self,coeficiente,x):
        self.__x= x
        self.__coeficiente = coeficiente
        self.__polinomio = coeficiente * x

    def evaluacion(self):
        return print("El polinomio es de grado: " + str(self.__grado) + " \n Coeficiente: " + str(self.__coeficiente) + "\n x: " + str(self.__x))

p1 = Polinomio() # instancia de la clase

p1.crear_polinomio(10,3)
p1.evaluacion()
print("Suma: " + str(p1.suma(5)))
print("Resta: " + str(p1.resta(10)))
print("Multiplicacion: " + str(p1.multiplicacion(5)))


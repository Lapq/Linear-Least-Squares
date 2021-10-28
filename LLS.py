class lls(object):
    import numpy as np
    __sumX: float
    __sumY: float
    __sumXY: float
    __sumX2: float
    __n: int
    __slope: float
    __intercept: float


    def __calculateSlope(self):
        m = ( (self.__n * self.__sumXY) - (self.__sumX * self.__sumY) ) / ( (self.__n * self.__sumX2) - (self.__sumX * self.__sumX) )
        return m

    def __calculateIntercept(self):
        b = ( self.__sumY - (self.__slope * self.__sumX) ) / self.__n
        return b

    def fit(self, x_fit: list, y_fit: list): #Recebe duas listas de listas, cada elemento das listas internas contendo valores individuais
        if len(x_fit) != len(y_fit):
            raise RuntimeError("Argumentos de fit são listas de tamanhos incompatíveis")
        XY = np.multiply(np.array(achataLista2d(x_fit)), np.array(achataLista2d(y_fit)))
        X2 = np.multiply(np.array(achataLista2d(x_fit)), np.array(achataLista2d(x_fit)))
        self.__sumX = sum(achataLista2d(x_fit))
        self.__sumY = sum(achataLista2d(y_fit))
        self.__sumXY = sum(XY.tolist())
        self.__sumX2 = sum(X2.tolist())
        self.__n = len(x_fit)
        self.__slope = self.__calculateSlope()
        self.__intercept = self.__calculateIntercept()

    def predict(self, l:list): #Recebe uma lista de um único valor, e retorna uma lista com o único valor de previsão
        if len(l) != 1:
            raise RuntimeError("Argumento de predict deve ser uma lista de tamanho 1x1")
        y = (self.__slope * l[0]) + self.__intercept
        return list([y]) 

# coding: utf-8

class Number(object):
    
    ''' 
    Classe que abstrai operações com dois número e seu resultado.
    
    '''
    
    def __init__(self, numeroAA, numeroBB, res):
        
        self.__numeroA = numeroAA
        self.__numeroB = numeroBB
        self.__resultado = res
    
    def getNumeroA(self):
        '''
        Função que retorna o NumeroA.
        
        '''
        return self.__numeroA
    
    def getNumeroB(self):
        '''
        Função que retorna o NumeroB.
        
        '''
        return self.__numeroB
    
    def getResultado(self):
        '''
        Função que retorna o resultado.
        
        '''
        return self.__resultado

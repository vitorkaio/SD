# coding: utf-8

from classe_number import *

class CacheNumber(object):
    
    ''' 
    Está classe possui uma lista com objetos do tipo Number.
    
    '''
    
    def __init__(self):
        
        self.__lista = list()
        
    
    def insere(self, obj):
        
        ''' 
        Metódo que insere um objeto na lista, caso consiga retorna True, caso contrário retorna False.
        
        '''
        verifica = CacheNumber.verifica(self, obj)
        if verifica == False:
           
            self.__lista.append(obj)
            return True
       
        return False
    
    def getValor(self, numeroUm, numeroDois):
        
        ''' 
        Função que verifica se um valor existe, caso exista retorna seu resultado, caso contrário
        retorna False.
        
        '''
        for contador in self.__lista:
            
            number = contador
            if number.getNumeroA() == numeroUm and number.getNumeroB() == numeroDois:
                return contador.getResultado()
            
        return False 
        
    @staticmethod
    def  verifica(self, obj):
        
        ''' 
        Metódo que verifica se o objeto passado já existe na lista, caso exista, retorne True, caso
        contrário retorna False.
        
        '''
        for contador in self.__lista:
            
            number = contador
            
            if number.getNumeroA() == obj.getNumeroA() and number.getNumeroB() == obj.getNumeroB():
                return True
            
        return False   

#Nome: Giulia Barauna Rocha
#RA: 1903189

import abc 
from unittest import TestCase, main  

class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def executar(self, n1, n2):
        pass

class Divisao(Operacao):
    def executar(self, n1, n2):
        divis=n1/n2
        return divis

class Soma(Operacao):
    def executar(self, n1, n2):
        somaa=n1+n2
        return somaa

class Subtracao(Operacao):
    def executar(self, n1, n2):
        sub=n1-n2
        return sub

class Multiplicacao(Operacao):
    def executar(self, n1, n2):
        mult=n1*n2
        return mult

class Calculadora():
    def calcular(self, n1, n2, operador):
        operacaoFabrica=OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if(operacao == None):
            return 0
        else:
            resultado = operacao.executar(n1, n2)
            return resultado

class OperacaoFabrica(object):
    def criar(self, operador):
        if (operador=='soma'):
            return Soma()
        elif (operador=='divisao'):
            return Divisao()
        elif (operador=='subtracao'):
            return Subtracao()
        elif (operador=='multiplicacao'):
            return Multiplicacao()

class Test(TestCase):
    def teste_divisao(self):
        testarD = Calculadora()
        resultado = testarD.calcular(75,3, 'divisao')
        self.assertEqual(resultado, 25)
        print ("Divisão OK")

    def teste_soma(self):
        testarS = Calculadora()
        resultado = testarS.calcular(15,10,'soma')
        self.assertEqual(resultado, 25)
        print ("Soma OK")

    def teste_subtracao(self):
        testarMenos = Calculadora()
        resultado = testarMenos.calcular(50,25,'subtracao')
        self.assertEqual(resultado, 25)
        print ("Subtração OK")
    
    def teste_multiplicacao(self):
        testarM = Calculadora()
        resultado = testarM.calcular(6,5,'multiplicacao')
        self.assertEqual(resultado, 30)
        print ("Multiplicação OK")
 
if _name_ == '_main_':
    main()
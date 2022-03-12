# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:17:09 2022

@author: Ricardo Antonio Cardoso
"""

class Forca:
    
    def __init__(self,palavra):
        self.palavra = palavra
        self.lacunas = []
        self.tentativas = 0
        # PREENCHE AS LACUNAS COM #
        for i in self.palavra:
            self.lacunas.append("#")
    
    # CONFERE A LETRA
    def letra_na_palavra(self, letra):
        if letra in self.palavra:
            for i, l in enumerate(self.palavra):
                if l == letra:
                    del self.lacunas[i]
                    self.lacunas.insert(i,l)
        else:
            self.tentativas += 1
            
    # CONFERE SE TEM MAIS TENTATIVAS
    def confere(self):
        if self.tentativas != 3:
            if self.lacunas.count("#") == 0:
                print(f"Voce descobriu a palavra {self.palavra}")
                return 1
            if self.lacunas.count("#") != 0:
                print(f'Voce tem ainda {int(3) - self.tentativas} tentativas')
                print("Continue a palavra ainda esta for descobrir.")
                for i in self.lacunas:
                    print(f'{i}', end=" ")
                return 0
        else:
            print("Voce não tem mais tentativas.")
            for i in self.lacunas:
                print(f'{i}', end=" ")
            return 1
      
            
            
            
            
           
            

    
jogo = Forca("TESTE")
# Preenche a palavra a ser descoberta
while True:
    letra = input("Digite uma letra: ")
    jogo.letra_na_palavra(letra)
    if jogo.confere == 1:
        jogo.confere()
        break
    else:
        jogo.confere()
        continue
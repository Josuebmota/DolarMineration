from Questoes import Questoes
import pandas as pd

#Dados
class Main:
        def main(self): #Seleciona a questão
                dados = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json")
                #Questoes.Questao1(self,dados)
                Questoes.Questao2(self,dados)
                #Questoes.Questao3(self,dados)
R = Main()
R.main()
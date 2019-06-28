import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta

class Questoes:

    def localizarposicao(self, dados, anos):
        data5 = date.today() - timedelta(anos*365)#Localizar a posicao de acordo com os anos
        data_antiga= data5.strftime('%d/%m/%Y')
        for i in range(len(dados), -1, -1):
            data = dados.iloc[i-1][0]
            if((data_antiga[4:len(data_antiga)]== data[4:len(data)])):
                return i

    def Questao1(self,dados):
        #localizei a posicao e Selecionei a parte desejada
        dados_5anos = dados.loc[Questoes.localizarposicao(self,dados,5):len(dados)]
        plt.plot(dados_5anos["data"],dados_5anos["valor"])#Plotando no grafico
        plt.title('Série temporal da cotação do dólar dos últimos 5 anos')
        plt.xlabel('Datas')
        plt.ylabel('Valor')
        plt.show()
        return dados_5anos #Retorno esse dataframe
    
    def Questao2(self,dados):
        #localizei a posicao e Selecionei a parte desejada
        divide = Questoes.localizarposicao(self,dados,5)
        dados5 = dados.loc[Questoes.localizarposicao(self,dados,5):len(dados)]
        dados_anos = []#Lista dos anos
        dados_media = []#Lista das medias
        media = 0 
        cont= 0 #quantidade de dados num ano
        for i in range(len(dados5)):
            data = dados5.iloc[i][0]#Pego a data que eu estou olhando
            ano  = data[-1]#Pego o ano da data
            if(i!=len(dados5)-1): #Esse if server para o loop nao estourar
                data_proximo = dados5.iloc[i+1][0] #Pego a proxima data
                anopro = data_proximo[-1]#Pego o proximo ano da proxima data
            #Caso o ano atual for diferente da proxima data, 
            #os dados estão prontos para serem salvos
            if(ano != anopro):
                    media = media + dados5.iloc[i][1]#Pego pela ultima vez um dos valores anuais
                    dados_anos.append(data[6:len(data)])#Armazeno a data
                    dados_media.append(media/(cont+1))#Armazeno a media
                    media = 0
                    cont = 0
            media = media + dados5.iloc[i][1]#Pego um dos valores anuais e somo o valor a media
            cont+=1
        #Coloco num dataframe
        cinco_Anos = pd.DataFrame({'Anos': dados_anos, 'Media': dados_media})
        plt.plot(cinco_Anos["Anos"],cinco_Anos["Media"])#Plotando no grafico
        plt.title('Estatística da cotação do dólar dos últimos 5 anos')
        plt.xlabel('Anos')
        plt.ylabel('Media')
        plt.show()
        return cinco_Anos #Retorno esse dataframe

    def Questao3(self,dados):
        #localizei a posicao e Selecionei a parte desejada
        divide = Questoes.localizarposicao(self,dados,10)
        dados10 = dados.loc[divide:len(dados)]
        dados_mensal = []#Lista dos meses
        dados_media = []#Lista das medias dos meses
        media = 0 
        cont= 0 #quantidade de dados num mes
        #o loop vai de acordo com a quantidade de linhas dos
        #dados coletados em 10 anos
        for i in range(len(dados10)):
            data = dados10.iloc[i][0]#Pego a data que eu estou olhando
            mes  = data[4]#Pego o mes da data
            if(i!=len(dados10)-1): #Esse if server para o loop nao estourar
                data_proximo = dados10.iloc[i+1][0] #Pego a proxima data
                mespro = data_proximo[4]#Pego o proximo mes da proxima data
            #Caso o mes atual for diferente da proxima data, 
            #os dados estão prontos para serem salvos
            if(mes != mespro):
                    media = media + dados10.iloc[i][1]#Pego pela ultima vez o valor mensal
                    dados_mensal.append(data[3:len(data)])#Armazeno a data
                    dados_media.append(media/(cont+1))#Armazeno a media
                    media = 0
                    cont = 0
            media = media + dados10.iloc[i][1]#Pego um dos valores mensais e somo o valor a media
            cont+=1
        #Coloquei os dados coletados num dataframe
        dez_Mensal = pd.DataFrame({'Mensal': dados_mensal, 'Media': dados_media})
        plt.bar(dez_Mensal["Mensal"],dez_Mensal["Media"])#Plotando no grafico
        plt.title('Gráfico da média móvel mensal da cotação do dólar dos último 10 anos')
        plt.xlabel('Meses')
        plt.ylabel('Media')
        plt.show()
        return dez_Mensal #Retorno esse dataframe
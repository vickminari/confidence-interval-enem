import math
import pandas as pd

df = pd.read_csv("MICRODADOS_ENEM_2023.csv", encoding='latin-1', delimiter=';')
#limpando os dados
df = df.dropna()
#filtrando os dados para a cidade de Teresina
df_muni = df.query(f"NO_MUNICIPIO_ESC == 'Teresina'")
#selecionando as colunas de notas das áreas de conhecimento
df_muni = df_muni[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT']]

#tabela de media e desvio padrao
df_muni_mean = df_muni.mean()
print(df_muni_mean)
df_muni_std = df_muni.std()
print(df_muni_std)

#quantidade de alunos
qtd = len(df_muni)
print(qtd)

#medias e desvios padrao
media_cn = df_muni['NU_NOTA_CN'].mean()
media_ch = df_muni['NU_NOTA_CH'].mean()
media_lc = df_muni['NU_NOTA_LC'].mean()
media_mt = df_muni['NU_NOTA_MT'].mean()
desvio_padrao_cn = df_muni['NU_NOTA_CN'].std()
desvio_padrao_ch = df_muni['NU_NOTA_CH'].std()
desvio_padrao_lc = df_muni['NU_NOTA_LC'].std()
desvio_padrao_mt = df_muni['NU_NOTA_MT'].std()


#calculando raiz de n
n = math.sqrt(len(df_muni))
#calculando intervalo de confiança
ic_cn = [media_cn - 1.96 * (desvio_padrao_cn/n), media_cn + 1.96 * (desvio_padrao_cn/n)]
ic_ch = [media_ch - 1.96 * (desvio_padrao_ch/n), media_ch + 1.96 * (desvio_padrao_ch/n)]
ic_lc = [media_lc - 1.96 * (desvio_padrao_lc/n), media_lc + 1.96 * (desvio_padrao_lc/n)]
ic_mt = [media_mt - 1.96 * (desvio_padrao_mt/n), media_mt + 1.96 * (desvio_padrao_mt/n)]
#arredondando os valores
ic_cn = [round(ic_cn[0], 4), round(ic_cn[1], 4)]
ic_ch = [round(ic_ch[0], 4), round(ic_ch[1], 4)]
ic_lc = [round(ic_lc[0], 4), round(ic_lc[1], 4)]
ic_mt = [round(ic_mt[0], 4), round(ic_mt[1], 4)]
#imprimindo os intervalos de confiança
print(f"Intervalo de confiança das notas de Ciências da Natureza: {ic_cn}")
print(f"Intervalo de confiança das notas de Ciências Humanas: {ic_ch}")
print(f"Intervalo de confiança das notas de Linguagens e Códigos: {ic_lc}")
print(f"Intervalo de confiança das notas de Matemática: {ic_mt}")

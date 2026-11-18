import pandas as pd 
import numpy as np 

def q25(x):
    return x.quantile(0.25)

def q50(x):
    return x.quantile(0.5)

def q75(x):
    return x.quantile(0.75)

def q90(x):
    return x.quantile(0.9)

usu = pd.read_excel('usuarios_ws.xlsx')
usu = usu.loc[usu['CARGO'].isnull()==False].reset_index(drop=True)
usu['CARGO_GERAL'] = usu['CARGO'].str.split(' ').str[0]

fato_ia_gemini = pd.read_excel('base_gemini.xlsx','Gemini Report 1026')
fato_ia = pd.read_csv('acesso_ia.csv')
fato_ia = fato_ia.loc[fato_ia['Usuário'].isin(usu['LOGIN'])==True].reset_index(drop=True)

base_gemini = fato_ia_gemini[['E-mail','Uso geral']].copy()
base_gemini = pd.merge(usu,fato_ia_gemini,'inner',left_on='EMAIL',right_on='E-mail')
base = pd.merge(usu,fato_ia,'inner',left_on='LOGIN',right_on='Usuário')


base_gemini['CARGO_GERAL'] = np.where(base_gemini['CARGO_GERAL'].str.contains('TEC.|TEC')==True,'TECNICO',base_gemini['CARGO_GERAL'])
base_gemini['NOME_DEPARTAMENTO'] = np.where(base_gemini['NOME_DEPARTAMENTO'].str.contains('TI')==True,'TI',base_gemini['NOME_DEPARTAMENTO'])
base_gemini['HIERARQUIA'] = np.where(base_gemini['CARGO'].str.contains('JR') == True, 'JR',
                              np.where(base_gemini['CARGO'].str.contains('PL') == True, 'PL',
                                       np.where(base_gemini['CARGO'].str.contains('SR') == True, 'SR','SEM_HIERARQUIA')))


base['CARGO_GERAL'] = np.where(base['CARGO_GERAL'].str.contains('TEC.|TEC')==True,'TECNICO',base['CARGO_GERAL'])
base['NOME_DEPARTAMENTO'] = np.where(base['NOME_DEPARTAMENTO'].str.contains('TI')==True,'TI',base['NOME_DEPARTAMENTO'])
base['HIERARQUIA'] = np.where(base['CARGO'].str.contains('JR') == True, 'JR',
                              np.where(base['CARGO'].str.contains('PL') == True, 'PL',
                                       np.where(base['CARGO'].str.contains('SR') == True, 'SR','SEM_HIERARQUIA')))


base = base['Qtd. de acessos'].groupby([base['LOGIN'],base['CARGO_GERAL'],base['NOME_DEPARTAMENTO'],base['SEGMENTO'],base['HIERARQUIA']]).sum().reset_index()
base_gemini = base_gemini['Uso geral'].groupby([base_gemini['LOGIN'],base_gemini['CARGO_GERAL'],base_gemini['NOME_DEPARTAMENTO'],base_gemini['SEGMENTO'],base_gemini['HIERARQUIA']]).sum().reset_index().rename(columns={'Uso geral':'Qtd. de acessos'})
final = pd.concat([base,base_gemini]).reset_index(drop=True)

# 


final.loc[final['NOME_DEPARTAMENTO']=='TD']['Qtd. de acessos'].describe()

fato_ia.loc[fato_ia['Nome'].str.contains('THIAGO')]

fato_ia['Serviço'].unique()
import pandas as pd 

#importando arquivos JSON, TXT, xls através da biblioteca pandas

#arquivos json
df_json = pd.read_json('aluguel.json')
df_json

#arquivos txt
df_txt = pd.read_table('aluguel.txt')
df_txt

#arquivos xlsx
df_xlsx = pd.read_excel('aluguel.xlsx')
df_xlsx

#arquivos html no pc
df_html = pd.read_html('dados_html_1.html')
df_html[0]

#arquivos html de um link
df_html = pd.read_html('https://www.federalreserve.gov/releases/h3/current/default.htm')
df_html[0] #imprimindo table1
df_html[1] #imprimindo table2
df_html[2] #imprimindo table3
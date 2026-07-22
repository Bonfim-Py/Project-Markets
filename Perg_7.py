filial = df['filial'].unique()
retirar = ['tipo','cidade','tipo_cliente','preço','quantidade','horário','pagamento','custo','rendimento'] 
df_fili = df.copy().drop(columns = retirar)
df_fili.head()
cond = (df['avaliação'] < 5)
df_fili[cond]

for i in tipos:
    cont = df_fili['filial'][cond].value_counts(dropna = False , sort = True)
    norm = df_fili['filial'][cond].value_counts(dropna = False , sort = True,normalize = True) *100
print(cont)
print(norm)

fig, ax = plt.subplots()
plt.xlabel('Tipos')
plt.ylabel('Qnt. avaliações negativas')
ax.bar(filial,cont)
plt.xticks(rotation = 90 , ha='left')
plt.show()

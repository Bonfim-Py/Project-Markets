tipos = df['tipo'].unique()
print(tipos)

meds_2 = []
for i in tipos:
    med = df[df['tipo'] == i]['avaliação'].mean()
    meds_2.append(med)
fig, ax = plt.subplots()
ax.barh(tipos,meds_2)
media_2 = [float(i) for i in meds_2]
media_2 = sts.mean(media_2)
ax.axvline(media_2, ls='--', color='r', label = "Média total de satisfação")
plt.title('Média de satisfação')
plt.xticks(rotation=90, ha='left')
plt.legend()
plt.show()

df.head()
retirar = ['filial','cidade','tipo_cliente','preço','quantidade','horário','pagamento','custo','rendimento'] 
df_aval = df.copy().drop(columns = retirar)
df_aval.head()

cond = (df['avaliação'] < 5)
df_aval[cond]
tipos = df_aval['tipo'][cond].unique()

for i in tipos:
    cont = df_aval['tipo'][cond].value_counts(dropna = False , sort = True)
    norm = df_aval['tipo'][cond].value_counts(dropna = False , sort = True,normalize = True) *100
print(cont)
print(norm)

fig, ax = plt.subplots()
plt.xlabel('Tipos')
plt.ylabel('Qnt. avaliações negativas')
ax.bar(tipos,cont)
plt.xticks(rotation = 90 , ha='left')
plt.show()






cliente = df['tipo_cliente'].unique()
print(cliente)

relacs = []
for i in cliente:
    relac = df[df['tipo_cliente'] == i]['rendimento'].sum()
    relacs.append(relac)
fig, ax = plt.subplots()
ax.barh(cliente, relacs )
plt.title('Relação Membros com rendimento')
plt.xticks(rotation=90, ha='left')
plt.legend()
plt.show()

df.head()
########################
colu_ret =["filial",
               "cidade",
               "tipo_cliente",
               "tipo",
               "pagamento" , 'horário']
df_stats = df.copy().drop(columns = colu_ret)
df_stats.head()
df_stats.corr()
###############
sns.heatmap(df_stats.corr(), annot = True)
plt.show()

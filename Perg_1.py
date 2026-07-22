filial = df['filial'].unique()
means = []
# Fazer Groupy para média de cada filial
for i in filial:
    mean = df[df['filial'] == i]['rendimento'].mean()
    means.append(mean)
for i,j in zip(filial,means):
    print(f'{i} = {j}')

fig,ax = plt.subplots()
plt.title('Média de Cada Mercado Filial')
plt.xlabel('Filiais')
plt.ylabel('Média dos Rendimentos')
ax.bar(filial,means)
plt.show()

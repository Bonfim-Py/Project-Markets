tipos = df['tipo'].unique()
print(tipos)

#####
sums = []
for i in tipos:
    sum = df[df['tipo'] == i]['custo'].sum()
    sums.append(sum)
fig,ax = plt.subplots()
plt.title('Lucro de Cada Tipo de Produto')
plt.xlabel('Tipos de Produtos')
plt.grid()
ax.barh(tipos,sums)
for i,j in zip(tipos,sums):
    print(f'{i} = {j}')
plt.xticks(rotation = 90, ha ='left')
plt.show()









medias = []
for i in tipos:
    media = df[df['tipo'] == i]['rendimento'].mean()
    medias.append(media)
fig, ax = plt.subplots()
plt.title('Rendimento médio para cada Tipo de Produto')
plt.grid()
ax.barh(tipos, medias)
medias = [float(i) for i in medias]
media_2 = sts.mean(medias)
print(media_2)
for i, j in zip(tipos, medias):
    print(f'{i} = {j}')
ax.axvline(media_2, ls='--', color='r', label = "Média total dos rendimentos")
plt.xticks(rotation=90, ha='left')
plt.legend()
plt.show()

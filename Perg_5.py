meds = []
for i in tipos:
    med = df[df['tipo'] == i]['horário'].mean()
    meds.append(med)
fig, ax = plt.subplots()
ax.barh(tipos,meds )
media_2 = [float(i) for i in meds]
media_2 = sts.mean(media_2)
ax.axvline(media_2, ls='--', color='r', label = "Média total dos horários")
plt.title('Média dos horários de saída')
plt.xticks(rotation=90, ha='left')
plt.legend()
plt.show()
#######################
cont = df['tipo'].value_counts()
print(cont)
tipos = ['Alimentos e Bedidas', 'Saúde e Beleza', 'Esportes', 'Acessórios' ,'Utensílios paraCasa', 'Tecnologia']

for i in tipos:
    hrs = df[df['tipo'] == i]['horário']
    plt.hist(hrs,label = i,edgecolor = 'black')
    plt.xticks(np.arange(10,20+2,2))
    plt.yticks (np.arange (0,30+2,5))
    plt.ylabel('Quantidade de Produto')
    plt.xlabel('Horário do Dia')
    plt.legend()
    plt.show()








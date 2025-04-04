from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

#LEEMOS LOS DATOS Y NOS QUEDAMOS SOLO CON LOS NECESARIOS PARA EL ANALISIS
df = pd.read_excel('C:\\Users\\LENOVO\\Desktop\\USM\\Ramos\\2025 I Visualizacion de Datos\\Tareas\\UTFSM-INF379\\fuentes_datos\\messi_cristiano_carrera.xlsx')
df = df[['Player', 'G+A']]

#DISEÑO DEL VIOLIN PLOT
palette = {
	'Lionel Messi': '#75AADB',
	'Cristiano Ronaldo': '#FF3333'
}
plt.title('Distribución de Goles + Asistencias por Jugador')
plt.ylabel('Goles + Asistencias')
plt.xlabel('Jugador')

#GENERAMOS EL VIOLIN PLOT
sns.violinplot(x='Player', y='G+A', data=df, palette=palette)
plt.show()
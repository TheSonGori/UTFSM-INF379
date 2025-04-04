import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from soccerplots.radar_chart import Radar

#LEEMOS LOS DATOS Y NOS QUEDAMOS SOLO CON LOS NECESARIOS PARA EL ANALISIS
df = pd.read_excel('C:\\Users\\LENOVO\\Desktop\\USM\\Ramos\\2025 I Visualizacion de Datos\\Tareas\\UTFSM-INF379\\fuentes_datos\\messi_cristiano_2017-2018.xlsx')
df = df[['Player', 'Gls', 'Ast', 'Sh', 'SoT', 'xG', 'xAG', 'Touches', 'Cmp', 'Att', 'Cmp%']]

#AJUSTAMOS LOS PARAMETROS
params = list(df.columns)
params = params[1:]

#CREAMOS LOS RANGOS DE VALORES PARA CADA PARAMETRO
ranges = []
for x in params:
	a = min(df[params][x])
	a = a - a * .25
	b = max(df[params][x])
	b = b + b * .25
	ranges.append((a, b))

#AÑADIMOS LOS VALORES DE CADA PARAMETRO PARA CADA JUGADOR
lio_values = []
cris_values = []
for x in range(len(df['Player'])):
	if df['Player'][x] == 'Lionel Messi':
		lio_values = df.iloc[x].values.tolist()
	if df['Player'][x] == 'Cristiano Ronaldo':
		cris_values = df.iloc[x].values.tolist()
lio_values = lio_values[1:]
cris_values = cris_values[1:]
values = [lio_values, cris_values]

#DISEÑO DEL RADAR
title = dict(
	title_name = 'Lionel Messi',
	title_color = '#75AADB',
	subtitle_name = 'Argentina / Barcelona',
	subtitle_color = '#75AADB',
	title_name_2 = 'Cristiano Ronaldo',
	title_color_2 = '#FF3333',
	subtitle_name_2 = 'Portugal / Real Madrid',
	subtitle_color_2 = '#FF3333',
)
endnote = 'Datos temporada 2017-2018 | Fuente: FBref.com'

#GRAFICAMOS EL RADAR
radar = Radar()
fig, ax = radar.plot_radar(
	ranges=ranges,
	params=params,
	values=values,
	radar_color=('#75AADB', '#FF3333'),
	alphas=[.75, .6],
	title=title,
	endnote=endnote,
	compare=True
)
plt.tight_layout()
plt.show()
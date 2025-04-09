import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 
import numpy as np 


years = [2002, 2006, 2010, 2014, 2018, 2022]
asistencia_masculino = [2705197, 3359439, 3178856, 3429873, 3031768, 3404252]
asistencia_femenino = [685664, 1190971, 845711, 1353506, 1131312, 1978274]


fig, ax = plt.subplots(figsize=(10, 6))


for i in range(len(years)):

    ax.plot([asistencia_femenino[i], asistencia_masculino[i]], 
            [years[i], years[i]],                           
            color='grey',                                   
            linestyle='-',                                  
            linewidth=1.5,                                  
            marker=None)                                    


ax.scatter(asistencia_masculino, years, color='#1f77b4', s=60, label='Masculino', zorder=3)

ax.scatter(asistencia_femenino, years, color='#ff7f0e', s=60, label='Femenino', zorder=3)

ax.set_title('Comparación Asistencia Total: Mundial FIFA Masculino vs. Femenino', fontsize=14, pad=20)
ax.set_xlabel('Cantidad Total de Asistentes', fontsize=11)
ax.set_ylabel('Año del Mundial Femenino', fontsize=11)

ax.set_yticks(years)
ax.set_yticklabels(years) 

def millions_formatter(x, pos):

    if x >= 1e6:
        return f'{x*1e-6:.1f}M'

    elif x >= 1e3:
         return f'{x*1e-3:.0f}K'

    else:
        return f'{x:.0f}'

ax.xaxis.set_major_formatter(mticker.FuncFormatter(millions_formatter))

ax.set_xlim(left=0, right=max(asistencia_masculino) * 1.05) 


ax.legend(loc='lower right', fontsize=10)

ax.grid(True, axis='x', linestyle='--', color='grey', alpha=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(0.5)
ax.spines['bottom'].set_linewidth(0.5)

plt.tight_layout()

plt.show()
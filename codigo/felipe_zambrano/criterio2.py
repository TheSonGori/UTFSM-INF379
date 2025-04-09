import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


years = [2017, 2025]
salario_mujer_nwsl = [27054, 65000]
salario_hombre_mls = [337355, 354390]
salario_mujer_d1 = [49000, 138000] 
categories = ['Mujer NWSL', 'Hombre MLS', 'Mujer D1']


fig, ax = plt.subplots(figsize=(9, 7)) 

x_coords = [0, 1]

ax.plot(x_coords, salario_mujer_nwsl, marker='o', linestyle='-', color='#ff7f0e', linewidth=2, markersize=8, label='Mujer NWSL')

ax.plot(x_coords, salario_hombre_mls, marker='o', linestyle='-', color='#1f77b4', linewidth=2, markersize=8, label='Hombre MLS')

ax.plot(x_coords, salario_mujer_d1, marker='o', linestyle='-', color='#2ca02c', linewidth=2, markersize=8, label='Mujer D1')

ax.text(x_coords[0] - 0.04, salario_mujer_nwsl[0], f'{salario_mujer_nwsl[0]:,}', ha='right', va='center', fontsize=9, color='#ff7f0e')
ax.text(x_coords[1] + 0.04, salario_mujer_nwsl[1], f'{salario_mujer_nwsl[1]:,}', ha='left', va='center', fontsize=9, color='#ff7f0e')

ax.text(x_coords[0] - 0.04, salario_hombre_mls[0], f'{salario_hombre_mls[0]:,}', ha='right', va='top', fontsize=9, color='#1f77b4') 
ax.text(x_coords[1] + 0.04, salario_hombre_mls[1], f'{salario_hombre_mls[1]:,}', ha='left', va='top', fontsize=9, color='#1f77b4') 
ax.text(x_coords[0] - 0.04, salario_mujer_d1[0], f'{salario_mujer_d1[0]:,}', ha='right', va='center', fontsize=9, color='#2ca02c')
ax.text(x_coords[1] + 0.04, salario_mujer_d1[1], f'{salario_mujer_d1[1]:,}', ha='left', va='center', fontsize=9, color='#2ca02c')


ax.set_title('Comparación Evolución Salario Promedio: 2017 vs 2025', fontsize=14, pad=20)
ax.set_ylabel('Salario Promedio Anual USD', fontsize=11) 
ax.set_xticks(x_coords)
ax.set_xticklabels(years, fontsize=12)
ax.tick_params(axis='x', length=0)

def comma_formatter(x, pos):
    return f'{x:,.0f}'
ax.yaxis.set_major_formatter(mticker.FuncFormatter(comma_formatter))
ax.tick_params(axis='y', labelsize=10)

ax.legend(fontsize=10, loc='best') 


ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5)
ax.tick_params(left=False)


min_val = min(salario_mujer_nwsl + salario_hombre_mls + salario_mujer_d1)
max_val = max(salario_mujer_nwsl + salario_hombre_mls + salario_mujer_d1)

ax.set_ylim(min_val * 0.7, max_val * 1.15)


plt.tight_layout()


plt.show()
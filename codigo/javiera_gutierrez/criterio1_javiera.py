import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import make_interp_spline
import numpy as np

# Leer datos
df_ig = pd.read_excel("../../fuentes_datos/criterio1_javiera/criterio1_javiera_instagram.xlsx")
df_ig["Plataforma"] = "Instagram"
df_tt = pd.read_excel("../../fuentes_datos/criterio1_javiera/criterio1_javiera_tiktok.xlsx")
df_tt["Plataforma"] = "TikTok"
df_yt = pd.read_excel("../../fuentes_datos/criterio1_javiera/criterio1_javiera_youtube.xlsx")
df_yt["Plataforma"] = "YouTube"

df = pd.concat([df_ig, df_tt, df_yt])
df["Fecha"] = pd.to_datetime(df["Year"].astype(str) + "-" + df["Month"], format="%Y-%B")
df = df.sort_values("Fecha")

# mejorar estetica del grafico
plataformas = ["YouTube", "TikTok", "Instagram"]
colores = ["#EF476F", "#06D6A0", "#FFC6D0"]

sns.set_style("white")
plt.rcParams.update({
    "font.family": "Segoe UI",
    "axes.edgecolor": "white",
    "axes.linewidth": 0.8,
    "font.size": 12
})

fig, axes = plt.subplots(len(plataformas), 1, figsize=(14, 8), sharex=True)
plt.subplots_adjust(hspace=0.75)

# joyplot por plataforma
for i, (plataforma, color) in enumerate(zip(plataformas, colores)):
    sub = df[df["Plataforma"] == plataforma]
    fechas = sub["Fecha"].values.astype("float64")
    y = sub["Followers"].values

    if len(fechas) > 3:
        xnew = np.linspace(fechas.min(), fechas.max(), 300)
        spl = make_interp_spline(fechas, y, k=2)
        y_smooth = spl(xnew)
        x_plot = pd.to_datetime(xnew)
    else:
        x_plot = sub["Fecha"]
        y_smooth = y

    ax = axes[i]
    ax.plot(x_plot, y_smooth, color=color, lw=2.8)
    ax.fill_between(x_plot, y_smooth, color=color, alpha=0.3)

    ax.text(
        x_plot.min(), max(y_smooth)*0.92, plataforma,
        color=color, fontsize=14, fontweight='bold',
        ha='left', va='top'
    )

    ax.set_yticks([])
    ax.set_ylabel("")
    ax.set_xlim([df["Fecha"].min(), df["Fecha"].max()])
    sns.despine(ax=ax, bottom=True, left=True)
    ax.grid(visible=False)

# Titulo bonito y centrado
fig.suptitle("Evolución mensual de seguidores por plataforma – Al-Nassr",
             fontsize=20, fontweight='bold', x=0.5, y=0.98)

axes[-1].set_xlabel("Mes", fontsize=13)
fig.autofmt_xdate()

# Guardar y mostrar
plt.savefig("ridge_plot_alnassr_final.png", dpi=300, bbox_inches="tight", transparent=True)
plt.show()

import pandas as pd
import plotly.express as px

# Leer los archivos
df_ig = pd.read_excel("../../fuentes_datos/criterio1_javiera/criterio1_javiera_instagram.xlsx")
df_ig["Plataforma"] = "Instagram"

df_tt = pd.read_excel("../../fuentes_datos/criterio1_javiera/criterio1_javiera_tiktok.xlsx")
df_tt["Plataforma"] = "TikTok"

df_yt = pd.read_excel("../../fuentes_datos/criterio1_javiera/criterio1_javiera_youtube.xlsx")
df_yt["Plataforma"] = "YouTube"

# Unir
df = pd.concat([df_ig, df_tt, df_yt], ignore_index=True)
df["Fecha"] = pd.to_datetime(df["Year"].astype(str) + "-" + df["Month"], format="%Y-%B")
df = df.sort_values("Fecha")

# Orden deseado (de arriba hacia abajo: YouTube, TikTok, Instagram)
orden_manual = ["YouTube", "TikTok", "Instagram"]
df["Plataforma"] = pd.Categorical(df["Plataforma"], categories=orden_manual, ordered=True)

# Graficar
fig = px.scatter(
    df,
    x="Fecha",
    y="Plataforma",
    size="Followers",
    color="Plataforma",
    hover_data=["Followers"],
    title="Dot Plot: Seguidores mensuales por plataforma – Al-Nassr",
    width=900,
    height=400,
    size_max=25
)

fig.update_yaxes(categoryorder="array", categoryarray=orden_manual[::-1]) 

fig.update_traces(marker=dict(sizemode='area', line=dict(width=1, color='gray')))
fig.update_layout(
    title={
        'text': "Dot Plot: Seguidores mensuales por plataforma – Al-Nassr",
        'x': 0.5, 
        'xanchor': 'center'
    },
    xaxis_title="Mes",
    yaxis_title="Plataforma (orden manual)",
    template="plotly_white"
)

fig.show()

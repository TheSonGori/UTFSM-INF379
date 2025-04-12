import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# Leer archivo Excel
df = pd.read_excel("../../fuentes_datos/criterio2_javiera/criterio2_javiera.xlsx")
df.columns = df.columns.astype(str).str.strip()

# Validacion de columnas
if "Club" not in df.columns or "2023" not in df.columns or "2024" not in df.columns:
    raise ValueError("Faltan columnas necesarias: 'Club', '2023' o '2024'.")

# Transformar a formato largo
df_long = df.melt(id_vars="Club", value_vars=["2023", "2024"],
                  var_name="Año", value_name="Ingresos")

# Angulos para cada club
n_clubs = df["Club"].nunique()
angles = np.linspace(0, 360, n_clubs, endpoint=False)
angle_map = dict(zip(df["Club"], angles))
df_long["theta"] = df_long["Club"].map(angle_map)

# Separar las barras 2023 y 2024
offset = 6  
df_long["theta"] = df_long.apply(
    lambda row: row["theta"] - offset if row["Año"] == "2023" else row["theta"] + offset,
    axis=1
)

# Colores únicos por club
palette = px.colors.qualitative.Bold 
club_list = df["Club"].tolist()
color_map = {club: palette[i % len(palette)] for i, club in enumerate(club_list)}

# Crear grrafico
fig = go.Figure()

for club in club_list:
    datos = df_long[df_long["Club"] == club]
    fig.add_trace(go.Barpolar(
        r=datos["Ingresos"],
        theta=datos["theta"],
        width=[8, 8],
        name=club,
        marker_color=color_map[club],
        hovertemplate=(
            f"<b>{club}</b><br>" +
            "Año: %{customdata[0]}<br>" +
            "Ingresos: %{r} M€<extra></extra>"
        ),
        customdata=np.stack([datos["Año"]], axis=-1)
    ))

#Mejorar la visual del grafico
fig.update_layout(
    title={
        "text": "Ingresos por camisetas por club 2023 vs 2024",
        "x": 0.5,
        "xanchor": "center",
        "font": dict(size=22)
    },
    polar=dict(
        radialaxis=dict(
            showticklabels=True,
            ticks='',
            gridcolor='lightgrey',
            linewidth=1,
            tickfont=dict(size=13)
        ),
        angularaxis=dict(
            tickmode='array',
            tickvals=angles,
            ticktext=club_list,
            tickfont=dict(size=14, family="Arial Black"),
            rotation=90,
            direction="clockwise"
        )
    ),
    legend=dict(
        title="Club",
        orientation="h",
        yanchor="bottom",
        y=-0.15,
        xanchor="center",
        x=0.5,
        font=dict(size=12)
    ),

    font=dict(family="Segoe UI", size=12),
    margin=dict(t=90, b=30),
    width=950,
    height=750,
    template="plotly_white"
)

fig.show()

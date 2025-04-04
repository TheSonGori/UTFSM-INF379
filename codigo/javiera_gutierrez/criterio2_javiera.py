import pandas as pd
import plotly.express as px

# Leer archivo
df = pd.read_excel("../../fuentes_datos/criterio2_javiera/criterio2_javiera.xlsx")
df.rename(columns={2023: "2023", 2024: "2024"}, inplace=True)

# Calcular métricas
df["Crecimiento absoluto"] = df["2024"] - df["2023"]
df["Crecimiento relativo (%)"] = ((df["2024"] - df["2023"]) / df["2023"]) * 100
df["Tendencia"] = df["Crecimiento absoluto"].apply(lambda x: "Sube" if x > 0 else "Baja")
df["Tamaño burbuja"] = df["Crecimiento absoluto"].abs()

# Bubble Plot
fig = px.scatter(
    df,
    x="2023",
    y="2024",
    size="Tamaño burbuja",
    color="Tendencia",
    hover_name="Club",
    size_max=40,
    title="Bubble Plot: Comparación de ingresos por camisetas (2023 vs 2024)",
    labels={
        "2023": "Ingresos 2023 (€M)",
        "2024": "Ingresos 2024 (€M)",
        "Tamaño burbuja": "Cambio Absoluto (€M)"
    }
)

fig.update_layout(
    title=dict(x=0.5, xanchor="center"),
    template="plotly_white",
    width=950,
    height=600
)

fig.show()

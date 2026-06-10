import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

st.title("🐺 Wolf Tracker")
st.write("Dashboard de análisis de riesgo financiero")

# --- Entrada de tickers libre ---
texto = st.text_input(
    "Escribe los tickers separados por coma:",
    placeholder="Ej. AAPL, MSFT, GOOG"
)

tickers = [t.strip().upper() for t in texto.split(",") if t.strip()]

# --- Selector de fecha ---
col1, col2 = st.columns(2) # dos columnas de lado a lado
with col1:
    fecha_inicio = st.date_input("Fecha de inicio", value=None)
with col2:
    fecha_fin = st.date_input("Fecha de fin", value=None)

# --- Validación + descarga ---
if not tickers:
    st.warning("Escribe al menos un ticker.")
elif fecha_inicio is None or fecha_fin is None:
    st.info("Selecciona ambas fechas para comenzar.")
elif fecha_inicio >= fecha_fin:
    st.error("La fecha de inicio debe ser anterior a la fecha de fin.")
else:
    data = yf.download(tickers=tickers, start=fecha_inicio, end=fecha_fin,
                        auto_adjust=True, progress=False)
    prices = data["Close"]

    # Detectar tickers que no trajeron datos (inválidos o mal escritos)
    validos = [t for t in tickers if t in prices.columns and prices[t].notna().any()]
    invalidos = [t for t in tickers if t not in validos]

    if invalidos:
        st.error(f"No encontré datos para: {', '.join(invalidos)}. Revisa que estén bien escritos.")

    if validos:
        prices = prices[validos]   # quedarse solo con los que sí jalaron
        st.subheader("Precios de cierre (últimos días)")
        st.dataframe(prices.tail(10))
        
        st.subheader("📈 Crecimiento comparado (base 100)")
        
        # Rebasear a base 100: todas arrancan en 100
        base100 = prices / prices.iloc[0] * 100
        st.line_chart(base100)
    else:
        st.warning("Ningún ticker válido. Intenta de nuevo.")


import streamlit as st

# Configuración visual para móvil
st.set_page_config(page_title="LH Aberturas", page_icon="🦁")

# CSS para mejorar el contraste de los totales
st.markdown("""
    <style>
    .stMetric {
        background-color: #1e1e1e !important;
        border: 1px solid #3d3d3d;
        padding: 15px !important;
        border-radius: 10px;
    }
    [data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-weight: bold;
    }
    [data-testid="stMetricLabel"] {
        color: #a0a0a0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("LH Aberturas")
st.subheader("Optimizador de Corte y Precios")

# Parámetros de Costos
P_ALU = 13000
P_COMUN = 20000
P_DVH = 60000
ACCESORIOS = 15000

# Entradas
linea = st.radio("Seleccione Línea:", ["Herrero", "Modena"], horizontal=True)
ancho = st.number_input("Ancho Total (cm)", min_value=0.0, step=0.1, format="%.1f")
alto = st.number_input("Alto Total (cm)", min_value=0.0, step=0.1, format="%.1f")

if ancho > 0 and alto > 0:
    st.markdown("---")
    
    if linea == "Herrero":
        # Cortes Herrero
        n1 = ancho  # Marco Horiz
        n1_v = alto # Marco Vert
        n2 = (ancho / 2) - 9.6
        n3_4 = alto - 6.4
        v_a, v_h = (ancho / 2) - 8, alto - 14.5
        
        # Peso Herrero: N1(0.58), N2(0.41), N3/4(0.40)
        peso = (((n1*2 + n1_v*2)/100)*0.58) + ((n2*4/100)*0.41) + ((n3_4*4/100)*0.40)
        costo_v = (v_a * v_h * 2 / 10000) * P_COMUN
        tipo_v = "Común"
        
        st.success("📐 LISTA DE CORTE (HERRERO)")
        st.write(f"**Número 1:** {n1:.1f} cm (Ancho) / {n1_v:.1f} cm (Alto)")
        st.write(f"**Número 2:** {n2:.1f} cm")
        st.write(f"**Número 3 y 4:** {n3_4:.1f} cm")
        st.info(f"🖼 **Vidrio {tipo_v}:** {v_a:.1f} x {v_h:.1f} cm (x2)")

    else:
        # Cortes Modena
        jamba = alto
        umbral = ancho - 4.3
        n2 = ((ancho - 4.3) / 2) - 0.4
        n3_4 = alto - 8
        v_a, v_h = (ancho / 2) - 7.3, alto - 16
        
        # Peso Modena: Umbral(1.33), Jamba/N2/N3/N4(0.66)
        peso = ((umbral*2/100)*1.33) + (((jamba*2 + n2*4 + n3_4*4)/100)*0.66)
        costo_v = (v_a * v_h * 2 / 10000) * P_DVH
        tipo_v = "DVH"
        
        st.success("📐 LISTA DE CORTE (MODENA)")
        st.write(f"**Jamba:** {jamba:.1f} cm")
        st.write(f"**Umbral:** {umbral:.1f} cm")
        st.write(f"**Número 2:** {n2:.1f} cm")
        st.write(f"**Número 3 y 4:** {n3_4:.1f} cm")
        st.info(f"🖼 **Vidrio {tipo_v}:** {v_a:.1f} x {v_h:.1f} cm (x2)")

    # Totales y Presupuesto
    costo_a = peso * P_ALU
    total = costo_a + costo_v + ACCESORIOS
    
    st.markdown("---")
    st.metric("PESO TOTAL", f"{peso:.2f} kg")
    st.metric("PRESUPUESTO TOTAL", f"${total:,.0f}")
    
    with st.expander("Ver detalle de costos"):
        st.write(f"Aluminio: ${costo_a:,.0f}")
        st.write(f"Vidrio: ${costo_v:,.0f}")
        st.write(f"Accesorios: ${ACCESORIOS:,.0f}")

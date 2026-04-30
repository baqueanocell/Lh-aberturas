import streamlit as st

# Configuración visual para móvil
st.set_page_config(page_title="LH Aberturas", page_icon="🦁")

# Estilo para que se vea bien en pantallas chicas
st.markdown("""
    <style>
    .main { text-align: center; }
    .stMetric { background-color: #f0f2f6; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("LH Aberturas")
st.subheader("Optimizador de Corte y Precios")

# Parámetros de Costos (Editables aquí)
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
        n1_hor = ancho
        n1_vert = alto
        n2 = (ancho / 2) - 9.6
        n3 = alto - 6.4
        v_a, v_h = (ancho / 2) - 8, alto - 14.5
        
        # Peso Herrero
        peso = (((ancho*2 + alto*2)/100)*0.58) + ((n2*4/100)*0.41) + ((n3*4/100)*0.40)
        costo_v = (v_a * v_h * 2 / 10000) * P_COMUN
        
        st.success("📐 LISTA DE CORTE (HERRERO)")
        st.write(f"**Marco Horiz. (#1):** {n1_hor:.1f} cm")
        st.write(f"**Marco Vert. (#1):** {n1_vert:.1f} cm")
        st.write(f"**Hoja Horiz. (#2):** {n2:.1f} cm")
        st.write(f"**Hoja Vert. (#3/4):** {n3:.1f} cm")
        st.info(f"🖼 **Vidrio Común:** {v_a:.1f} x {v_h:.1f} cm (x2)")

    else:
        # Cortes Modena
        jamba = alto
        umbral = ancho - 4.3
        n2 = ((ancho - 4.3) / 2) - 0.4
        n3 = alto - 8
        v_a, v_h = (ancho / 2) - 7.3, alto - 16
        
        # Peso Modena
        peso = (((ancho-4.3)*2/100)*1.33) + (((alto*2 + n2*4 + n3*4)/100)*0.66)
        costo_v = (v_a * v_h * 2 / 10000) * P_DVH
        
        st.success("📐 LISTA DE CORTE (MODENA)")
        st.write(f"**Jamba:** {jamba:.1f} cm")
        st.write(f"**Umbral:** {umbral:.1f} cm")
        st.write(f"**Hoja Horiz. (N2):** {n2:.1f} cm")
        st.write(f"**Hoja Vert. (N3/4):** {n3:.1f} cm")
        st.info(f"🖼 **Vidrio DVH:** {v_a:.1f} x {v_h:.1f} cm (x2)")

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

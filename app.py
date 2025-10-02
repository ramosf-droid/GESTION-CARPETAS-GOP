import streamlit as st

st.title("📂 Gestión de Carpetas del Estudio Jurídico")

# Simulación de una base de datos en memoria (se borrará al reiniciar)
if "carpetas" not in st.session_state:
    st.session_state["carpetas"] = []

# Formulario para agregar una carpeta
with st.form("nueva_carpeta"):
    nro_carpeta = st.text_input("Número de carpeta (6 dígitos)")
    caratula = st.text_input("Carátula")
    nro_expediente = st.text_input("Número de expediente")
    tipo_caso = st.selectbox("Tipo de caso", ["Civil", "Penal", "Laboral", "Familia", "Otro"])
    cliente = st.text_input("Cliente")
    color = st.color_picker("Color de cartulina")
    submitted = st.form_submit_button("Agregar")

    if submitted:
        st.session_state["carpetas"].append({
            "nro_carpeta": nro_carpeta,
            "caratula": caratula,
            "nro_expediente": nro_expediente,
            "tipo_caso": tipo_caso,
            "cliente": cliente,
            "color": color
        })
        st.success("✅ Carpeta agregada")

# Mostrar lista de carpetas cargadas
st.subheader("📑 Carpetas registradas")
for carpeta in st.session_state["carpetas"]:
    st.write(f"📂 **{carpeta['nro_carpeta']}** - {carpeta['caratula']} ({carpeta['tipo_caso']}) - Cliente: {carpeta['cliente']}")

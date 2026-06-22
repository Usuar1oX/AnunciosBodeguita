import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Generador de Publicidad - La Bodeguita", layout="wide")

st.title("Automator Pro: La Bodeguita (Espacios Optimizados 9:16)")
st.write("Estructura de márgenes ultra-compactos para maximizar el tamaño de las fuentes.")

# --- INICIALIZACIÓN DE ESTADOS DINÁMICOS ---
if "llegada_custom" not in st.session_state:
    st.session_state.llegada_custom = [""]
if "gancho_custom" not in st.session_state:
    st.session_state.gancho_custom = [{"nombre": "", "valor": 0}]
if "tabla_custom" not in st.session_state:
    st.session_state.tabla_custom = [{"nombre": "", "valor": 0}]

# --- SELECTOR DE PALETAS DE COLORES ---
paletas = {
    "🟡 Tradicional La Bodeguita (Amarillo/Negro/Rojo)": {
        "bg_canvas": "#FFDE00", "borde_canvas": "#000000", "texto_ppal": "#000000", "acento": "#D32F2F",
        "card_oscura_bg": "#111111", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#FFFFFF", "card_clara_fg": "#000000"
    },
    "🔴 Oferta Agresiva (Rojo/Blanco/Amarillo)": {
        "bg_canvas": "#D32F2F", "borde_canvas": "#FFFFFF", "texto_ppal": "#FFFFFF", "acento": "#FFDE00",
        "card_oscura_bg": "#FFFFFF", "card_oscura_fg": "#000000", "card_clara_bg": "#111111", "card_clara_fg": "#FFFFFF"
    },
    "⚫ Elegancia Nocturna (Negro/Blanco/Oro)": {
        "bg_canvas": "#111111", "borde_canvas": "#FFD700", "texto_ppal": "#FFFFFF", "acento": "#FFD700",
        "card_oscura_bg": "#222222", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#FFFFFF", "card_clara_fg": "#000000"
    },
    "🔵 Clásico Americano (Azul Marino/Rojo/Blanco)": {
        "bg_canvas": "#002366", "borde_canvas": "#FFFFFF", "texto_ppal": "#FFFFFF", "acento": "#D32F2F",
        "card_oscura_bg": "#FFFFFF", "card_oscura_fg": "#000000", "card_clara_bg": "#111111", "card_clara_fg": "#FFFFFF"
    },
    "🟢 Descuento Neón (Negro/Verde Neón/Blanco)": {
        "bg_canvas": "#000000", "borde_canvas": "#39FF14", "texto_ppal": "#39FF14", "acento": "#FFFFFF",
        "card_oscura_bg": "#1A1A1A", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#FFFFFF", "card_clara_fg": "#000000"
    },
    "🌸 Impacto Fucsia (Rosa Encendido/Negro/Blanco)": {
        "bg_canvas": "#FF007F", "borde_canvas": "#000000", "texto_ppal": "#FFFFFF", "acento": "#000000",
        "card_oscura_bg": "#111111", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#FFFFFF", "card_clara_fg": "#000000"
    },
    "🟤 Estilo Vintage (Crema/Marrón/Ladrillo)": {
        "bg_canvas": "#F5F5DC", "borde_canvas": "#4A2E1B", "texto_ppal": "#4A2E1B", "acento": "#B22222",
        "card_oscura_bg": "#4A2E1B", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#FFFFFF", "card_clara_fg": "#4A2E1B"
    },
    "🟠 Otoño Cálido (Mostaza/Naranja/Negro)": {
        "bg_canvas": "#E5A93C", "borde_canvas": "#111111", "texto_ppal": "#111111", "acento": "#D35400",
        "card_oscura_bg": "#111111", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#FFFFFF", "card_clara_fg": "#111111"
    },
    "💎 Verano Fresco (Turquesa/Blanco/Coral)": {
        "bg_canvas": "#40E0D0", "borde_canvas": "#000000", "texto_ppal": "#000000", "acento": "#FF6F61",
        "card_oscura_bg": "#004040", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#FFFFFF", "card_clara_fg": "#000000"
    },
    "⚪ Moda Boutique (Blanco/Gris Oxford/Negro)": {
        "bg_canvas": "#FFFFFF", "borde_canvas": "#111111", "texto_ppal": "#111111", "acento": "#555555",
        "card_oscura_bg": "#111111", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#F5F5F5", "card_clara_fg": "#111111"
    }
}

# --- SELECTOR DE FUENTES (GOOGLE FONTS) ---
fuentes = {
    "💥 Impacto Urbano (Bebas Neue + Montserrat)": {
        "import": "@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@700;900&display=swap');",
        "titulos": "'Bebas Neue', sans-serif", "cuerpo": "'Montserrat', sans-serif"
    },
    "🎯 Comercial Moderno (Oswald + Roboto)": {
        "import": "@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Roboto:wght@700;900&display=swap');",
        "titulos": "'Oswald', sans-serif", "cuerpo": "'Roboto', sans-serif"
    },
    "💎 Boutique Elegante (Playfair Display + Lora)": {
        "import": "@import url('https://fonts.googleapis.com/css2?family=Lora:wght@700&family=Playfair+Display:wght@700;900&display=swap');",
        "titulos": "'Playfair Display', serif", "cuerpo": "'Lora', serif"
    },
    "👾 Retro / Ofertas Locas (Rubik Mono One + Rubik)": {
        "import": "@import url('https://fonts.googleapis.com/css2?family=Rubik+Mono+One&family=Rubik:wght@700;900&display=swap');",
        "titulos": "'Rubik Mono One', sans-serif", "cuerpo": "'Rubik', sans-serif"
    },
    "🎈 Escolar y Dinámico (Fredoka + Quicksand)": {
        "import": "@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@700&family=Quicksand:wght@700&display=swap');",
        "titulos": "'Fredoka', sans-serif", "cuerpo": "'Quicksand', sans-serif"
    }
}

# --- LISTAS DE CATEGORÍAS FIJAS ---
categorias_ropa = ["Bebé", "Niño y Niña", "Dama", "Caballero", "Tallas Extra"]
categorias_otros = [
    "Zapatos, Bolsas, Juguetes y Vitrina",
    "Trajes de baño, Playa y Lencería",
    "Ropa de casa (Edredones, toallas, etc.)"
]
categorias_totales = categorias_ropa + categorias_otros

# --- BLOQUE 1: DATOS GENERALES ---
col_1, col_2 = st.columns(2)
with col_1:
    sucursal = st.selectbox("Sucursal:", ["La Bodeguita de la 100", "La Bodeguita Tierra Maya", "La Bodeguita Villas Otoch"])
    fechas = st.text_input("Vigencia del anuncio:", placeholder="Ej. Del miércoles 3 al sábado 6 de junio")
    gancho = st.text_input("Frase gancho (Encabezado superior):", value="¡EXCELENTES NOTICIAS PARA TI!")

with col_2:
    st.markdown("### 🎛️ PANEL DE ESTILO")
    paleta_sel = st.selectbox("1. Paleta de Colores:", list(paletas.keys()))
    c_paleta = paletas[paleta_sel]
    
    fuente_sel = st.selectbox("2. Combinación Tipográfica (Fuentes):", list(fuentes.keys()))
    c_fuente = fuentes[fuente_sel]
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        textura_fondo = st.selectbox("3A. Patrón del Fondo:", ["Liso Sólido", "Triángulos Geométricos", "Olas Chevron", "Rombos 3D", "Ondas Circulares"])
    with col_p2:
        textura_cuadros = st.selectbox("3B. Patrón de Cuadros:", ["Liso Limpio", "Geometría Sutil", "Ondas Tenues", "Líneas Diagonales"])

horarios_dict = {
    "La Bodeguita de la 100": "Horario: Lunes a Sábado 12:00 PM a 9:00 PM | Domingos 9:00 AM a 6:00 PM",
    "La Bodeguita Tierra Maya": "Horario: 11:00 AM a 8:00 PM",
    "La Bodeguita Villas Otoch": "Horario: 10:00 AM a 7:00 PM"
}
horario_automatico = horarios_dict[sucursal]

st.markdown("---")

# --- BLOQUE 2: CONSTRUCTOR DEL ANUNCIO ---
st.header("Configuración de Contenido")
tabs = st.tabs(["📦 1. Llegada (Llega para ti:)", "👗 2. Descuentos (Gancho)", "👕 3. Precios (Tabla)"])

llegada_gancho_activas = []
llegada_tabla_activas = []
llegada_otros_activas = []
fecha_llegada = ""

# -- PESTAÑA 1: LLEGADA --
with tabs[0]:
    st.subheader("Configuración de Mercancía")
    activa_llegada = st.checkbox("Incluir bloque de 'Llega para ti:'")
    if activa_llegada:
        fecha_llegada = st.text_input("Fecha específica de llegada:", placeholder="Ej. ESTE MIÉRCOLES")
        
        st.markdown("#### 👕 Ropa Colgada en Gancho")
        cols_lg = st.columns(5)
        for i, cat in enumerate(categorias_ropa):
            with cols_lg[i]:
                if st.checkbox(cat, key=f"llegada_g_{cat}"):
                    llegada_gancho_activas.append(cat)
                    
        st.markdown("#### 🧺 Ropa de Tabla")
        cols_lt = st.columns(5)
        for i, cat in enumerate(categorias_ropa):
            with cols_lt[i]:
                if st.checkbox(cat, key=f"llegada_t_{cat}"):
                    llegada_tabla_activas.append(cat)
                    
        st.markdown("#### 👜 Otros Departamentos")
        for cat in categorias_otros:
            if st.checkbox(cat, key=f"llegada_o_{cat}"):
                llegada_otros_activas.append(cat)
        
        for idx, item in enumerate(st.session_state.llegada_custom):
            st.session_state.llegada_custom[idx] = st.text_input(f"Concepto extra de llegada {idx+1}:", value=item, key=f"input_llegada_c_{idx}")
            if st.session_state.llegada_custom[idx].strip():
                llegada_otros_activas.append(st.session_state.llegada_custom[idx].strip())
        
        if st.button("➕ Agregar fila de llegada", key="btn_add_llegada"):
            st.session_state.llegada_custom.append("")
            st.rerun()

# -- PESTAÑA 2: DESCUENTOS --
gancho_dict = {}
with tabs[1]:
    st.subheader("Descuentos en Ropa de Gancho (%)")
    activa_gancho = st.checkbox("Incluir bloque de Descuentos")
    if activa_gancho:
        cols_gancho = st.columns(2)
        for i, cat in enumerate(categorias_totales):
            with cols_gancho[i % 2]:
                val = st.number_input(f"% Descuento en {cat}", min_value=0, max_value=100, step=10, key=f"gancho_{cat}")
                if val > 0:
                    gancho_dict[cat] = val
        
        for idx, item in enumerate(st.session_state.gancho_custom):
            c1, c2 = st.columns([3, 1])
            with c1: item["nombre"] = st.text_input(f"Descuento extra {idx+1}:", value=item["nombre"], key=f"name_g_c_{idx}")
            with c2: item["valor"] = st.number_input(f"%", min_value=0, max_value=100, value=item["valor"], step=10, key=f"val_g_c_{idx}")
            if item["nombre"].strip() and item["valor"] > 0:
                gancho_dict[item["nombre"].strip()] = item["valor"]
        
        if st.button("➕ Agregar fila de descuento", key="btn_add_gancho"):
            st.session_state.gancho_custom.append({"nombre": "", "valor": 0})
            st.rerun()

# -- PESTAÑA 3: ROPA DE TABLA --
tabla_dict = {}
with tabs[2]:
    st.subheader("Precios de Oferta en Ropa de Tabla ($)")
    activa_tabla = st.checkbox("Incluir bloque de Tabla")
    if activa_tabla:
        cols_tabla = st.columns(2)
        for i, cat in enumerate(categorias_totales):
            with cols_tabla[i % 2]:
                val = st.number_input(f"$ Precio en {cat}", min_value=0, step=10, key=f"tabla_{cat}")
                if val > 0:
                    tabla_dict[cat] = val
        
        for idx, item in enumerate(st.session_state.tabla_custom):
            t1, t2 = st.columns([3, 1])
            with t1: item["nombre"] = st.text_input(f"Tabla extra {idx+1}:", value=item["nombre"], key=f"name_t_c_{idx}")
            with t2: item["valor"] = st.number_input(f"$ Precio", min_value=0, value=item["valor"], step=10, key=f"val_t_c_{idx}")
            if item["nombre"].strip() and item["valor"] > 0:
                tabla_dict[item["nombre"].strip()] = item["valor"]
        
        if st.button("➕ Agregar fila de tabla", key="btn_add_tabla"):
            st.session_state.tabla_custom.append({"nombre": "", "valor": 0})
            st.rerun()

st.markdown("---")

# --- MOTOR LÓGICO DE FUSIÓN ---
def fusionar_adultos(lista_o_dict):
    if isinstance(lista_o_dict, list):
        if "Dama" in lista_o_dict and "Caballero" in lista_o_dict:
            lista_o_dict.remove("Dama")
            lista_o_dict.remove("Caballero")
            lista_o_dict.append("Adulto (Dama y Caballero)")
        return lista_o_dict
    elif isinstance(lista_o_dict, dict):
        if "Dama" in lista_o_dict and "Caballero" in lista_o_dict:
            if lista_o_dict["Dama"] == lista_o_dict["Caballero"]:
                val = lista_o_dict["Dama"]
                lista_o_dict["Adulto (Dama y Caballero)"] = val
                del lista_o_dict["Dama"]
                del lista_o_dict["Caballero"]
        return lista_o_dict

# --- GENERACIÓN ---
if st.button("🚀 PROCESAR Y VESTIR ANUNCIO VERTICAL", type="primary", use_container_width=True):
    
    mostrar_llegada = activa_llegada and (llegada_gancho_activas or llegada_tabla_activas or llegada_otros_activas or fecha_llegada)
    mostrar_gancho = activa_gancho and gancho_dict
    mostrar_tabla = activa_tabla and tabla_dict
    
    modulos_activos = sum([1 if mostrar_llegada else 0, 1 if mostrar_gancho else 0, 1 if mostrar_tabla else 0])
    
    # --- CONFIGURACIÓN DE PATRONES DE FONDO GEOMÉTRICOS Y ONDAS ---
    if textura_fondo == "Triángulos Geométricos":
        css_fondo = "background-image: linear-gradient(45deg, rgba(0,0,0,0.04) 50%, transparent 50%), linear-gradient(-45deg, rgba(255,255,255,0.06) 50%, transparent 50%); background-size: 30px 30px;"
    elif textura_fondo == "Olas Chevron":
        css_fondo = "background-image: linear-gradient(135deg, rgba(255,255,255,0.06) 25%, transparent 25%), linear-gradient(225deg, rgba(255,255,255,0.06) 25%, transparent 25%), linear-gradient(45deg, rgba(0,0,0,0.04) 25%, transparent 25%), linear-gradient(315deg, rgba(0,0,0,0.04) 25%, transparent 25%); background-position: -20px 0, -20px 0, 0 0, 0 0; background-size: 40px 40px;"
    elif textura_fondo == "Rombos 3D":
        css_fondo = "background-image: linear-gradient(45deg, rgba(255,255,255,0.07) 25%, transparent 25%, transparent 75%, rgba(255,255,255,0.07) 75%, rgba(255,255,255,0.07)), linear-gradient(45deg, rgba(0,0,0,0.05) 25%, transparent 25%, transparent 75%, rgba(0,0,0,0.05) 75%, rgba(0,0,0,0.05)); background-size: 40px 40px; background-position: 0 0, 20px 20px;"
    elif textura_fondo == "Ondas Circulares":
        css_fondo = "background-image: radial-gradient(circle at 100% 50%, transparent 20%, rgba(255,255,255,0.06) 21%, rgba(255,255,255,0.06) 34%, transparent 35%, transparent), radial-gradient(circle at 0% 50%, transparent 20%, rgba(0,0,0,0.04) 21%, rgba(0,0,0,0.04) 34%, transparent 35%, transparent); background-size: 40px 50px;"
    else:
        css_fondo = ""

    # --- PATRONES INTERNOS PARA LOS CUADROS (MAYOR LEGIBILIDAD) ---
    if textura_cuadros == "Geometría Sutil":
        css_textura_c_oscura = "background-image: linear-gradient(45deg, rgba(255,255,255,0.03) 25%, transparent 25%, transparent 75%, rgba(255,255,255,0.03) 75%), linear-gradient(45deg, rgba(255,255,255,0.03) 25%, transparent 25%, transparent 75%, rgba(255,255,255,0.03) 75%); background-size: 20px 20px; background-position: 0 0, 10px 10px;"
        css_textura_c_clara = "background-image: linear-gradient(45deg, rgba(0,0,0,0.02) 25%, transparent 25%, transparent 75%, rgba(0,0,0,0.02) 75%), linear-gradient(45deg, rgba(0,0,0,0.02) 25%, transparent 25%, transparent 75%, rgba(0,0,0,0.02) 75%); background-size: 20px 20px; background-position: 0 0, 10px 10px;"
    elif textura_cuadros == "Ondas Tenues":
        css_textura_c_oscura = "background-image: radial-gradient(circle, transparent 20%, rgba(255,255,255,0.03) 20%, rgba(255,255,255,0.03) 80%, transparent 80%, transparent); background-size: 30px 30px;"
        css_textura_c_clara = "background-image: radial-gradient(circle, transparent 20%, rgba(0,0,0,0.02) 20%, rgba(0,0,0,0.02) 80%, transparent 80%, transparent); background-size: 30px 30px;"
    elif textura_cuadros == "Líneas Diagonales":
        css_textura_c_oscura = "background-image: repeating-linear-gradient(45deg, transparent, transparent 10px, rgba(255,255,255,0.03) 10px, rgba(255,255,255,0.03) 12px);"
        css_textura_c_clara = "background-image: repeating-linear-gradient(45deg, transparent, transparent 10px, rgba(0,0,0,0.03) 10px, rgba(0,0,0,0.03) 12px);"
    else:
        css_textura_c_oscura = ""
        css_textura_c_clara = ""


    # --- ESCALAS FUERTES Y RECALIBRADAS (NUEVO: FUENTES MÁS GRANDES) ---
    if modulos_activos == 1:
        size_sucursal = "48px"
        size_titulo_modulo = "26px"
        size_subheading_llegada = "21px"  
        size_texto = "19px"  # Categorías gigantes
        size_porcentaje = "50px"
        size_precio = "24px"
    elif modulos_activos == 2:
        size_sucursal = "42px"
        size_titulo_modulo = "23px"
        size_subheading_llegada = "18px"  
        size_texto = "16px"  # Categorías muy visibles
        size_porcentaje = "42px"
        size_precio = "20px"
    else: 
        size_sucursal = "36px"
        size_titulo_modulo = "20px"
        size_subheading_llegada = "15px"  
        size_texto = "14px"  # Formato comprimido optimizado
        size_porcentaje = "34px"
        size_precio = "17px"

    sufijo_sucursal = sucursal.replace("La Bodeguita ", "").upper()
    html_modulos = ""
    
    # Lógica 1: "LLEGA PARA TI:"
    if mostrar_llegada:
        html_llegada_interior = ""
        if fecha_llegada.strip():
            html_llegada_interior += f"<div style='text-align:center; background:{c_paleta['bg_canvas']}; color:{c_paleta['texto_ppal']}; padding:4px; font-size:{size_texto}; font-weight:900; margin-bottom:8px; border-radius:4px; border:2px solid {c_paleta['borde_canvas']}; font-family:{c_fuente['titulos']}; letter-spacing:1px;'>🚀 {fecha_llegada.strip().upper()} 🚀</div>"
        
        if llegada_gancho_activas:
            gancho_fusionado = fusionar_adultos(llegada_gancho_activas.copy())
            li_gancho = "".join([f"<div style='margin-left:4px; margin-bottom:1px; font-size:{size_texto}; font-weight:700; color:{c_paleta['card_oscura_fg']};'>• {c.upper()}</div>" for c in gancho_fusionado])
            html_llegada_interior += f"""
            <div style='margin-bottom:8px; line-height:1.25;'>
                <b style='color:{c_paleta['bg_canvas']}; font-size:{size_subheading_llegada}; font-family:{c_fuente['titulos']}; letter-spacing:0.5px;'>ROPA COLGADA EN GANCHO</b>
                {li_gancho}
            </div>
            """
            
        if llegada_tabla_activas:
            tabla_fusionada = fusionar_adultos(llegada_tabla_activas.copy())
            li_tabla = "".join([f"<div style='margin-left:4px; margin-bottom:1px; font-size:{size_texto}; font-weight:700; color:{c_paleta['card_oscura_fg']};'>• {c.upper()}</div>" for c in tabla_fusionada])
            html_llegada_interior += f"""
            <div style='margin-bottom:8px; line-height:1.25;'>
                <b style='color:{c_paleta['bg_canvas']}; font-size:{size_subheading_llegada}; font-family:{c_fuente['titulos']}; letter-spacing:0.5px;'>ROPA DE TABLA</b>
                {li_tabla}
            </div>
            """
            
        if llegada_otros_activas:
            if llegada_gancho_activas or llegada_tabla_activas:
                html_llegada_interior += f"<div style='margin-bottom:6px; border-top:2px dashed {c_paleta['bg_canvas']}; opacity:0.2;'></div>"
            for o in llegada_otros_activas:
                html_llegada_interior += f"<div style='margin-bottom:2px; color:{c_paleta['card_oscura_fg']}; font-size:{size_texto}; font-weight:700;'>📌 {o.upper()}</div>"
                
        html_modulos += f"<div style='background:{c_paleta['card_oscura_bg']}; {css_textura_c_oscura} color:{c_paleta['card_oscura_fg']}; padding:10px 12px; margin-bottom:8px; text-align:left; border:3px solid {c_paleta['borde_canvas']}; box-shadow:0 3px 0 {c_paleta['borde_canvas']};'><h3 style='color:{c_paleta['bg_canvas']}; text-align:center; margin-top:0; font-family:{c_fuente['titulos']}; font-size:{size_titulo_modulo}; letter-spacing:1px; margin-bottom:6px; white-space: nowrap;'>LLEGA PARA TI:</h3>{html_llegada_interior}</div>"

    # Lógica 2: Descuentos en Ropa de Gancho
    if mostrar_gancho:
        gancho_dict = fusionar_adultos(gancho_dict)
        grupos_desc = {}
        for cat, desc in gancho_dict.items():
            if desc not in grupos_desc: grupos_desc[desc] = []
            grupos_desc[desc].append(cat.upper())
            
        bloques_desc_html = ""
        for desc, categories in sorted(grupos_desc.items(), reverse=True):
            texto_cats = " Y ".join(categories) if len(categories) <= 2 else ", ".join(categories[:-1]) + " Y " + categories[-1]
            bloques_desc_html += f"""
            <div style='margin-bottom:8px; display:flex; align-items:center;'>
                <div style='display:flex; justify-content:center; align-items:center; min-width:85px; width:85px; height:85px; background-color:{c_paleta['acento']}; color:#fff; font-family:{c_fuente['titulos']}; font-size:{size_porcentaje}; text-shadow:2px 2px 0px rgba(0,0,0,0.4); margin-right:12px; clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);'>
                    {desc}%
                </div>
                <span style='font-size:{size_texto}; font-weight:900; margin-left:12px; line-height:1.2; text-align:left; font-family:{c_fuente['cuerpo']}; color:{c_paleta['card_clara_fg']};'>
                    DE DESCUENTO EN<br><span style='color:{c_paleta['acento']};'>{texto_cats}</span>
                </span>
            </div>
            """
            
        html_modulos += f"""
        <div style='background:{c_paleta['card_clara_bg']}; {css_textura_c_clara} border:3px solid {c_paleta['borde_canvas']}; padding:10px 12px; margin-bottom:8px; box-shadow:0 3px 0 {c_paleta['borde_canvas']};'>
            <h3 style='color:{c_paleta['texto_ppal']}; text-align:center; margin-top:0; background:{c_paleta['bg_canvas']}; padding:4px; border-radius:4px; font-family:{c_fuente['titulos']}; font-size:{size_titulo_modulo}; border:2px solid {c_paleta['borde_canvas']}; letter-spacing:0.5px; margin-bottom:8px; line-height:1.1;'>
                🔥 DESCUENTOS EN ROPA<br>COLGADA EN GANCHO 🔥
            </h3>
            {bloques_desc_html}
        </div>
        """

    # Lógica 3: Ropa de Tabla
    if mostrar_tabla:
        tabla_dict = fusionar_adultos(tabla_dict)
        items_tabla = ""
        for cat, precio in tabla_dict.items():
            items_tabla += f"""
            <div style='border-bottom:1px dashed #ddd; padding-bottom:2px; display:flex; flex-direction:column; text-align:left; font-family:{c_fuente['cuerpo']};'>
                <span style='font-size:{size_texto}; color:{c_paleta['card_clara_fg']}; font-weight:900; line-height:1.15;'>📌 {cat.upper()}</span>
                <span style='font-size:{size_texto}; font-weight:900; color:{c_paleta['card_clara_fg']}; line-height:1.15;'><b style='color:{c_paleta['acento']}; font-size:{size_precio}; font-family:{c_fuente['titulos']};'>${precio}</b> LA PIEZA</span>
            </div>
            """
        
        html_modulos += f"""
        <div style='background:{c_paleta['card_clara_bg']}; {css_textura_c_clara} border:3px solid {c_paleta['borde_canvas']}; padding:10px 12px; margin-bottom:8px; box-shadow:0 3px 0 {c_paleta['borde_canvas']};'>
            <h3 style='color:{c_paleta['card_oscura_fg']}; background:{c_paleta['card_oscura_bg']}; text-align:center; margin-top:0; padding:4px; border-radius:4px; font-family:{c_fuente['titulos']}; font-size:{size_titulo_modulo}; letter-spacing:1px; margin-bottom:8px; white-space: nowrap;'>ROPA DE TABLA</h3>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 8px;'>
                {items_tabla}
            </div>
        </div>
        """

    # --- PLANTILLA MAESTRA ADAPTABLE CON MÁRGENES COMPACTOS ---
    html_completo = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <style>{c_fuente['import']}</style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
        <style>
            body {{ font-family: {c_fuente['cuerpo']}; background: #f0f2f5; padding: 5px; text-align: center; }}
            /* NUEVO MARCO COMPACTO: padding reducido al mínimo para ensanchar los textos internos */
            .contenedor-canvas {{ 
                width: 432px; 
                height: auto; 
                background-color: {c_paleta['bg_canvas']}; 
                {css_fondo} 
                padding: 12px; /* Reducido de 24px a 12px para ganar espacio horizontal */
                box-sizing: border-box; 
                border: 8px solid {c_paleta['borde_canvas']}; /* Reducido de 10px a 8px */
                margin: 0 auto; 
                position: relative; 
                overflow: hidden; 
                display: flex; 
                flex-direction: column; 
                gap: 8px; /* Reducido de 15px a 8px para un empaquetado ultra-apretado */
            }}
            .marca-principal {{
                font-size: 19px;
                font-family: {c_fuente['titulos']};
                color: {c_paleta['texto_ppal']};
                margin: 2px 0 0 0;
                text-transform: uppercase;
                letter-spacing: 2px;
                line-height: 1;
                font-weight: normal;
                opacity: 0.85;
            }}
            .sucursal-estricta {{
                font-size: {size_sucursal}; 
                font-family: {c_fuente['titulos']}; 
                margin: 0 0 4px 0; 
                color: {c_paleta['acento']}; 
                text-transform: uppercase; 
                letter-spacing: 0.5px; 
                font-weight: 900; 
                line-height: 1; 
                white-space: nowrap; 
            }}
            .btn-descargar {{ background: #25D366; color: white; border: 3px solid #000; padding: 12px 24px; font-family: {c_fuente['titulos']}; font-size: 24px; border-radius: 8px; cursor: pointer; margin-top: 15px; box-shadow: 4px 4px 0 #000; letter-spacing: 1px; }}
            .btn-descargar:active {{ transform: translate(2px, 2px); box-shadow: 1px 1px 0 #000; }}
        </style>
    </head>
    <body>

        <div id="anuncioPublicitario" class="contenedor-canvas">
            <div style="font-size:22px; font-family:{c_fuente['titulos']}; background:{c_paleta['borde_canvas']}; color:{c_paleta['card_oscura_fg']}; padding:5px; border-radius:4px; text-transform:uppercase; letter-spacing:1px;">
                {gancho}
            </div>
            
            <div>
                <div class="marca-principal">LA BODEGUITA</div>
                <div class="sucursal-estricta">{sufijo_sucursal}</div>
            </div>
            
            <div style="display:flex; flex-direction:column; justify-content:center;">
                {html_modulos}
            </div>
            
            <div style="background:{c_paleta['borde_canvas']}; color:{c_paleta['bg_canvas']}; padding:8px; border-radius:6px; text-align:center; border: 2px solid {c_paleta['borde_canvas']}; margin-top: auto;">
                <div style="font-size:19px; font-family:{c_fuente['titulos']}; margin-bottom:2px; letter-spacing:0.5px;">VÁLIDO: {fechas}</div>
                <div style="font-size:11px; font-weight:700; opacity:0.9;">{horario_automatico}</div>
            </div>
        </div>

        <button class="btn-descargar" onclick="descargarAnuncio()">📥 DESCARGAR ANUNCIO PERSONALIZADO</button>

        <script>
        function descargarAnuncio() {{
            const elemento = document.getElementById('anuncioPublicitario');
            html2canvas(elemento, {{
                scale: 2.5, 
                useCORS: true,
                width: 432,
                height: elemento.offsetHeight
            }}).then(canvas => {{
                let enlace = document.createElement('a');
                enlace.download = 'historia_la_bodeguita_custom.png';
                enlace.href = canvas.toDataURL('image/png');
                enlace.click();
            }});
        }}
        </script>
    </body>
    </html>
    """
    
    st.success("¡Estructura compactada al límite! Los textos de las categorías ahora aprovechan el ancho máximo.")
    components.html(html_completo, height=1000, scrolling=True)
import html
import math
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

def generar_estrella_clip_path(puntas=8, factor_radio_interno=0.5):
    """Genera un clip-path 'polygon(...)' para una estrella de N puntas,
    calculando cada vértice con trigonometría en vez de escribir coordenadas
    a mano. factor_radio_interno controla qué tan picudas son las puntas
    (más bajo = puntas más afiladas)."""
    vertices = []
    total_vertices = puntas * 2
    radio_externo = 50.0
    radio_interno = radio_externo * factor_radio_interno
    for i in range(total_vertices):
        angulo = (math.pi / puntas) * i - (math.pi / 2)
        radio = radio_externo if i % 2 == 0 else radio_interno
        x = 50 + radio * math.cos(angulo)
        y = 50 + radio * math.sin(angulo)
        vertices.append(f"{x:.2f}% {y:.2f}%")
    return "polygon(" + ", ".join(vertices) + ")"

ESTRELLA_INSIGNIA_CLIP = generar_estrella_clip_path(puntas=8, factor_radio_interno=0.55)

# --- MOTOR DE CONTRASTE AUTOMÁTICO ---
# Evita que, en paletas como "Elegancia Nocturna" o "Descuento Neón", un
# texto quede invisible por tener casi la misma luminosidad que su fondo
# (ej. blanco sobre amarillo dorado, o blanco sobre blanco).
def luminancia(color_hex):
    color_hex = color_hex.lstrip("#")
    r, g, b = int(color_hex[0:2], 16), int(color_hex[2:4], 16), int(color_hex[4:6], 16)
    return (0.299 * r + 0.587 * g + 0.114 * b) / 255

def texto_legible_sobre(color_hex):
    return "#161616" if luminancia(color_hex) > 0.6 else "#FFFFFF"

def color_destacado_seguro(fondo_hex, candidato_hex, alterno_hex, umbral=0.35):
    """Usa `candidato_hex` (normalmente el acento) como color de texto/resalte,
    salvo que su luminosidad sea demasiado parecida a la del fondo donde se
    dibuja, en cuyo caso cae a `alterno_hex` para seguir siendo legible."""
    if abs(luminancia(fondo_hex) - luminancia(candidato_hex)) < umbral:
        return alterno_hex
    return candidato_hex

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

    # Colores de texto calculados para garantizar contraste sin importar la paleta
    texto_sobre_borde = texto_legible_sobre(c_paleta['borde_canvas'])   # para el ribbon del gancho
    texto_sobre_acento = texto_legible_sobre(c_paleta['acento'])       # para la insignia de % y title-pills
    acento_en_claro = color_destacado_seguro(c_paleta['card_clara_bg'], c_paleta['acento'], c_paleta['card_clara_fg'])  # para resaltes dentro de tarjetas claras
    
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

    # --- PATRONES INTERNOS PARA LOS CUADROS (MÁS PRESENCIA, SIN PERDER LEGIBILIDAD) ---
    if textura_cuadros == "Geometría Sutil":
        css_textura_c_oscura = "background-image: linear-gradient(45deg, rgba(255,255,255,0.07) 25%, transparent 25%, transparent 75%, rgba(255,255,255,0.07) 75%), linear-gradient(45deg, rgba(255,255,255,0.07) 25%, transparent 25%, transparent 75%, rgba(255,255,255,0.07) 75%); background-size: 22px 22px; background-position: 0 0, 11px 11px;"
        css_textura_c_clara = "background-image: linear-gradient(45deg, rgba(0,0,0,0.05) 25%, transparent 25%, transparent 75%, rgba(0,0,0,0.05) 75%), linear-gradient(45deg, rgba(0,0,0,0.05) 25%, transparent 25%, transparent 75%, rgba(0,0,0,0.05) 75%); background-size: 22px 22px; background-position: 0 0, 11px 11px;"
    elif textura_cuadros == "Ondas Tenues":
        css_textura_c_oscura = "background-image: radial-gradient(circle, rgba(255,255,255,0.10) 0, rgba(255,255,255,0.10) 2px, transparent 2.5px); background-size: 16px 16px;"
        css_textura_c_clara = "background-image: radial-gradient(circle, rgba(0,0,0,0.08) 0, rgba(0,0,0,0.08) 2px, transparent 2.5px); background-size: 16px 16px;"
    elif textura_cuadros == "Líneas Diagonales":
        css_textura_c_oscura = "background-image: repeating-linear-gradient(45deg, transparent, transparent 9px, rgba(255,255,255,0.07) 9px, rgba(255,255,255,0.07) 11px);"
        css_textura_c_clara = "background-image: repeating-linear-gradient(45deg, transparent, transparent 9px, rgba(0,0,0,0.06) 9px, rgba(0,0,0,0.06) 11px);"
    else:
        css_textura_c_oscura = ""
        css_textura_c_clara = ""


    # --- ESCALAS RECALIBRADAS: fuentes más grandes para reducir espacios vacíos ---
    if modulos_activos == 1:
        size_sucursal = "54px"
        size_titulo_modulo = "30px"
        size_subheading_llegada = "23px"
        size_texto = "23px"  # Categorías gigantes
        size_porcentaje = "44px"
        size_precio = "27px"
    elif modulos_activos == 2:
        size_sucursal = "46px"
        size_titulo_modulo = "26px"
        size_subheading_llegada = "20px"
        size_texto = "20px"  # Categorías muy visibles
        size_porcentaje = "38px"
        size_precio = "23px"
    else: 
        size_sucursal = "40px"
        size_titulo_modulo = "23px"
        size_subheading_llegada = "17px"
        size_texto = "18px"  # Formato compacto pero con presencia
        size_porcentaje = "33px"
        size_precio = "20px"

    sufijo_sucursal = html.escape(sucursal.replace("La Bodeguita ", "").upper())
    gancho_safe = html.escape(gancho)
    fechas_safe = html.escape(fechas)
    fecha_llegada_safe = html.escape(fecha_llegada.strip().upper())
    html_modulos = ""
    
    # Lógica 1: "LLEGA PARA TI:"
    if mostrar_llegada:
        html_llegada_interior = ""
        if fecha_llegada_safe:
            html_llegada_interior += f"<div class='pill-fecha'>🚀 {fecha_llegada_safe} 🚀</div>"
        
        if llegada_gancho_activas:
            gancho_fusionado = fusionar_adultos(llegada_gancho_activas.copy())
            li_gancho = "".join([f"<div class='li-item'>• {html.escape(c.upper())}</div>" for c in gancho_fusionado])
            html_llegada_interior += f"""
            <div class='llegada-grupo'>
                <b class='llegada-subtitulo'>ROPA COLGADA EN GANCHO</b>
                {li_gancho}
            </div>
            """
            
        if llegada_tabla_activas:
            tabla_fusionada = fusionar_adultos(llegada_tabla_activas.copy())
            li_tabla = "".join([f"<div class='li-item'>• {html.escape(c.upper())}</div>" for c in tabla_fusionada])
            html_llegada_interior += f"""
            <div class='llegada-grupo'>
                <b class='llegada-subtitulo'>ROPA DE TABLA</b>
                {li_tabla}
            </div>
            """
            
        if llegada_otros_activas:
            if llegada_gancho_activas or llegada_tabla_activas:
                html_llegada_interior += "<div class='divisor-suave'></div>"
            for o in llegada_otros_activas:
                html_llegada_interior += f"<div class='li-otro'>📌 {html.escape(o.upper())}</div>"
                
        html_modulos += f"""
        <div class="card card-dark">
            <h3 class="title-glow">LLEGA PARA TI:</h3>
            {html_llegada_interior}
        </div>
        """

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
            <div class='fila-descuento'>
                <div class='badge-percent'>
                    <span class='badge-num'>{desc}%</span>
                </div>
                <span class='texto-descuento'>
                    DE DESCUENTO EN<br><span class='texto-categoria'>{html.escape(texto_cats)}</span>
                </span>
            </div>
            """
            
        html_modulos += f"""
        <div class="card card-light">
            <h3 class="title-pill">🔥 DESCUENTOS EN ROPA<br>COLGADA EN GANCHO 🔥</h3>
            {bloques_desc_html}
        </div>
        """

    # Lógica 3: Ropa de Tabla
    if mostrar_tabla:
        tabla_dict = fusionar_adultos(tabla_dict)
        items_tabla = ""
        for cat, precio in tabla_dict.items():
            items_tabla += f"""
            <div class='chip-precio'>
                <span class='chip-cat'>📌 {html.escape(cat.upper())}</span>
                <span class='chip-precio-valor'><b class='chip-precio-num'>${precio}</b> LA PIEZA</span>
            </div>
            """
        
        html_modulos += f"""
        <div class="card card-light">
            <h3 class="title-pill dark-bg">ROPA DE TABLA</h3>
            <div class="grid-precios">
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
            :root {{
                --bg-canvas: {c_paleta['bg_canvas']};
                --borde-canvas: {c_paleta['borde_canvas']};
                --texto-ppal: {c_paleta['texto_ppal']};
                --acento: {c_paleta['acento']};
                --card-dark-bg: {c_paleta['card_oscura_bg']};
                --card-dark-fg: {c_paleta['card_oscura_fg']};
                --card-light-bg: {c_paleta['card_clara_bg']};
                --card-light-fg: {c_paleta['card_clara_fg']};
                --texto-sobre-borde: {texto_sobre_borde};
                --texto-sobre-acento: {texto_sobre_acento};
                --acento-en-claro: {acento_en_claro};
                --font-title: {c_fuente['titulos']};
                --font-body: {c_fuente['cuerpo']};
                --size-sucursal: {size_sucursal};
                --size-modulo: {size_titulo_modulo};
                --size-sub: {size_subheading_llegada};
                --size-texto: {size_texto};
                --size-badge: {size_porcentaje};
                --size-precio: {size_precio};
            }}

            * {{ box-sizing: border-box; }}

            body {{
                font-family: var(--font-body);
                background: #eef0f3;
                padding: 24px 5px;
                text-align: center;
            }}

            .contenedor-canvas {{
                width: 432px;
                background-color: var(--bg-canvas);
                {css_fondo}
                padding: 20px 16px;
                border: 3px solid var(--borde-canvas);
                border-radius: 22px;
                box-shadow: 0 22px 45px -14px rgba(0,0,0,0.35);
                margin: 0 auto;
                position: relative;
                overflow: hidden;
                display: flex;
                flex-direction: column;
                gap: 14px;
            }}

            /* --- ENCABEZADO --- */
            .ribbon-gancho {{
                font-size: 22px;
                font-family: var(--font-title);
                background: var(--borde-canvas);
                color: var(--texto-sobre-borde);
                padding: 9px 10px;
                border-radius: 12px;
                text-transform: uppercase;
                letter-spacing: 1px;
                line-height: 1.15;
                box-shadow: 0 6px 14px -6px rgba(0,0,0,0.35);
            }}

            .masthead {{ line-height: 1; }}
            .marca-principal {{
                font-size: 19px;
                font-family: var(--font-title);
                color: var(--texto-ppal);
                text-transform: uppercase;
                letter-spacing: 2px;
                font-weight: normal;
                opacity: 0.85;
                margin-bottom: 2px;
            }}
            .sucursal-estricta {{
                font-size: var(--size-sucursal);
                font-family: var(--font-title);
                color: var(--acento);
                text-transform: uppercase;
                letter-spacing: 0.5px;
                font-weight: 900;
                white-space: nowrap;
            }}

            /* --- TARJETAS --- */
            .card {{
                border-radius: 16px;
                padding: 14px 14px;
                text-align: left;
                box-shadow: 0 10px 22px -10px rgba(0,0,0,0.30);
            }}
            .card-dark {{ background: var(--card-dark-bg); color: var(--card-dark-fg); {css_textura_c_oscura} }}
            .card-light {{ background: var(--card-light-bg); color: var(--card-light-fg); {css_textura_c_clara} }}

            .title-glow {{
                text-align: center;
                font-family: var(--font-title);
                font-size: var(--size-modulo);
                letter-spacing: 1px;
                line-height: 1.15;
                margin: 0 0 10px 0;
                padding: 6px 10px;
                border-radius: 10px;
                background: var(--acento);
                color: var(--texto-sobre-acento);
                white-space: nowrap;
            }}
            .title-pill {{
                text-align: center;
                font-family: var(--font-title);
                font-size: var(--size-modulo);
                letter-spacing: 0.5px;
                line-height: 1.15;
                padding: 6px 10px;
                border-radius: 10px;
                margin: 0 0 10px 0;
                background: var(--bg-canvas);
                color: var(--texto-ppal);
            }}
            .title-pill.dark-bg {{ background: var(--card-dark-bg); color: var(--card-dark-fg); white-space: nowrap; }}

            .pill-fecha {{
                text-align: center;
                background: var(--bg-canvas);
                color: var(--texto-ppal);
                padding: 6px 8px;
                font-size: var(--size-texto);
                font-weight: 900;
                margin-bottom: 8px;
                border-radius: 8px;
                font-family: var(--font-title);
                letter-spacing: 1px;
            }}
            .llegada-grupo {{ margin-bottom: 10px; line-height: 1.3; }}
            .llegada-subtitulo {{
                color: var(--bg-canvas);
                font-size: var(--size-sub);
                font-family: var(--font-title);
                letter-spacing: 0.5px;
            }}
            .li-item, .li-otro {{
                margin-left: 4px;
                font-size: var(--size-texto);
                font-weight: 700;
            }}
            .li-otro {{ margin-bottom: 3px; }}
            .divisor-suave {{
                margin: 6px 0;
                border-top: 1px solid rgba(255,255,255,0.15);
            }}

            /* --- DESCUENTOS: INSIGNIA EN FORMA DE ESTRELLA --- */
            .fila-descuento {{
                display: flex;
                align-items: center;
                margin-bottom: 16px;
            }}
            .fila-descuento:last-child {{ margin-bottom: 0; }}
            .badge-percent {{
                position: relative;
                display: flex;
                justify-content: center;
                align-items: center;
                min-width: 104px;
                width: 104px;
                height: 104px;
                clip-path: {ESTRELLA_INSIGNIA_CLIP};
                background: radial-gradient(circle at 35% 28%, rgba(255,255,255,0.45), rgba(255,255,255,0) 65%), var(--acento);
                filter: drop-shadow(0 8px 10px rgba(0,0,0,0.45));
                margin-right: 14px;
                flex-shrink: 0;
            }}
            .badge-num {{
                color: var(--texto-sobre-acento);
                font-family: var(--font-title);
                font-size: var(--size-badge);
                line-height: 1;
            }}
            .texto-descuento {{
                font-size: var(--size-texto);
                font-weight: 900;
                line-height: 1.3;
                text-align: left;
                font-family: var(--font-body);
            }}
            .texto-categoria {{ color: var(--acento-en-claro); }}

            /* --- TABLA DE PRECIOS --- */
            .grid-precios {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 8px;
            }}
            .chip-precio {{
                background: rgba(127,127,127,0.08);
                border-left: 4px solid var(--acento-en-claro);
                border-radius: 8px;
                padding: 7px 9px;
                display: flex;
                flex-direction: column;
                font-family: var(--font-body);
            }}
            .chip-cat {{ font-size: var(--size-texto); font-weight: 900; line-height: 1.15; }}
            .chip-precio-valor {{ font-size: var(--size-texto); font-weight: 900; line-height: 1.15; }}
            .chip-precio-num {{ color: var(--acento-en-claro); font-size: var(--size-precio); font-family: var(--font-title); }}

            /* --- PIE: VIGENCIA Y HORARIO --- */
            .footer-bar {{
                background: var(--borde-canvas);
                color: var(--bg-canvas);
                padding: 10px 12px;
                border-radius: 14px;
                text-align: center;
                margin-top: auto;
                box-shadow: 0 6px 14px -6px rgba(0,0,0,0.30);
            }}
            .footer-bar .vigencia {{
                font-size: 19px;
                font-family: var(--font-title);
                letter-spacing: 0.5px;
                margin-bottom: 3px;
            }}
            .footer-bar .horario {{
                font-size: 11px;
                font-weight: 700;
                opacity: 0.9;
            }}

            .btn-descargar {{
                background: #25D366;
                color: white;
                border: none;
                padding: 13px 26px;
                font-family: var(--font-title);
                font-size: 22px;
                border-radius: 30px;
                cursor: pointer;
                margin-top: 18px;
                box-shadow: 0 10px 22px -8px rgba(0,0,0,0.45);
                letter-spacing: 1px;
            }}
            .btn-descargar:active {{ transform: translateY(2px); box-shadow: 0 4px 10px -4px rgba(0,0,0,0.4); }}
            .btn-descargar:disabled {{ opacity: 0.7; cursor: wait; }}
        </style>
    </head>
    <body>

        <div id="anuncioPublicitario" class="contenedor-canvas">
            <div class="ribbon-gancho">{gancho_safe}</div>

            <div class="masthead">
                <div class="marca-principal">LA BODEGUITA</div>
                <div class="sucursal-estricta">{sufijo_sucursal}</div>
            </div>

            <div style="display:flex; flex-direction:column; justify-content:center; gap:14px;">
                {html_modulos}
            </div>

            <div class="footer-bar">
                <div class="vigencia">VÁLIDO: {fechas_safe}</div>
                <div class="horario">{html.escape(horario_automatico)}</div>
            </div>
        </div>

        <button class="btn-descargar" onclick="descargarAnuncio()">📥 DESCARGAR ANUNCIO PERSONALIZADO</button>

        <script>
        function descargarAnuncio() {{
            const boton = document.querySelector('.btn-descargar');
            const textoOriginal = boton.innerText;
            boton.disabled = true;
            boton.innerText = '⏳ GENERANDO...';

            // Espera a que las fuentes de Google Fonts terminen de cargar
            // antes de capturar; si no, html2canvas puede tomar la foto
            // con la tipografía de respaldo del sistema y se ve "feo".
            document.fonts.ready.then(() => {{
                setTimeout(() => {{
                    const elemento = document.getElementById('anuncioPublicitario');
                    html2canvas(elemento, {{
                        scale: 2.5,
                        useCORS: true,
                        backgroundColor: null,
                        width: 432,
                        height: elemento.offsetHeight
                    }}).then(canvas => {{
                        let enlace = document.createElement('a');
                        enlace.download = 'historia_la_bodeguita_custom.png';
                        enlace.href = canvas.toDataURL('image/png');
                        enlace.click();
                        boton.disabled = false;
                        boton.innerText = textoOriginal;
                    }});
                }}, 250);
            }});
        }}
        </script>
    </body>
    </html>
    """

    st.success("¡Diseño actualizado! Tarjetas con sombras suaves, badges sin clip-path y espera de fuentes antes de exportar.")
    components.html(html_completo, height=1000, scrolling=True)
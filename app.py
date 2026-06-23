import html
import math
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Generador de Publicidad - La Bodeguita", layout="wide")

st.title("✨ GENERADOR DE ANUNCIOS PREMIUM - LA BODEGUITA")

# --- INICIALIZACIÓN DE ESTADOS DINÁMICOS ---
if "llegada_custom" not in st.session_state:
    st.session_state.llegada_custom = [""]
if "gancho_custom" not in st.session_state:
    st.session_state.gancho_custom = [{"nombre": "", "valor": 0}]
if "tabla_custom" not in st.session_state:
    st.session_state.tabla_custom = [{"nombre": "", "valor": 0}]

# --- SELECTOR DE PALETAS DE COLORES ---
paletas = {
    "🟡 Tradicional (Amarillo/Negro/Rojo)": {
        "bg_canvas": "#FFDE00", "borde_canvas": "#111111", "texto_ppal": "#111111", "acento": "#D32F2F",
        "card_oscura_bg": "#111111", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#FFFFFF", "card_clara_fg": "#111111",
        "precio_color": "#D32F2F"
    },
    "🔴 Oferta Agresiva (Rojo/Blanco/Amarillo)": {
        "bg_canvas": "#D32F2F", "borde_canvas": "#FFFFFF", "texto_ppal": "#FFFFFF", "acento": "#FFDE00",
        "card_oscura_bg": "#111111", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#FFFFFF", "card_clara_fg": "#111111",
        "descuento_color": "#CC9900"
    },
    "⚫ Elegancia Nocturna (Negro/Blanco/Oro)": {
        "bg_canvas": "#111111", "borde_canvas": "#FFD700", "texto_ppal": "#FFFFFF", "acento": "#FFD700",
        "card_oscura_bg": "#222222", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#FFFFFF", "card_clara_fg": "#111111",
        "descuento_color": "#FFD700", "precio_color": "#B8860B"
    },
    "🔵 Clásico Americano (Azul Marino/Rojo)": {
        "bg_canvas": "#002366", "borde_canvas": "#FFFFFF", "texto_ppal": "#FFFFFF", "acento": "#D32F2F",
        "card_oscura_bg": "#0A192F", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#FFFFFF", "card_clara_fg": "#111111"
    },
    "🟢 Descuento Neón (Negro/Verde Neón)": {
        "bg_canvas": "#050505", "borde_canvas": "#39FF14", "texto_ppal": "#39FF14", "acento": "#39FF14",
        "card_oscura_bg": "#1A1A1A", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#FFFFFF", "card_clara_fg": "#111111",
        "descuento_color": "#39FF14", "precio_color": "#1aad00"
    },
    "🌸 Impacto Fucsia (Rosa/Negro/Blanco)": {
        "bg_canvas": "#FF007F", "borde_canvas": "#111111", "texto_ppal": "#FFFFFF", "acento": "#111111",
        "card_oscura_bg": "#111111", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#FFFFFF", "card_clara_fg": "#111111",
        "descuento_color": "#FF007F"
    },
    "🟤 Estilo Vintage (Crema/Marrón)": {
        "bg_canvas": "#F5F5DC", "borde_canvas": "#4A2E1B", "texto_ppal": "#4A2E1B", "acento": "#B22222",
        "card_oscura_bg": "#4A2E1B", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#FFFFFF", "card_clara_fg": "#4A2E1B"
    },
    "💎 Verano Fresco (Turquesa/Coral)": {
        "bg_canvas": "#40E0D0", "borde_canvas": "#111111", "texto_ppal": "#111111", "acento": "#FF6F61",
        "card_oscura_bg": "#004040", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#FFFFFF", "card_clara_fg": "#111111",
        "precio_color": "#E84A3A"
    },
    "⚪ Moda Boutique (Blanco/Negro)": {
        "bg_canvas": "#FFFFFF", "borde_canvas": "#111111", "texto_ppal": "#111111", "acento": "#111111",
        "card_oscura_bg": "#111111", "card_oscura_fg": "#FFFFFF", "card_clara_bg": "#F5F5F5", "card_clara_fg": "#111111"
    }
}

# --- SELECTOR DE FUENTES (GOOGLE FONTS) ---
fuentes = {
    "💥 Impacto Urbano (Montserrat + Inter)": {
        "import": "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Montserrat:wght@700;900&display=swap');",
        "titulos": "'Montserrat', sans-serif", "cuerpo": "'Inter', sans-serif"
    },
    "🎯 Comercial Moderno (Roboto Condensed + Roboto)": {
        "import": "@import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@700;900&family=Roboto:wght@400;500;700;900&display=swap');",
        "titulos": "'Roboto Condensed', sans-serif", "cuerpo": "'Roboto', sans-serif"
    },
    "💎 Boutique Elegante (Merriweather + Lora)": {
        "import": "@import url('https://fonts.googleapis.com/css2?family=Lora:wght@500;700&family=Merriweather:wght@700;900&display=swap');",
        "titulos": "'Merriweather', serif", "cuerpo": "'Lora', serif"
    },
    "🎨 Minimalista Moderno (Poppins + Open Sans)": {
        "import": "@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&family=Poppins:wght@700;800;900&display=swap');",
        "titulos": "'Poppins', sans-serif", "cuerpo": "'Open Sans', sans-serif"
    },
    "🎈 Escolar y Dinámico (Nunito + Quicksand)": {
        "import": "@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@700;900&family=Quicksand:wght@600;700&display=swap');",
        "titulos": "'Nunito', sans-serif", "cuerpo": "'Quicksand', sans-serif"
    },
    "🌾 Estilo Orgánico (Bitter + Work Sans)": {
        "import": "@import url('https://fonts.googleapis.com/css2?family=Bitter:wght@700;900&family=Work+Sans:wght@500;700&display=swap');",
        "titulos": "'Bitter', serif", "cuerpo": "'Work Sans', sans-serif"
    }
}

# --- LISTAS DE CATEGORÍAS FIJAS ---
categorias_ropa = ["Bebé", "Niño y Niña", "Dama", "Caballero", "Tallas Extra"]
categorias_otros = [
    "Zapatos, Bolsas, Juguetes y Accesorios de vitrina",
    "Trajes de baño, salidas de playa, corsetería y lencería",
    "Ropa de casa: Edredones, cortinas, frazadas, toallas, etc."
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
    
    fuente_names = list(fuentes.keys())
    fuente_imports = "".join(
        f"<style>{f['import']}</style>" for f in fuentes.values()
    )
    # Build CSS: each radio label nth-child gets its own font
    fuente_list = list(fuentes.values())
    radio_css_rules = ""
    for i, fdata in enumerate(fuente_list, start=1):
        # Streamlit radio: each option is a label inside a fieldset
        radio_css_rules += (
            f"div[data-testid='stRadio'] label:nth-of-type({i}) p "
            f"{{ font-family: {fdata['titulos']} !important; "
            f"font-size: 15px !important; font-weight: 700 !important; }}"
        )
    st.markdown(
        fuente_imports + f"<style>{radio_css_rules}</style>",
        unsafe_allow_html=True
    )
    fuente_sel = st.radio("2. Combinación Tipográfica (Fuentes):", fuente_names)
    c_fuente = fuentes[fuente_sel]
    
    textura_fondo = st.selectbox("3. Patrón del Fondo:", ["Liso Sólido", "Triángulos Geométricos", "Olas Chevron", "Rombos 3D", "Ondas Circulares"])

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

def ajustar_brillo(color_hex, factor):
    color_hex = color_hex.lstrip("#")
    r, g, b = int(color_hex[0:2], 16), int(color_hex[2:4], 16), int(color_hex[4:6], 16)
    def ajustar(c):
        nuevo = c + (255 - c) * factor if factor >= 0 else c * (1 + factor)
        return max(0, min(255, int(nuevo)))
    r, g, b = ajustar(r), ajustar(g), ajustar(b)
    return f"#{r:02x}{g:02x}{b:02x}"

def hex_a_rgba(color_hex, alpha):
    color_hex = color_hex.lstrip("#")
    r, g, b = int(color_hex[0:2], 16), int(color_hex[2:4], 16), int(color_hex[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"

def luminancia(color_hex):
    color_hex = color_hex.lstrip("#")
    r, g, b = int(color_hex[0:2], 16), int(color_hex[2:4], 16), int(color_hex[4:6], 16)
    return (0.299 * r + 0.587 * g + 0.114 * b) / 255

def texto_legible_sobre(color_hex):
    return "#161616" if luminancia(color_hex) > 0.6 else "#FFFFFF"

def color_destacado_seguro(fondo_hex, candidato_hex, alterno_hex, umbral=0.35):
    if abs(luminancia(fondo_hex) - luminancia(candidato_hex)) < umbral:
        return alterno_hex
    return candidato_hex

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

    texto_sobre_borde = texto_legible_sobre(c_paleta['borde_canvas'])
    texto_sobre_acento = texto_legible_sobre(c_paleta['acento'])
    
    # Safe contrast accents
    acento_claro = color_destacado_seguro(c_paleta['card_clara_bg'], c_paleta['acento'], c_paleta['card_clara_fg'])
    acento_oscuro = color_destacado_seguro(c_paleta['card_oscura_bg'], c_paleta['acento'], c_paleta['card_oscura_fg'])
    acento_canvas = color_destacado_seguro(c_paleta['bg_canvas'], c_paleta['acento'], c_paleta['texto_ppal'])
    
    # Per-palette overrides for price and discount badge colors
    color_precio_alt = c_paleta.get('precio_color', None)
    if color_precio_alt is None:
        color_precio_alt = color_destacado_seguro(c_paleta['card_clara_bg'], c_paleta['bg_canvas'], c_paleta['card_clara_fg'])
        if color_precio_alt == acento_claro:
            color_precio_alt = color_destacado_seguro(c_paleta['card_clara_bg'], c_paleta['borde_canvas'], c_paleta['card_clara_fg'])
    
    color_descuento_alt = c_paleta.get('descuento_color', None)
    if color_descuento_alt is None:
        color_descuento_alt = acento_oscuro
    
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

    if modulos_activos == 1:
        size_sucursal = "58px"
        size_titulo_modulo = "32px"
        size_subheading_llegada = "24px"
        size_texto = "24px"
        size_porcentaje = "26px"
        size_precio = "28px"
    elif modulos_activos == 2:
        size_sucursal = "50px"
        size_titulo_modulo = "28px"
        size_subheading_llegada = "21px"
        size_texto = "21px"
        size_porcentaje = "23px"
        size_precio = "24px"
    else: 
        size_sucursal = "44px"
        size_titulo_modulo = "25px"
        size_subheading_llegada = "18px"
        size_texto = "19px"
        size_porcentaje = "20px"
        size_precio = "21px"

    sufijo_sucursal = html.escape(sucursal.replace("La Bodeguita ", "").upper())
    gancho_safe = html.escape(gancho)
    fechas_safe = html.escape(fechas)
    fecha_llegada_safe = html.escape(fecha_llegada.strip().upper())
    html_modulos = ""
    
    if mostrar_llegada:
        html_llegada_interior = ""
        if fecha_llegada_safe:
            html_llegada_interior += f"<div style='text-align:center;'><div class='pill-fecha'>🚀 {fecha_llegada_safe} 🚀</div></div>"
        
        if llegada_gancho_activas:
            gancho_fusionado = fusionar_adultos(llegada_gancho_activas.copy())
            li_gancho = "".join([f"<div class='li-item'>{html.escape(c.upper())}</div>" for c in gancho_fusionado])
            html_llegada_interior += f"""
            <div class='llegada-grupo'>
                <span class='llegada-subtitulo'>ROPA COLGADA EN GANCHO</span>
                {li_gancho}
            </div>
            """
            
        if llegada_tabla_activas:
            tabla_fusionada = fusionar_adultos(llegada_tabla_activas.copy())
            li_tabla = "".join([f"<div class='li-item'>{html.escape(c.upper())}</div>" for c in tabla_fusionada])
            html_llegada_interior += f"""
            <div class='llegada-grupo'>
                <span class='llegada-subtitulo'>ROPA DE TABLA</span>
                {li_tabla}
            </div>
            """
            
        if llegada_otros_activas:
            if llegada_gancho_activas or llegada_tabla_activas:
                html_llegada_interior += "<div class='divisor-suave'></div>"
            for o in llegada_otros_activas:
                html_llegada_interior += f"<div class='li-otro'>{html.escape(o.upper())}</div>"
                
        html_modulos += f"""
        <div class="card card-dark">
            <div class="title-glow">✨ LLEGA PARA TI ✨</div>
            {html_llegada_interior}
        </div>
        """

    if mostrar_gancho:
        gancho_dict = fusionar_adultos(gancho_dict)
        grupos_desc = {}
        for cat, desc in gancho_dict.items():
            if desc not in grupos_desc: grupos_desc[desc] = []
            grupos_desc[desc].append(cat.upper())
            
        lista_grupos = []
        for desc, categories in grupos_desc.items():
            texto_cats = " Y ".join(categories) if len(categories) <= 2 else ", ".join(categories[:-1]) + " Y " + categories[-1]
            es_largo = len(texto_cats.split()) > 3
            lista_grupos.append((desc, texto_cats, es_largo))
            
        lista_grupos.sort(key=lambda x: (x[2], x[0]), reverse=True)

        bloques_desc_html = ""
        for desc, texto_cats, es_largo in lista_grupos:
            span_class = " span-full" if es_largo else ""
            bloques_desc_html += f"""
            <div class='fila-descuento{span_class}'>
                <div class='badge-percent'>
                    <span class='badge-num'>{desc}%</span>
                </div>
                <div class='texto-descuento'>
                    <span style='opacity: 0.8; font-size: 0.85em; text-transform: uppercase;'>De descuento en</span><br>
                    <span class='texto-categoria'>{html.escape(texto_cats)}</span>
                </div>
            </div>
            """
            
        html_modulos += f"""
        <div class="card card-dark">
            <div class="title-pill" style="background: rgba(255,255,255,0.08); color: var(--card-dark-fg); box-shadow: none;">🔥 DESCUENTOS EN ROPA 🔥<br><span style="font-size: 0.7em; opacity: 0.8;">COLGADA EN GANCHO</span></div>
            <div class="grid-descuentos">
                {bloques_desc_html}
            </div>
        </div>
        """

    if mostrar_tabla:
        tabla_dict = fusionar_adultos(tabla_dict)
        lista_tabla = []
        for cat, precio in tabla_dict.items():
            es_largo = len(cat.split()) > 3
            lista_tabla.append((cat, precio, es_largo))
            
        # Stable sort: keep original order but pull large ones to the front
        lista_tabla.sort(key=lambda x: x[2], reverse=True)

        items_tabla = ""
        for cat, precio, es_largo in lista_tabla:
            span_class = " span-full" if es_largo else ""
            items_tabla += f"""
            <div class='chip-precio{span_class}'>
                <span class='chip-cat'>🏷️ {html.escape(cat.upper())}</span>
                <span class='chip-precio-valor'><b class='chip-precio-num'>${precio}</b><span style="font-size: 0.75em; opacity: 0.8; font-weight: 600; color: #555555; display: block; margin-top: -2px;">LA PIEZA</span></span>
            </div>
            """
        
        html_modulos += f"""
        <div class="card-tabla">
            <div class="ticket-header">ROPA DE TABLA</div>
            <div class="ticket-body">
                <div class="grid-precios">
                    {items_tabla}
                </div>
            </div>
        </div>
        """

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
                --acento-claro: {acento_claro};
                --acento-oscuro: {acento_oscuro};
                --acento-canvas: {acento_canvas};
                --color-precio-alt: {color_precio_alt};
                --color-descuento-alt: {color_descuento_alt};
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
                background: linear-gradient(135deg, #e0e5ec 0%, #f4f6f8 100%);
                padding: 40px 10px;
                text-align: center;
                display: flex;
                flex-direction: column;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }}

            .contenedor-canvas {{
                width: 500px;
                background-color: var(--bg-canvas);
                {css_fondo}
                padding: 24px 16px;
                border: none;
                border-radius: 28px;
                box-shadow: 
                    0 40px 80px -20px rgba(0,0,0,0.3),
                    inset 0 0 0 2px rgba(255,255,255,0.2),
                    inset 0 0 30px rgba(255,255,255,0.1);
                margin: 0 auto;
                position: relative;
                overflow: hidden;
                display: flex;
                flex-direction: column;
                gap: 12px;
                z-index: 1;
            }}

            .ribbon-gancho {{
                position: absolute;
                top: 0; left: 0; right: 0;
                font-size: 22px;
                font-weight: 900;
                font-family: var(--font-title);
                background: linear-gradient(135deg, var(--borde-canvas) 0%, {ajustar_brillo(c_paleta['borde_canvas'], -0.2)} 100%);
                color: var(--texto-sobre-borde);
                padding: 12px 16px 16px 16px;
                text-transform: uppercase;
                letter-spacing: 2px;
                line-height: 1.2;
                box-shadow: 0 15px 30px rgba(0,0,0,0.2);
                clip-path: polygon(0 0, 100% 0, 100% 85%, 50% 100%, 0 85%);
                z-index: 10;
            }}

            .masthead {{ 
                margin-top: 40px; 
                line-height: 1.1; 
                position: relative;
                z-index: 2;
                display: flex;
                flex-direction: column;
                gap: 4px;
            }}
            .marca-principal {{
                font-size: 18px;
                font-family: var(--font-body);
                color: var(--texto-ppal);
                text-transform: uppercase;
                letter-spacing: 6px;
                font-weight: 800;
                opacity: 0.85;
            }}
            .sucursal-estricta {{
                font-size: var(--size-sucursal);
                font-family: var(--font-title);
                color: var(--acento-canvas);
                text-transform: uppercase;
                letter-spacing: 1px;
                font-weight: 900;
                text-shadow: 2px 2px 0 rgba(0,0,0,0.1), 0 8px 16px rgba(0,0,0,0.15);
                line-height: 1;
            }}

            .card {{
                position: relative;
                border-radius: 20px;
                padding: 16px 16px;
                text-align: left;
                box-shadow: 
                    0 20px 40px rgba(0,0,0,0.12),
                    inset 0 1px 1px rgba(255,255,255,0.2);
                backdrop-filter: blur(16px);
                -webkit-backdrop-filter: blur(16px);
                z-index: 2;
                overflow: hidden;
            }}
            
            .card-dark {{
                background: linear-gradient(135deg, {hex_a_rgba(c_paleta['card_oscura_bg'], 0.85)} 0%, {hex_a_rgba(c_paleta['card_oscura_bg'], 0.95)} 100%);
                color: var(--card-dark-fg);
                border: 1px solid rgba(255,255,255,0.15);
            }}
            .card-light {{
                background: linear-gradient(135deg, {hex_a_rgba(c_paleta['card_clara_bg'], 0.9)} 0%, {hex_a_rgba(c_paleta['card_clara_bg'], 0.98)} 100%);
                color: var(--card-light-fg);
                border: 1px solid rgba(255,255,255,0.4);
            }}

            .title-glow {{
                text-align: center;
                font-family: var(--font-title);
                font-size: var(--size-modulo);
                letter-spacing: 1px;
                line-height: 1.2;
                margin: 0 0 12px 0;
                padding: 8px 16px;
                border-radius: 12px;
                text-transform: uppercase;
                background: linear-gradient(135deg, var(--acento) 0%, {ajustar_brillo(c_paleta['acento'], -0.2)} 100%);
                color: var(--texto-sobre-acento);
                box-shadow: 0 10px 20px {hex_a_rgba(c_paleta['acento'], 0.4)}, inset 0 2px 0 rgba(255,255,255,0.2);
            }}
            .title-pill {{
                text-align: center;
                font-family: var(--font-title);
                font-size: calc(var(--size-modulo) - 8px);
                letter-spacing: 0.5px;
                line-height: 1.2;
                margin: 0 0 12px 0;
                padding: 8px 14px;
                border-radius: 12px;
                text-transform: uppercase;
                white-space: nowrap;
                background: linear-gradient(135deg, var(--bg-canvas) 0%, {ajustar_brillo(c_paleta['bg_canvas'], -0.1)} 100%);
                color: var(--texto-ppal);
                box-shadow: 0 10px 20px rgba(0,0,0,0.15), inset 0 2px 0 rgba(255,255,255,0.3);
            }}

            .pill-fecha {{
                text-align: center;
                background: var(--acento);
                color: var(--texto-sobre-acento);
                padding: 6px 12px;
                font-size: var(--size-texto);
                font-weight: 800;
                margin-bottom: 12px;
                border-radius: 16px;
                font-family: var(--font-body);
                letter-spacing: 1px;
                box-shadow: 0 8px 16px {hex_a_rgba(c_paleta['acento'], 0.3)};
                display: inline-block;
            }}
            .llegada-grupo {{ margin-bottom: 10px; }}
            .llegada-subtitulo {{
                color: var(--acento-oscuro);
                font-size: var(--size-sub);
                font-family: var(--font-title);
                letter-spacing: 1px;
                display: block;
                margin-bottom: 4px;
                text-transform: uppercase;
            }}
            .li-item, .li-otro {{
                font-size: var(--size-texto);
                font-weight: 600;
                margin-bottom: 2px;
                display: flex;
                align-items: center;
            }}
            .li-item::before, .li-otro::before {{
                content: '✨';
                font-size: 16px;
                margin-right: 8px;
            }}
            .li-otro::before {{ content: '📌'; }}

            .divisor-suave {{
                margin: 8px 0;
                border-top: 1px dashed rgba(255,255,255,0.2);
            }}

            .grid-descuentos {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 8px;
            }}
            .fila-descuento {{
                display: flex;
                flex-direction: column;
                align-items: center;
                text-align: center;
                background: rgba(255,255,255,0.08);
                padding: 12px 8px;
                border-radius: 16px;
                border: 1px solid rgba(255,255,255,0.1);
            }}
            .fila-descuento.span-full {{
                grid-column: 1 / -1;
                flex-direction: row;
                text-align: left;
            }}
            .fila-descuento.span-full .badge-percent {{
                margin-bottom: 0;
                margin-right: 16px;
            }}
            .fila-descuento.span-full .texto-descuento {{
                text-align: left;
            }}
            
            .badge-percent {{
                position: relative;
                display: flex;
                justify-content: center;
                align-items: center;
                min-width: 70px;
                width: 70px;
                height: 70px;
                background: linear-gradient(135deg, var(--acento) 0%, {ajustar_brillo(c_paleta['acento'], -0.2)} 100%);
                border-radius: 50%;
                filter: drop-shadow(0 8px 16px {hex_a_rgba(c_paleta['acento'], 0.4)});
                margin-bottom: 8px;
                flex-shrink: 0;
                color: var(--texto-sobre-acento);
                border: 4px solid rgba(255,255,255,0.4);
            }}
            .badge-percent::after {{
                content: '';
                position: absolute;
                top: 3px; left: 3px; right: 3px; bottom: 3px;
                border-radius: 50%;
                border: 1px dashed rgba(255,255,255,0.6);
            }}
            .badge-num {{
                font-family: var(--font-title);
                font-size: var(--size-badge);
                line-height: 1;
                font-weight: 900;
                z-index: 2;
                max-width: 62px;
                overflow: hidden;
                text-overflow: clip;
                letter-spacing: -1px;
                text-align: center;
            }}
            .texto-descuento {{
                font-size: var(--size-texto);
                font-weight: 700;
                line-height: 1.4;
                text-align: center;
                font-family: var(--font-body);
                color: var(--card-dark-fg);
            }}
            .texto-categoria {{ 
                color: var(--color-descuento-alt); 
                font-weight: 900; 
                text-transform: uppercase;
                background: rgba(0,0,0,0.05);
                padding: 3px 8px;
                border-radius: 6px;
                display: inline-block;
                margin-top: 4px;
            }}

            .card-tabla {{
                position: relative;
                background: linear-gradient(135deg, {hex_a_rgba(c_paleta['card_oscura_bg'], 0.85)} 0%, {hex_a_rgba(c_paleta['card_oscura_bg'], 0.95)} 100%);
                color: var(--card-dark-fg);
                border: 1px solid rgba(255,255,255,0.15);
                border-radius: 20px;
                padding: 0;
                overflow: hidden;
                box-shadow: 0 20px 40px rgba(0,0,0,0.12);
            }}
            .ticket-header {{
                background: linear-gradient(135deg, var(--borde-canvas) 0%, {ajustar_brillo(c_paleta['borde_canvas'], -0.2)} 100%);
                color: var(--texto-sobre-borde);
                font-family: var(--font-title);
                font-size: var(--size-modulo);
                text-align: center;
                letter-spacing: 2px;
                line-height: 1.2;
                padding: 12px 8px;
                text-transform: uppercase;
            }}
            .ticket-body {{
                padding: 16px;
                background-image: radial-gradient(circle, rgba(255,255,255,0.1) 1.5px, transparent 1.5px);
                background-size: 14px 14px;
            }}
            .grid-precios {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 8px;
            }}
            .chip-precio {{
                display: flex;
                flex-direction: column;
                align-items: center;
                text-align: center;
                background: rgba(255,255,255,0.9);
                border-radius: 12px;
                padding: 10px;
                box-shadow: 0 6px 12px rgba(0,0,0,0.06);
                border-top: 6px solid var(--acento);
            }}
            .chip-precio.span-full {{
                grid-column: 1 / -1;
                flex-direction: row;
                justify-content: space-between;
                text-align: left;
                border-top: none;
                border-left: 6px solid var(--acento);
            }}
            .chip-precio.span-full .chip-precio-valor {{
                text-align: right;
                margin-top: 0;
            }}
            .chip-cat {{ 
                font-size: var(--size-texto); 
                font-weight: 800; 
                flex: 1;
                text-transform: uppercase;
                color: #222222;
            }}
            .chip-precio-valor {{ 
                font-size: var(--size-texto); 
                font-weight: 600; 
                text-align: center;
                line-height: 1.1;
                margin-top: 4px;
            }}
            .chip-precio-num {{ 
                color: var(--color-precio-alt); 
                font-size: var(--size-precio); 
                font-family: var(--font-title); 
                font-weight: 900;
                display: block;
                margin-top: 2px;
            }}

            .footer-bar {{
                background: linear-gradient(135deg, var(--borde-canvas) 0%, {ajustar_brillo(c_paleta['borde_canvas'], -0.2)} 100%);
                color: var(--texto-sobre-borde);
                padding: 16px 12px;
                text-align: center;
                border-radius: 20px;
                box-shadow: 0 -10px 30px rgba(0,0,0,0.15);
                margin-top: 4px;
                position: relative;
                z-index: 2;
            }}
            .footer-bar .vigencia {{
                font-size: 14px;
                font-family: var(--font-title);
                letter-spacing: 1px;
                margin-bottom: 4px;
                text-transform: uppercase;
                color: var(--texto-sobre-borde);
                background: rgba(255,255,255,0.15);
                display: inline-block;
                padding: 4px 12px;
                border-radius: 8px;
            }}
            .footer-bar .horario {{
                font-size: 14px;
                font-weight: 600;
                font-family: var(--font-body);
                opacity: 0.85;
                margin-top: 4px;
            }}

            .btn-descargar {{
                background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
                color: white;
                border: none;
                padding: 18px 40px;
                font-family: var(--font-title);
                font-size: 22px;
                border-radius: 40px;
                cursor: pointer;
                margin-top: 40px;
                box-shadow: 0 15px 30px rgba(56, 239, 125, 0.4);
                letter-spacing: 1px;
                transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
                text-transform: uppercase;
                font-weight: 900;
            }}
            .btn-descargar:hover {{ 
                transform: translateY(-4px); 
                box-shadow: 0 20px 40px rgba(56, 239, 125, 0.5); 
            }}
            .btn-descargar:active {{ 
                transform: translateY(2px); 
                box-shadow: 0 8px 15px rgba(56, 239, 125, 0.4); 
            }}
            .btn-descargar:disabled {{ 
                opacity: 0.7; 
                cursor: wait; 
                transform: none;
            }}
        </style>
    </head>
    <body>

        <div id="anuncioPublicitario" class="contenedor-canvas">
            <div class="ribbon-gancho">{gancho_safe}</div>

            <div class="masthead">
                <div class="marca-principal">LA BODEGUITA</div>
                <div class="sucursal-estricta">{sufijo_sucursal}</div>
            </div>

            <div style="display:flex; flex-direction:column; justify-content:center; gap:12px;">
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

            document.fonts.ready.then(() => {{
                setTimeout(() => {{
                    const elemento = document.getElementById('anuncioPublicitario');
                    html2canvas(elemento, {{
                        scale: 2.5,
                        useCORS: true,
                        backgroundColor: null,
                        width: 500,
                        height: elemento.offsetHeight
                    }}).then(canvas => {{
                        let enlace = document.createElement('a');
                        enlace.download = 'historia_la_bodeguita_custom.png';
                        enlace.href = canvas.toDataURL('image/png');
                        enlace.click();
                        boton.disabled = false;
                        boton.innerText = textoOriginal;
                    }});
                }}, 300);
            }});
        }}
        </script>
    </body>
    </html>
    """

    st.success("✨ ¡Diseño Premium Generado! Disfruta de sombras suaves, tipografía moderna, bordes redondeados, y texturas tipo cristal.")
    components.html(html_completo, height=1200, scrolling=True)
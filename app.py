import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="✨ Horóscopo Inteligente",
    page_icon="🔮",
    layout="centered"
)

st.markdown("""
<style>
.main-header { text-align: center; color: #2c3e50; margin-bottom: 1rem; }
.card { background-color: #f8f9fa; border-radius: 10px; padding: 1.5rem; margin: 1rem 0; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); }
.insight-box { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 10px; padding: 1.5rem; margin: 1rem 0; }
.footer { text-align: center; color: #6c757d; font-size: 0.9rem; margin-top: 2rem; }
.disclaimer { background-color: #fff3cd; color: #856404; padding: 1rem; border-radius: 8px; margin: 1rem 0; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>✨ Horóscopo Inteligente</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6c757d;'>Tu guía astrológica personalizada</p>", unsafe_allow_html=True)

with st.form("user_data"):
    st.markdown("### 📝 Tus Datos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Nombre", "María")
        sign = st.selectbox("Tu signo solar", 
                           ["Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", 
                            "Libra", "Escorpio", "Sagitario", "Capricornio", "Acuario", "Piscis"])
    
    with col2:
        birth_time_known = st.radio("¿Conoces tu hora de nacimiento?", ["No", "Sí"])
        birth_time = st.time_input("Hora de nacimiento", datetime.now().time()) if birth_time_known == "Sí" else None
    
    context = st.selectbox("Enfoque de hoy", 
                          ["general", "amor", "carrera", "salud", "crecimiento personal"],
                          format_func=lambda x: {
                              "general": "General",
                              "amor": "Amor y Relaciones",
                              "carrera": "Carrera y Dinero",
                              "salud": "Salud y Bienestar",
                              "crecimiento personal": "Crecimiento Personal"
                          }[x])
    
    submit = st.form_submit_button("✨ Obtener Mi Horóscopo", type="primary", use_container_width=True)

if submit:
    with st.spinner("🌌 Consultando las estrellas..."):
        import time
        time.sleep(1)
    
    st.success(f"¡Hola {name}! Aquí está tu horóscopo personalizado para hoy")
    
    horoscopes = {
        "general": {
            "Aries": "🔥 Marte en tu Casa 1 te da energía para empezar proyectos nuevos. ¡No dejes que nadie apague tu fuego interior!",
            "Tauro": "💰 Venus en tu Casa 2 activa tu abundancia. Confía en que el universo proveerá lo que necesitas esta semana.",
            "Géminis": "💡 Mercurio en tu Casa 3 te hace brillante en comunicaciones. Usa tus palabras para sanar, no para herir.",
            "Cáncer": "🌊 La Luna en tu Casa 4 te pide: cuida tu hogar y tu corazón. No ignores las señales de tu intuición hoy.",
            "Leo": "✨ El Sol en tu Casa 5 te recuerda: eres el protagonista de tu historia. Brilla sin miedo, el mundo necesita tu luz.",
            "Virgo": "🧹 Mercurio en tu Casa 6 te ayuda a organizar tu vida. Pequeños pasos hoy crearán grandes cambios mañana.",
            "Libra": "⚖️ Venus en tu Casa 7 te invita a equilibrar relaciones. Pide lo que necesitas sin miedo a molestar.",
            "Escorpio": "🔍 Plutón en tu Casa 8 te da poder para transformar lo que ya no sirve. Suéltalo y renace más fuerte.",
            "Sagitario": "🏹 Júpiter en tu Casa 9 expande tus horizontes. Un viaje (físico o mental) te cambiará la perspectiva esta semana.",
            "Capricornio": "🏔️ Saturno en tu Casa 10 te pide paciencia. Las grandes montañas se escalan paso a paso.",
            "Acuario": "⚡ Urano en tu Casa 11 te trae ideas revolucionarias. No temas ser diferente, el mundo necesita tu originalidad.",
            "Piscis": "🌊 Neptuno en tu Casa 12 te conecta con tu intuición. Confía en tus sueños y visiones, contienen mensajes importantes."
        },
        "amor": {
            "Aries": "❤️‍🔥 Tu energía apasionada atrae relaciones intensas. Busca pareja que pueda seguir tu ritmo sin agotarse.",
            "Tauro": "💖 La lealtad es tu superpoder en el amor. Atraes relaciones estables pero cuida de no aferrarte a lo que ya no crece.",
            "Géminis": "💬 Tu mente brillante necesita estimulación constante. Busca pareja que disfrute conversaciones profundas a medianoche.",
            "Cáncer": "🏡 Tu corazón necesita un hogar seguro. Atraes a personas que buscan tu protección emocional, pero recuerda cuidarte tú primero.",
            "Leo": "✨ Tu luz natural atrae admiradores. Busca pareja que celebre tus éxitos sin sentirse amenazada por tu brillo.",
            "Virgo": "🧩 Tu atención al detalle hace relaciones sólidas. Busca pareja que valore tu forma de cuidar los pequeños detalles.",
            "Libra": "💞 El equilibrio es tu don. Atraes relaciones armoniosas pero cuida de no perder tu identidad por mantener la paz.",
            "Escorpio": "⚡ La intensidad es tu sello. Busca pareja que no tema tu profundidad emocional y pueda acompañarte en tus transformaciones.",
            "Sagitario": "🌍 Tu espíritu libre necesita espacio. Atraes a personas que aman la aventura, pero cuida de no huir del compromiso real.",
            "Capricornio": "🏔️ Tu seriedad atrae relaciones maduras. Busca pareja que entienda que tu ambición no es falta de amor, sino dedicación.",
            "Acuario": "💫 Tu originalidad fascina. Atraes mentes brillantes pero cuida de no priorizar ideas sobre conexiones humanas reales.",
            "Piscis": "🌊 Tu sensibilidad es un regalo. Busca pareja que proteja tu corazón y entienda tus necesidades emocionales únicas."
        },
        "carrera": {
            "Aries": "🚀 Tu energía emprendedora te llevará lejos. Aprovecha oportunidades que requieran iniciativa y acción inmediata.",
            "Tauro": "💰 Tu perseverancia construye riqueza estable. Busca carreras donde tu paciencia y consistencia sean valoradas.",
            "Géminis": "📚 Tu mente adaptable triunfa en comunicaciones. Medios, marketing o educación son campos donde brillarás.",
            "Cáncer": "🤝 Tu intuición emocional te hace excelente en roles de cuidado. Salud, educación o recursos humanos te darán satisfacción.",
            "Leo": "🌟 Tu carisma natural te lleva a liderar. Busca roles donde puedas inspirar a otros y brillar en público.",
            "Virgo": "🔍 Tu atención al detalle es invaluable. Análisis de datos, edición, o cualquier rol que requiera precisión es ideal para ti.",
            "Libra": "⚖️ Tu sentido de la justicia te lleva al derecho o negociaciones. Cualquier campo que requiera diplomacia y equilibrio.",
            "Escorpio": "🕵️‍♂️ Tu capacidad para ver lo que otros no ven te hace excelente en investigación o roles estratégicos.",
            "Sagitario": "✈️ Tu espíritu aventurero triunfa en roles internacionales. Viajes, filosofía, o educación superior son tus campos.",
            "Capricornio": "🏢 Tu disciplina construye imperios. Administración, finanzas o cualquier rol de alta responsabilidad te espera.",
            "Acuario": "💡 Tu innovación cambia industrias. Tecnología, investigación social o cualquier campo que requiera pensar fuera de la caja.",
            "Piscis": "🎨 Tu creatividad ilumina el arte y la sanación. Música, cine, terapia o cualquier rol que use tu imaginación."
        }
    }
    
    context_key = context.lower()
    if context_key not in horoscopes:
        context_key = "general"
    
    horoscope_text = horoscopes[context_key].get(sign, horoscopes["general"][sign])
    
    st.markdown(f"""
    <div class='insight-box'>
        <h3>💫 Tu Horóscopo de {context.title()} para {sign}</h3>
        <p style='font-size: 1.1em; line-height: 1.6;'>{horoscope_text}</p>
    </div>
    """, unsafe_allow_html=True)
    
    additional_insights = {
        "Aries": "⚠️ **Alerta cósmica:** Mercurio retrógrado en tu Casa 3 - evita firmar contratos importantes esta semana.",
        "Tauro": "💡 **Insight profundo:** Saturno en tu Casa 2 te pide revisar tus valores. ¿Qué realmente importa en tu vida?",
        "Géminis": "✨ **Oportunidad:** Venus en trino con Júpiter - excelente día para conectar con personas influyentes.",
        "Cáncer": "🌊 **Reflexión:** La Luna en tu Casa 4 activa tu necesidad de hogar. ¿Dónde te sientes verdaderamente seguro/a?",
        "Leo": "🔥 **Energía:** El Sol en tu Casa 5 te da creatividad ilimitada. Usa esta energía para proyectos que apasionen tu alma.",
        "Virgo": "📝 **Consejo práctico:** Mercurio en tu Casa 6 te ayuda a organizar tu espacio. Dedica 15 minutos hoy a ordenar un cajón.",
        "Libra": "⚖️ **Equilibrio:** Venus en tu Casa 7 te pide armonía en relaciones. Di lo que sientes sin miedo, pero con amor.",
        "Escorpio": "🔍 **Transformación:** Plutón en tu Casa 8 te da poder para renacer. ¿Qué parte de ti estás listo/a para soltar?",
        "Sagitario": "🏹 **Expansión:** Júpiter en tu Casa 9 te abre puertas. Di \"sí\" a oportunidades que te saquen de tu zona de confort.",
        "Capricornio": "🏔️ **Paciencia:** Saturno en tu Casa 10 te recuerda: las grandes obras toman tiempo. Celebra los pequeños avances.",
        "Acuario": "⚡ **Innovación:** Urano en tu Casa 11 te trae ideas revolucionarias. Escribe tus locuras - podrían cambiar el mundo.",
        "Piscis": "🌙 **Intuición:** Neptuno en tu Casa 12 te conecta con lo divino. Medita 5 minutos hoy y escucha los mensajes."
    }
    
    st.markdown(f"""
    <div class='card'>
        <h4>✨ Insight Cósmico Extra</h4>
        <p>{additional_insights[sign]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🌟 Tu Carta Natal Simplificada")
    
    svg_signs = {
        "Aries": "♈", "Tauro": "♉", "Géminis": "♊", "Cáncer": "♋", "Leo": "♌", "Virgo": "♍",
        "Libra": "♎", "Escorpio": "♏", "Sagitario": "♐", "Capricornio": "♑", "Acuario": "♒", "Piscis": "♓"
    }
    
    svg_content = f"""
    <svg width="300" height="300" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
        <circle cx="150" cy="150" r="120" fill="none" stroke="#667eea" stroke-width="2"/>
        <circle cx="150" cy="150" r="90" fill="none" stroke="#764ba2" stroke-width="1" stroke-dasharray="5,5"/>
        <circle cx="150" cy="80" r="15" fill="#ffcc00" stroke="#ff9900" stroke-width="2"/>
        <text x="150" y="85" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold">☉</text>
        <text x="150" y="105" text-anchor="middle" font-family="Arial" font-size="14" fill="#2c3e50">{svg_signs[sign]}</text>
        <circle cx="210" cy="150" r="12" fill="#99ccff" stroke="#3399cc" stroke-width="1"/>
        <text x="210" y="155" text-anchor="middle" font-family="Arial" font-size="14" font-weight="bold">☽</text>
        <text x="210" y="175" text-anchor="middle" font-family="Arial" font-size="12" fill="#2c3e50">Cáncer</text>
        <circle cx="150" cy="220" r="12" fill="#ff99cc" stroke="#ff6699" stroke-width="1"/>
        <text x="150" y="225" text-anchor="middle" font-family="Arial" font-size="14" font-weight="bold">ASC</text>
        <text x="150" y="245" text-anchor="middle" font-family="Arial" font-size="12" fill="#2c3e50">Libra</text>
        <text x="150" y="270" text-anchor="middle" font-family="Arial" font-size="14" font-weight="bold" fill="#2c3e50">
            Carta de {name}
        </text>
    </svg>
    """
    
    st.components.v1.html(svg_content, height=350)
    
    st.markdown("### 📲 Acciones Rápidas")
    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            label="💾 Descargar PDF",
            data=f"Horóscopo para {name} - {sign}\\n\\n{horoscope_text}\\n\\n{additional_insights[sign]}",
            file_name=f"horoscopo_{name.lower().replace(' ', '_')}.txt",
            mime="text/plain",
            use_container_width=True
        )
    with col2:
        if st.button("🔄 Nueva Lectura", use_container_width=True):
            st.experimental_rerun()

st.markdown("""
<div class='disclaimer'>
    <strong>⚠️ Nota importante:</strong> Este horóscopo es para entretenimiento y reflexión personal. 
    La astrología no sustituye consejos médicos, financieros o legales. Usa esta información con discernimiento.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='footer'>
    <p>Creado con ❤️ | Versión DEMO - Sin conexión a APIs reales</p>
</div>
""", unsafe_allow_html=True)
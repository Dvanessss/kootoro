import streamlit as st
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore
import json

# --- Configuración de la aplicación ---
st.set_page_config(
    page_title="App de Educación Ambiental",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Inicialización de Firebase (Simulación) ---
# En una aplicación real de Streamlit, debes usar st.secrets para almacenar tus credenciales.
# Aquí se muestra cómo se inicializaría el SDK de Firebase Admin con esas credenciales.
# Reemplaza 'path/to/your/serviceAccountKey.json' con la información de st.secrets.
# Si estás ejecutando localmente, puedes usar un archivo JSON.
# Para el despliegue en Streamlit Cloud, usa los secretos directamente.

try:
    if not firebase_admin._apps:
        # En un entorno de producción de Streamlit Cloud,
        # la clave de servicio se almacenaría como un secreto.
        # Aquí se simula la carga de esas credenciales.
        # Por seguridad, no incluyas tu clave de servicio JSON directamente en el código.
        # Se asume que el usuario la configurará en su entorno.

        # Ejemplo de credenciales en st.secrets
        # firebase_creds_json = st.secrets["firebase_credentials"]
        # cred = credentials.Certificate(json.loads(firebase_creds_json))
        
        # Para demostración, usamos un diccionario
        mock_firebase_config = {
            "type": "service_account",
            "project_id": "tu-proyecto-firebase-id",
            "private_key_id": "tu-private-key-id",
            "private_key": "---BEGIN PRIVATE KEY---\n...\n---END PRIVATE KEY---\n",
            "client_email": "firebase-adminsdk-xyz@tu-proyecto.iam.gserviceaccount.com",
            "client_id": "1234567890",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/tu-email.iam.gserviceaccount.com",
            "universe_domain": "googleapis.com"
        }
        
        # Inicializa la app de Firebase
        cred = credentials.Certificate(mock_firebase_config)
        firebase_admin.initialize_app(cred)
        st.success("Conexión a Firebase inicializada correctamente (simulada).")
    
    db = firestore.client()
except Exception as e:
    st.error(f"Error al inicializar Firebase: {e}. Por favor, verifica tus credenciales.")
    st.info("Para un despliegue real, asegúrate de haber configurado tu clave de servicio de Firebase como un secreto en Streamlit.")


# --- Configuración de Gemini (Simulación) ---
# Al igual que con Firebase, tu API Key debe estar en st.secrets.
# Ejemplo de configuración en Streamlit secrets.toml:
# [gemini]
# api_key = "TU_API_KEY_AQUI"
# st.secrets.gemini.api_key

try:
    # Simula la carga de la clave de la API
    # gemini_api_key = st.secrets["gemini"]["api_key"]
    gemini_api_key = "AIzaSyBIAidcxExUpA4AbplXFNyp3htKRR5ulak" # Reemplaza esto con tu clave real
    genai.configure(api_key=gemini_api_key)
    gemini_model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error al configurar la API de Gemini: {e}.")
    st.info("Asegúrate de haber configurado tu clave de API de Gemini como un secreto en Streamlit o en tu entorno local.")


# --- Contenido de los documentos (Simulado como si estuviera en Firebase) ---
# En una aplicación real, esta información se recuperaría de una base de datos de Firebase.
# Por simplicidad y para que el código sea funcional, se incluye aquí como un diccionario.
#
# Para una implementación real, podrías tener una estructura así en Firestore:
# `db.collection('project_info').document('docs')`
# Con campos como:
#   `analisis_brecha`: texto del Documento.pdf
#   `autores`: texto de Autores e investigaciones clave.pdf
#   `estado_arte`: texto de El estado del arte en aplicaciones de educación eco-ambienta.pdf
#   `metodologia`: texto de Metodologia.pdf

project_info = {
    "analisis_brecha": """
        Análisis de la Brecha de Investigación en Eco-Educación
        Basado en la literatura reciente, la narrativa sobre la educación eco-ambiental ha cambiado de un enfoque de "sacrificio" a uno de "estilo de vida aspiracional" y "recompensas". Existen vacíos de investigación significativos.
        1. Eficacia a Largo Plazo de la Gamificación y la Gratificación Instantánea
        Descripción: Las mecánicas de juego son efectivas para el compromiso inicial, pero se cuestiona su capacidad para sostener un cambio de comportamiento a largo plazo. Falta investigación longitudinal.
        2. Impacto Cultural y Demográfico de la Tecnología Persuasiva
        Descripción: No hay suficiente investigación comparativa sobre cómo los diferentes grupos demográficos (personas mayores, comunidades de bajos ingresos, culturas no occidentales) responden a estas técnicas. El impacto cultural y generacional no está bien documentado.
        3. El Debate Ético y la Privacidad en el Seguimiento de Comportamientos
        Descripción: Se discuten los dilemas éticos relacionados con el seguimiento de los comportamientos de los usuarios, lo que introduce un debate fundamental sobre la privacidad y la moralidad.
    """,
    "autores": """
        Autores e Investigaciones Clave
        1. K. L. Hsu y J. L. Chen (2022): Artículo "Gamified applications for sustainable behavior: A systematic review of design features and effectiveness". Justificación: Ofrecen una revisión sistemática de aplicaciones gamificadas.
        2. S. C. Tan y K. M. Lee (2023): Artículo "From guilt to gain: The impact of positive framing on user engagement in environmental apps". Justificación: Abordan el cambio de paradigma de la culpa a la ganancia.
        3. J. Li y Y. Wang (2021): Artículo "Beyond sacrifice: The role of persuasive technology in reframing sustainable lifestyles among Gen Z". Justificación: Se centran en la Generación Z y la tecnología persuasiva.
        4. Y. Wu y P. Liu (2021): Artículo "The dark side of green tech: Examining ethical dilemmas in behavior-tracking sustainability apps". Justificación: Abordan la ética y privacidad en las aplicaciones.
        5. K. Schulz y L. Becker (2020): Artículo "Aesthetic sustainability: How design trends and social media influence pro-environmental intentions". Justificación: Destacan la importancia de la estética y las tendencias de diseño.
    """,
    "estado_arte": """
        El estado del arte en aplicaciones de educación eco-ambiental ha evolucionado, alejándose del modelo de "sacrificio" para abrazar la tecnología persuasiva y el diseño de comportamiento. La corriente principal se centra en la gamificación y la influencia social para promover la sostenibilidad como un estilo de vida aspiracional.
        Debates clave:
        - Eficacia a largo plazo: Cuestionamiento sobre si la gratificación instantánea genera un cambio duradero.
        - Eco-blanqueo (greenwashing): El riesgo de que la adopción de tendencias superficiales desvíe la atención de problemas sistémicos.
        Metodologías más utilizadas:
        - Estudios de experiencia de usuario (UX)
        - Análisis de datos cuantitativos
        - Encuestas
        - Entrevistas cualitativas y grupos focales.
    """,
    "metodologia": """
        Metodología de Investigación
        - Estudios de Experiencia de Usuario (UX) y Análisis de Datos Cuantitativos: Se centran en la medición y la interacción del usuario. Usan datos cuantitativos (tiempo de uso, frecuencia) para cuantificar el compromiso.
        - Análisis de Contenido y Revisión Sistemática: Se utiliza para analizar grandes volúmenes de literatura existente. Permite identificar patrones y brechas en la investigación.
        - Investigación Cualitativa (Entrevistas y Grupos Focales): Se complementa con metodologías cuantitativas para entender las motivaciones, percepciones y barreras psicológicas.
    """
}


# --- Funciones para interactuar con Gemini ---
def get_gemini_response(prompt):
    """Genera una respuesta de Gemini a partir de un prompt."""
    try:
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error al generar contenido con Gemini: {e}")
        return "No se pudo generar la respuesta. Por favor, revisa tu clave de API."

def process_and_summarize_documents():
    """Combina el contenido de los documentos y pide a Gemini un resumen."""
    full_text = "\n\n".join(project_info.values())
    prompt = f"""
        Actúa como un analista de proyectos de tecnología y sostenibilidad.
        Basado en los siguientes documentos sobre una aplicación de educación ambiental,
        genera un resumen conciso y coherente que sirva como una introducción ejecutiva.
        
        Documentos:
        {full_text}
    """
    return get_gemini_response(prompt)


# --- Interfaz de usuario con Streamlit ---
st.title("Asistente para Qarks, una App de Educación Ambiental")
st.markdown("---")

st.sidebar.header("Documentos del Proyecto")
for doc_name, content in project_info.items():
    with st.sidebar.expander(f"Ver {doc_name.replace('_', ' ').capitalize()}"):
        st.markdown(f"```text\n{content}\n```")


# --- Sección de procesamiento de información con Gemini ---
st.header("Análisis de Documentos con Gemini")
st.write("Usa el poder de la inteligencia artificial para procesar y entender la información del proyecto.")

with st.spinner('Procesando documentos...'):
    summary_text = process_and_summarize_documents()
    if summary_text:
        st.subheader("Resumen General del Proyecto")
        st.markdown(summary_text)

st.markdown("---")


# --- Sección de preguntas y respuestas ---
st.header("Preguntas y Respuestas")
st.write("Haz una pregunta sobre los documentos y el asistente de Gemini te responderá.")

user_question = st.text_area(
    "Escribe tu pregunta aquí:",
    "¿Cuáles son las principales metodologías de investigación mencionadas en los documentos?"
)

if st.button("Obtener Respuesta"):
    if user_question:
        prompt = f"""
            Basado en los siguientes documentos sobre una aplicación de educación ambiental,
            responde a la siguiente pregunta del usuario de manera clara y concisa.
            
            Documentos:
            {project_info['analisis_brecha']}
            {project_info['autores']}
            {project_info['estado_arte']}
            {project_info['metodologia']}
            
            Pregunta del usuario: {user_question}
            
            Respuesta:
        """
        with st.spinner('Gemini está pensando...'):
            answer = get_gemini_response(prompt)
            if answer:
                st.subheader("Respuesta de Gemini")
                st.markdown(answer)
    else:
        st.warning("Por favor, escribe una pregunta.")

st.markdown("---")
st.info("Este es un prototipo. El despliegue real requiere configurar tus credenciales de Firebase y Gemini en Streamlit Cloud o en tu entorno local de forma segura.")

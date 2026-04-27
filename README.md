# JARVIS - Prototipo de cerebro con Claude (Anthropic)

Este repo contiene un prototipo mínimo para un "cerebro" llamado JARVIS:
- Backend: FastAPI (Python)
- Ingestión: scripts para procesar documentos y subir a un vector store (Pinecone/FAISS)
- Cliente LLM: wrapper para Anthropic (Claude)
- Frontend demo: Streamlit

Requisitos
- Python 3.10+
- Cuenta Anthropic (API key) y acceso a skills (si aplica)
- Pinecone account o configuración FAISS local
- Variables de entorno: .env (ver .env.example)

Cómo ejecutar (local)
1. Crear virtualenv e instalar:
   pip install -r requirements.txt
2. Configurar .env con ANTHROPIC_API_KEY, PINECONE_API_KEY, PINECONE_ENV, EMBEDDINGS_PROVIDER_API_KEY
3. Ingestar datos:
   python backend/ingest.py --dir ./data --namespace jarvis
4. Ejecutar backend:
   uvicorn backend.app:app --reload
5. Ejecutar frontend demo:
   streamlit run frontend/streamlit_app.py

Nota: Los clientes LLM y embeddings en este prototipo son pluggables: cambia la implementación en backend/anthropic_client.py y backend/embeddings.py según proveedor.

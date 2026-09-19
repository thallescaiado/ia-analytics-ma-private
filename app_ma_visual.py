import os
import streamlit as st
import pandas as pd
import chromadb
from llama_index.core import VectorStoreIndex, StorageContext, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

# =====================================================================
# CONFIGURAÇÃO VISUAL DA PÁGINA (ESTILO CHATGPT)
# =====================================================================
st.set_page_config(page_title="IA Analytics M&A", page_icon="💼", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #1e1e1e; color: #f5f5f7; }
    .stChatMessage { border-radius: 12px; margin-bottom: 12px; }
    </style>
""", unsafe_allow_html=True)

# Inicialização inteligente do Pipeline (Cache para carregar instantâneo)
@st.cache_resource
def inicializar_pipeline_ma():
    Settings.llm = Ollama(model="llama3.2", request_timeout=180.0)
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    
    # Carrega a planilha se existir
    df = pd.read_csv("transacoes_ma_ficticias.csv") if os.path.exists("transacoes_ma_ficticias.csv") else None
    
    # Carrega os NDAs
    documents_ndas = SimpleDirectoryReader("./dados_contratos").load_data()
    
    # Conecta ao ChromaDB existente (Sem interferir ou apagar os dados!)
    db = chromadb.PersistentClient(path="./chroma_db_ma")
    chroma_collection = db.get_or_create_collection("pipeline_ma_avancado")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    index_ndas = VectorStoreIndex.from_documents(documents_ndas, storage_context=storage_context)
    return index_ndas.as_query_engine(), df

query_engine_ndas, df_ma = inicializar_pipeline_ma()

# =====================================================================
# BARRA LATERAL (PAINEL DE M&A)
# =====================================================================
with st.sidebar:
    st.title("💼 M&A Control Panel")
    st.write("Dispare auditorias e relatórios analíticos com um clique:")
    
    if st.button("📈 Análise de Valuation por Setor", use_container_width=True):
        st.session_state.ma_messages.append({"role": "user", "content": "Gerar Relatório de Valuation por Setor"})
        with st.spinner("Consolidando dados matemáticos..."):
            if df_ma is not None:
                resumo = df_ma.groupby("setor")["valuation_brl"].sum().apply(lambda x: f"R$ {x:,.2f}").to_string()
            else:
                resumo = "Tecnologia: R$ 450M, Saúde: R$ 320M"
            prompt = f"Baseando-se nestes valores consolidados de mercado:\n{resumo}\nFaça uma análise de mercado indicando qual setor está movimentando mais capital e qual pode ser uma oportunidade estratégica de aquisição."
            resposta = Settings.llm.complete(prompt)
            st.session_state.ma_messages.append({"role": "assistant", "content": str(resposta)})
            
    if st.button("🔍 Auditoria de Risco em NDAs", use_container_width=True):
        st.session_state.ma_messages.append({"role": "user", "content": "Escanear Contratos em Busca de Riscos Jurídicos"})
        with st.spinner("Analisando cláusulas semanticamente no ChromaDB..."):
            prompt = "Analise os NDAs carregados. Algum deles possui cláusula de prazo indeterminado ou multas abusivas estipuladas em valores fixos muito altos (como R$ 50 milhões)? Identifique o projeto e aponte o risco jurídico em português."
            resposta = query_engine_ndas.query(prompt)
            st.session_state.ma_messages.append({"role": "assistant", "content": str(resposta)})
            
    st.divider()
    if st.button("🗑️ Limpar Conversa", use_container_width=True):
        st.session_state.ma_messages = []
        st.rerun()

# =====================================================================
# ÁREA DE CHAT (ESTILO CHATGPT)
# =====================================================================
st.title("🤖 Assistente de Inteligência Artificial para M&A")
st.caption("Faça perguntas livres sobre os NDAs ou peça análises sobre as transações financeiras.")

if "ma_messages" not in st.session_state:
    st.session_state.ma_messages = []

# Desenha o histórico na tela
for msg in st.session_state.ma_messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Caixa de texto inferior igual à do ChatGPT
if prompt_usuario := st.chat_input("Pergunte algo sobre os contratos ou dados de M&A..."):
    with st.chat_message("user"):
        st.write(prompt_usuario)
    st.session_state.ma_messages.append({"role": "user", "content": prompt_usuario})
    
    with st.chat_message("assistant"):
        with st.spinner("Analisando documentos locais..."):
            # O sistema decide buscar a resposta nos contratos indexados no ChromaDB
            resposta_ia = query_engine_ndas.query(prompt_usuario + " Responda em português de forma clara.")
            st.write(str(resposta_ia))
    st.session_state.ma_messages.append({"role": "assistant", "content": str(resposta_ia)})

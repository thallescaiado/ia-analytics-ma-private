# 💼 Assistente de Inteligência Artificial para M&A (RAG + ChromaDB + Pandas)

Este projeto consiste em um sistema de **Inteligência Artificial focado em Fusões e Aquisições (M&A)**, projetado para operar de forma 100% local, privada e offline. 

A solução resolve o desafio de conformidade e governança de dados corporativos em transações financeiras, permitindo a análise de contratos e auditoria analítica sem expor informações confidenciais a nuvens públicas.

---

## 🛠️ Arquitetura Híbrida e Tecnologias

- **Cérebro da IA (LLM):** `Ollama` rodando o modelo local `Llama 3.2 (3B)`.
- **Orquestrador de Dados:** `LlamaIndex` para fragmentação e busca semântica em contratos.
- **Banco de Dados Vetorial:** `ChromaDB` configurado de forma persistente para o armazenamento dos NDAs.
- **Mecanismo de Análise Financeira:** Integração com a biblioteca `Pandas` para consolidação matemática exata de grandes volumes de transações, mitigando alucinações da LLM.
- **Interface de Usuário:** `Streamlit` com interface escura integrada (estilo ChatGPT) e automações na barra lateral.

---

## 📈 Funcionalidades e Engenharia de Prompts

- **Análise Financeira Avançada:** Cruzamento de um histórico volumoso de transações de mercado (simulando bases de valuation de M&A), gerando relatórios de participação por setor econômico.
- **Auditoria Automática de Risco em NDAs:** Varredura semântica em contratos de confidencialidade armazenados no banco vetorial para identificar cláusulas de risco jurídico (prazos indeterminados, multas abusivas ou quebras de conformidade).
- **Interface Inteligente:** Sistema web de chat com memória ativa de conversa e acionadores rápidos para geração de relatórios estratégicos com um único clique.

---

## 🚀 Processo de Desenvolvimento & Compliance

O projeto foi construído utilizando **Engenharia de Prompts e Programação Assistida por IA**, com foco em simular o pipeline real de uma mesa de operações de M&A. 
Por questões de conformidade e privacidade baseadas em boas práticas de mercado, a base de dados pesada e as planilhas brutas de transações foram mantidas locais através da configuração do arquivo `.gitignore`, disponibilizando publicamente apenas a arquitetura dos scripts de automação.


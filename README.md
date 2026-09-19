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

## 📸 Interface do Usuário

Aqui está o visual da plataforma de M&A rodando localmente com o modelo Llama 3.2:

<img width="1898" height="856" alt="IA Analytics M A - 1" src="https://github.com/user-attachments/assets/e0273afd-9af5-4f2b-b7c1-c231002f96f2" />

<img width="1895" height="823" alt="IA Analytics M A - 2" src="https://github.com/user-attachments/assets/53996aeb-5578-4810-9445-cd1ff3482586" />

<img width="1892" height="846" alt="IA Analytics M A - 3" src="https://github.com/user-attachments/assets/7be17869-cbc6-43e4-9b91-626ff4b1cb7a" />

<img width="1381" height="551" alt="image" src="https://github.com/user-attachments/assets/53167afb-7a89-43cd-a2ea-5e9d8edf19ca" />

<img width="1392" height="677" alt="IA Analytics M A - 4" src="https://github.com/user-attachments/assets/ee60a2f3-cf72-4a67-a56b-f87651466994" />

---

## 🧠 Processo de Aprendizado & Uso de IA

Desenvolvi este projeto como um exercício prático pessoal para entender os conceitos de Inteligência Artificial e bancos de dados vetoriais aplicados ao mercado de M&A.

Como estou no início da minha jornada na programação, utilizei a Inteligência Artificial como assistente colaboradora para me guiar passo a passo na escrita do código, na resolução de erros de ambiente (como caminhos de pastas e compatibilidade de bibliotecas no Windows) e na estruturação do fluxo.

Este projeto foi fundamental para eu praticar de forma realista:
- **Lógica e Resolução de Problemas:** Aprender a ler mensagens de erro do terminal e aplicar as correções sugeridas.
- **Engenharia de Prompts:** Entender como detalhar minhas necessidades para que a IA gerasse os códigos de apoio corretos.
- **Arquitetura de Sistemas de IA:** Compreender na prática o funcionamento de uma estrutura RAG offline, separando o modelo de linguagem local (Llama 3.2) do banco de dados vetorial (ChromaDB).

O foco principal foi ganhar familiaridade com novas tecnologias de automação através de uma postura prática e de aprendizado contínuo.

---

## 📈 Funcionalidades e Engenharia de Prompts

- **Análise Financeira Avançada:** Cruzamento de um histórico volumoso de transações de mercado (simulando bases de valuation de M&A), gerando relatórios de participação por setor econômico.
- **Auditoria Automática de Risco em NDAs:** Varredura semântica em contratos de confidencialidade armazenados no banco vetorial para identificar cláusulas de risco jurídico (prazos indeterminados, multas abusivas ou quebras de conformidade).
- **Interface Inteligente:** Sistema web de chat com memória ativa de conversa e acionadores rápidos para geração de relatórios estratégicos com um único clique.

---

## 🚀 Processo de Desenvolvimento & Compliance

O projeto foi construído utilizando **Engenharia de Prompts e Programação Assistida por IA**, com foco em simular o pipeline real de uma mesa de operações de M&A. 
Por questões de conformidade e privacidade baseadas em boas práticas de mercado, a base de dados pesada e as planilhas brutas de transações foram mantidas locais através da configuração do arquivo `.gitignore`, disponibilizando publicamente apenas a arquitetura dos scripts de automação.


import os

# Cria a pasta para os contratos se ela não existir
os.makedirs("./dados_contratos", exist_ok=True)

# Definição dos textos dos contratos fictícios com armadilhas de risco
nda_1 = """
CONTRATO DE CONFIDENCIALIDADE (NDA) - PROJETO ALFA
Partech Participações S.A. (Compradora) e TechSoluções Ltda (Alvo).
1. OBJETO: Avaliação de potencial transação de Fusão e Aquisição (M&A).
2. PRAZO DE CONFIDENCIALIDADE: As informações confidenciais deverão ser mantidas em sigilo pelo prazo padrão de 3 (três) anos a contar da data de assinatura.
3. MULTA: Em caso de descumprimento do sigilo, a parte infratora indenizará a outra parte com base nas perdas e danos comprovados em juízo.
"""

nda_2 = """
CONTRATO DE CONFIDENCIALIDADE (NDA) - PROJETO BETA
Alpha Investimentos (Compradora) e BioSaúde S.A. (Alvo).
1. OBJETO: Análise de Due Diligence para aquisição de controle acionário.
2. PRAZO DE CONFIDENCIALIDADE: [ALERTA DE RISCO] As obrigações de sigilo deste acordo permanecerão válidas por prazo INDETERMINADO, não expirando nunca.
3. EXCLUSIVIDADE: Fica estabelecido que a empresa Alvo não poderá negociar com terceiros pelos próximos 24 meses.
"""

nda_3 = """
CONTRATO DE CONFIDENCIALIDADE (NDA) - PROJETO GAMA
VarejoGlobal S.A. (Compradora) e LogExpress Logística (Alvo).
1. OBJETO: Troca de informações financeiras para joint-venture.
2. PRAZO DE CONFIDENCIALIDADE: As informações serão confidenciais pelo prazo de 5 (cinco) anos.
3. MULTA ABUSIVA: [ALERTA DE RISCO] O descumprimento de qualquer cláusula deste acordo resultará em MULTA AUTOMÁTICA E IMEDIATA de R$ 50.000.000,00 (cinquenta milhões de reais), independentemente da comprovação de dano real.
"""

# Salvando os arquivos texto físicos no computador
with open("./dados_contratos/nda_projeto_alfa.txt", "w", encoding="utf-8") as f: f.write(nda_1)
with open("./dados_contratos/nda_projeto_beta.txt", "w", encoding="utf-8") as f: f.write(nda_2)
with open("./dados_contratos/nda_projeto_gama.txt", "w", encoding="utf-8") as f: f.write(nda_3)

print("📄 3 Contratos (NDAs) fictícios com armadilhas de risco foram criados na pasta 'dados_contratos'!")

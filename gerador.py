import random
import pandas as pd
from faker import Faker

# Inicializa o gerador de dados configurado para o Brasil
fake = Faker("pt_BR")

print("🔄 Gerando base de dados fictícia para M&A...")

# Listas de apoio para deixar os dados realistas
setores = ["Tecnologia", "Saúde", "Finanças", "Energia", "Varejo", "Logística"]
status_transacao = ["Concluída", "Em Due Diligence", "Análise de NDA", "Cancelada"]

dados_ma = []

# Altere o número 1000 para a quantidade de linhas que você quiser!
for id_transacao in range(5001, 6001):
    empresa_compradora = fake.company()
    empresa_alvo = fake.company()
    
    # Simula valores de Valuation entre 5 milhões e 500 milhões de reais
    valuation = round(random.uniform(5000000, 500000000), 2)
    
    # Monta a linha da tabela
    linha = {
        "id_transacao": id_transacao,
        "compradora": empresa_compradora,
        "alvo": empresa_alvo,
        "setor": random.choice(setores),
        "valuation_brl": valuation,
        "data_anuncio": fake.date_between(start_date="-3y", end_date="today").strftime("%Y-%m-%d"),
        "status": random.choice(status_transacao),
        "email_assessor": f"advisor.{fake.first_name().lower()}@ficticio-ma.com.br"
    }
    dados_ma.append(linha)

# Transforma os dados em uma planilha e salva em formato CSV
df = pd.DataFrame(dados_ma)
df.to_csv("transacoes_ma_ficticias.csv", index=False, encoding="utf-8")

print("📊 Sucesso! Arquivo 'transacoes_ma_ficticias.csv' gerado com 1.000 linhas.")

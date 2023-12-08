from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "database/Dataset - teste.csv"
colunas = ['Age', 'Gender', 'Tenure', 'UsageFrequency', 'SupportCalls', 'PaymentDelay', 'SubscriptionType', 'ContractLength', 'TotalSpend', 'LastInteraction', 'Churn']


# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]

# Método para testar o modelo de Regressão Logística a partir do arquivo correspondente
def test_modelo_lr():  
    # Importando o modelo de regressão logística
    dt_path = 'ml_model/classificadorNovo.pkl'
    modelo_dt = Model.carrega_modelo(dt_path)

    # Obtendo as métricas da Regressão Logística
    acuracia_dt, recall_dt, precisao_dt, f1_dt = avaliador.avaliar(modelo_dt, X, Y)
    
    # Testando as métricas da Regressão Logística 
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_dt >= 0.95 
    assert recall_dt >= 0.85 
    assert precisao_dt >= 0.85 
    assert f1_dt >= 0.85 
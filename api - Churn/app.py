from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Cliente, Model
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
cliente_tag = Tag(name="Cliente", description="Adição, visualização, remoção e predição de pacientes com Diabetes")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de pacientes
@app.get('/listcliente', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema})
def get_clientes():
    """Lista todos os pacientes cadastrados na base
    Retorna uma lista de pacientes cadastrados na base.
    
    Args:
        nome (str): nome do paciente
        
    Returns:
        list: lista de pacientes cadastrados na base
    """
    session = Session()
    
    # Buscando todos os pacientes
    clientes = session.query(Cliente).all()
    
    if not clientes:
        logger.warning("Não há pacientes cadastrados na base :/")
        return {"message": "Não há pacientes cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d pacientes econtrados" % len(clientes))
        return apresenta_clientes(clientes), 200


# Rota de adição de paciente
@app.post('/addcliente', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: ClienteSchema):
    """Adiciona um novo paciente à base de dados
    Retorna uma representação dos pacientes e diagnósticos associados.
    
    Args:
            age: idade
            gend: gênero do cliente
            tenu: 
            usfr: Frequencia de uso
            supcl: Quantidade de ligações para o suporte
            payd: Atraso do pagamento
            subt: Tipo de inscrição
            conlen: Duração do contrato
            totsp: Total gasto
            lasint: Ultima interação com o cliente
            outcome: Resultado
        
    Returns:
        dict: representação se o cliente continua usando os serviços
    """
    
    # Carregando modelo
    ml_path = 'ml_model/classificadorNovo.pkl'
    modelo = Model.carrega_modelo(ml_path)
    
    cliente = Cliente(
        Age=form.Age, 
        Gender=form.Gender, 
        Tenure=form.Tenure, 
        UsageFrequency=form.UsageFrequency, 
        SupportCalls=form.SupportCalls, 
        PaymentDelay=form.PaymentDelay, 
        SubscriptionType=form.SubscriptionType, 
        ContractLength=form.ContractLength,
        TotalSpend=form.TotalSpend,
        LastInteraction=form.LastInteraction,
        Churn=Model.preditor(modelo, form)
    )
    logger.debug(f"Adicionando cliente com as informações inseridas.")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se paciente já existe na base
        if session.query(Cliente).filter(Cliente.Age == form.Age, Cliente.Gender == form.Gender, Cliente.Tenure == form.Tenure,
                                         Cliente.UsageFrequency == form.UsageFrequency, Cliente.SupportCalls == form.SupportCalls, Cliente.PaymentDelay == form.PaymentDelay,
                                         Cliente.SubscriptionType == form.SubscriptionType, Cliente.ContractLength == form.ContractLength, Cliente.TotalSpend == form.TotalSpend,
                                         Cliente.LastInteraction == form.LastInteraction,).first():
            error_msg = "Cliente já existente na base :/"
            logger.warning(f"Erro ao adicionar cliente com as informações inseridas, {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando paciente
        session.add(cliente)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Cliente adicionado com as informações inseridas")
        return apresenta_cliente(cliente), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar cliente com as informações inseridas, {error_msg}")
        return {"message": error_msg}, 400
    
   
# Rota de remoção de paciente por nome
@app.delete('/delcliente', tags=[cliente_tag],
            responses={"200": ClienteViewSchema, "404": ErrorSchema})
def delete_cliente(query: ClienteBuscaSchema):
    """Remove um paciente cadastrado na base a partir do nome

    Args:
        nome (str): nome do paciente
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    cliente_Age = query.Age 
    cliente_Gender = query.Gender 
    cliente_Tenure = query.Tenure 
    cliente_UsageFrequency = query.UsageFrequency 
    cliente_SupportCalls = query.SupportCalls 
    cliente_PaymentDelay = query.PaymentDelay 
    cliente_SubscriptionType = query.SubscriptionType 
    cliente_ContractLength = query.ContractLength
    cliente_TotalSpend = query.TotalSpend
    cliente_LastInteraction = query.LastInteraction

    logger.debug(f"Deletando dados sobre o cliente")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando paciente
    cliente = session.query(Cliente).filter(Cliente.Age == cliente_Age, Cliente.Gender == cliente_Gender, Cliente.Tenure == cliente_Tenure, 
                                            Cliente.UsageFrequency == cliente_UsageFrequency, Cliente.SupportCalls == cliente_SupportCalls, Cliente.PaymentDelay == cliente_PaymentDelay, 
                                            Cliente.SubscriptionType == cliente_SubscriptionType, Cliente.ContractLength == cliente_ContractLength, Cliente.TotalSpend == cliente_TotalSpend, 
                                            Cliente.LastInteraction == cliente_LastInteraction).first()
    
    if not cliente:
        error_msg = "Paciente não encontrado na base :/"
        logger.warning(f"Erro ao deletar cliente, {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(cliente)
        session.commit()
        logger.debug(f"Deletado cliente")
        return {"message": f"Cliente removido com sucesso!"}, 200
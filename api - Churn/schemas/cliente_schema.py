from pydantic import BaseModel
from typing import Optional, List
from model.cliente import Cliente
import json
import numpy as np

class ClienteSchema(BaseModel):
    """ Define como um novo cliente a ser inserido deve ser representado
    """
    Age : int = 30 
    Gender : str = "Female" 
    Tenure : int = 25 
    UsageFrequency : int = 14 
    SupportCalls : int = 4 
    PaymentDelay : int = 27 
    SubscriptionType : str = "Basic" 
    ContractLength : str = "Monthly"
    TotalSpend : int = 600
    LastInteraction : int = 10
    
    
class ClienteViewSchema(BaseModel):
    """Define como um cliente será retornado
    """
    Age : int = 30 
    Gender : str = "Female" 
    Tenure : int = 25 
    UsageFrequency : int = 14 
    SupportCalls : int = 4 
    PaymentDelay : int = 27 
    SubscriptionType : str = "Basic" 
    ContractLength : str = "Monthly"
    TotalSpend : int = 600
    LastInteraction : int = 10
    Churn : int = None
    
class ClienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base nos dados do cliente.
    """
    Age : int = 30 
    Gender : str = "Female" 
    Tenure : int = 25 
    UsageFrequency : int = 14 
    SupportCalls : int = 4 
    PaymentDelay : int = 27 
    SubscriptionType : str = "Basic" 
    ContractLength : str = "Monthly"
    TotalSpend : int = 600
    LastInteraction : int = 10

class ListaClientesSchema(BaseModel):
    """Define como uma lista de clientes será representada
    """
    clientes: List[ClienteSchema]

    
class ClienteDelSchema(BaseModel):
    """Define como um cliente para deleção será representado
    """
    Age : int = 30 
    Gender : str = "Female" 
    Tenure : int = 25 
    UsageFrequency : int = 14 
    SupportCalls : int = 4 
    PaymentDelay : int = 27 
    SubscriptionType : str = "Basic" 
    ContractLength : str = "Monthly"
    TotalSpend : int = 600
    LastInteraction : int = 10
    
# Apresenta apenas os dados de um cliente    
def apresenta_cliente(cliente: Cliente):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    return {
        "id": cliente.id,
        "Age": cliente.Age,
        "Gender": cliente.Gender,
        "Tenure": cliente.Tenure,
        "UsageFrequency": cliente.UsageFrequency,
        "SupportCalls": cliente.SupportCalls,
        "PaymentDelay": cliente.PaymentDelay,
        "SubscriptionType": cliente.SubscriptionType,
        "ContractLength": cliente.ContractLength,
        "TotalSpend": cliente.TotalSpend,
        "LastInteraction": cliente.LastInteraction,
        "Churn": cliente.Churn
    }
    
# Apresenta uma lista de clientes
def apresenta_clientes(clientes: List[Cliente]):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    result = []
    for cliente in clientes:
        result.append({
            "id": cliente.id,
            "Age": cliente.Age,
            "Gender": cliente.Gender,
            "Tenure": cliente.Tenure,
            "UsageFrequency": cliente.UsageFrequency,
            "SupportCalls": cliente.SupportCalls,
            "PaymentDelay": cliente.PaymentDelay,
            "SubscriptionType": cliente.SubscriptionType,
            "ContractLength": cliente.ContractLength,
            "TotalSpend": cliente.TotalSpend,
            "LastInteraction": cliente.LastInteraction,
            "Churn": cliente.Churn
        })

    return {"clientes": result}


from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = Age, Gender, Tenure, Usage Frequency, Support Calls, Payment Delay, Subscription Type, 
#           Contract Length,Total Spend, Last Interaction, Churn

class Cliente(Base):
    __tablename__ = 'clientes'
    
    id = Column(Integer, primary_key=True)
    Age = Column("Age", Integer)
    Gender = Column("Gender", Integer)
    Tenure = Column("Tenure", Integer)
    UsageFrequency = Column("Usage Frequency", Integer)
    SupportCalls = Column("Support Calls", Integer)
    PaymentDelay = Column("Payment Delay", Integer)
    SubscriptionType = Column("Subscription Type", Integer)
    ContractLength = Column("Contract Length", Integer)
    TotalSpend = Column("Total Spend", Integer)
    LastInteraction = Column("Last Interaction", Integer)
    Churn = Column("Churn", Integer, nullable=True)

    
    def __init__(self, Age:int, Gender:int, Tenure:int, UsageFrequency:int,
                 SupportCalls:int, PaymentDelay:int, SubscriptionType:int, 
                 ContractLength:int, TotalSpend:int, LastInteraction:int, Churn:int):
        """
        Cria um Cliente

        Arguments:
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

            data_insercao: data de quando o paciente foi inserido à base
        """
        self.Age = Age
        self.Gender = Gender
        self.Tenure = Tenure
        self.UsageFrequency = UsageFrequency
        self.SupportCalls = SupportCalls
        self.PaymentDelay = PaymentDelay
        self.SubscriptionType = SubscriptionType
        self.ContractLength = ContractLength
        self.TotalSpend = TotalSpend
        self.LastInteraction = LastInteraction
        self.Churn = Churn
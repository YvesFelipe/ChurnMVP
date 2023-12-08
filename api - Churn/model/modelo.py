import numpy as np
import pickle
import joblib

class Model:
    
    def carrega_modelo(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(model, form):
        """Realiza a predição de um cliente com base no modelo treinado
        """

        if form.Gender == "Female":
            Gender = 1
        elif form.Gender == "Male" :
            Gender = 2

        if form.SubscriptionType == "Basic":
            SubscriptionType = 1
        elif form.SubscriptionType == "Standard":
            SubscriptionType = 2
        elif form.SubscriptionType == "Premium":
            SubscriptionType = 3


        if form.ContractLength == "Monthly":
            ContractLength = 1
        elif form.ContractLength == "Quarterly":
            ContractLength = 2
        elif form.ContractLength == "Annual":
            ContractLength = 3

        X_input = np.array([form.Age, 
                            Gender, 
                            form.Tenure, 
                            form.UsageFrequency, 
                            form.SupportCalls, 
                            form.PaymentDelay, 
                            SubscriptionType, 
                            ContractLength,
                            form.TotalSpend,
                            form.LastInteraction                   
                        ])
        # Faremos o reshape para que o modelo entenda que estamos passando
        diagnosis = model.predict(X_input.reshape(1, -1))
        return int(diagnosis[0])
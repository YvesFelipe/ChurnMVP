/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/listcliente';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.clientes.forEach(item => insertList(item.Age, 
                                              item.Gender, 
                                              item.Tenure,
                                              item.UsageFrequency,
                                              item.SupportCalls,
                                              item.PaymentDelay,
                                              item.SubscriptionType,
                                              item.ContractLength,
                                              item.TotalSpend,
                                              item.LastInteraction,
                                              item.Churn,
                                              ))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()




/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (Age, Gender, Tenure,
                        UsageFrequency, SupportCalls, PaymentDelay, 
                        SubscriptionType, ContractLength, TotalSpend,LastInteraction) => {
    
  const formData = new FormData();
  formData.append('Age', Age);
  formData.append('Gender', Gender);
  formData.append('Tenure', Tenure);
  formData.append('UsageFrequency', UsageFrequency);
  formData.append('SupportCalls', SupportCalls);
  formData.append('PaymentDelay', PaymentDelay);
  formData.append('SubscriptionType', SubscriptionType);
  formData.append('ContractLength', ContractLength);
  formData.append('TotalSpend', TotalSpend);
  formData.append('LastInteraction', LastInteraction);

  let url = 'http://127.0.0.1:5000/addcliente';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertDeleteButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  // var table = document.getElementById('myTable');
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItem(nomeItem, div)
        alert("Removido!")
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item, nomeItem) => {
  console.log(nomeItem)
  delAge = nomeItem.getElementsByTagName('td')[0].innerHTML
  delGender = nomeItem.getElementsByTagName('td')[1].innerHTML
  delTenure = nomeItem.getElementsByTagName('td')[2].innerHTML
  delUsageFrequency = nomeItem.getElementsByTagName('td')[3].innerHTML
  delSupportCalls = nomeItem.getElementsByTagName('td')[4].innerHTML
  delPaymentDelay = nomeItem.getElementsByTagName('td')[5].innerHTML
  delSubscriptionType = nomeItem.getElementsByTagName('td')[6].innerHTML
  delContractLength = nomeItem.getElementsByTagName('td')[7].innerHTML
  delTotalSpend = nomeItem.getElementsByTagName('td')[8].innerHTML
  delLastInteraction = nomeItem.getElementsByTagName('td')[9].innerHTML

  let url = 'http://127.0.0.1:5000/delcliente?Age='+delAge + '&Gender=' + delGender + '&Tenure=' + delTenure + '&UsageFrequency=' + delUsageFrequency + '&SupportCalls=' + delSupportCalls + '&PaymentDelay=' + delPaymentDelay + '&SubscriptionType=' + delSubscriptionType + '&ContractLength=' + delContractLength + '&TotalSpend=' + delTotalSpend + '&LastInteraction=' + delLastInteraction;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
  let inputAge = document.getElementById("Age").value;
  let inputGender = document.getElementById("Gender").value;
  let inputTenure = document.getElementById("Tenure").value;
  let inputUsageFrequency = document.getElementById("UsageFrequency").value;
  let inputSupportCalls = document.getElementById("SupportCalls").value;
  let inputPaymentDelay = document.getElementById("PaymentDelay").value;
  let inputSubscriptionType = document.getElementById("SubscriptionType").value;
  let inputContractLength = document.getElementById("ContractLength").value;
  let inputTotalSpend = document.getElementById("TotalSpend").value;
  let inputLastInteraction = document.getElementById("LastInteraction").value;

  // Verifique se o nome do produto já existe antes de adicionar
  const checkUrl = `http://127.0.0.1:5000/listcliente?Age=${inputAge}&Gender=${inputGender}&Tenure=${inputTenure}&UsageFrequency=${inputUsageFrequency}&SupportCalls=${inputSupportCalls}&PaymentDelay=${inputPaymentDelay}&SubscriptionType=${inputSubscriptionType}&ContractLength=${inputContractLength}&TotalSpend=${inputTotalSpend}&LastInteraction=${inputLastInteraction}`;
  fetch(checkUrl, {
    method: 'get'
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.clientes && data.clientes.some(item => item.Age === inputAge && item.Gender === inputGender && item.Tenure === inputTenure && item.UsageFrequency === inputUsageFrequency && item.SupportCalls === inputSupportCalls && item.PaymentDelay === inputPaymentDelay && item.SubscriptionType === inputSubscriptionType && item.ContractLength === inputContractLength && item.TotalSpend === inputTotalSpend && item.LastInteraction === inputLastInteraction)) {
        alert("O cliente já está cadastrado.\nCadastre o cliente com entradas diferentes.");
      } else if (inputAge === '' || inputGender === '' || inputTenure === '' || inputUsageFrequency === '' || inputSupportCalls === '' || inputPaymentDelay === '' || inputSubscriptionType === '' || inputContractLength === '' || inputTotalSpend === '' || inputLastInteraction === '') {
        alert("Nenhum campo pode estar vazio!");
      } else if (isNaN(inputAge) || isNaN(inputTenure) || isNaN(inputUsageFrequency) || isNaN(inputSupportCalls) || isNaN(inputPaymentDelay) || isNaN(inputTotalSpend) || isNaN(inputLastInteraction)) {
        alert("Esse(s) campo(s) precisam ser números!");
      } else {
        insertList(inputAge, inputGender, inputTenure, inputUsageFrequency, inputSupportCalls, inputPaymentDelay, inputSubscriptionType, inputContractLength, inputTotalSpend,inputLastInteraction);
        postItem(inputAge, inputGender, inputTenure, inputUsageFrequency, inputSupportCalls, inputPaymentDelay, inputSubscriptionType, inputContractLength, inputTotalSpend,inputLastInteraction);
        alert("Cliente adicionado!");
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (Age, Gender, Tenure, UsageFrequency, SupportCalls, PaymentDelay, SubscriptionType, ContractLength, TotalSpend, LastInteraction,Churn) => {
  var item = [Age, Gender, Tenure, UsageFrequency, SupportCalls, PaymentDelay, SubscriptionType, ContractLength, TotalSpend, LastInteraction,Churn];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  var deleteCell = row.insertCell(-1);
  insertDeleteButton(deleteCell);


  document.getElementById("Age").value = "";
  document.getElementById("Gender").value = "";
  document.getElementById("Tenure").value = "";
  document.getElementById("UsageFrequency").value = "";
  document.getElementById("SupportCalls").value = "";
  document.getElementById("PaymentDelay").value = "";
  document.getElementById("SubscriptionType").value = "";
  document.getElementById("ContractLength").value = "";
  document.getElementById("TotalSpend").value = "";
  document.getElementById("LastInteraction").value = "";
 

  removeElement()
}
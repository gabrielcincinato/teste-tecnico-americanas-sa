
# Teste Técnico Americanas SA
![Logo](/img/americanas_sa.png)

Este teste consiste em desenvolver um modelo de aprendizado de máquina capaz de classificar as amostras do conjunto de dados [dataset_cdjr.parquet.gzip](https://drive.google.com/file/d/1HXq9mczY-5OpFaXK3kk8zAgFEgEgF3jt/view?usp=sharing), fornecido para a realização do teste técnico das Lojas Americanas SA.  

O teste consiste em 5 partes:

* Análise de dados
* Preparação dos dados
* Modelagem
* Avaliação da performance do modelo
* Entrega do modelo

### Análise de dados
Esta parte consiste em verificar como são os dados com que estamos
lidando; verificar os tipos dos valores que compõem as colunas, as distribuições dos valores,
se há valores faltantes ou errôneos no dataset, ou se há insights que podemos tirar dos dados. Como não temos muita informação sobre os dados e suas features, a retirada de insights acaba por ser bastante limitada. Mesmo assim, foi o suficiente para tirar certas conclusões:
* As features são todas numéricas e com valores muito divergentes, com presença de vários outliers.
* Não há valores faltantes ou errôneos no dataset, sendo desnecessário fazer imputação ou limpeza.
* Há pelo pelo menos uma feature que é altamente correlacionada com outra. A feature4 possui 0.99 de correlação com a feature0.
* 56% dos valores da coluna alvo recebem o valor 1 e 44% recebe o valor 0. Esse desequilíbrio deverá ser levado em conta na hora de separar os dados de teste e treinamento.

### Preparação dos dados
Esta parte consiste em deixar os dados prontos para a modelagem. De acordo com a análise anterior, as ações que precisaram ser tomadas para deixar os dados prontos para a modelagem foram:
* Separar os dados de treinamento e de teste da coluna target com a mesma proporção do dataset completo.
* Padronizar e normalizar os dados, devido a valores muito divergentes e com presença de outliers.
* Eliminar colunas altamente correlacionadas, para evitar a redundância.  

Foram usados os scalers Power Transformer para a padronização, e posteriormente o Min Max Scaler para a normalização.  
A coluna feature4 foi removida por sua alta correlação com a feature0, para evitar a redundância dos dados.

### Modelagem
Antes de iniciar a modelagem, criei um modelo dummy que tenta adivinhar os resultados de forma totalmente aleatória, para termos uma base da performance de um modelo "burro". Foi usado a métrica AUC para definir a performance do modelo. O modelo dummy obteve pontuação AUC média de 0.5 nos testes de validação.  
De forma preliminar, foram selecionados 5 modelos para terem suas performances comparadas no teste de validação para posteriormente passarem por uma regulagem dos hiperparâmetros. Os modelos escolhidos foram:
* K-Nearest Neighbors
* Logistic Regression
* Random Forest Classifier
* LinearSVC
* XGBoost

Dos 5 modelos testados, o que obteve a melhor performance nos testes de validação pré-regulagem dos parâmetros foi o LinearSVC, com uma pontuação AUC de 0.7.  
Posteriormente, foi feita a regulagem dos hiperparâmetros para melhorar a performance do modelo, mas a regulagem não obteve nenhum ganho significativo de performance.

### Avaliação da performance do modelo
Depois dos testes de validação e regulagem dos hiperparâmetros, foi testada a performance
do modelo nos dados de teste, e o modelo obteve performance similar aos testes de validação, tendo uma pontuação AUC de 0.72, em contraste com 0.34 do modelo dummy no teste.

### Entrega do modelo
O modelo foi salvo e integrado em uma interface simples feita na biblioteca Tkinter.

#### Como executar o modelo

No terminal, instale as dependências

```bash
  pip install -r requirements.txt
```

Execute o script

```bash
  python3 executar_modelo.py
```

![modelo](/img/model.png)

Preencha cada campo com o respectivo valor da feature. Lembrando que não há campo para a feature4, porque ela foi removida por redundância.

## Autor

- [@gabrielcincinato](https://github.com/gabrielcincinato)


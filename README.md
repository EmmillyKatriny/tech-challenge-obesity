# tech-challenge-obesity

## Predição de Nível de Obesidade com Machine Learning

# 1. Contexto do Problema

A obesidade é uma condição médica multifatorial que impacta diretamente a saúde da população.
Este projeto foi desenvolvido com o objetivo de construir um modelo preditivo capaz de auxiliar a equipe médica na identificação do nível de obesidade de um paciente, com base em dados comportamentais, físicos e hábitos de vida.

O sistema foi desenvolvido como parte do Tech Challenge da pós-graduação, integrando todas as etapas da pipeline de Machine Learning.

# 2. Base de Dados

Base utilizada: Obesity.csv

Contém 2.111 registros e 17 variáveis, incluindo:

Dados físicos (Age, Height, Weight)

Hábitos alimentares

Atividade física

Histórico familiar

Meio de transporte

Nível de obesidade (variável alvo)

# 3. Feature Engineering

Foram realizadas as seguintes transformações:

Arredondamento das variáveis de escala (FCVC, NCP, CH2O, FAF, TUE)

Criação da variável IMC (BMI)

Separação de variáveis numéricas e categóricas

Aplicação de:

StandardScaler (variáveis numéricas)

OneHotEncoder (variáveis categóricas)

Toda a transformação foi implementada utilizando Pipeline do Scikit-learn, garantindo ausência de vazamento de dados.

A distribuição das classes mostrou-se relativamente balanceada, reduzindo risco de viés do modelo.

# 4. Modelagem

Foram testados três algoritmos:

Logistic Regression

Random Forest

Gradient Boosting

| Modelo               | Accuracy |
|----------------------|----------|
| Logistic Regression  | 90.78%   |
| Random Forest        | 97.63%   |
| Gradient Boosting ⭐ | **98.34%** |


O modelo escolhido foi Gradient Boosting, por apresentar melhor desempenho.

Também foram avaliadas:

Matriz de Confusão

Classification Report (Precision, Recall, F1-score)

# 5. Aplicação Preditiva

O modelo foi deployado utilizando Streamlit.

A aplicação permite:

Inserção dos dados do paciente

Cálculo automático do IMC

Previsão do nível de obesidade

Acesse o app aqui:
(https://tech-challenge-obesity-mpu2ixco4gqgl9t2qo73p5.streamlit.app/)

# 6. Dashboard Analítico

Foi desenvolvido um painel analítico com foco em insights para decisão médica, incluindo:

Distribuição dos níveis de obesidade

Relação IMC × obesidade

Histórico familiar × obesidade

Atividade física × obesidade

Tempo de tela × obesidade

Consumo de álcool × obesidade

Acesse o dashboard aqui:

# 7. Estrutura do Projeto
tech-challenge-obesity/  
│
├── data/  
│   └── obesity.csv  
│  
├── tech_challenge_obesity.ipynb  
├── app.py  
├── modelo_obesidade.pkl  
├── requirements.txt  
├── dashboard.pbix  
└── README.md  

# 8. Vídeo de Apresentação

Link do vídeo explicando estratégia e resultados:

# 9. Conclusão

O modelo desenvolvido atingiu alta performance preditiva (>98% de acurácia), demonstrando forte capacidade de identificar padrões associados ao nível de obesidade.

A aplicação e o dashboard fornecem suporte visual e analítico para auxiliar a equipe médica na tomada de decisão.

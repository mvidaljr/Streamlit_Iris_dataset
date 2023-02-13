import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



from model_methods import predict
st.set_option('deprecation.showPyplotGlobalUse', False)
classes = {0:'setosa',1:'versicolor',2:'virginica'}
class_labels = list(classes.values())
st.title("Tipificação das Espécies de Plantas")
st.markdown('**Objetivo** : Dadas as características das flores vamos prever a especie da flor.')
st.markdown('A Máquina Preditiva pode prever se a planta pertence às três categorias a seguir : **setosa, versicolor, virginica**')
def predict_class():
    data = list(map(float,[sepal_length, sepal_width, petal_length, petal_width]))
    result, probs = predict(data)
    st.write("A planta é do tipo ",result)
    probs = [np.round(x,6) for x in probs]
    ax = sns.barplot(probs ,class_labels, palette="winter", orient='h')
    ax.set_yticklabels(class_labels,rotation=0)
    plt.title("Probabilidades dos Dados pertencentes a cada classe")
    for index, value in enumerate(probs):
        plt.text(value, index,str(value))
    st.pyplot()
st.markdown("**Por favor, insira os detalhes da flor na forma de 4 valores decimais separados por vírgulas**")
sepal_length = st.text_input('Valor do sepal_length', '')
sepal_width = st.text_input('Valor do sepal_width', '')
petal_length = st.text_input('Valor do petal_length', '')
petal_width = st.text_input('Valor do petal_width', '')
if st.button("Previsão"):
    predict_class()
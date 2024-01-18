import streamlit as st

st.image('img/neurona.jpg', width=300)

st.title('¡Hola neurona!')

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
   st.header("Una neurona con una entrada y un peso")

   w = st.slider('Peso', 0.0, 5.0, key=1)
   x = st.number_input('Introduzca el valor de la entrada', key=2)
   
   y = x * w
   
   if st.button("Calcular la salida", key=3):
      st.write('La salida de la neurona es', y)

with tab2:
   st.header("Una neurona con dos entradas y dos pesos")

   col1, col2 = st.columns(2)
   w0 = col1.slider('Peso w₀', 0.0, 5.0, key=4)
   w1 = col2.slider('Peso w₁', 0.0, 5.0, key=5)
   
   x0 = col1.number_input('Entrada x₀', key=6)
   x1 = col2.number_input('Entrada x₁', key=7)

   y = (x0 * w0) + (x1 * w1)

   if st.button("Calcular la salida", key=8):
      st.write('La salida de la neurona es', y)

with tab3:
   st.header("Una neurona con tres entradas y bias")

   col1, col2, col3 = st.columns(3)
   w0 = col1.slider('Peso w₀', 0.0, 5.0, key=9)
   w1 = col2.slider('Peso w₁', 0.0, 5.0, key=10)
   w2 = col3.slider('Peso w₂', 0.0, 5.0, key=11)

   x0 = col1.number_input('Entrada x₀', key=12)
   x1 = col2.number_input('Entrada x₁', key=13)
   x2 = col3.number_input('Entrada x₂', key=14)

   b = st.number_input('Introduzca el valor del sesgo', key=15)

   y = (x0 * w0) + (x1 * w1) + (x2 * w2) + b

   if st.button("Calcular la salida", key=16):
      st.write('La salida de la neurona es', y)


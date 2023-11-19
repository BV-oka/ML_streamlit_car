# импортируем библиотеку streamlit
import streamlit as st
# импортируем библиотеку pandas
import pandas as pd

if st.button('Нажми на меня'):
  st.write('Привет, мир!')


# Название
st.title("Песочница")

# Заголовок
st.header("Это заголовок")

# Подзаголовок
st.subheader("Это подзаголовок")

# Подзаголовок
st.subheader("Это подзаголовок")

# Текст
st.text("Просто текст")

st.divider()
st.divider()


status = st.radio("выберите вариант: ", ('да', 'нет'), label_visibility="hidden")

if (status == 'да'):
    st.success("да")
else:
    st.success("нет")

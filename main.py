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

# полоски
st.divider()
st.divider()

st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
# st.snow()
# st.balloons()




# переключатели
status = st.radio("выберите вариант: ", ('да', 'нет'))

if (status == 'да'):
    st.success("да")
else:
    st.success("нет")
    
  

status = st.radio("выберите вариант: ", ('да', 'нет'), horizontal=True)

if (status == 'да'):
    st.success("да")
else:
    st.success("нет")
    st.snow()



genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.success('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")


option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


# слайдеры

# age = st.slider('How old are you?', 0, 130, 25)
# st.write("I'm ", age, 'years old')



values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)


# заголовок приложения
st.title('Калькулятор индекса массы тела (ИМТ)')

# СЧИТЫВАЕМ ВЕС
weight = st.number_input("Введите ваш вес (в килограммах)")

# СЧИТЫВАЕМ РОСТ
# используем radio button, чтобы указать единицы измерения
status = st.radio('Укажите единицы измерения роста: ', ('см', 'м', 'футы'))

# сравниваем различные статусы для единиц измерения роста
if (status == 'см'):
    # считываем значение роста в сантиметрах
    height = st.number_input('Сантиметры')

    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        st.text("Введите ваш рост")

elif (status == 'м'):
    # считываем значение роста в метрах
    height = st.number_input('Метры')

    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Введите ваш рост")

else:
    # считываем значение роста в футах
    height = st.number_input('Футы')

    # 1 meter = 3.28
    try:
        bmi = weight / (((height / 3.28)) ** 2)
    except:
        st.text("Введите ваш рост")

# проверяем нажата кнопка или нет
if (st.button('Рассчитать ИМТ')):

    # напечатать значение ИМТ
    st.text(f"Ваш ИМТ равен {bmi:.2f}")

    # интерпретация ИМТ
    if (bmi < 16):
        st.error("Выраженный дефицит массы тела")
    elif (bmi >= 16 and bmi < 18.5):
        st.warning("Недостаточная (дефицит) масса тела")
    elif (bmi >= 18.5 and bmi < 25):
        st.success("Норма")
    elif (bmi >= 25 and bmi < 30):
        st.warning("Избыточная масса тела")
    elif (bmi >= 30):
        st.error("Любитель вкусняшек")

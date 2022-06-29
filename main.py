import streamlit as st
import time

st.title('streamlit 超入門')


##st.write('DataFrame')


st.write('プログレスバー')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.1)


left_column,right_column = st.columns(2)
button = left_column.button('右からカラムにボタンを表示')

if button:
  right_column.write('ここは右カラム')



expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')














##if st.checkbox('Show Image'):
##  img = Image.open('razu.png')
##  st.image(img, caption='ラズパイ', use_column_width=True)
##
##option = st.selectbox(
##    'あなたが好きな数字',
##    list(range(1,11))
##)
##
##
##'好きな数字は',option,'です'
##
##
##textinp = st.text_input('あなたの趣味')
##
##condition = st.slider('今の調子',0,100,50)
##
##
##'あなたの趣味は:',textinp
##'コンディション:',condition
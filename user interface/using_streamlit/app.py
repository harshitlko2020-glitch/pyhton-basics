import streamlit as st

#st.title("My Streamlit App")
#st.subheader("My first Web App using Python")
#st.text('my name is harshit')

#st.text_input('enter your name',placeholder='Lestrade')
#st.text_area('enter your address')
#st.number_input('enter the number')

c1,c2 = st.columns(2)

v1 = c1.number_input('enter first number')
v2 = c2.number_input('enter second number')

operations = ['add','sub','product','divide']
choice = st.radio('select operation',options=operations)

submit_button = st.button('calculate')

result = 0
if choice =='add':
    result = v1+v2
elif choice == 'sub':
    result = v1-v2
elif choice == 'product':
    result = v1*v2
else:
    result = v1/v2

st.markdown(f'''
            ### Result :{result}
            ''')
st.success(f'Result Calculated : {result}')
st.balloons()
st.snow()






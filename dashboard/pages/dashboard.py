import streamlit as st
import pandas as pd 
import seaborn as sns
import plotly.express as px

df = sns.load_dataset("titanic")
filtered_df = df.copy()


sidebar = st.sidebar

sidebar.title("Dashboard Filters")
gender = sidebar.multiselect("Gender",options=df["sex"].unique())

pclass = sidebar.multiselect("Passengers Class",options=df['class'].unique())

age = sidebar.slider("age range",min_value=int(df['age'].min()),
                     max_value=int(df["age"].max()),
                     value=(int(df['age'].min()),int(df['age'].max())))

if gender:
    filtered_df = filtered_df[filtered_df["sex"].isin(gender)]
if pclass:
    filtered_df = filtered_df[filtered_df["class"].isin(pclass)]

if age:
    filtered_df = filtered_df[(filtered_df["age"]>= age[0])&
                              (filtered_df['age']<= age[1])]

st.dataframe(filtered_df)

fig1 = px.histogram(filtered_df,x = 'age', nbins= 30, title = "Age Distribution")

st.plotly_chart(fig1,use_container_width=True)
st.markdown('''**Conclusion**: The age distribution of titanic passenges is right-skewed,
            with a higher concentration of younger passengers.
            There is noticible drop in the no of passengers above 
            60 years old''')


#  Add bar chart for survival count. Add pie chart for passengers class In the dashboard

survival_count = sidebar.multiselect("survived",options=df['survived'].unique())

if survival_count:
    filtered_df = filtered_df[filtered_df["survived"].isin(survival_count)]

fig2 = px.bar(filtered_df,x = "survived",y= "pclass",title="Survival count based on pclass")

st.plotly_chart(fig2)



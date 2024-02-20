import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.title("Student Mental Health Assessment")

selected_x_var = st.selectbox('Select x Variable',
                              ['Stress_Level', 'Depression_Score','Anxiety_Score', 'Financial_Stress'])

selected_y_var = st.selectbox('Select y Variable',
                              ['Stress_Level', 'Depression_Score','Anxiety_Score', 'Financial_Stress'])

course = st.radio("Select Course", ["Engineering", "Business", "Computer Science", "Medical", "Law", "Others"])

student_file = st.file_uploader("Upload student dataset (CSV)", type=["csv"])
if student_file is not None:
    student_df = pd.read_csv(student_file)
    st.write(student_df)
else:
    st.stop()

filtered_by_course = student_df.loc[student_df['Course'] == course]

sns.set_style('darkgrid')
markers = {"Engineering": "o", "Business": "s", "Computer Science": "^", "Medical": "x", "Law": "p", "Others": "*"}

fig, ax = plt.subplots()
ax = sns.scatterplot(data=filtered_by_course,
                     x=selected_x_var, y=selected_y_var,
                     hue='Course', style='Course', markers=markers)

plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title(f"Scatterplot - {course}")
st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt
st.title('E-commerce Company Insights')
st.write('Here is our LLM generated dashboard')
import matplotlib.pyplot as plt

# Data
categories = ['Intimates', 'Jeans', 'Fashion Hoodies & Sweatshirts']
returns = [5348, 4932, 4612]
return_percentages = [2.13, 1.96, 1.84]

# Plotting
fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Product Categories')
ax1.set_ylabel('Number of Returns', color=color)
ax1.bar(categories, returns, color=color, alpha=0.6)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Return Percentage (%)', color=color)
ax2.plot(categories, return_percentages, color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Top 3 Product Categories with Highest Number of Returns')

fig = plt.gcf()
st.pyplot(fig)

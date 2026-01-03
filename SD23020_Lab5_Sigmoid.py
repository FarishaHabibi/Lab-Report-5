import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Sigmoid Activation Function")

x = np.linspace(-10, 10, 100)
sigmoid = 1 / (1 + np.exp(-x))

fig, ax = plt.subplots()
ax.plot(x, sigmoid)
ax.set_xlabel("Input")
ax.set_ylabel("Output")
ax.set_title("Sigmoid Function")

st.pyplot(fig)

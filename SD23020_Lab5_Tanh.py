import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Tanh Activation Function")

x = np.linspace(-10, 10, 100)
tanh = np.tanh(x)

fig, ax = plt.subplots()
ax.plot(x, tanh)
ax.set_xlabel("Input")
ax.set_ylabel("Output")
ax.set_title("Tanh Function")

st.pyplot(fig)

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("ReLU Activation Function")

x = np.linspace(-10, 10, 100)
relu = np.maximum(0, x)

fig, ax = plt.subplots()
ax.plot(x, relu)
ax.set_xlabel("Input")
ax.set_ylabel("Output")
ax.set_title("ReLU Function")

st.pyplot(fig)

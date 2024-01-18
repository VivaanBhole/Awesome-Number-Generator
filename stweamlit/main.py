import random

import streamlit as st

f = st.button('red[button]')

if(f):
    st.text(str(random.Random(9)+1))

import streamlit as st
from PIL import Image

st.title("The Anointed Realtor")
img = Image.open("v.jpg")
st.subheader("The best form of investment is land")
st.image(img)
st.text("CAP")
st.selectbox("animals", ["Lion", "Goat", "Cat"])


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.selectbox('Total', ["instalment", "outright"])

with col2:
    st.text_input('Avg Price')

with col3:
    st.selectbox('Avg DOM', ["$200", "$400", "$1000"])

with col4:
    st.selectbox('Avg PPSQFT', ["$5000", "$2000", "$8000"])

st.video("est.mp4")
st.sidebar.radio('africa', ["nigeria", "Ghana", "Egypt", 1])
with col5:
     st.radio('student', ["university", "collage", "pre-school"])

tab1, tab2, tab3, tab4 = st.tabs(["colour", "shape", "angles", "gender"])

with tab1:
    st.image('col.png')
    st.write("red", "white", "yellow", "blue")

with tab2:
    st.image('shap.png')
    st.write("circle", "square", "triangle", "rectangle")

with tab3:
    st.image('ang.png')
    st.write("polygon", "pentagon", "hexagon", "octagon")

with tab4:
    st.image('gen.png')
    st.write("female", "male", 'others', 'prefer not to say')
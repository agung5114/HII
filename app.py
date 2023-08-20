import streamlit as st
st.set_page_config(page_title="HII", page_icon=None, layout="wide", initial_sidebar_state="auto",menu_items=None)
import plotly.express as px 
import plotly.graph_objects as go

# EDA Pkgs
import pandas as pd 
import numpy as np 
from datetime import datetime
# import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)

# Utils
import joblib 

# Image
from PIL import Image

st.sidebar.title("Health Intelligence & Insight")
menu = ["Dashboard","Prediksi DM & TB"]
choice = st.sidebar.selectbox("Select Menu", menu)

if choice == "Prediksi DM & TB":
    st.subheader("Prediksi DM & TB")
    # iris= Image.open('iris.png')
    # st.image(iris)

    model= open("modeldt.sav", "rb")
    dt_clf=joblib.load(model)
    #Loading images
    # setosa= Image.open('setosa.png')
    # versicolor= Image.open('versicolor.png')
    # virginica = Image.open('virginica.png')

    st.sidebar.title("Features")
    #Intializing
    v1 = st.sidebar.slider(label="Umur",value=30,min_value=0, max_value=150, step=1)
    v2 = st.sidebar.slider(label="Jenis Kelamin",value=0,min_value=0, max_value=1, step=1)
    v3 = st.sidebar.slider(label="Status",value=3,min_value=1, max_value=5, step=1)
    v4 = st.sidebar.slider(label="Kelas",value=1,min_value=1, max_value=3, step=1)
    v5 = st.sidebar.slider(label="Kelompok Peserta",value=3,min_value=1, max_value=5, step=1)
    v6 = st.sidebar.slider(label="Alamat Provinsi",value=11,min_value=11, max_value=99, step=1)

    if st.button("Jalankan Prediksi"):
        dfvalues = pd.DataFrame(list(zip([v1],[v2],[v3],[v4],[v5],[v6])),columns =['Umur','JK','Status','Kelas','Kelompok','Prov'])
        # input_variables = np.array(dfvalues[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
        prediction = dt_clf.predict(dfvalues)
        if prediction[0] == 1:
            st.subheader('Risiko Diabetes Militus')
        elif prediction == 2:
            st.subheader('Risiko Tuberkolosis')
        elif prediction == 0:
            st.subheader('Risiko Diabetes Militus & Tuberkolosis Rendah')
elif choice == "Dashboard":
    # st.subheader('Dashboard')
    import streamlit.components.v1 as components
    components.html('''
        <div class='tableauPlaceholder' id='viz1692541777917' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;bp&#47;bpjs_2023&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='bpjs_2023&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;bp&#47;bpjs_2023&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1692541777917');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='2327px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        ''',width=1440,height=720)

import streamlit as st
st.set_page_config(page_title="GRIP", page_icon=None,layout="wide", initial_sidebar_state="auto",menu_items=None)
                #    {'About': "# This is a header. This is an *extremely* cool app!"}
# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'


import streamlit.components.v1 as components

import plotly.express as px 
import plotly.graph_objects as go

# EDA Pkgs
import pandas as pd 
import numpy as np 
from datetime import datetime
# import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)

# from annotated_text import annotated_text

# Utils
import joblib 

# Image
from PIL import Image

import numpy as np
def assignRisk(df,pcol,rcol):
    conditions = [
        (df[pcol] <=0.5),
        (df[pcol] <0.8),
        (df[pcol] >=0.8)
        ]
    choices = ['Rendah','Sedang','Tinggi']

    df[rcol] = np.select(conditions, choices, default='Low')
    return df

st.sidebar.image('grip1.png')
st.sidebar.title("GEOSPATIAL RISK PREDICTION \
                 FOR DM & TB")
menu = ["Monitoring","Geospatial Factors","Region Risk Mapping","Individual Risk Prediction"]
choice = st.sidebar.selectbox("Select Menu", menu)

@st.cache_data
def getData(url,sep):
    df = pd.read_csv(url,sep=sep)
    return df

if choice == "Monitoring":
    components.html('''
    <div class='tableauPlaceholder' id='viz1693744472041' style='position: relative'><noscript><a href='#'><img alt='Dashboard Monitoring DM dan TB ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;gr&#47;grip_overview&#47;DashboardMonitoringDMdanTB&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='grip_overview&#47;DashboardMonitoringDMdanTB' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;gr&#47;grip_overview&#47;DashboardMonitoringDMdanTB&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1693744472041');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1477px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    ''',height=1477)
    
    # <div class='tableauPlaceholder' id='viz1693410447726' style='position: relative'><noscript><a href='#'><img alt='Dashboard Monitoring DM dan TB ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;bp&#47;bpjs_2023&#47;DashboardMonitoringDMdanTB&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='bpjs_2023&#47;DashboardMonitoringDMdanTB' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;bp&#47;bpjs_2023&#47;DashboardMonitoringDMdanTB&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1693410447726');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1677px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        
    
elif choice == "Geospatial Factors":
    components.html(
    '''<div class='tableauPlaceholder' id='viz1693666462409' style='position: relative'><noscript><a href='#'><img alt='Peta Risiko DM dan TB  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pe&#47;PetaRisikoDMdanTB&#47;PetaRisikoDMdanTB_1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PetaRisikoDMdanTB&#47;PetaRisikoDMdanTB_1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pe&#47;PetaRisikoDMdanTB&#47;PetaRisikoDMdanTB_1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1693666462409');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    ''',height=900)
    components.html(
    '''
    <div class='tableauPlaceholder' id='viz1693750546209' style='position: relative'><noscript><a href='#'><img alt='Dashboard 3 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;bp&#47;bpjs_grip&#47;Dashboard3&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='bpjs_grip&#47;Dashboard3' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;bp&#47;bpjs_grip&#47;Dashboard3&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1693750546209');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1427px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    ''',height=900)
    # with c2:
    #     st.subheader('Analisis Regresi')
    #     st.write('Faktor-faktor lingkungan dan Gaya hidup berdasarkan lokasi peserta terbukti berpengaruh terhadap tingkat prevelansi risiko DM dan TB')
    #     st.image('dmfactors.png')
    #     st.image('tbfactors.png')

elif choice == "Region Risk Mapping":
    components.html(
    '''
    <div class='tableauPlaceholder' id='viz1693420731003' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;bp&#47;bpjs_grip&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='bpjs_grip&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;bp&#47;bpjs_grip&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1693420731003');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='977px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    '''
    ,height=977)
    # components.iframe(
    # '''
    # https://public.tableau.com/views/bpjs_grip/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link
    # '''
    # ,width=1600,height=900)
elif choice == "Individual Risk Prediction":
    # genre = st.sidebar.radio("",('Prediction','Treatment'))
    # if genre == 'Prediction':
    st.subheader('Prediksi Risiko Peserta Berdasarkan Karakteristik Individu, Faktor Lingkungan dan Gaya Hidup')
    df = getData('sample_peserta.csv',',')
    # df['IPM'] = df['IPM'].str.replace(',','.').astype('float')
    peserta = df['PSTV01'].head(100).tolist()
    # datapeserta = df[df['PSTV01'].isin([peserta[0]])]
    ops = ['Rendah','Tinggi']
    ops_dict = {'Rendah':0,'Tinggi':1}
    selectForm = st.sidebar.selectbox("Pilih Peserta", peserta)
    # if submitted:
    datapeserta = df[df['PSTV01'].isin([selectForm])]

    k1,k2 = st.columns((1,4))
    with k1:
        st.image(Image.open('accnt.png'))
        with st.expander('Data Pokok Peserta', expanded=True):
            st.write(f"Nomor Peserta: {datapeserta['PSTV01'].values[0]}")
            i2 = datapeserta['JK'].values[0]
            st.write(f"Jenis Kelamin: {['Laki-Laki' if i2==1 else 'Perempuan'][0]}")
            # i3 = datapeserta['Status'].values[0]
            # st.write(f"Status Peserta: {i3}")
            st.write(f"Kota: {datapeserta['PSTV10'].values[0]}")
            st.write(f"Provinsi: {datapeserta['PSTV09'].values[0]}")
        with st.expander('Prediksi Risiko DM dan TB', expanded=True):
                tbrisk = datapeserta['tb_risk'].values[0]
                dmrisk = datapeserta['dm_risk'].values[0]
                st.subheader(f"Risiko DM: {dmrisk}")
                st.subheader(f"Risiko TB: {tbrisk}")
                # annotated_text("Risiko Diabetes Melitus: ",("",f'{dmrisk}'))
                # annotated_text("Risiko Tuberkulosis: ",("",f'{tbrisk}'))

    with k2:
        dmrisk1 = None
        tbrisk2 = None
        c1,c2 = st.columns((1,1))
        with c1:
            with st.expander('Faktor Gaya Hidup dan Konsumsi', expanded=True):
                i13 = st.text_input(label='Konsumsi Gula',value=['Tinggi' if datapeserta['Gula_level'].values == 1 else 'Rendah'][0])
                i11 = st.text_input(label='Konsumsi Rokok',value=['Tinggi' if datapeserta['Rokok_level'].values == 1 else 'Rendah'][0])
                i12 = st.text_input(label='Konsumsi Sayur',value=['Tinggi' if datapeserta['Sayur_level'].values == 1 else 'Rendah'][0])
            
            with st.expander('Faktor Individual Peserta', expanded=True):
                i1 = st.text_input(label='Umur',value=datapeserta['Umur'].values[0])
                i4 = st.text_input(label='Kelas Peserta',value=datapeserta['Kelas'].values[0])
                i5 = st.text_input(label='Kelompok Peserta',value=datapeserta['Kelompok'].values[0])
                i3 = st.text_input(label='Status Peserta',value=datapeserta['Status'].values[0])
        with c2:
            with st.expander('Faktor Pembangunan Wilayah', expanded=True):
                i6 = st.text_input(label='Tingkat IPM',value=datapeserta['IPM'].values[0])
                i7 = st.text_input(label='Kepadatan Wilayah',value=['Tinggi' if datapeserta['Kepadatan_level'].values == 1 else 'Rendah'][0])
            with st.expander('Faktor Lingkungan', expanded=True):
                i10 = st.text_input(label='Tingkat Sanitasi Layak',value=['Tinggi' if datapeserta['Sanitasi_level'].values == 1 else 'Rendah'][0])
                i8 = st.text_input(label='Tingkat Pencemaran Air',value=['Tinggi' if datapeserta['Penc_Air_level'].values == 1 else 'Rendah'][0])
                i9 = st.text_input(label='Tingkat Pencemaran Udara',value=['Tinggi' if datapeserta['Penc_Udara_level'].values == 1 else 'Rendah'][0])
            v1 = i1
            v2 = i2
            v3 = i3
            v4 = i4
            v5 = i5
            v6 = i6
            v7 = [1 if i7 =='Tinggi' else 0][0]
            v8 = [1 if i8 =='Tinggi' else 0][0]
            v9 = [1 if i9 =='Tinggi' else 0][0]
            v10 = [1 if i10 =='Tinggi' else 0][0]
            v11 = [1 if i11 =='Tinggi' else 0][0]
            v12 = [1 if i12 =='Tinggi' else 0][0]
            v13 = [1 if i13 =='Tinggi' else 0][0]
            clm = ['Umur','JK','Status','Kelas','Kelompok','IPM','Kepadatan_level','Penc_Air_level','Penc_Udara_level','Sanitasi_level','Rokok_level','Sayur_level','Gula_level']
            dftest =  pd.DataFrame([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13]],columns=clm)
            
            with st.expander('Update Prediksi Risiko DM dan TB', expanded=True):
                # if st.button('Jalankan'):
                # sideform = st.form("my_form")
                # submitted = sideform.form_submit_button("Jalankan Ulang Prediksi")
                # if submitted:
                if st.button("Jalankan Ulang Prediksi"):
                    model = joblib.load('dmmodel.sav')
                    result = model.predict_proba(dftest)
                    dfresult = pd.DataFrame(result,columns=['non_pred','dm_pred'])
                    dfrisk1 = assignRisk(dfresult,'dm_pred','dm_risk')
                    # dfrisk1 = assignRisk(dfrisk1,'tb_pred','tb_risk')
                    dmrisk1 = dfrisk1['dm_risk'].values[0]
                    # tbrisk1 = dfresult['tb_risk'].values[0]
                    # nonrisk1 = dfresult['non_pred'].values[0]
                    # from annotated_text import annotated_text

                    model2 = joblib.load('tbmodel.sav')
                    result2 = model2.predict_proba(dftest)
                    dfresult2 = pd.DataFrame(result2,columns=['non_pred','tb_pred'])
                    dfrisk2 = assignRisk(dfresult2,'tb_pred','tb_risk')
                    # dfrisk1 = assignRisk(dfrisk1,'tb_pred','tb_risk')
                    # dmrisk2 = dfresult2['tb_pred'].values[0]
                    tbrisk2 = dfrisk2['tb_risk'].values[0]
                    # nonrisk2 = dfresult2['non_pred'].values[0]

                    # annotated_text("Risiko Diabetes Melitus: ",("",f'{dmrisk1}'))
                    # annotated_text("Risiko Tuberkulosis: ",("",f'{tbrisk2}'))
                    st.subheader(f"Risiko DM: {dmrisk1}")
                    st.subheader(f"Risiko TB: {tbrisk2}")
                    # st.write(f"Risiko Diabetes Militus: {dmrisk1}")
                    # st.write(f"Risiko Tuberkulosis: {tbrisk1}")
    t1,t2 = st.columns((1,1))  
    with t1:  
        with st.expander('Penanganan Diabetes Melitus', expanded=True):
            if dmrisk1 != None:
                st.image(f'dm_{dmrisk1}.png')
            else:
                st.image(f'dm_{dmrisk}.png')
    with t2:
        with st.expander('Penanganan Tuberkulosis', expanded=True):
            if tbrisk2 != None:
                st.image(f'tb_{tbrisk2}.png')
            else:
                st.image(f'tb_{tbrisk}.png')

import streamlit as st
st.set_page_config(page_title="GRIP", page_icon=None, layout="wide", initial_sidebar_state="auto",menu_items=None)
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

st.sidebar.image('grip.png')
st.sidebar.title("GEOSPATIAL RISK PREDICTION \
                 FOR DM & TB")
menu = ["Monitoring","Geospatial Factors","Early Risk Detection","Risk Prediction","Treatment & Help"]
choice = st.sidebar.selectbox("Select Menu", menu)

@st.cache_data
def getData(url,sep):
    df = pd.read_csv(url,sep=sep)
    return df

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
            st.subheader('Prediksi: Berisiko Diabetes Militus')
        elif prediction == 2:
            st.subheader('Prediksi: Berisiko Tuberkolosis')
        elif prediction == 0:
            st.subheader('Prediksi: Risiko Diabetes Militus & Tuberkolosis Rendah')
elif choice == "Monitoring":
    # st.subheader('Dashboard')
    import streamlit.components.v1 as components
    components.html('''
        <div class='tableauPlaceholder' id='viz1693410447726' style='position: relative'><noscript><a href='#'><img alt='Dashboard Monitoring DM dan TB ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;bp&#47;bpjs_2023&#47;DashboardMonitoringDMdanTB&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='bpjs_2023&#47;DashboardMonitoringDMdanTB' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;bp&#47;bpjs_2023&#47;DashboardMonitoringDMdanTB&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1693410447726');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1677px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        ''',width=1280,height=950)
    
elif choice == "Geospatial Factors":
    # st.subheader('Dashboard')
    c1,c2 = st.columns((2,1))
    with c1:
        import streamlit.components.v1 as components
        components.html(
        '''<div class='tableauPlaceholder' id='viz1693288229970' style='position: relative'><noscript><a href='#'><img alt='Peta Risiko DM dan TB  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pe&#47;PetaRisikoDMdanTB&#47;PetaRisikoDMdanTB_1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PetaRisikoDMdanTB&#47;PetaRisikoDMdanTB_1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pe&#47;PetaRisikoDMdanTB&#47;PetaRisikoDMdanTB_1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1693288229970');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='800px';vizElement.style.height='627px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='800px';vizElement.style.height='627px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>'''
        ,width=1280,height=720)
    with c2:
        st.subheader('Analisis Regresi')
        st.write('Faktor-faktor lingkungan dan Gaya hidup berdasarkan lokasi peserta terbukti berpengaruh terhadap tingkat prevelansi risiko DM dan TB')
        st.image('dmfactors.png')
        st.image('tbfactors.png')

elif choice == "Early Risk Detection":
    genre = st.sidebar.radio("Risk Level",('Cities', 'Individuals'))
    if genre == 'Cities':
        import streamlit.components.v1 as components
        components.html(
        '''
        <div class='tableauPlaceholder' id='viz1693420731003' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;bp&#47;bpjs_grip&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='bpjs_grip&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;bp&#47;bpjs_grip&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1693420731003');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='977px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        '''
        ,width=1600,height=900)
    else:
        st.subheader('Prediksi Risiko Peserta Berdasarkan Karakteristik Individu, Faktor Lingkungan dan Gaya Hidup')
        df = getData('sample_peserta.csv',';')
        peserta = df['PSTV01'].tolist()
        st.subheader('Pencarian Peserta Berdasarkan ID Peserta')
        formation = ["442","343","433"]
        selectForm = st.selectbox("Pilih Peserta", peserta[:100])
        datapeserta = df[df['PSTV01'].isin([selectForm])]
        k1,k2,k3 = st.columns((1,2,2))
        ops = ['Rendah','Tinggi']
        ops_dict = {'Rendah':0,'Tinggi':1}
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
                # st.subheader(f"Prevalensi TB: {int(datapeserta['tb_pred'].values[0]*100)/1000}")
            # fig0 = go.Figure()
            # lum = 0.0002
            # fig0.add_trace(go.Indicator(
            #                 mode = "number+delta",
            #                 # value = status*100,
            #                 value = int(datapeserta['dm_pred'].values[0]*100000)/100000,
            #                 title = {"text": "Prediksi Risiko DM"},
            #                 delta = {'reference': 0.5, 'relative': False},
            #                 domain = {'row': 0, 'column': 0},
            #                 ))
            # fig0.add_trace(go.Indicator(
            #                 mode = "number+delta",
            #                 # value = status*100,
            #                 value = int(datapeserta['tb_pred'].values[0]*100000)/100000,
            #                 title = {"text": "Prediksi Risiko TB"},
            #                 delta = {'reference': 0.5, 'relative': False},
            #                 domain = {'row': 0, 'column': 1},
            #                 ))
            # fig0.update_layout(grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
            #                     # autosize=True,)
            #                     # width=300,
            #                     # height=100,)
            # st.plotly_chart(fig0,use_container_width=True)
        with k2:
            with st.expander('Faktor Gaya Hidup dan Konsumsi', expanded=True):
                i13 = st.text_input(label='Konsumsi Gula',value=['Tinggi' if datapeserta['Gula_level'].values == 1 else 'Rendah'][0])
                i11 = st.text_input(label='Konsumsi Rokok',value=['Tinggi' if datapeserta['Rokok_level'].values == 1 else 'Rendah'][0])
                i12 = st.text_input(label='Konsumsi Sayur',value=['Tinggi' if datapeserta['Sayur_level'].values == 1 else 'Rendah'][0])
            
            with st.expander('Faktor Individual Peserta', expanded=True):
                i1 = st.text_input(label='Umur',value=datapeserta['Umur'].values[0])
                i4 = st.text_input(label='Kelas Peserta',value=datapeserta['Kelas'].values[0])
                i5 = st.text_input(label='Kelompok Peserta',value=datapeserta['Kelompok'].values[0])
                i3 = st.text_input(label='Status Peserta',value=datapeserta['Status'].values[0])
        with k3:
            with st.expander('Faktor Lingkungan dan Pembangunan', expanded=True):
                i6 = st.text_input(label='Tingkat IPM',value=datapeserta['IPM'].values[0])
                i10 = st.text_input(label='Tingkat Sanitasi Layak',value=['Tinggi' if datapeserta['Sanitasi_level'].values == 1 else 'Rendah'][0])
                i7 = st.text_input(label='Kepadatan Wilayah',value=['Tinggi' if datapeserta['Kepadatan_level'].values == 1 else 'Rendah'][0])
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
            import numpy as np
            def assignRisk(df,pcol,rcol):
                conditions = [
                    (df[pcol] <0.6),
                    (df[pcol] <0.9),
                    (df[pcol] >=0.9)
                    ]
                choices = ['Low','Moderate','High']

                df[rcol] = np.select(conditions, choices, default='Low')
                return df
            clm = ['Umur','JK','Status','Kelas','Kelompok','IPM','Kepadatan_level','Penc_Air_level','Penc_Udara_level','Sanitasi_level','Rokok_level','Sayur_level','Gula_level']
            dftest =  pd.DataFrame([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13]],columns=clm)
            
            with st.expander('Jalankan Ulang Prediksi Risiko DM dan TB', expanded=True):
                if st.button('Jalankan'):
                    model = joblib.load('dmtbmodel.sav')
                    result = model.predict_proba(dftest)
                    dfresult = pd.DataFrame(result,columns=['dm_pred','tb_pred'])
                    dfrisk = assignRisk(dfresult,'dm_pred','dm_risk')
                    dfrisk = assignRisk(dfrisk,'tb_pred','tb_risk')
                    dmrisk = dfrisk['dm_risk'].values[0]
                    tbrisk = dfrisk['tb_risk'].values[0]
                else: 
                    dmrisk = datapeserta['dm_risk'].values[0]
                    tbrisk = datapeserta['tb_risk'].values[0]

                st.subheader(f"Risiko DM: {dmrisk}")
                # st.subheader(f"Prevalensi DM: {int(datapeserta['dm_pred'].values[0]*100)/1000}")
                st.subheader(f"Risiko TB: {tbrisk}")
        # input vars
        

        # st.table(dftest)

elif choice=="Risk Prediction":
    with st.expander('Environment & Lifestyle Factors', expanded=True):
            c1,c2,c3= st.columns((1,1,1))
            with c1:
                # bv = dfc.iloc[0,1:15].astype('float').tolist()
                st.text_input(label='s1'+" (%)",value=int(10000)/100)
                st.text_input(label='s2'+" (%)",value=int(10000)/100)
            with c2:
                #min value
                v1min = st.number_input(label="PelayananUmum min(%)",value=50.0,min_value=0.0, max_value=100.0, step=1.0)
                v2min = st.number_input(label="Pendidikan min(%)",value=20.0,min_value=0.0, max_value=100.0, step=1.0)
            with c3:
                #max value
                v1max = st.number_input(label="PelayananUmum max (%)",value=60.0,min_value=0.0, max_value=100.0, step=1.0)
                v2max = st.number_input(label="Pendidikan max (%)",value=80.0,min_value=0.0, max_value=100.0, step=1.0)

    with st.expander('Individual Factors', expanded=True):
            c1,c2,c3= st.columns((1,1,1))
            with c1:
                # bv = dfc.iloc[0,1:15].astype('float').tolist()
                st.text_input(label='s3'+" (%)",value=int(10000)/100)
                st.text_input(label='s4'+" (%)",value=int(10000)/100)
            with c2:
                #min value
                v1min = st.number_input(label="s5",value=50.0,min_value=0.0, max_value=100.0, step=1.0)
                v2min = st.number_input(label="s6",value=20.0,min_value=0.0, max_value=100.0, step=1.0)
            with c3:
                #max value
                v1max = st.number_input(label="s7",value=60.0,min_value=0.0, max_value=100.0, step=1.0)
                v2max = st.number_input(label="s8",value=80.0,min_value=0.0, max_value=100.0, step=1.0)

        # Solve the problem
    st.write("Penghitungan Alokasi Anggaran Paling Efisien")
    if st.button("Klik untuk Jalankan"):
        st.write("Sukses")

elif choice == "Treatment & Help":
    st.write("")
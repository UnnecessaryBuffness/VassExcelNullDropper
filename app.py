import numpy as np
import pandas as pd
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
import streamlit as st


st.title('Vass's Excel Null Dropper')
#st.markdown("_Let's get educated brother_")
st.markdown("_Drops entirely blank columns from Excel files_")

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data         

uploaded_file = st.file_uploader(“Choose a file”,type=['xlsx'],accept_multiple_files=False)
if uploaded_file is not None:
  #read excel
  df=pd.read_excel(uploaded_file)


df_xlsx = to_excel(df)
st.download_button(label='📥 Download ',
                                data=df_xlsx ,
                                file_name= f'{uploaded_file.name}')




st.markdown('___')
st.markdown('Created by [Ben Davis](https://github.com/BenDavis71/)')

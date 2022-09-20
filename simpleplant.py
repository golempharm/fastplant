import streamlit as st
from pymed import PubMed
import pandas as pd

st.title('GoLem Pharm')
st.write('')

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a number of abstracts ',
    0, 10000, 1000, 1)

add_slider2 = st.sidebar.slider(
    'Select a number of plants ',
    0, 200000, 10000, 1)

#input box
int_put = st.text_input('Ask about your disease here:')

if int_put:
 with st.spinner('Please wait...'):

  text = int_put
  max1 =int(add_slider)  # ilosc zapytan ze slidera abstracts
  maxplant = int(add_slider2) # ilosc zapytan ze slidera plants

  #wporwadzenie zapytania do pubmed
  pubmed = PubMed(tool="MyTool", email="p.karabowicz@gmail.com")
  results1 = pubmed.query(text, max_results=max1)
  lista_abstract_3=[]
  for i in results1:
    lista_abstract_3.append(i.abstract)

  df_abstract = pd.DataFrame(lista_abstract_3, columns = ['abstracts'])
  df_abstract['abstracts_lower'] = df_abstract['abstracts'].str.lower()
  df_abstract_1 = df_abstract.dropna()

  Not_none_values = filter(None.__ne__, lista_abstract_3)
  list_of_values = list(Not_none_values)
  list_of_values = ' '.join(list_of_values)
  text1 = str(list_of_values)
  text1 = text1.lower()

  df1 = pd.read_csv('./plants3.csv')
  df2 = pd.read_csv('./plants4.csv')
  df_drug = pd.concat([df1, df2], axis=0)
  df_drug = df_drug.drop_duplicates('scientificName')
  list_drug = set(list(df_drug['scientificName']))
  list_drug = list(list_drug)
  list_drug_lower = [x.lower() for x in list_drug]

  co = []
  na = []
  for w in list_drug_lower[0:maxplant]:
   co.append(int(text1.count(w)))
   na.append(w)

  df = pd.DataFrame(list(zip(na, co)), columns =['Plant name', 'value'])
  df1 = df[df['value']>0].reset_index(drop=True)
  st.write('your results for request: ', int_put)
 df1

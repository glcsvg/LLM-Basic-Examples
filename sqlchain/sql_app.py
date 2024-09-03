#streamlit run sql_app.py --server.fileWatcherType none
import streamlit as st
from sqldatabase import DatabaseClass
from sqlalchemy import create_engine, MetaData,  Table, select
import pandas as pd

db_con = DatabaseClass()

table = db_con.get_table()

##sonra
query =  select(table).where(table.c.artists == 'Ben Woodward')


result = db_con.db_execute(query)
# Sonuçları yazdırmak
res = []
for row in result:
    res.append(row)


df = pd.DataFrame(res)


st.title("Streamlit Tutorial App")
button1 = st.button("Click Me")
if button1:
    #st.write(df, width=1000)
    st.markdown(
        f"""
        <style>
        .dataframe {{ width: 80%; }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.dataframe(df)










# text = speech_to_text(
#     language='tr',
#     start_prompt="Start recording",
#     stop_prompt="Stop recording",
#     just_once=False,
#     use_container_width=False,
#     callback=None,
#     args=(),
#     kwargs={},
#     key=None
# )



# st.write(text)


# def callback():
#     if st.session_state.my_stt_output:
#         st.write(st.session_state.my_stt_output)


# r = speech_to_text(key='my_stt', callback=callback)
#st.write(r)

# button1 = st.button("Click Me")
# if button1:
#     text = load_text("xx.txt")
#     st.write(text)

# uploaded_file = st.file_uploader("Bir dosya seçin", type=['txt'])
# if uploaded_file is not None:
#     # # Dosya bilgilerini göster
#     # st.write("Dosya Adı: ", uploaded_file.name)
#     # st.write("Dosya Tipi: ", uploaded_file.type)
#     # st.write("Dosya Boyutu: ", uploaded_file.size, "bytes")

#     if uploaded_file.type == "text/plain":
#         content = uploaded_file.read().decode("utf-8")
#         #st.text_area(" ",content, height=300)

# sumbutton = st.button("Summarize")
# if sumbutton:
#     response = generate_summary(content)
#     st.text_area(" ",response,height=300)
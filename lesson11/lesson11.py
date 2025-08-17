# 當輸出df變數時,st.write()會自動執行
"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import datasource


st.sidebar.title("台鐵車站資訊")
st.sidebar.header("2023年各站進出站人口數")
st.subheader("進出站人數顯示區")


@st.cache_resource #增加效能，選取車站可以減少消耗搜尋資料庫時間
def get_stations():
    """取得車站資料"""
    return datasource.get_stations_names()

stations = get_stations()
station = st.sidebar.selectbox(
    "請選擇車站",
    stations,
)

st.write("你選擇的車站:", station)

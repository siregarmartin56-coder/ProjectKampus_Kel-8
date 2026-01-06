import streamlit as st
from datetime import date, datetime
import time
import uuid

# ================== KONFIGURASI HALAMAN ==================
st.set_page_config(
    page_title="Sistem Pengembalian Alat Praktikum",
    layout="centered"
)

# ================== STYLE ==================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ff758c, #ff7eb3);
}
h1, h2, h3 {
    color: white;
    text-align: center;
}
label {
    color: white !important;
    font-weight: bold;
}
.card {
    background-color: rgba(255,255,255,0.18);
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 20px;
}
.stButton > button

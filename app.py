import streamlit as st
import pandas as pd
from datetime import date

# ================= KONFIGURASI AWAL =================
st.set_page_config(
    page_title="Sistem Peminjaman Alat Lab",
    page_icon="🔬",
    layout="wide"
)

# ================= LOAD DATA =================
alat = pd.read_csv("data/alat.csv")
peminjaman = pd.read_csv("data/peminjaman.csv")

# ================= HEADER / PEMBUKAAN =================
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: gray;
}
.card {
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #ddd;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🔬 Sistem Peminjaman Alat Laboratorium</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Aplikasi Peminjaman Alat Praktikum Berbasis Web</div>', unsafe_allow_html=True)

st.markdown("---")

# ================= SIDEBAR =================
st.sidebar.title("📌 Menu")

role = st.sidebar.radio("Login sebagai:", ["User", "Admin"])

# Login admin sederhana
if role == "Admin":
    password = st.sidebar.text_input("Password Admin", type="password")
    if password != "admin123":
        st.sidebar.warning("Password salah")
        st.stop()

menu = st.sidebar.selectbox(
    "Navigasi",
    ["🏠 Beranda", "📦 Daftar Alat", "📝 Pinjam Alat", "📊 Data Peminjaman"]
)

# ================= BERANDA =================
if menu == "🏠 Beranda":
    st.subheader("👋 Selamat Datang")

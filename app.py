import streamlit as st
import pandas as pd
from datetime import date

# ================== KONFIGURASI HALAMAN ==================
st.set_page_config(
    page_title="Sistem Peminjaman Alat Laboratorium",
    layout="centered"
)

# ================== INISIALISASI DATA ==================
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "Nama Peminjam", "NIM/NIP", "Unit",
        "Nama Alat", "Jumlah",
        "Tanggal Pinjam", "Tanggal Kembali",
        "Status"
    ])

# ================== HEADER ==================
st.title("Sistem Peminjaman Alat Laboratorium")
st.caption("Aplikasi berbasis Python (Streamlit) untuk pengelolaan peminjaman alat")

# ================== FORM PEMINJAMAN ==================
st.subheader("Form Peminjaman Alat")

with st.form("form_peminjaman"):
    nama = st.text_input("Nama Peminjam")
    nim = st.text_input("NIM / NIP")
    unit = st.text_input("Program Studi / Unit")
    alat = st.text_input("Nama Alat")
    jumlah = st.number_input("Jumlah", min_value=1, step=1)
    tgl_pinjam = st.date_input("Tanggal Pinjam", value=date.today())
    tgl_kembali = st.date_input("Tanggal Kembali")
    submit = st.form_submit_button("Ajukan Peminjaman")

if submit:
    if not all([nama, nim, unit, alat]):
        st.error("Semua field wajib diisi.")
    elif tgl_kembali < tgl_pinjam:
        st.error("Tanggal kembali tidak boleh lebih awal dari tanggal pinjam.")
    else:
        new_row = {
            "Nama Peminjam": nama,
            "NIM/NIP": nim,
            "Unit": unit,
            "Nama Alat": alat,
            "Jumlah": jumlah,
            "Tanggal Pinjam": tgl_pinjam,
            "Tanggal Kembali": tgl_kembali,
            "Status": "Menunggu"
        }
        st.session_state.data = pd.concat([
            st.session_state.data,
            pd.DataFrame([new_row])
        ], ignore_index=True)
        st.success("Pengajuan peminjaman berhasil disimpan.")

# ================== TABEL DATA ==================
st.subheader("Daftar Peminjaman")
st.dataframe(st.session_state.data, use_container_width=True)

# ================== PANEL ADMIN SEDERHANA ==================
st.subheader("Panel Admin (Simulasi)")

if not st.session_state.data.empty:
    index = st.selectbox(
        "Pilih data untuk diubah statusnya",
        st.session_state.data.index
    )
    status_baru = st.selectbox(
        "Ubah Status",
        ["Menunggu", "Disetujui", "Ditolak", "Dikembalikan"]
    )
    if st.button("Simpan Status"):
        st.session_state.data.loc[index, "Status"] = status_baru
        st.success("Status berhasil diperbarui.")

# ================== FOOTER ==================
st.markdown("---")
st.caption("© 2026 Sistem Peminjaman Laboratorium | Dibangun dengan Python & Streamlit")

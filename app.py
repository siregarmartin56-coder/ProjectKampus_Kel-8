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
.stButton > button {
    background-color: white;
    color: #ff758c;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ================== SESSION STATE ==================
if "step" not in st.session_state:
    st.session_state.step = 1

if "data" not in st.session_state:
    st.session_state.data = {}

# ================== DATA ==================
alat_list = [
    "Pipet tetes",
    "Gelas beaker",
    "Gelas ukur",
    "Labu takar",
    "Cawan petri",
    "Buret",
    "Kasa asbes",
    "Bunsen",
    "Tabung reaksi",
    "Corong kaca",
    "Penjepit kayu",
    "Batang pengaduk",
    "Kaki tiga"
]

mata_kuliah_list = [
    "Kimia Dasar",
    "Kimia Analitik",
    "Kimia Organik",
    "Biokimia",
    "Praktikum Farmasi",
    "Lainnya"
]

# ================== PROGRESS ==================
st.progress(st.session_state.step / 4)

# ================== STEP 1 ==================
if st.session_state.step == 1:
    st.title("Form Peminjaman Alat Praktikum")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    nama = st.text_input("Nama Lengkap")
    kelompok = st.text_input("Kelompok")
    tanggal = st.date_input("Tanggal Praktikum", value=date.today())
    judul = st.text_input("Judul Praktikum")
    matkul = st.selectbox("Mata Kuliah", mata_kuliah_list)

    st.subheader("Alat yang Digunakan")
    alat_dipilih = {}

    for alat in alat_list:
        col1, col2 = st.columns([3, 1])
        with col1:
            pilih = st.checkbox(alat)
        with col2:
            jumlah = st.number_input(
                "Jumlah",
                min_value=1,
                step=1,
                key=f"jml_{alat}",
                disabled=not pilih
            )
        if pilih:
            alat_dipilih[alat] = jumlah

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Lanjutkan"):
        if not nama or not kelompok or not judul or not alat_dipilih:
            st.warning("Semua data wajib diisi.")
        elif tanggal > date.today():
            st.warning("Tanggal tidak boleh di masa depan.")
        else:
            st.session_state.data = {
                "id": str(uuid.uuid4())[:8].upper(),
                "nama": nama,
                "kelompok": kelompok,
                "tanggal": tanggal,
                "judul": judul,
                "matkul": matkul,
                "alat": alat_dipilih,
                "waktu": datetime.now().strftime("%d-%m-%Y %H:%M")
            }
            st.session_state.step = 2
            st.rerun()

# ================== STEP 2 ==================
elif st.session_state.step == 2:
    st.title("Konfirmasi Data Peminjaman")

    d = st.session_state.data
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write(f"**ID Peminjaman:** {d['id']}")
    st.write(f"**Nama:** {d['nama']}")
    st.write(f"**Kelompok:** {d['kelompok']}")
    st.write(f"**Mata Kuliah:** {d['matkul']}")
    st.write(f"**Judul Praktikum:** {d['judul']}")
    st.write(f"**Tanggal:** {d['tanggal']}")

    st.subheader("Daftar Alat:")
    for alat, jml in d["alat"].items():
        st.write(f"- {alat} ({jml} unit)")

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Lanjutkan ke Pengembalian"):
        st.session_state.step = 3
        st.rerun()

# ================== STEP 3 ==================
elif st.session_state.step == 3:
    st.title("Dokumentasi Pengembalian Alat")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    foto = st.file_uploader(
        "Upload foto alat setelah dikembalikan",
        type=["jpg", "jpeg", "png"]
    )

    if foto:
        st.image(foto, use_container_width=True)
        st.caption(f"Nama file: {foto.name}")

        if st.button("Konfirmasi Pengembalian"):
            st.session_state.step = 4
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ================== STEP 4 ==================
elif st.session_state.step == 4:
    st.title("Pengembalian Berhasil")

    with st.spinner("Memverifikasi data..."):
        time.sleep(2)

    st.success("Pengembalian alat telah diverifikasi.")
    st.write("Silakan simpan ID peminjaman sebagai bukti.")

    if st.button("Input Peminjaman Baru"):
        st.session_state.clear()
        st.rerun()

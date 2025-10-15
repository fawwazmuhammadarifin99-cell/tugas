import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Energi Keadilan: Kasus Impor BBM", page_icon="⛽", layout="centered")

# ---------------- STYLE ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #f8fafc, #e0f2fe);
    color: #1e293b;
    font-family: 'Poppins', sans-serif;
}
h1, h2 {
    text-align: center;
    color: #2563eb;
}
.choice {
    background-color: #f1f5f9;
    border-radius: 12px;
    padding: 12px;
    text-align: center;
    font-weight: 600;
    margin: 8px 0;
    transition: 0.3s;
}
.choice:hover {
    background-color: #3b82f6;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- STATE ----------------
if "scene" not in st.session_state:
    st.session_state.scene = "intro"
    st.session_state.log = []

def goto(scene, note=""):
    st.session_state.scene = scene
    st.session_state.log.append(note)

# ---------------- HEADER ----------------
# ---------------- HEADER ----------------
st.markdown("""
<h1 style='text-align:center; color:#2563eb; font-weight:800;'>
⚖️ Energi Keadilan
</h1>
<p style='text-align:center; color:#334155; font-size:18px;'>
Kasus Impor Shell & Vivo melalui Pertamina – Kuota 110%, E10, dan Keadilan Pasar
</p>
<p style='text-align:center; color:#1e293b; font-size:20px; font-weight:700; margin-top:8px;'>
Fawwaz Muhammad Arifin - 8G
</p>
""", unsafe_allow_html=True)
st.divider()

# ---------------- GLOSARIUM (baru) ----------------
with st.expander("Apa itu E10 dan Certificate of Origin (CO)?"):
    st.markdown(
        """
**E10**  
- Bensin yang dicampur **etanol hingga 10%**. Di kasus ini yang beredar sekitar **3,5% etanol**.  
- Tujuan: menaikkan angka oktan, menurunkan emisi, dan memperluas sumber bahan bakar.  
- Dampak teknis: umumnya **aman untuk kendaraan modern**; perlu **SOP penyimpanan** karena etanol higroskopis (mudah menarik air).  

**Certificate of Origin (CO)**  
- **Dokumen resmi** yang menyatakan **asal negara barang** (diterbitkan otoritas/instansi berwenang di negara asal).  
- Fungsi: keperluan **bea cukai**, validasi **perjanjian dagang**, dan **kepatuhan regulasi**.  
- Tanpa CO: berisiko **penundaan impor, sanksi**, atau penolakan barang.  

**Relevansi pada kasus ini**  
- **E10 3,5%** boleh dipakai jika memenuhi **spesifikasi RON & emisi** dan SOP penanganannya jelas.  
- **CO wajib** untuk memastikan asal pasokan legal dan transparan saat impor via Pertamina/Patra Niaga.
        """
    )

# ---------------- SCENES ----------------
if st.session_state.scene == "intro":
    st.write("""
    Tahun 2025, beberapa SPBU seperti **Shell dan Vivo** mengalami kekurangan BBM.  
    Pemerintah mengizinkan mereka **impor bensin melalui Pertamina (Patra Niaga)** agar stok tidak habis.  
    Kamu sebagai **manajer pasokan BBM** diminta menentukan langkah cepat namun tetap adil dan sesuai aturan.
    """)
    if st.button("🛢️ Segera impor melalui Pertamina supaya stok aman"):
        goto("via_pertamina")
    if st.button("📑 Cek dulu dokumen dan kualitas bensin sebelum impor"):
        goto("cek_dokumen")

elif st.session_state.scene == "via_pertamina":
    st.write("""
    Kamu memutuskan memakai pasokan dari Pertamina.  
    Namun bensin yang ditawarkan mengandung **etanol 3,5% (E10)** dan **dokumen asal (CO)** belum lengkap.  
    Beberapa media mulai mempertanyakan transparansi dan kualitas.
    """)
    if st.button("🧾 Jelaskan ke publik bahwa etanol aman dan CO sedang dilengkapi"):
        goto("transparan")
    if st.button("🤐 Diam saja supaya masalah tidak makin besar"):
        goto("tutup_info")

elif st.session_state.scene == "cek_dokumen":
    st.write("""
    Setelah diperiksa, bensin E10 sebenarnya aman, tapi memang belum semua dokumen CO selesai.  
    Sementara itu, banyak SPBU hampir kehabisan stok.
    """)
    if st.button("✅ Izinkan impor tapi dengan syarat dokumen dilengkapi setelahnya"):
        goto("transparan")
    if st.button("🚫 Tolak dulu sampai semua dokumen lengkap"):
        goto("krisis")

elif st.session_state.scene == "transparan":
    st.success("Kamu memilih jalan tengah yang adil dan transparan.")
    st.write("""
    Kamu menjelaskan ke masyarakat bahwa bensin E10 aman dan dokumen CO sedang diselesaikan.  
    Regulator (ESDM) mendukung langkahmu karena tetap patuh, publik tenang, dan stok kembali normal.
    """)
    st.write("### Nilai Pancasila yang tercermin:")
    st.write("- **Sila 2:** Kemanusiaan yang adil dan beradab (jujur, terbuka, tidak menyesatkan masyarakat)  \n"
             "- **Sila 4:** Musyawarah dan tanggung jawab dalam membuat kebijakan publik  \n"
             "- **Sila 5:** Keadilan sosial bagi seluruh rakyat Indonesia (harga dan pasokan BBM stabil)")
    st.write("### Dampak jika kasus seperti ini terjadi:")
    st.info("""
    Jika impor BBM dilakukan tanpa transparansi dan kepatuhan, dampaknya besar:
    - Harga BBM bisa tidak adil antar SPBU.  
    - Muncul kecurigaan publik terhadap pemerintah.  
    - Potensi kerugian negara dan rusaknya kepercayaan konsumen.  
    Dengan langkah transparan seperti yang kamu pilih, keadilan sosial tetap terjaga.
    """)
    st.markdown("👉 **Poster Kasus Impor BBM melalui Pertamina 2025:** [Link Canva Poster](https://www.canva.com/design/DAG11CwV9Kg/AVvhty1eCf9LEqUoHuo1Bg/edit?utm_content=DAG11CwV9Kg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)")
    if st.button("🔁 Main Lagi"):
        st.session_state.scene = "intro"
        st.session_state.log = []

elif st.session_state.scene == "tutup_info":
    st.error("Kamu memilih diam dan tidak memberikan penjelasan.")
    st.write("""
    Akibatnya, masyarakat panik karena takut harga naik dan kualitas menurun.  
    Berita simpang siur muncul di media sosial, dan kepercayaan publik terhadap perusahaan turun.
    """)
    st.write("### Dampak nyata jika hal ini terjadi:")
    st.warning("""
    - Masyarakat kehilangan kepercayaan pada lembaga energi.  
    - Potensi boikot dan keresahan sosial meningkat.  
    - Prinsip keadilan dan keterbukaan dalam Pancasila dilanggar.
    """)
    st.markdown("👉 **Upload Canva hasil karyamu:** [Canva Link](https://www.canva.com/)")
    if st.button("🔁 Main Lagi"):
        st.session_state.scene = "intro"
        st.session_state.log = []

elif st.session_state.scene == "krisis":
    st.error("Krisis BBM!")
    st.write("""
    Karena kamu menolak impor sampai semua dokumen lengkap, SPBU kosong selama beberapa hari.  
    Banyak warga kesulitan membeli bensin untuk bekerja dan distribusi barang pun terganggu.
    """)
    st.write("### Dampak jika kasus seperti ini benar-benar terjadi:")
    st.warning("""
    - Aktivitas ekonomi melambat karena pasokan energi terganggu.  
    - Pendapatan masyarakat turun, harga barang naik.  
    - Pemerintah dianggap lamban dan tidak tanggap.
    """)
    st.markdown("👉 **Upload Canva tugasmu di sini:** [Canva Link](https://www.canva.com/)")
    if st.button("🔁 Main Lagi"):
        st.session_state.scene = "intro"
        st.session_state.log = []

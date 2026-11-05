import streamlit as st
import pandas as pd

st.set_config = st.set_page_config(page_title="Kalkulator BMI", page_icon="⚖️", layout="centered")
st.title("⚖️ Kalkulator BMI (Body Mass Index)")
st.write("Hitung indeks massa tubuh Anda secara akurat berdasarkan rentang usia dan gender.")

st.divider()

jk = st.radio("Jenis Kelamin:", ["Laki-laki 👨", "Perempuan 👩"], index=None, horizontal=True)

kolom1, kolom2, kolom3 = st.columns(3)
with kolom1:
    usia = st.number_input("Usia (Tahun):", min_value=1, max_value=120, value=None, step=1)
with kolom2:
    berat = st.number_input("Berat Badan (kg):", min_value=1, max_value=300, value=None, step=1)
with kolom3:
    tinggi_cm = st.number_input("Tinggi Badan (cm):", min_value=50, max_value=250, value=None, step=1)

st.divider()

if st.button("Hitung BMI Saya 🚀", type="primary"):
    if jk is None or usia is None or berat is None or tinggi_cm is None:
        st.error("⚠️ Silakan lengkapi semua data Anda terlebih dahulu.")
    else:
        tinggi_m = tinggi_cm / 100
        bmi = berat / (tinggi_m ** 2)
        
        st.write("")
        st.markdown("<h3 style='text-align: center;'>Hasil Analisis</h3>", unsafe_allow_html=True)
        
        st.markdown(
            f"""
            <div style="text-align: center;">
                <p style="font-size: 16px; color: gray; margin-bottom: 0px;">Skor BMI Anda</p>
                <h1 style="font-size: 64px; font-weight: bold; margin-top: 0px; margin-bottom: 20px;">{bmi:.2f}</h1>
            </div>
            """, 
            unsafe_allow_html=True
        )

        sapaan = f"Berdasarkan data Anda (Usia {usia} tahun),"

        if usia <= 20:
            st.info(f"👦👧 **Kategori Anak & Remaja (Usia {usia} Tahun)**")
            st.write(
                "Untuk anak-anak dan remaja, nilai BMI murni tidak bisa menjadi acuan tunggal. "
                "Penilaian harus disesuaikan dengan grafik **Persentil Pertumbuhan CDC/WHO** berdasarkan usia bulan dan jenis kelamin."
            )
            
            if bmi < 15.0:
                st.warning("⚠️ Berdasarkan estimasi grafik pertumbuhan, anak kemungkinan berada di kategori **Kurus (Underweight)**.")
                st.info("💡 **Tips:** Pastikan anak mendapatkan asupan kalori dan protein yang cukup untuk mendukung fase pertumbuhan aktifnya [fitness-and-nutrition].")
            elif 15.0 <= bmi < 22.0:
                st.success("✅ Berdasarkan estimasi grafik pertumbuhan, anak berada di kategori **Normal / Ideal**.")
                st.info("💡 **Tips:** Pertahankan pola makan gizi seimbang dan dukung anak untuk aktif bergerak minimal 60 menit sehari.")
            elif 22.0 <= bmi < 25.0:
                st.warning("⚠️ Berdasarkan estimasi grafik pertumbuhan, anak berada di kategori **Kelebihan Berat Badan (Overweight)**.")
                st.info("💡 **Tips:** Batasi konsumsi minuman manis serta makanan siap saji, dan ajak anak melakukan aktivitas fisik yang menyenangkan.")
            else:
                st.error("🚨 Berdasarkan estimasi grafik pertumbuhan, anak berada di kategori **Obesitas (Obesity)**.")
                st.info("💡 **Tips:** Sangat disarankan untuk memplot hasil ini langsung ke grafik KMS atau berkonsultasi dengan dokter anak untuk program pemantauan nutrisi yang aman.")

        elif usia >= 65:
            if bmi < 22.0:
                st.warning(f"⚠️ {sapaan} Anda termasuk dalam kategori **Kurus (Underweight)**.")
                st.info("💡 **Tips:** Bagi lansia, BMI di bawah 22 berisiko terhadap kepadatan tulang. Fokuslah pada makanan padat nutrisi tinggi kalsium dan vitamin D [fitness-and-nutrition].")
            elif 22.0 <= bmi <= 27.0:
                st.success(f"✅ {sapaan} Anda termasuk dalam kategori **Normal (Ideal)**.")
                st.info("💡 **Tips:** Kerja bagus! Memiliki sedikit cadangan massa tubuh di usia senja sangat baik untuk proteksi kesehatan dan pemulihan tubuh.")
            elif 27.0 < bmi < 30.0:
                st.warning(f"⚠️ {sapaan} Anda termasuk dalam kategori **Kelebihan Berat Badan (Overweight)**.")
                st.info("💡 **Tips:** Tetap aktif bergerak dengan olahraga intensitas rendah seperti jalan kaki atau berenang untuk menjaga massa otot sendi.")
            else:
                st.error(f"🚨 {sapaan} Anda termasuk dalam kategori **Obesitas (Obesity)**.")
                st.info("💡 **Tips:** Disarankan berkonsultasi dengan dokter untuk memantau kesehatan kardiovaskular dan menjaga agar beban sendi tidak terlalu berat.")

        else:
            if jk == "Laki-laki 👨":
                if bmi < 20.0:
                    st.warning(f"⚠️ {sapaan} Anda termasuk dalam kategori **Kurus (Underweight)**.")
                    st.info("💡 **Tips:** Tingkatkan asupan kalori sehat dari karbohidrat kompleks dan protein untuk membangun massa otot secara optimal [fitness-and-nutrition].")
                elif 20.0 <= bmi < 25.0:
                    st.success(f"✅ {sapaan} Anda termasuk dalam kategori **Normal (Ideal)**.")
                    st.info("💡 **Tips:** Kondisi fisik Anda sangat baik. Pertahankan kombinasi latihan beban dan kardio serta pola tidur yang cukup.")
                elif 25.0 <= bmi < 30.0:
                    st.warning(f"⚠️ {sapaan} Anda termasuk dalam kategori **Gemuk (Overweight)**.")
                    st.info("💡 **Tips:** Mulai kurangi porsi karbohidrat sederhana (gula/tepung) dan tingkatkan intensitas olahraga mingguan Anda.")
                else:
                    st.error(f"🚨 {sapaan} Anda termasuk dalam kategori **Obesitas (Obesity)**.")
                    st.info("💡 **Tips:** Evaluasi total asupan kalori harian Anda. Sangat disarankan untuk berkonsultasi dengan ahli gizi demi defisit kalori yang aman dan terukur [fitness-and-nutrition].")
                    
            elif jk == "Perempuan 👩":
                if bmi < 19.0:
                    st.warning(f"⚠️ {sapaan} Anda termasuk dalam kategori **Kurus (Underweight)**.")
                    st.info("💡 **Tips:** Pastikan kebutuhan lemak sehat (seperti alpukat/kacang-kacangan) dan zat besi terpenuhi demi regulasi hormon yang seimbang.")
                elif 19.0 <= bmi < 24.0:
                    st.success(f"✅ {sapaan} Anda termasuk dalam kategori **Normal (Ideal)**.")
                    st.info("💡 **Tips:** Kerja bagus! Pertahankan hidrasi tubuh yang baik dan pola makan kaya serat demi menjaga kestabilan berat badan ideal ini.")
                elif 24.0 <= bmi < 30.0:
                    st.warning(f"⚠️ {sapaan} Anda termasuk dalam kategori **Gemuk (Overweight)**.")
                    st.info("💡 **Tips:** Padukan pola makan gizi seimbang porsi kecil dengan latihan ketahanan untuk membakar kelebihan cadangan lemak tubuh [fitness-and-nutrition].")
                else:
                    st.error(f"🚨 {sapaan} Anda termasuk dalam kategori **Obesitas (Obesity)**.")
                    st.info("💡 **Tips:** Utamakan program penurunan berat badan secara konsisten dan bertahap. Konsultasikan dengan dokter untuk pemeriksaan metabolisme berkala.")

        st.write("")
        with st.expander("📊 Lihat Tabel Standar Rujukan Kategori BMI"):

            data_rujukan = {
                "Status Kategori": ["Kurus (Underweight)", "Normal (Ideal)", "Gemuk (Overweight)", "Obesitas (Obesity)"],
                "Anak & Remaja (2-20 Thn)": ["< Persentil ke-5", "Persentil ke-5 s.d <85", "Persentil ke-85 s.d <95", "≥ Persentil ke-95"],
                "Dewasa Laki-laki": ["< 20.0", "20.0 - 24.9", "25.0 - 29.9", ">= 30.0"],
                "Dewasa Perempuan": ["< 19.0", "19.0 - 23.9", "24.0 - 29.9", ">= 30.0"],
                "Lansia (≥ 65 Thn)": ["< 22.0", "22.0 - 27.0", "27.1 - 29.9", ">= 30.0"]
            }

            df_rujukan = pd.DataFrame(data_rujukan)
            st.dataframe(df_rujukan, use_container_width=True, hide_index=True)
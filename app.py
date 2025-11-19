import streamlit as st
import math
import os

# ==========================================
# SAYFA AYARLARI
# ==========================================
st.set_page_config(
    page_title="İTÜ - Açık İşletme Tasarımı",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# VERİ TABANI
# ==========================================
CONNECTIONS = {
    '1': {'72': 8.0, '71': 4.9, '70': 5.8},
    '2': {'72': 6.8, '71': 6.1, '302': 11.9, '75/A': 15.5},
    '3': {'101': 4.6},
    '7': {'8': 11.4, '74/A': 6.9},
    '8': {'7': 11.4, '74/A': 6.0},
    '11': {'63': 8.5, '76': 6.6},
    '12': {'63': 14.6, '76': 5.5, '75/A': 8.9},
    '13': {},
    '16': {'80': 8.0, '78': 7.3, '303': 6.6, '77': 5.6, '62': 6.1},
    '17': {'81': 6.2, '78': 8.2, '79/A': 5.6, '18': 8.5, '80': 4.3},
    '18': {'81': 5.0, '79/A': 6.0},
    '19': {'61': 7.3, '106': 5.8},
    '61': {'19': 7.3, '106': 7.0},
    '62': {'16': 6.1, '77': 5.1},
    '63': {'11': 8.5, '76': 12.1, '12': 14.6},
    '66': {'73': 7.2, '67': 7.8, '103': 7.6, '104': 5.5},
    '67': {'102': 5.7, '103': 4.2, '66': 7.8, '73': 4.5},
    '68': {'73': 8.9, '102': 8.2},
    '70': {'1': 5.8, '71': 6.6},
    '71': {'1': 4.9, '2': 6.1, '72': 7.5, '70': 6.6},
    '72': {'302': 8.4, '2': 6.8, '71': 7.5, '1': 8.0},
    '73': {'66': 7.2, '67': 4.5, '68': 5.4},
    '74/A': {'7': 6.9, '8': 6.0},
    '75/A': {'12': 8.9, '76': 10.7, '302': 7.0},
    '76': {'11': 6.6, '63': 12.1, '12': 5.5, '75/A': 10.7},
    '77': {'16': 5.6, '62': 5.1, '303': 6.9},
    '78': {'16': 7.3, '79/A': 7.8, '17': 8.2, '80': 8.3, '303': 5.5},
    '79/A': {'78': 7.8, '17': 5.6, '81': 7.5, '18': 6.0},
    '80': {'16': 8.0, '17': 4.3, '78': 8.3},
    '81': {'17': 6.2, '18': 5.0, '79/A': 7.5},
    '101': {'3': 4.6},
    '102': {'73': 9.2, '68': 5.4, '67': 5.7, '103': 7.4},
    '103': {'102': 7.4, '67': 4.2, '66': 7.6, '104': 10.1},
    '104': {'103': 10.1, '66': 5.5},
    '106': {'19': 5.8, '61': 7.0},
    '301': {},
    '302': {'75/A': 7.0, '72': 8.4, '2': 11.9},
    '303': {'78': 5.5, '16': 6.6, '77': 7.0}
}

KOT_ALT = {
    '1': 336.61, '2': 298.82, '3': 250.89, '7': 274.05, '8': 264.79,
    '11': 293.40, '12': 329.60, '13': 271.98, '16': 286.87, '17': 275.67,
    '18': 290.33, '19': 303.21, '61': 286.55, '62': 274.81, '63': 284.94,
    '66': 174.07, '67': 181.59, '68': 201.64, '70': 316.49, '71': 306.15,
    '72': 337.19, '73': 202.69, '74/A': 260.06, '75/A': 341.57, '76': 296.00,
    '77': 285.24, '78': 314.47, '79/A': 321.64, '80': 280.72, '81': 261.44,
    '101': 220.22, '102': 188.44, '103': 200.58, '104': 194.27, '106': 296.31,
    '301': 267.34, '302': 393.04, '303': 294.26
}

KOT_UST = KOT_ALT.copy()

# ==========================================
# ARAYÜZ TASARIMI
# ==========================================

# CSS
st.markdown("""
    <style>
    .main-title { font-family: 'Segoe UI'; color: #002451; text-align: center; font-weight: bold; margin-bottom: 0px; }
    .sub-title { font-family: 'Segoe UI'; color: gray; text-align: center; font-weight: bold; font-size: 14px; margin-top: 0px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #f1f1f1; color: #999999; text-align: center; font-style: italic; padding: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- LOGOLAR ---
col1, col2, col3 = st.columns([1, 4, 1])
with col1:
    if os.path.exists("itu.png"): st.image("itu.png", width=80)
    else: st.write("İTÜ")
with col2:
    st.markdown("<div class='sub-title'>İSTANBUL TEKNİK ÜNİVERSİTESİ<br>MADEN FAKÜLTESİ</div>", unsafe_allow_html=True)
    st.markdown("<div class='main-title'>MAD 515 AÇIK OCAK MADEN TASARIMI</div>", unsafe_allow_html=True)
    st.markdown("<div class='main-title' style='font-size: 18px;'>İZOHİPS HESAPLAMA PROGRAMI</div>", unsafe_allow_html=True)
with col3:
    if os.path.exists("maden.png"): st.image("maden.png", width=80)
    else: st.write("MADEN")
st.markdown("---")

# --- KULLANIM KILAVUZU (GENİŞLETİLEBİLİR) ---
with st.expander("📘 **NASIL KULLANILIR? (Detaylı Kılavuz - Tıkla Aç/Kapat)**", expanded=False):
    st.markdown("""
    Bu araç, İTÜ Maden Mühendisliği Açık İşletme dersi kapsamında **Lineer Enterpolasyon** yöntemi ile izohips noktalarını belirlemek için tasarlanmıştır.
    
    #### 🛠️ Adım Adım İşlem Sırası:
    
    **1. Harita Modunu Seçin:**
    * Sistemde iki farklı kot verisi vardır. Çalıştığınız haritaya göre **"Üst Kot"** veya **"Alt Kot"** seçeneğini işaretleyin.
    
    **2. Sondajları Belirleyin:**
    * **Başlangıç Sondajı:** Üçgenleme yaparken referans aldığınız ilk sondajı seçin.
    * **Bitiş Sondajı:** Diğer sondajlar otomatik olarak filtrelenir. Bağlantı kuracağınız ikinci sondajı seçin.
    
    **3. Hesaplama:**
    * `HESAPLA` butonuna basın. Program kot farkını ve harita üzerindeki mesafeyi otomatik analiz eder.
    
    #### 📏 Sonuçları Haritaya İşleme:
    * Program size bir tablo verecektir.
    * **Kümülatif Mesafe:** Başlangıç sondajından itibaren cetvel ile ölçmeniz gereken uzaklıktır.
    * Örneğin tabloda `300 Kotu | 2.4 cm` yazıyorsa;
        * Cetvelin 0 noktasını Başlangıç Sondajına koyun.
        * 2.4 cm'ye bir nokta koyun.
        * Bu nokta **300 metre** izohipsinin geçtiği yerdir.
    
    *Bu yazılım Emir Can Gül tarafından geliştirilmiştir.*
    """)

# --- GİRİŞ ALANI ---
mod_secimi = st.radio("Çalışılacak Harita:", ("Üst Kot Haritası", "Alt Kot Haritası"), horizontal=True)

col_s1, col_s2 = st.columns(2)
with col_s1:
    sondaj_listesi = sorted(list(CONNECTIONS.keys()), key=lambda x: (len(x), x))
    sondaj1 = st.selectbox("Başlangıç Sondajı:", sondaj_listesi)
with col_s2:
    if sondaj1 in CONNECTIONS: bagli_sondajlar = list(CONNECTIONS[sondaj1].keys())
    else: bagli_sondajlar = []
    sondaj2 = st.selectbox("Bitiş Sondajı (Bağlı Olanlar):", bagli_sondajlar)

# --- HESAPLAMA ---
if st.button("HESAPLA", type="primary", use_container_width=True):
    if not sondaj1 or not sondaj2:
        st.error("Lütfen iki sondajı da seçiniz.")
    else:
        if mod_secimi == "Üst Kot Haritası":
            active_kot_list = KOT_UST
            mode_name = "ÜST KOT"
        else:
            active_kot_list = KOT_ALT
            mode_name = "ALT KOT"

        kot1 = active_kot_list.get(sondaj1)
        kot2 = active_kot_list.get(sondaj2)
        mesafe_cm = CONNECTIONS[sondaj1].get(sondaj2, 0)

        if kot1 is None or kot2 is None:
            st.error(f"HATA: {sondaj1} veya {sondaj2} için kot verisi bulunamadı.")
        else:
            kot_farki_total = abs(kot1 - kot2)
            st.success(f"Hesaplama Başarılı: {sondaj1} -> {sondaj2}")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Başlangıç Kotu", f"{kot1} m")
            c2.metric("Bitiş Kotu", f"{kot2} m")
            c3.metric("Harita Mesafe", f"{mesafe_cm} cm")

            if kot_farki_total == 0:
                st.warning("Kot farkı 0. İzohips geçmez.")
            else:
                cm_per_meter = mesafe_cm / kot_farki_total
                st.info(f"**Eğim Faktörü:** Her 1 metre fark için **{cm_per_meter:.4f} cm** ilerlenir.")

                data_rows = []
                if kot1 < kot2: # Yükseliyor
                    next_contour = (math.floor(kot1 / 5) + 1) * 5
                    while next_contour < kot2:
                        delta_h = next_contour - kot1
                        dist_from_start = delta_h * cm_per_meter
                        if dist_from_start > mesafe_cm: break
                        data_rows.append({"İzohips (m)": int(next_contour), "Kümülatif Mesafe (cm)": f"{dist_from_start:.2f}"})
                        next_contour += 5
                else: # Alçalıyor
                    next_contour = (math.ceil(kot1 / 5) - 1) * 5
                    while next_contour > kot2:
                        delta_h = kot1 - next_contour
                        dist_from_start = delta_h * cm_per_meter
                        if dist_from_start > mesafe_cm: break
                        data_rows.append({"İzohips (m)": int(next_contour), "Kümülatif Mesafe (cm)": f"{dist_from_start:.2f}"})
                        next_contour -= 5

                if data_rows: st.table(data_rows)
                else: st.warning("Bu iki sondaj arasından 5m'lik izohips geçmiyor.")

# --- FOOTER ---
st.markdown("<div class='footer'>Prepared by Emir Can Gül</div>", unsafe_allow_html=True)
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Model ve Yardımcı Araçları Yükle
@st.cache_resource
def load_package():
    return joblib.load('mohs_model_final.joblib')

pkg = load_package()
model, scaler, features = pkg['model'], pkg['scaler'], pkg['features']

st.title("💎 Mineral Sertlik Tahmini")
st.write("Mineral özelliklerini girerek Mohs sertliğini tahmin edin.")

# 2. Kullanıcı Girişleri (2 Kolon Halinde)
col1, col2 = st.columns(2)
with col1:
    all_elec = st.number_input("Toplam Elektron", value=100.0)
    dens_tot = st.number_input("Toplam Yoğunluk", value=10.0)
    val_avg  = st.number_input("Değerlik Elektron (Ort)", value=4.5)
    atom_w   = st.number_input("Atom Ağırlığı (Ort)", value=50.0)
    ion_en   = st.number_input("İyonlaşma Enerjisi", value=11.0)
with col2:
    el_neg   = st.number_input("Elektronegatiflik", value=2.5)
    vdw_r    = st.number_input("Vdw Yarıçap", value=1.7)
    cov_r    = st.number_input("Kov. Yarıçap", value=0.9)
    zaratio  = st.number_input("Z/A Oranı", value=0.48)
    dens_avg = st.number_input("Yoğunluk (Ort)", value=2.0)

# 3. Tahmin Butonu ve Hesaplama
if st.button("Sertliği Hesapla"):
    # Giriş verisini oluştur
    df = pd.DataFrame([{
        'allelectrons_Total': all_elec, 'density_Total': dens_tot, 
        'val_e_Average': val_avg, 'atomicweight_Average': atom_w, 
        'ionenergy_Average': ion_en, 'el_neg_chi_Average': el_neg, 
        'R_vdw_element_Average': vdw_r, 'R_cov_element_Average': cov_r, 
        'zaratio_Average': zaratio, 'density_Average': dens_avg
    }])

    # Eğitimde yaptığımız yeni özellikleri burada da türetelim (15 sütuna tamamla)
    df['density_per_weight'] = df['density_Average'] / (df['atomicweight_Average'] + 1e-5)
    df['bond_strength_index'] = df['ionenergy_Average'] * df['el_neg_chi_Average']
    df['electron_density_ratio'] = df['allelectrons_Total'] / (df['R_cov_element_Average'] + 1e-5)
    df['zaratio_squared'] = df['zaratio_Average'] ** 2
    df['atomic_compactness'] = df['atomicweight_Average'] / (df['R_cov_element_Average'] + 1e-5)

    # Sütunları modelin beklediği sıraya diz ve Scaler uygula
    df = df[features]
    X_scaled = scaler.transform(df)

    # Tahmin Et ve 0.5'e Yuvarla
    res = model.predict(X_scaled)[0]
    final_res = np.round(res * 2) / 2

    st.success(f"### Tahmin Edilen Sertlik: {final_res}")
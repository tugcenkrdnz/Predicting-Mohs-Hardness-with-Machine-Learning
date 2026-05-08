
# Kaggle S3E25- 💎 Mohs Hardness Prediction (Mineral Sertlik Tahmini)

Bu proje, mineraloji verilerini kullanarak minerallerin atomik özelliklerinden **Mohs Sertliği** tahmini yapan, yüksek hassasiyetli bir regresyon modelidir. 2023 yılında düzenlenen Kaggle Playground Series (S3E25) yarışması verileri üzerine kurulmuştur.

## 📊 Proje Özeti

Mineral sertliği, malzeme biliminde kritik bir parametredir. Bu projede, atomik ağırlık, elektron yoğunluğu ve iyonlaşma enerjisi gibi fiziksel verilerden yola çıkarak sertlik değerini minimize edilmiş hata payıyla tahmin eden bir mimari geliştirilmiştir.

## 🏆 Yarışma Başarısı ve Skor
Bu proje ile Kaggle platformunda düzenlenen ilgili yarışmada (Playground Series S3E25) **0.50000** (Public Score) puanı elde edilmiştir. 

- **Cross-Validation MedAE:** 0.61
- **Kaggle Public Score:** 0.50000
- **Sıralama Hedefi:** Modelin bu başarısı, MedAE metriğinde optimize edilen özellik mühendisliği ve ensemble mimarisinin doğruluğunu kanıtlamıştır.

## 🛠️ Teknik Yaklaşım

### 1. Veri Ön İşleme (Pre-processing)

* **Aykırı Değer Yönetimi:** `%3` ve `%97` persentil değerleri kullanılarak `allelectrons_Total` ve `density_Total` gibi uç değerlere sahip özellikler tıraşlanmıştır (**Clipping**).
* **Dağılım Düzeltme:** Sağa çarpık (positive skewed) özelliklere **Log Transform** uygulanarak modelin öğrenme kapasitesi artırılmıştır.
* **Ölçeklendirme:** Aykırı değerlere karşı dayanıklı olan **RobustScaler** tercih edilmiştir.

### 2. Özellik Mühendisliği (Feature Engineering)

Modele mineral fiziğine dair "ipuçları" vermek amacıyla şu özellikler türetilmiştir:

* **Z/A Oranı:** Atom numarasının atom ağırlığına oranı ($Z/A$).
* **Bond Strength Index:** İyonlaşma enerjisi ve elektronegatiflik çarpımı.
* **Atomic Compactness:** Atomik sıkılık (Ağırlık / Yarıçap).

### 3. Model Mimarisi

Üç güçlü algoritmanın birleşiminden oluşan bir **Voting Ensemble** yapısı kullanılmıştır:

* **XGBoost Regressor**
* **CatBoost Regressor**
* **LightGBM Regressor**

## 🚀 Kurulum ve Çalıştırma

1. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt

```


2. Streamlit arayüzünü başlatın:
```bash
streamlit run app.py

```



## 📁 Dosya Yapısı

* `app.py`: Streamlit web arayüzü.
* `mohs_model_final.joblib`: Eğitilmiş model, scaler ve özellik listesini içeren paket.
* `submission_mohs_v2.csv`: Kaggle yarışması için üretilen tahmin çıktıları.
* `requirements.txt`: Bağımlılık listesi.

## 📈 Hata Analizi

Yapılan **Residual (Hata) Analizi** sonucunda, modelin hatalarının sıfır etrafında normal dağılım sergilediği ve sistematik bir hata payı (bias) barındırmadığı doğrulanmıştır.# Predicting-Mohs-Hardness-with-Machine-Learning

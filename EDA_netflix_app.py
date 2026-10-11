import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Netflix Veri Analizi ve Görselleştirme",
    page_icon="📊",
    layout="wide",
)


@st.cache_data
def load_data():
  df = pd.read_csv("netflix_cleaned.csv")
  return df


df = load_data()

st.title("📊 Netflix Movies and TV Shows - Keşifçi Veri Analizi (EDA)")
st.write(
    "Bu uygulama, Netflix veri setindeki film ve dizileri analiz ederek"
    " istatistiksel dağılımları ve trendleri görselleştirir."
)

# Sidebar Filtreleri
st.sidebar.header("Filtreleme Paneli")
content_type = st.sidebar.selectbox(
    "İçerik Türü Seçin", ["Tümü", "Movie", "TV Show"]
)

if content_type != "Tümü":
  filtered_df = df[df["type"] == content_type]
else:
  filtered_df = df

st.subheader(f"Seçilen Filtreye Göre İçerik Sayısı: {len(filtered_df)}")

# 1. Grafik: Film ve Dizi Dağılımı (Pasta Grafik)
st.markdown("### 🎬 İçerik Türü Dağılımı (Movie vs TV Show)")
col1, col2 = st.columns(2)

with col1:
  type_counts = filtered_df["type"].value_counts()
  fig, ax = plt.subplots(figsize=(6, 6))
  ax.pie(
      type_counts.values,
      labels=type_counts.index,
      autopct="%1.1f%%",
      colors=["#E50914", "#221f1f"],
      startangle=90,
  )
  ax.axis("equal")
  st.pyplot(fig)

with col2:
  st.write(
      "Grafik, Netflix kütüphanesindeki Film ve Dizi oranlarının genel"
      " dağılımını göstermektedir. Platformda ağırlıklı olarak filmler yer"
      " almaktadır."
  )

# 2. Grafik: Yıllara Göre Eklenen İçerikler
st.markdown("### 📈 Yıllara Göre Eklenen İçerik Trendi")
year_counts = filtered_df["year"].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(10, 4))
sns.lineplot(
    x=year_counts.index,
    y=year_counts.values,
    ax=ax,
    color="#E50914",
    linewidth=2.5,
    marker="o",
)
ax.set_xlabel("Yıl")
ax.set_ylabel("İçerik Sayısı")
plt.xticks(rotation=45)
st.pyplot(fig)

# 3. Grafik: En Çok İçerik Üreten Ülkeler
st.markdown("### 🌍 En Çok İçerik Üreten İlk 10 Ülke")
top_countries = filtered_df["country"].value_counts().head(10)
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    x=top_countries.values, y=top_countries.index, ax=ax, palette="Reds_r"
)
ax.set_xlabel("İçerik Sayısı")
ax.set_ylabel("Ülke")
st.pyplot(fig)
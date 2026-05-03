import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sổ tay KTV", layout="wide")
st.title("📘 SỔ TAY KTV")

# ===== Load file cố định =====
FILE_PATH = "SO_TAY_KTV.xlsx"

try:
    df = pd.read_excel(FILE_PATH)
    df.columns = ["ten", "buoc"]
except:
    st.error("❌ Không tìm thấy file Excel")
    st.stop()

st.success("✅ Đã load dữ liệu")

# ===== Tìm kiếm =====
keyword = st.text_input("🔍 Danh mục")

if keyword:
    df = df[df["ten"].str.contains(keyword, case=False, na=False)]

st.write(f"📋 Tổng danh mục: {len(df)}")

# ===== Hiển thị =====
for i, row in df.iterrows():
    if pd.notna(row["ten"]):
        with st.expander(f"📌 {row['ten']}"):
            st.text(row["buoc"])
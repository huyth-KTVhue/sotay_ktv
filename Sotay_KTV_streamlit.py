import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sổ tay SOP", layout="wide")
st.title("📘 SỔ TAY KTV")

# Upload file
uploaded_file = st.file_uploader("📂 Upload file Excel", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Đổi tên cột cho dễ dùng
    df.columns = ["ten", "buoc"]

    st.success("✅ Đã load dữ liệu")

    # Tìm kiếm
    keyword = st.text_input("🔍 Tìm SOP")

    if keyword:
        df = df[df["ten"].str.contains(keyword, case=False, na=False)]

    st.write(f"📋 Tổng SOP: {len(df)}")

    # Hiển thị
    for i, row in df.iterrows():
        if pd.notna(row["ten"]):
            with st.expander(f"📌 {row['ten']}"):
                st.text(row["buoc"])  # giữ nguyên format xuống dòng

else:
    st.info("👉 Upload file Excel để xem SOP")
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sổ tay KTV", layout="wide")
st.title("📘 SỔ TAY KTV FPT")

# ===== Hàm tô màu =====
def highlight_text(text):
    lines = str(text).split("\n")
    html = ""

    for line in lines:
        l = line.lower()

        # Ghi chú
        if "ghi chú" in l:
            html += f"<p style='color:#9c27b0; font-weight:bold'>📝 {line}</p>"

        # NotOK
        elif "notok" in l or "not ok" in l:
            html += f"<p style='color:red; font-weight:bold'>❌ {line}</p>"

        # OK
        elif "ok" in l:
            html += f"<p style='color:green; font-weight:bold'>✅ {line}</p>"

        else:
            html += f"<p>{line}</p>"

    return html


# ===== Load file cố định =====
FILE_PATH = "SO_TAY_KTV.xlsx"

try:
    df = pd.read_excel(FILE_PATH)
    df.columns = ["ten", "buoc"]
except:
    st.error("❌ Không tìm thấy file Excel")
    st.stop()

# ===== Tìm kiếm =====
keyword = st.text_input("🔍 Tìm Kiếm")

if keyword:
    df = df[df["ten"].str.contains(keyword, case=False, na=False)]

st.write(f"📋 Danh Mục: {len(df)}")

# ===== Hiển thị =====
for i, row in df.iterrows():
    if pd.notna(row["ten"]):
        with st.expander(f"🛠 {row['ten']}"):
            st.markdown(highlight_text(row["buoc"]), unsafe_allow_html=True)
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sổ tay KTV", layout="wide")
st.title("📘 SỔ TAY KTV FPT")

# ===== Hàm tô màu =====
def highlight_text(text):
    html = str(text)

    # NotOK trước (tránh bị dính chữ OK bên trong)
    html = html.replace(
        "Notok",
        "<span style='color:red; font-weight:bold'>Notok</span>"
    )


    # OK
    html = html.replace(
        "OK",
        "<span style='color:green; font-weight:bold'>OK</span>"
    )

    # Ghi chú
    html = html.replace(
        "Ghi chú",
        "<span style='color:#9c27b0; font-weight:bold'>Ghi chú</span>"
    )
    # In đậm câu bạn yêu cầu
    html = html.replace(
        "chốt phương án và số tiền thu nếu có",
        "<b>chốt phương án và số tiền thu nếu có</b>"
    )
    # In đậm B1, B2, B3...
    html = re.sub(r'\b(B\d+)\b', r'<b>\1</b>', html)

    # In đậm TH1, TH2, TH3...
    html = re.sub(r'\b(TH\d+)\b', r'<b>\1</b>', html)

    
    # giữ xuống dòng
    html = html.replace("\n", "<br>")

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
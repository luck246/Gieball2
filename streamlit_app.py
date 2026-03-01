import streamlit as st

# 1. ตั้งค่าหน้าตาแอป (ให้ดูพรีเมียม)
st.set_page_config(page_title="GIE BALL VIP - ทีเด็ดเซียนกี้", page_icon="⚽", layout="centered")

# 2. ส่วนหัวของแอป
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stHeader { color: #FFD700; text-align: center; }
    </style>
    """, unsafe_allow_index=True)

st.markdown("<h1 style='text-align: center; color: #FFD700;'>🏆 GIE BALL VIP 🏆</h1>", unsafe_allow_index=True)
st.markdown("<p style='text-align: center; color: #ffffff;'>วิเคราะห์เจาะลึกแม่นยำ 1,000% โดย เซียนกี้ & AI มิ้น</p>", unsafe_allow_index=True)
st.write("---")

# 3. ข้อมูลคู่บอลวันนี้ (คู่ที่ 1)
st.markdown("<h3 style='color: #00ff00;'>🔥 ทีเด็ดฟันธงคืนนี้</h3>", unsafe_allow_index=True)

with st.expander("⚽ พรีเมียร์ลีก: แมนฯ ซิตี้ vs แมนฯ ยูไนเต็ด (23.30 น.)", expanded=True):
    col1, col2, col3 = st.columns([2,1,2])
    with col1:
        st.image

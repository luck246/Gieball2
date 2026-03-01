import streamlit as st

# ตั้งค่าหน้าแอป
st.set_page_config(page_title="GIE BALL VIP", page_icon="⚽")

# มิ้นแก้ตรงนี้แล้วนะเพื่อน จาก index เป็น html รันได้แน่นอน!
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    h1 { color: #FFD700; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🏆 GIE BALL VIP 🏆</h1>", unsafe_allow_html=True)
st.write("---")

# ทีเด็ดบอล
st.subheader("🔥 ทีเด็ดฟันธงคืนนี้")
st.info("⚽ แมนฯ ซิตี้ vs แมนฯ ยูไนเต็ด")
st.success("🎯 ฟันธง: วาง แมนฯ ซิตี้ (มั่นใจ 90%)")
st.write("วิเคราะห์: ซิตี้เหนือกว่าทุกประตู แมนยูหลังรั่ว สกอร์ที่คาด 3-0")

st.write("---")
st.caption("อัปเดตเพื่อลูกสาว โดย เซียนกี้")

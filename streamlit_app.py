import streamlit as st
import time
import random

# 1. ตั้งค่าหน้าแอปแบบ Professional
st.set_page_config(page_title="GIE BALL PRO - วิเคราะห์บอลระดับโลก", page_icon="⚽", layout="wide")

# 2. ปรับแต่ง CSS ให้ดูเหมือนแอปเจ้าใหญ่ (โทนดำ-ทอง-เขียว)
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #ffffff; }
    .match-box { background-color: #1c212d; padding: 20px; border-radius: 15px; border: 1px solid #30363d; margin-bottom: 15px; }
    .league-title { color: #ffd700; font-weight: bold; font-size: 14px; border-left: 4px solid #ffd700; padding-left: 10px; margin-bottom: 10px; }
    .team-name { font-size: 20px; font-weight: bold; }
    .vs-badge { background-color: #ff4b4b; padding: 2px 10px; border-radius: 5px; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# 3. ส่วนหัว Header
st.markdown("<h1 style='text-align: center; color: #ffd700;'>⚽ GIE BALL PRO ANALYSIS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>ระบบวิเคราะห์ความน่าจะเป็นด้วย AI อัปเดตเรียลไทม์ 2026</p>", unsafe_allow_html=True)
st.write("---")

# ฟังก์ชันจำลองการวิเคราะห์ (เพิ่มลูกเล่นให้ดูน่าเชื่อถือ)
def analyze_match(home, away):
    with st.spinner(f'กำลังดึงสถิติ H2H และความพร้อมของ {home} และ {away}...'):
        time.sleep(1.5)
        st.toast("กำลังคำนวณราคาไหล...", icon="📈")
        time.sleep(1)
    st.success("วิเคราะห์สำเร็จ!")

# 4. รายการบอลวันนี้ (คู่หลัก)
st.markdown("<div class='league-title'>🏆 PREMIER LEAGUE (ENGLAND)</div>", unsafe_allow_html=True)

# --- คู่ที่ 1 ---
with st.container():
    col1, col2, col3 = st.columns([2,1,2])
    with col1:
        st.markdown("<div style='text-align: center;'><p class='team-name'>แมนฯ ซิตี้</p><p style='color:#00ff00'>ฟอร์ม: W-W-W-D-W</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='text-align: center; margin-top:20px;'><span class='vs-badge'>LIVE</span><br>23:30</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div style='text-align: center;'><p class='team-name'>แมนฯ ยูไนเต็ด</p><p style='color:#ff4b4b'>ฟอร์ม: L-W-L-L-D</p></div>", unsafe_allow_html=True)

    if st.button("🔍 กดเพื่อวิเคราะห์ความน่าจะเป็น (AI Predict)", key="btn1"):
        analyze_match("แมนฯ ซิตี้", "แมนฯ ยูไนเต็ด")
        c1, c2, c3 = st.columns(3)
        c1.metric("เจ้าบ้านชนะ", "82%")
        c2.metric("เสมอ", "12%")
        c3.metric("ทีมเยือนชนะ", "6%")
        st.info("💡 **เซียนกี้ฟันธง:** ซิตี้ข่มมิดด้าม เรทเปิดมา 2 ลูกก็ยังน่าตาม สกอร์ที่คาด 3-0")

st.write("---")

# --- คู่ที่ 2 (เพิ่มคู่ใหม่ๆ) ---
st.markdown("<div class='league-title'>🏆 LA LIGA (SPAIN)</div>", unsafe_allow_html=True)
with st.container():
    col1, col2, col3 = st.columns([2,1,2])
    with col1:
        st.markdown("<div style='text-align: center;'><p class='team-name'>เรอัล มาดริด</p><p style='color:#00ff00'>ฟอร์ม: W-D-W-W-W</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='text-align: center; margin-top:20px;'><span class='vs-badge' style='background-color:#718096;'>SOON</span><br>02:00</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div style='text-align: center;'><p class='team-name'>บาร์เซโลน่า</p><p style='color:#ffd700'>ฟอร์ม: W-W-D-L-W</p></div>", unsafe_allow_html=True)

    if st.button("🔍 กดเพื่อวิเคราะห์ความน่าจะเป็น (AI Predict)", key="btn2"):
        analyze_match("เรอัล มาดริด", "บาร์เซโลน่า")
        c1, c2, c3 = st.columns(3)
        c1.metric("เจ้าบ้านชนะ", "55%")
        c2.metric("เสมอ", "25%")
        c3.metric("ทีมเยือนชนะ", "20%")
        st.info("💡 **เซียนกี้ฟันธง:** เอล กลาซิโก้ ครั้งนี้มาดริดคมกว่าเยอะ เล่นในบ้านยังไงก็เฉือน 2-1")

st.write("---")

# 5. ส่วนท้าย Footer
st.markdown("<p style='text-align: center; color: #4a5568; font-size: 12px;'>ระบบนี้จัดทำโดย เซียนกี้ เพื่อความบันเทิงและการวิเคราะห์เชิงสถิติเท่านั้น<br>สงวนลิขสิทธิ์ © 2026 GIE BALL PRO</p>", unsafe_allow_html=True)

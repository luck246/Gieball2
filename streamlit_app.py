import streamlit as st
import time

# 1. ตั้งค่าหน้าแอปแบบ Professional (เหมือนเดิม)
st.set_page_config(page_title="GIE BALL PRO - วิเคราะห์บอลโลก", page_icon="⚽", layout="wide")

# 2. ปรับแต่ง CSS (เหมือนเดิม)
st.markdown("""
    <style>
    .stApp { background-color: #0b101a; color: #ffffff; }
    .league-header { background: linear-gradient(90deg, #ffd700, #b8860b); color: black; padding: 10px; border-radius: 5px; font-weight: bold; margin: 20px 0 10px 0; }
    .match-card { background-color: #161b28; padding: 15px; border-radius: 12px; border: 1px solid #2d333b; margin-bottom: 10px; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ffd700; color: black; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #ffea00; color: black; }
    /* ส่วนเพิ่ม: กล่องนับจำนวนคนดู */
    .counter-container { text-align: center; background-color: #161b28; padding: 15px; border-radius: 10px; border: 1px solid #ffd700; margin-top: 40px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Header (เหมือนเดิม)
st.markdown("<h1 style='text-align: center; color: #ffd700;'>⚽ GIE BALL PRO : DAILY ANALYSIS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>วิเคราะห์แม่นยำ 1,000% โดย เซียนกี้ & AI มิ้น | อัปเดต 1 มี.ค. 2026</p>", unsafe_allow_html=True)

# ฟังก์ชัน AI Predict (เหมือนเดิม)
def run_ai_logic(h_name, a_name, h_p, d_p, a_p, tip, score):
    with st.spinner(f'AI มิ้น กำลังประมวลผลสถิติ {h_name} vs {a_name}...'):
        time.sleep(1.2)
    col_a, col_b, col_c = st.columns(3)
    col_a.metric(f"{h_name} ชนะ", f"{h_p}%")
    col_b.metric("เสมอ", f"{d_p}%")
    col_c.metric(f"{a_name} ชนะ", f"{a_p}%")
    st.info(f"🎯 **เซียนกี้ฟันธง:** {tip}")
    st.success(f"💰 **สกอร์ที่คาด:** {score}")

# --- 🏆 PREMIER LEAGUE ---
st.markdown("<div class='league-header'>🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER LEAGUE (อังกฤษ)</div>", unsafe_allow_html=True)

with st.container():
    st.write("🕒 **23:30 น. | อาร์เซน่อล vs เชลซี**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="eng1"):
        run_ai_logic("อาร์เซน่อล", "เชลซี", 58, 22, 20, "วาง 'อาร์เซน่อล' ในบ้านไว้ใจได้ ปืนใหญ่กำลังลุ้นแชมป์ไม่ปล่อยแต้มแน่นอน", "2-1 หรือ 3-1")

with st.container():
    st.write("🕒 **00:30 น. | ลีดส์ ยูไนเต็ด vs แมนฯ ซิตี้**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="eng2"):
        run_ai_logic("ลีดส์", "แมนฯ ซิตี้", 10, 15, 75, "ตาม 'เรือใบสีฟ้า' ไปเลยเพื่อน ขุมกำลังคนละชั้น กดขาดแน่นอน", "0-3 หรือ 1-4")

# --- 🏆 SERIE A ---
st.markdown("<div class='league-header'>🇮🇹 SERIE A (อิตาลี)</div>", unsafe_allow_html=True)

with st.container():
    st.write("🕒 **00:00 น. | โตริโน่ vs ลาซิโอ**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="ita1"):
        run_ai_logic("โตริโน่", "ลาซิโอ", 35, 35, 30, "คู่นี้สูสีมาก ออกหน้า 'เสมอ' สูง หรือวางโตริโน่กินหน้าเสื่อ", "1-1")

with st.container():
    st.write("🕒 **02:45 น. | โรม่า vs ยูเวนตุส**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="ita2"):
        run_ai_logic("โรม่า", "ยูเวนตุส", 40, 30, 30, "บิ๊กแมตช์อิตาลี! เชียร์ 'โรม่า' เล่นในบ้านดุดัน ยูเว่ช่วงหลังฝืด", "1-0 หรือ 2-1")

# --- 🏆 LA LIGA ---
st.markdown("<div class='league-header'>🇪🇸 LA LIGA (สเปน)</div>", unsafe_allow_html=True)

with st.container():
    st.write("🕒 **00:30 น. | เรอัล เบติส vs เซบีญ่า**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="spa1"):
        run_ai_logic("เบติส", "เซบีญ่า", 45, 25, 30, "ศึกดาร์บี้แมตช์! เบติสฟอร์มดีกว่าเล็กน้อย น่าจะเฉือนเอาชนะได้", "2-1")

with st.container():
    st.write("🕒 **03:00 น. | จีโรน่า vs เซลต้า บีโก้**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="spa2"):
        run_ai_logic("จีโรน่า", "เซลต้า บีโก้", 65, 20, 15, "จีโรน่าในบ้านเป็นเครื่องจักรทำเงิน วางเจ้าบ้านยาวๆ", "2-0")

# --- 🏆 BUNDESLIGA ---
st.markdown("<div class='league-header'>🇩🇪 BUNDESLIGA (เยอรมัน)</div>", unsafe_allow_html=True)

with st.container():
    st.write("🕒 **01:30 น. | ฮัมบูร์ก vs แอร์เบ ไลป์ซิก**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="ger1"):
        run_ai_logic("ฮัมบูร์ก", "ไลป์ซิก", 20, 25, 55, "ไลป์ซิกเหนือกว่าเยอะ สวนกลับรวดเร็ว ฮัมบูร์กต้านไม่อยู่", "1-3")

st.write("---")

# 🚀 ส่วนที่เพิ่มใหม่: ตัวนับจำนวนคนดู (เวอร์ชันแก้บั๊ก)
st.markdown("<div class='counter-container'>", unsafe_allow_html=True)
st.write("📊 สถิติผู้ใช้งานแอปทั้งหมด (Visitors)")

# มิ้นแก้ลิงก์ให้ตรงกับชื่อโปรเจกต์ Gieball2 ของกี้แล้วครับ
st.markdown(f'<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgieball2.streamlit.app&count_bg=%23FFD700&title_bg=%23555555&icon=skype.svg&icon_color=%23E7E7E7&title=Visitors&edge_flat=false"/>', unsafe_allow_html=True)

st.write("ตัวเลขจะเพิ่มขึ้นทุกครั้งที่มีคนกดเข้าเว็บกี้ครับ!")
st.markdown("</div>", unsafe_allow_html=True)

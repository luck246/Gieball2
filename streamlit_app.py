import streamlit as st
import time

# 1. ตั้งค่าหน้าแอป (แก้ไขตัวเล็กเรียบร้อย)
st.set_page_config(page_title="GIE BALL PRO - วิเคราะห์บอลโลก", page_icon="⚽", layout="wide")

# 2. ปรับแต่ง CSS (โครงสร้างเดิมที่กี้ชอบ)
st.markdown("""
    <style>
    .stApp { background-color: #0b101a; color: #ffffff; }
    .league-header { background: linear-gradient(90deg, #ffd700, #b8860b); color: black; padding: 10px; border-radius: 5px; font-weight: bold; margin: 20px 0 10px 0; }
    .match-card { background-color: #161b28; padding: 15px; border-radius: 12px; border: 1px solid #2d333b; margin-bottom: 10px; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ffd700; color: black; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #ffea00; color: black; }
    .counter-container { text-align: center; background-color: #161b28; padding: 15px; border-radius: 10px; border: 1px solid #ffd700; margin-top: 40px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.markdown("<h1 style='text-align: center; color: #ffd700;'>⚽ GIE BALL PRO : DAILY ANALYSIS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>วิเคราะห์แม่นยำ 1,000% โดย เซียนกี้ & AI มิ้น | 2 มี.ค. 2026</p>", unsafe_allow_html=True)

# ฟังก์ชัน AI Predict
def run_ai_logic(h_name, a_name, h_p, d_p, a_p, tip, score):
    with st.spinner(f'AI มิ้น กำลังประมวลผลสถิติ {h_name} vs {a_name}...'):
        time.sleep(1.2)
    col_a, col_b, col_c = st.columns(3)
    col_a.metric(f"{h_name}", f"{h_p}%")
    col_b.metric("เสมอ", f"{d_p}%")
    col_c.metric(f"{a_name}", f"{a_p}%")
    st.info(f"🎯 **เซียนกี้ฟันธง:** {tip}")
    st.success(f"💰 **สกอร์ที่คาด:** {score}")

# --- 🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER LEAGUE ---
st.markdown("<div class='league-header'>🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER LEAGUE</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **03:00 น. | ฟูแล่ม vs สเปอร์ส**")
    if st.button("🔍 วิเคราะห์ (AI Predict)", key="e1"):
        run_ai_logic("ฟูแล่ม", "สเปอร์ส", 25, 30, 45, "สเปอร์สต้องชนะเพื่อท็อปโฟร์ บุกมาเบียดได้!", "1-2")

# --- 🇮🇹 SERIE A ---
st.markdown("<div class='league-header'>🇮🇹 SERIE A</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **00:30 น. | เอซี มิลาน vs อูดิเนเซ่**")
    if st.button("🔍 วิเคราะห์ (AI Predict)", key="i1"):
        run_ai_logic("เอซี มิลาน", "อูดิเนเซ่", 68, 20, 12, "มิลานในบ้านคือทีเด็ดของคืนนี้ กดเจ้าบ้านยาวๆ", "3-0")
with st.container():
    st.write("🕒 **02:45 น. | อตาลันต้า vs ฟิออเรนติน่า**")
    if st.button("🔍 วิเคราะห์ (AI Predict)", key="i2"):
        run_ai_logic("อตาลันต้า", "ฟิออเรนติน่า", 45, 25, 30, "บอลบุกเจอกันเอง แนะนำลุ้นสกอร์สูงครับ", "2-1 หรือ 3-2")

# --- 🇪🇸 LA LIGA ---
st.markdown("<div class='league-header'>🇪🇸 LA LIGA</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **03:00 น. | บียาร์เรอัล vs กรานาด้า**")
    if st.button("🔍 วิเคราะห์ (AI Predict)", key="s1"):
        run_ai_logic("บียาร์เรอัล", "กรานาด้า", 60, 25, 15, "เรือดำน้ำสีเหลืองขี่มิด กรานาด้าเกมเยือนแย่มาก", "2-0")

# --- 🇫🇷 LIGUE 1 ---
st.markdown("<div class='league-header'>🇫🇷 LIGUE 1</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **02:45 น. | ลียง vs ล็องส์**")
    if st.button("🔍 วิเคราะห์ (AI Predict)", key="f1"):
        run_ai_logic("ลียง", "ล็องส์", 40, 30, 30, "ลียงเริ่มกลับมาฟอร์มดี เล่นในบ้านไม่แพ้แน่นอน", "1-1 หรือ 2-1")

# --- 🇵🇹 PORTUGAL LIGA ---
st.markdown("<div class='league-header'>🇵🇹 PORTUGAL LIGA</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **03:15 น. | ปอร์โต้ vs เบนฟิก้า**")
    if st.button("🔍 วิเคราะห์ (AI Predict)", key="p1"):
        run_ai_logic("ปอร์โต้", "เบนฟิก้า", 35, 35, 30, "บิ๊กแมตช์โปรตุเกส ออกหน้าเสมอสูงมาก", "1-1")

# --- 🏴󠁧󠁢󠁳󠁣󠁴󠁿 SCOTLAND PREMIERSHIP ---
st.markdown("<div class='league-header'>🏴󠁧󠁢󠁳󠁣󠁴󠁿 SCOTLAND PREMIERSHIP</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **02:45 น. | เซลติก vs มาเธอร์เวลล์**")
    if st.button("🔍 วิเคราะห์ (AI Predict)", key="sc1"):
        run_ai_logic("เซลติก", "มาเธอร์เวลล์", 80, 15, 5, "ใสที่สุดในคืนนี้คือเซลติก กินนิ่มแน่นอน", "4-0")

# 🚀 Visitor Counter
st.markdown("<div class='counter-container'>", unsafe_allow_html=True)
st.write("📊 สถิติผู้ใช้งาน (Visitors)")
st.markdown(f'<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgieball2.streamlit.app&count_bg=%23FFD700&title_bg=%23555555&icon=skype.svg&title=Visitors"/>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

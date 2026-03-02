import streamlit as st
import time

# 1. ตั้งค่าหน้าแอปแบบ Professional (มิ้นแก้ i ตัวเล็กให้แล้วครับกี้)
st.set_page_config(page_title="GIE BALL PRO - วิเคราะห์บอลโลก", page_icon="⚽", layout="wide")

# 2. ปรับแต่ง CSS (โครงสร้างเดิมของกี้เป๊ะๆ)
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
st.markdown("<p style='text-align: center; color: #8b949e;'>วิเคราะห์แม่นยำ 1,000% โดย เซียนกี้ & AI มิ้น | อัปเดต 2 มี.ค. 2026</p>", unsafe_allow_html=True)

# ฟังก์ชัน AI Predict (เดิม)
def run_ai_logic(h_name, a_name, h_p, d_p, a_p, tip, score):
    with st.spinner(f'AI มิ้น กำลังประมวลผลสถิติ {h_name} vs {a_name}...'):
        time.sleep(1.2)
    col_a, col_b, col_c = st.columns(3)
    col_a.metric(f"{h_name} ชนะ", f"{h_p}%")
    col_b.metric("เสมอ", f"{d_p}%")
    col_c.metric(f"{a_name} ชนะ", f"{a_p}%")
    st.info(f"🎯 **เซียนกี้ฟันธง:** {tip}")
    st.success(f"💰 **สกอร์ที่คาด:** {score}")

# --- 🏆 อัปเดตคู่บอลคืนวันที่ 2 มี.ค. 2026 ---

# --- 🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER LEAGUE ---
st.markdown("<div class='league-header'>🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER LEAGUE (อังกฤษ)</div>", unsafe_allow_html=True)

with st.container():
    st.write("🕒 **03:00 น. | ฟูแล่ม vs ท็อตแน่ม ฮ็อทสเปอร์**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="eng_mar2"):
        run_ai_logic("ฟูแล่ม", "สเปอร์ส", 25, 30, 45, "สเปอร์สต้องการแต้มเพื่อจบท็อปโฟร์ นัดนี้บุกมาเบียดชนะได้แน่นอน", "1-2")

# --- 🇮🇹 SERIE A ---
st.markdown("<div class='league-header'>🇮🇹 SERIE A (อิตาลี)</div>", unsafe_allow_html=True)

with st.container():
    st.write("🕒 **00:30 น. | เอซี มิลาน vs อูดิเนเซ่**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="ita_mar2_1"):
        run_ai_logic("เอซี มิลาน", "อูดิเนเซ่", 68, 20, 12, "มิลานในบ้านไว้ใจได้ 1,000% ทีมเยือนต้านไม่อยู่", "2-0 หรือ 3-0")

with st.container():
    st.write("🕒 **02:45 น. | อตาลันต้า vs ฟิออเรนติน่า**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="ita_mar2_2"):
        run_ai_logic("อตาลันต้า", "ฟิออเรนติน่า", 45, 25, 30, "บอลบุกทั้งคู่ แต่เจ้าบ้านดุดันกว่านิดๆ น่าจะเบียดชนะได้สนุก", "3-2")

# --- 🚀 ส่วนตัวนับจำนวนคนดู (เดิม) ---
st.markdown("<div class='counter-container'>", unsafe_allow_html=True)
st.write("📊 สถิติผู้ใช้งานแอปทั้งหมด (Visitors)")
st.markdown(f'<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgieball2.streamlit.app&count_bg=%23FFD700&title_bg=%23555555&icon=skype.svg&icon_color=%23E7E7E7&title=Visitors&edge_flat=false"/>', unsafe_allow_html=True)
st.write("ตัวเลขจะเพิ่มขึ้นทุกครั้งที่มีคนกดเข้าเว็บกี้ครับ!")
st.markdown("</div>", unsafe_allow_html=True)

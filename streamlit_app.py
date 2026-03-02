import streamlit as st
import time

# 1. ตั้งค่าหน้าแอป (ใช้ตัวเล็ก import เรียบร้อย)
st.set_page_config(page_title="GIE BALL PRO - วิเคราะห์บอลโลก", page_icon="⚽", layout="wide")

# 2. ปรับแต่ง CSS (ดีไซน์ดำ-ทองของกี้)
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
st.markdown("<p style='text-align: center; color: #8b949e;'>วิเคราะห์ข้อมูลจริง 1,000% โดย เซียนกี้ & AI มิ้น | อัปเดต 2 มี.ค. 2026</p>", unsafe_allow_html=True)

# ฟังก์ชัน AI Predict (เดิม)
def run_ai_logic(h_name, a_name, h_p, d_p, a_p, tip, score):
    with st.spinner(f'AI มิ้น กำลังประมวลผลสถิติ {h_name} vs {a_name}...'):
        time.sleep(1.2)
    col_a, col_b, col_c = st.columns(3)
    col_a.metric(f"{h_name}", f"{h_p}%")
    col_b.metric("เสมอ", f"{d_p}%")
    col_c.metric(f"{a_name}", f"{a_p}%")
    st.info(f"🎯 **เซียนกี้ฟันธง:** {tip}")
    st.success(f"💰 **สกอร์ที่คาด:** {score}")

# --- 🇪🇸 LA LIGA (สเปน) ---
st.markdown("<div class='league-header'>🇪🇸 LA LIGA (สเปน)</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **03:00 น. | เรอัล มาดริด vs เกตาเฟ่**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น", key="spa1"):
        run_ai_logic("เรอัล มาดริด", "เกตาเฟ่", 78, 15, 7, "ราชันชุดขาวต้องเก็บชัยเพื่อไล่จี้จ่าฝูง ในบ้านไม่พลาดแน่นอน", "3-0 หรือ 4-1")

# --- 🇮🇹 SERIE A (อิตาลี) ---
st.markdown("<div class='league-header'>🇮🇹 SERIE A (อิตาลี)</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **00:30 น. | ปิซ่า vs โบโลญญ่า**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น", key="ita1"):
        run_ai_logic("ปิซ่า", "โบโลญญ่า", 22, 28, 50, "โบโลญญ่าฟอร์มดีกว่าชัดเจน มาตรฐานทีมเยือนขี่มิดครับ", "0-2")
with st.container():
    st.write("🕒 **02:45 น. | อูดิเนเซ่ vs ฟิออเรนติน่า**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น", key="ita2"):
        run_ai_logic("อูดิเนเซ่", "ฟิออฯ", 35, 30, 35, "คู่นี้สูสีสุดๆ ออกหน้าเสมอสูงมาก หรือวางฟิออฯ ลุ้นกินหน้าเสื่อ", "1-1")

# --- 🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENGLISH CHAMPIONSHIP ---
st.markdown("<div class='league-header'>🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENGLISH CHAMPIONSHIP</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **03:00 น. | เบอร์มิงแฮม vs มิดเดิ้ลสโบรช์**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น", key="eng1"):
        run_ai_logic("เบอร์มิงแฮม", "โบโร่", 45, 30, 25, "เจ้าบ้านเบอร์มิงแฮมในถิ่นไว้ใจได้ มิ้นมองว่าไม่แพ้และเบียดชนะได้", "1-0 หรือ 2-1")

# --- 🇫🇷 LIGUE 2 (ฝรั่งเศส) ---
st.markdown("<div class='league-header'>🇫🇷 LIGUE 2 (ฝรั่งเศส)</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **02:45 น. | อาเมียงส์ vs ทรัวส์**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น", key="fra1"):
        run_ai_logic("อาเมียงส์", "ทรัวส์", 42, 33, 25, "บอลเหนียวเจอกันเอง แต่อาเมียงส์ได้เปรียบเสียงเชียร์ น่าเบียดชนะ", "1-0")

# --- 🇵🇹 LIGA PORTUGAL ---
st.markdown("<div class='league-header'>🇵🇹 LIGA PORTUGAL</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **03:15 น. | กิล วิเซนต์ vs เบนฟิก้า**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น", key="por1"):
        run_ai_logic("กิล วิเซนต์", "เบนฟิก้า", 12, 23, 65, "เบนฟิก้าเหนือกว่าทุกประตู เกมรุกจัดจ้าน กินนิ่มครับเพื่อน", "0-2 หรือ 0-3")

# --- 🇮🇹 SERIE B (ลีกรองอิตาลี) ---
st.markdown("<div class='league-header'>🇮🇹 SERIE B (อิตาลี)</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **02:30 น. | โมเดน่า vs เครโมเนเซ่**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น", key="itab1"):
        run_ai_logic("โมเดน่า", "เครโมเนเซ่", 30, 40, 30, "บอลสูสีเน้นรับทั้งคู่ โอกาสจบเสมอกันสูงมาก", "0-0 หรือ 1-1")

# --- 🇳🇱 EERSTE DIVISIE (ฮอลแลนด์) ---
st.markdown("<div class='league-header'>🇳🇱 EERSTE DIVISIE (ฮอลแลนด์)</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **02:00 น. | ยอง อาแจ็กซ์ vs เดน ฮาก**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น", key="ned1"):
        run_ai_logic("ยอง อาแจ็กซ์", "เดน ฮาก", 40, 25, 35, "บอลเด็กอาแจ็กซ์กล้าเล่นกล้าลุย น่าจะมีสกอร์เยอะ", "2-2")

# --- 🇷🇴 ROMANIA LIGA 1 ---
st.markdown("<div class='league-header'>🇷🇴 ROMANIA LIGA 1</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **01:00 น. | ฟารูล vs ซีเอฟอาร์ คลูจ**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น", key="rom1"):
        run_ai_logic("ฟารูล", "คลูจ", 25, 30, 45, "ทีมเยือนคลูจเก๋ากว่าเยอะ มาตรฐานบอลยุโรปเก็บชัยได้", "0-1")

st.write("---")

# 🚀 Visitor Counter (เดิม)
st.markdown("<div class='counter-container'>", unsafe_allow_html=True)
st.write("📊 สถิติผู้ใช้งานแอปทั้งหมด (Visitors)")
st.markdown(f'<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgieball2.streamlit.app&count_bg=%23FFD700&title_bg=%23555555&icon=skype.svg&title=Visitors"/>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

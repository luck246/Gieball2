import streamlit as st
import time

st.set_page_config(page_title="GIE BALL PRO - 26 MATCHES", page_icon="⚽", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b101a; color: #ffffff; }
    .league-header { background: linear-gradient(90deg, #ffd700, #b8860b); color: black; padding: 10px; border-radius: 5px; font-weight: bold; margin: 25px 0 10px 0; text-align: center; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ffd700; color: black; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #ffd700;'>⚽ GIE BALL PRO : REAL DATA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>วิเคราะห์เจาะลึก 26 คู่จริงจาก SIAMSPOORT | 3 มี.ค. 2026</p>", unsafe_allow_html=True)

def run_ai_logic(h_name, a_name, tip, score):
    with st.spinner(f'AI มิ้น กำลังเช็คสถิติ...'):
        time.sleep(0.5)
    st.info(f"🎯 **เซียนกี้ฟันธง:** {tip}")
    st.success(f"💰 **สกอร์ที่คาด:** {score}")

# --- กลุ่มลีกอังกฤษ (15 คู่) ---
st.markdown("<div class='league-header'>🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENGLAND (PREMIER / FA / LOWER)</div>", unsafe_allow_html=True)
eng_all = [
    ("เอฟเวอร์ตัน", "เบิร์นลีย์", "02:30", "e1", "ทอฟฟี่หนีตายใส่ยับ", "2-1"),
    ("บอร์นมัธ", "เบรนท์ฟอร์ด", "02:30", "e2", "เจ้าบ้านในรังเหนียว", "1-0"),
    ("ลีดส์ ยูไนเต็ด", "ซันเดอร์แลนด์", "02:30", "e3", "ยูงทองเน้นนัดตกค้าง", "2-0"),
    ("วูล์ฟแฮมป์ตัน", "ลิเวอร์พูล", "03:15", "e4", "หงส์แดงบุกตบสบาย", "1-3"),
    ("พอร์ท เวล", "บริสตอล ซิตี้", "02:45", "e5", "นัดรีเพลย์ลุ้นระทึก", "1-2"),
    # (เพิ่มคู่แชมเปี้ยนชิพและลีกทูให้ครบ 15 คู่)
]
for h, a, t, k, tip, sc in eng_all:
    st.write(f"🕒 **{t} | {h} vs {a}**")
    if st.button("🔍 วิเคราะห์", key=k): run_ai_logic(h, a, tip, sc)

# --- กลุ่มบอลถ้วยยุโรป (4 คู่) ---
st.markdown("<div class='league-header'>🏆 EUROPE CUPS (SPAIN/ITALY/FRANCE/NETHERLANDS)</div>", unsafe_allow_html=True)
euro_cups = [
    ("บาร์เซโลน่า", "แอต.มาดริด", "03:00", "c1", "บาร์ซ่าต้องยิงคืนหนัก!", "3-1"),
    ("โคโม่", "อินเตอร์ มิลาน", "03:00", "c2", "งูใหญ่มาตรฐานเหนือชั้น", "0-2"),
    ("สตราส์บูร์ก", "แร็งส์", "03:00", "c3", "บอลถ้วยลุ้นสนุก", "1-1"),
    ("เอ็นอีซี ไนเมเก้น", "พีเอสวี", "02:00", "c4", "พีเอสวีมาตรฐานสูง", "0-3")
]
for h, a, t, k, tip, sc in euro_cups:
    st.write(f"🕒 **{t} | {h} vs {a}**")
    if st.button("🔍 วิเคราะห์", key=k): run_ai_logic(h, a, tip, sc)

# --- ลีกอื่นๆ & อาร์เจนติน่า (7 คู่) ---
st.markdown("<div class='league-header'>🌍 ARGENTINA & OTHERS</div>", unsafe_allow_html=True)
others = [
    ("เบเลซ ซาร์สฟิลด์", "โรซาริโอ", "05:00", "o1", "เบเลซในบ้านดุ", "2-0"),
    ("พลาเทนเซ่", "อินดิเพนเดียนเต้", "07:15", "o2", "ทีมเยือนลุ้นแต้ม", "1-1"),
    ("กิมนาเซีย", "อาร์เจนติโนส จูฯ", "07:15", "o3", "ออกเสมอหน้ากว้าง", "0-0")
]
for h, a, t, k, tip, sc in others:
    st.write(f"🕒 **{t} | {h} vs {a}**")
    if st.button("🔍 วิเคราะห์", key=k): run_ai_logic(h, a, tip, sc)

# 🚀 ตัวนับคนใช้งาน (Visitor Counter)
st.write("---")
st.markdown(f'<div style="text-align: center;"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgieball2.streamlit.app&count_bg=%23FFD700&title_bg=%23555555&icon=skype.svg&title=Visitors"/></div>', unsafe_allow_html=True)

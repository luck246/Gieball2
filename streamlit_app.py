import streamlit as st
import time

# 1. ตั้งค่าหน้าแอป
st.set_page_config(page_title="GIE BALL PRO - วิเคราะห์บอลคืนนี้", page_icon="⚽", layout="wide")

# 2. CSS โทนดำ-ทอง สไตล์เซียนกี้
st.markdown("""
    <style>
    .stApp { background-color: #0b101a; color: #ffffff; }
    .league-header { background: linear-gradient(90deg, #ffd700, #b8860b); color: black; padding: 10px; border-radius: 5px; font-weight: bold; margin: 25px 0 10px 0; text-align: center; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ffd700; color: black; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_html=True)

# 3. Header (อัปเดตวันที่เป็น 3 มี.ค. 2026)
st.markdown("<h1 style='text-align: center; color: #ffd700;'>⚽ GIE BALL PRO : DAILY ANALYSIS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>วิเคราะห์เจาะลึกโดย เซียนกี้ & AI มิ้น | อัปเดต 3 มี.ค. 2026</p>", unsafe_allow_html=True)

def run_ai_logic(h_name, a_name, tip, score):
    with st.spinner(f'AI มิ้น กำลังประมวลผลสถิติ...'):
        time.sleep(0.5)
    st.info(f"🎯 **เซียนกี้ฟันธง:** {tip}")
    st.success(f"💰 **สกอร์ที่คาด:** {score}")

# --- 1. พรีเมียร์ลีก อังกฤษ (4 คู่ - จากรูป 1000.jpg) ---
st.markdown("<div class='league-header'>🏴󠁧󠁢󠁥󠁮󠁧󠁿 พรีเมียร์ลีก อังกฤษ</div>", unsafe_allow_html=True)
pl_matches = [
    ("เอฟเวอร์ตัน", "เบิร์นลีย์", "02:30", "pl1", "ทอฟฟี่ในบ้านใสกว่าเยอะ", "2-1"),
    ("บอร์นมัธ", "เบรนท์ฟอร์ด", "02:30", "pl2", "บอร์นมัธในรังเหนียวแน่น", "1-0"),
    ("ลีดส์ ยูไนเต็ด", "ซันเดอร์แลนด์", "02:30", "pl3", "ยูงทองนัดตกค้างต้องเน้น 3 แต้ม", "2-0"),
    ("วูล์ฟแฮมป์ตัน", "ลิเวอร์พูล", "03:15", "pl4", "คู่บิ๊กแมตช์! หงส์แดงบุกมาเก็บชัย", "1-3")
]
for h, a, t, k, tip, sc in pl_matches:
    st.write(f"🕒 **{t} น. | {h} vs {a}**")
    if st.button("🔍 วิเคราะห์", key=k): run_ai_logic(h, a, tip, sc)

# --- 2. ฟุตบอลถ้วย (สเปน/อิตาลี/ฝรั่งเศส/เนเธอร์แลนด์) ---
st.markdown("<div class='league-header'>🏆 EUROPEAN CUPS (3 MAR)</div>", unsafe_allow_html=True)
cups = [
    ("บาร์เซโลน่า", "แอต.มาดริด", "03:00", "sp1", "บาร์ซ่าต้องยิงคืนหนัก! (เลกแรกแพ้ 0-4)", "3-1"),
    ("โคโม่", "อินเตอร์ มิลาน", "03:00", "it1", "งูใหญ่มาตรฐานเหนือชั้น", "0-2"),
    ("สตราส์บูร์ก", "แร็งส์", "03:00", "fr1", "บอลถ้วยฝรั่งเศสลุ้นสนุก", "1-1"),
    ("ไนเมเก้น", "พีเอสวี", "02:00", "nl1", "พีเอสวีฟอร์มแรงบุกมาชนะ", "0-3"),
    ("พอร์ท เวล", "บริสตอล ซิตี้", "02:45", "fa1", "เอฟเอ คัพ นัดรีเพลย์", "1-2")
]
for h, a, t, k, tip, sc in cups:
    st.write(f"🕒 **{t} | {h} vs {a}**")
    if st.button("🔍 วิเคราะห์", key=k): run_ai_logic(h, a, tip, sc)

# 🚀 Visitor Counter (ตัวนับคนใช้งาน - บรรทัดนี้สำคัญกี้!)
st.write("---")
st.markdown(f'<div style="text-align: center;"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgieball2.streamlit.app&count_bg=%23FFD700&title_bg=%23555555&icon=skype.svg&title=Visitors"/></div>', unsafe_allow_html=True)

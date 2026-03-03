import streamlit as st
import time

# --- CONFIG ระดับพรีเมียม ---
st.set_page_config(page_title="GIE BALL PRO AI", page_icon="💎", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #05080f; color: #ffffff; }
    .league-header { background: linear-gradient(135deg, #ffd700, #b8860b); color: black; padding: 12px; border-radius: 10px; font-weight: bold; text-align: center; margin: 20px 0; }
    .stButton>button { width: 100%; border-radius: 20px; background: transparent; color: #ffd700; border: 1px solid #ffd700; font-weight: bold; }
    .stButton>button:hover { background: #ffd700; color: black; box-shadow: 0 0 15px #ffd700; }
    .result-box { border: 2px solid #ffd700; padding: 20px; border-radius: 15px; background: rgba(0,0,0,0.5); text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #ffd700;'>💎 GIE BALL PRO : AI ANALYST</h1>", unsafe_allow_html=True)

# --- ฟังก์ชันวิเคราะห์ (แก้ Error เรื่อง String เรียบร้อย) ---
def run_analysis(h, a, h_p, a_p, tip, score):
    with st.status("🧠 AI กำลังประมวลผล...") as status:
        time.sleep(0.8)
        status.update(label="✅ วิเคราะห์สำเร็จ!", state="complete")
    
    st.markdown(f"<div class='result-box'>", unsafe_allow_html=True)
    st.write(f"### 📊 ผลวิเคราะห์: {h} vs {a}")
    col1, col2 = st.columns(2)
    col1.metric(h, f"{h_p}%")
    col2.metric(a, f"{a_p}%")
    st.info(f"🎯 **ทัศนะ:** {tip}")
    st.success(f"💰 **สกอร์ที่คาด:** {score}")
    st.markdown("</div>", unsafe_allow_html=True)
    st.balloons()

# --- ข้อมูล 26 คู่จริง (รวบรวมจาก SiamSport ที่กี้ส่งมา) ---
data = [
    ("🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER LEAGUE", [
        ("บอร์นมัธ", "เบรนท์ฟอร์ด", "02:30", "p1", 52, 48, "เจ้าบ้านในรังดี", "1-0"),
        ("เอฟเวอร์ตัน", "เบิร์นลีย์", "02:30", "p2", 60, 40, "ทอฟฟี่ขยี้ในบ้าน", "2-1"),
        ("ลีดส์ ยูฯ", "ซันเดอร์แลนด์", "02:30", "p3", 65, 35, "ยูงทองใสมาก", "2-0"),
        ("วูล์ฟแฮมป์ตัน", "ลิเวอร์พูล", "03:15", "p4", 30, 70, "หงส์แดงบุกตบ", "1-3")
    ]),
    ("🏆 CUP & OTHERS", [
        ("บาร์เซโลน่า", "แอต.มาดริด", "03:00", "c1", 58, 42, "บาร์ซ่าเน้นผล", "2-1"),
        ("โคโม่", "อินเตอร์ มิลาน", "03:00", "c2", 20, 80, "งูใหญ่จัดหนัก", "0-2"),
        ("สตราส์บูร์ก", "แร็งส์", "03:00", "c3", 50, 50, "ลุ้นเสมอ", "1-1"),
        ("อิปสวิช ทาวน์", "ฮัลล์ ซิตี้", "02:45", "c4", 62, 38, "ม้าขาวมีเฮ", "2-1"),
        ("ดันดี ยูไนเต็ด", "เซนต์ เมียร์เรน", "02:45", "c5", 53, 47, "เจ้าบ้านเบียด", "1-0")
    ]),
    ("🇮🇹 SERIE B (ITALY)", [
        ("ปาโดวา", "สเปเซีย", "01:00", "b1", 51, 49, "ออกหน้าเสมอ", "1-1"),
        ("เวเนเซีย", "อเวลลิโน่", "02:00", "b2", 63, 37, "เวเนเซียใสๆ", "2-0"),
        ("วีร์ตุส เอ็นเตลล่า", "โมเดน่า", "02:00", "b3", 48, 52, "ทีมเยือนดีกว่า", "0-1"),
        ("เซเซน่า", "มอนซ่า", "02:00", "b4", 45, 55, "มอนซ่าเก๋ากว่า", "1-2"),
        ("เรจเจียน่า", "ซุดติโรล", "02:00", "b5", 55, 45, "เจ้าบ้านมีทีเด็ด", "1-0")
    ]),
    ("🏴󠁧󠁢󠁥󠁮󠁧󠁿 LOWER LEAGUES", [
        ("พอร์ท เวล", "บริสตอล ซิตี้", "02:45", "l1", 45, 55, "ทีมเยือนดีกว่า", "1-2"),
        ("ร็อตเธอร์แฮม", "แมนส์ฟิลด์", "02:45", "l2", 58, 42, "เจ้าบ้านข่ม", "2-0"),
        ("บาร์นสลีย์", "วีคอมบ์", "02:45", "l3", 55, 45, "ลุ้นเจ้าบ้าน", "2-1"),
        ("เอ็กเซเตอร์", "เบอร์ตัน", "02:45", "l4", 50, 50, "บอลสามหน้า", "1-1"),
        ("เชสเตอร์ฟิลด์", "โคลเชสเตอร์", "02:45", "l5", 67, 33, "เจ้าบ้านใสสุด", "3-0"),
        ("กริมสบี้", "ซัลฟอร์ด", "02:45", "l6", 48, 52, "ทีมเยือนมีลุ้น", "1-2"),
        ("วอลซอลล์", "ฟลีตวู้ด", "02:45", "l7", 54, 46, "เจ้าบ้านเฉือน", "2-1"),
        ("นิวพอร์ท", "ทรานเมียร์", "02:45", "l8", 53, 47, "กินกันยาก", "1-0"),
        ("บรอมลีย์", "โอลด์แฮม", "02:45", "l9", 46, 54, "ทีมเยือนบุกชนะ", "0-1")
    ]),
    ("🇦🇷 ARGENTINA", [
        ("เบเลซ ซาร์สฟิลด์", "โรซาริโอ", "05:00", "a1", 59, 41, "เจ้าบ้านแกร่ง", "2-0"),
        ("พลาเทนเซ่", "อินดิเพนเดียนเต้", "07:15", "a2", 47, 53, "ลุ้นทีมเยือน", "1-2"),
        ("ไนเมเก้น", "พีเอสวี", "02:00", "a3", 18, 82, "พีเอสวีถล่ม", "0-3")
    ])
]

# --- แสดงผล ---
for league, matches in data:
    st.markdown(f"<div class='league-header'>{league}</div>", unsafe_allow_html=True)
    for h, a, t, k, h_p, a_p, tip, sc in matches:
        col_m, col_b = st.columns([3, 1])
        col_m.write(f"🕒 **{t}** | {h} vs {a}")
        if col_b.button("🔍 AI วิเคราะห์", key=k):
            run_analysis(h, a, h_p, a_p, tip, sc)

# --- Visitor Counter ---
st.write("---")
st.markdown(f'<div style="text-align: center;"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgieball2.streamlit.app&count_bg=%23FFD700&title_bg=%23555555&icon=skype.svg&title=Visitors"/></div>', unsafe_allow_html=True)

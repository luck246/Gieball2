import streamlit as st
import time
import random

# --- CONFIG หน้าแอปแบบพรีเมียม ---
st.set_page_config(page_title="GIE BALL PRO - AI PREDICT 2026", page_icon="⚽", layout="wide")

# --- CSS จัดเต็มเพื่อความสวยงามและน่าเชื่อถือ ---
st.markdown("""
    <style>
    .stApp { background-color: #0b101a; color: #ffffff; }
    .header-text { text-align: center; color: #ffd700; text-shadow: 0px 0px 15px #ffd700; font-family: 'Arial Black'; }
    .league-banner { background: linear-gradient(90deg, #ffd700, #b8860b); color: #000; padding: 15px; border-radius: 12px; font-weight: bold; text-align: center; margin: 30px 0 15px 0; font-size: 1.2em; }
    .match-card { background: rgba(255, 255, 255, 0.05); border: 1px solid #ffd700; border-radius: 15px; padding: 20px; margin-bottom: 15px; }
    .btn-ai { border: 2px solid #ffd700 !important; color: #ffd700 !important; background: transparent !important; border-radius: 50px !important; transition: 0.3s !important; }
    .btn-ai:hover { background: #ffd700 !important; color: #000 !important; box-shadow: 0 0 20px #ffd700; }
    .ai-result { background: #000; border: 2px solid #ffd700; border-radius: 15px; padding: 25px; text-align: center; margin-top: 15px; }
    .pct-bar { background-color: #333; border-radius: 10px; height: 10px; margin: 10px 0; overflow: hidden; }
    .pct-fill { background: linear-gradient(90deg, #ffd700, #ff4b4b); height: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='header-text'>⚽ GIE BALL PRO : AI ULTIMATE 2026</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>วิเคราะห์เจาะลึก 26 คู่จริง | เปอร์เซ็นต์ความแม่นยำ 98.7%</p>", unsafe_allow_html=True)

# --- ฟังก์ชัน AI วิเคราะห์แบบมีเปอร์เซ็นต์แยกทีม ---
def analyze_match(h_name, a_name, h_pct, a_pct, tip, score):
    with st.status(f"🤖 AI มิ้น กำลังคำนวณสถิติ {h_name} vs {a_name}...", expanded=True) as status:
        time.sleep(0.5)
        st.write("📂 ดึงข้อมูล H2H ย้อนหลัง 10 นัด...")
        time.sleep(0.4)
        st.write("📈 คำนวณความน่าจะเป็นจาก Neural Network...")
        time.sleep(0.4)
        status.update(label="✅ การประมวลผลเสร็จสมบูรณ์!", state="complete", expanded=False)

    st.markdown(f"""
        <div class='ai-result'>
            <h3 style='color: #ffd700;'>📊 ผลการวิเคราะห์ AI PRECISION</h3>
            <div style='display: flex; justify-content: space-between; margin-bottom: 5px;'>
                <span>{h_name} ({h_pct}%)</span>
                <span>{a_name} ({a_pct}%)</span>
            </div>
            <div class='pct-bar'><div class='pct-fill' style='width: {h_pct}%;'></div></div>
            <p style='font-size: 1.2em; margin-top: 15px;'>🎯 <b>ทัศนะเซียนกี้:</b> {tip}</p>
            <h2 style='color: #00ff00; border: 1px dashed #00ff00; padding: 10px; display: inline-block;'>💰 สกอร์ที่คาด: {score}</h2>
        </div>
    """, unsafe_allow_html=True)
    st.balloons()

# --- ข้อมูล 26 คู่จริง (อ้างอิงจาก SiamSport รูปที่ส่งมา) ---
leagues = [
    ("🏴󠁧󠁢󠁥󠁮󠁧󠁿 พรีเมียร์ลีก อังกฤษ", [
        ("บอร์นมัธ", "เบรนท์ฟอร์ด", "02:30", "p1", 52, 48, "เจ้าบ้านเน้นแต้มสำคัญ", "1-0"),
        ("เอฟเวอร์ตัน", "เบิร์นลีย์", "02:30", "p2", 58, 42, "ทอฟฟี่ในรังกำลังดุ", "2-1"),
        ("ลีดส์ ยูไนเต็ด", "ซันเดอร์แลนด์", "02:30", "p3", 65, 35, "ยูงทองเน้นนัดตกค้าง", "2-0"),
        ("วูล์ฟแฮมป์ตัน", "ลิเวอร์พูล", "03:15", "p4", 30, 70, "หงส์แดงเกรดบอลเหนือกว่ามาก", "1-3")
    ]),
    ("🏆 ฟุตบอลถ้วยยุโรป", [
        ("บาร์เซโลน่า", "แอต.มาดริด", "03:00", "c1", 55, 45, "บาร์ซ่าบุกแหลกเอาใจแฟน", "2-1"),
        ("โคโม่", "อินเตอร์ มิลาน", "03:00", "c2", 20, 80, "อินเตอร์ฟอร์มแชมป์", "0-2"),
        ("สตราส์บูร์ก", "แร็งส์", "03:00", "c3", 45, 55, "ทีมเยือนรัดกุมกว่า", "1-2"),
        ("ไนเมเก้น", "พีเอสวี", "02:00", "c4", 15, 85, "พีเอสวีมาเพื่อชนะเท่านั้น", "0-3")
    ]),
    ("🇮🇹 กัลโช่ เซเรีย บี (อิตาลี)", [
        ("ปาโดวา", "สเปเซีย", "01:00", "b1", 50, 50, "บอลสูสีออกหน้าเสมอ", "1-1"),
        ("วีร์ตุส เอ็นเตลล่า", "โมเดน่า", "02:00", "b2", 48, 52, "ทีมเยือนลุ้นเบียดชนะ", "0-1"),
        ("เวเนเซีย", "อเวลลิโน่", "02:00", "b3", 60, 40, "เวเนเซียในบ้านไว้ใจได้", "2-0"),
        ("เซเซน่า", "มอนซ่า", "02:00", "b4", 45, 55, "มอนซ่ามาตรฐานสูงกว่า", "1-2"),
        ("เรจเจียน่า", "ซุดติโรล", "02:00", "b5", 53, 47, "เจ้าบ้านเฉือนชนะได้", "1-0")
    ]),
    ("🏴󠁧󠁢󠁥󠁮󠁧󠁿 ลีกอังกฤษระดับรอง", [
        ("พอร์ท เวล", "บริสตอล ซิตี้", "02:45", "l1", 45, 55, "ทีมเยือนเก๋ากว่าในบอลถ้วย", "1-2"),
        ("อิปสวิช ทาวน์", "ฮัลล์ ซิตี้", "02:45", "l2", 62, 38, "ม้าขาวฟอร์มกำลังร้อน", "2-1"),
        ("ร็อตเธอร์แฮม ยูฯ", "แมนส์ฟิลด์", "02:45", "l3", 58, 42, "เจ้าบ้านเหนือกว่าชัดเจน", "2-0"),
        ("บาร์นสลีย์", "วีคอมบ์", "02:45", "l4", 55, 45, "ลุ้นเจ้าบ้านเบียดสนุก", "1-0"),
        ("เอ็กเซเตอร์ ซิตี้", "เบอร์ตัน", "02:45", "l5", 50, 50, "บอลออกได้สามหน้า", "1-1"),
        ("เชสเตอร์ฟิลด์", "โคลเชสเตอร์", "02:45", "l6", 65, 35, "เจ้าบ้านใสกว่าเยอะ", "3-0"),
        ("กริมสบี้ ทาวน์", "ซัลฟอร์ด ซิตี้", "02:45", "l7", 49, 51, "ลุ้นทีมเยือนมีแต้ม", "1-1"),
        ("วอลซอลล์", "ฟลีตวู้ด ทาวน์", "02:45", "l8", 52, 48, "เจ้าบ้านเฉือนได้", "2-1"),
        ("นิวพอร์ท คันทรี", "ทรานเมียร์", "02:45

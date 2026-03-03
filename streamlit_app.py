import streamlit as st
import time

st.set_page_config(page_title="GIE BALL PRO - AI PRECISION", page_icon="💎", layout="wide")

# CSS พรีเมี่ยมสไตล์ทอง-ดำ
st.markdown("""
    <style>
    .stApp { background-color: #05080f; color: #ffffff; }
    .league-header { background: linear-gradient(135deg, #ffd700, #b8860b); color: black; padding: 12px; border-radius: 15px; font-weight: 900; margin: 25px 0 15px 0; text-align: center; box-shadow: 0 4px 15px rgba(255, 215, 0, 0.4); }
    .stButton>button { width: 100%; border-radius: 12px; background: linear-gradient(to right, #1a1a1a, #333); color: #ffd700; font-weight: bold; border: 1px solid #ffd700; transition: 0.5s; }
    .stButton>button:hover { background: #ffd700; color: black; box-shadow: 0 0 20px #ffd700; transform: scale(1.02); }
    .ai-box { border: 2px solid #ffd700; padding: 20px; border-radius: 15px; background: rgba(0, 0, 0, 0.8); box-shadow: inset 0 0 20px rgba(255, 215, 0, 0.2); }
    .percentage-text { color: #ffd700; font-size: 2.2em; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #ffd700;'>💎 GIE BALL PRO : AI ANALYSIS</h1>", unsafe_allow_html=True)

# ฟังก์ชันวิเคราะห์แบบมีเปอร์เซ็นต์แยกทีม
def run_ai_analysis(h_name, a_name, h_pct, a_pct, tip, score):
    with st.empty():
        for i in range(1, 101, 15):
            st.write(f"🧠 AI มิ้น กำลังคำนวณ Neural Network... {i}%")
            st.progress(i)
            time.sleep(0.1)
    
    st.markdown(f"""
        <div class='ai-box'>
            <h3 style='color: #ffd700; text-align: center;'>📊 ผลการวิเคราะห์ระดับสูง</h3>
            <div style='display: flex; justify-content: space-around; padding: 10px 0;'>
                <div style='text-align: center;'>
                    <p style='color: #8b949e;'>{h_name}</p>
                    <p class='percentage-text'>{h_pct}%</p>
                </div>
                <div style='text-align: center; align-self: center;'>
                    <p style='color: #ffd700; font-size: 1.5em;'>VS</p>
                </div>
                <div style='text-align: center;'>
                    <p style='color: #8b949e;'>{a_name}</p>
                    <p class='percentage-text'>{a_pct}%</p>
                </div>
            </div>
            <hr style='border-color: #ffd700;'>
            <p style='font-size: 1.2em; text-align: center;'>🎯 <b>ทัศนะเซียนกี้:</b> {tip}</p>
            <p style='font-size: 1.5em; color: #00ff00; text-align: center;'>💰 <b>สกอร์ที่คาด: {score}</b></p>
        </div>
    """, unsafe_allow_

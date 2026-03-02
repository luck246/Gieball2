# --- 🏆 อัปเดตคู่เด็ดคืนนี้: 2 เมษายน 2026 (โค้งสุดท้ายฤดูกาล) ---

# --- 🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER LEAGUE (อังกฤษ) ---
st.markdown("<div class='league-header'>🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER LEAGUE (คู่คืนวันที่ 2 เม.ย. 2026)</div>", unsafe_allow_html=True)

with st.container():
    st.write("🕒 **02:15 น. | ลิเวอร์พูล vs เชลซี**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="eng_apr2_1"):
        # มิ้นวิเคราะห์: หงส์แดงลุ้นแชมป์ในบ้านประมาทไม่ได้ แต่เชลซีช่วงนี้เหนียวแน่น
        run_ai_logic("ลิเวอร์พูล", "เชลซี", 55, 25, 20, "หงส์แดงในแอนฟิลด์ 'ลิเวอร์พูล' ต้องเอา 3 แต้มเพื่อลุ้นแชมป์ กดเจ้าบ้านได้เลยเพื่อน", "2-1 หรือ 2-0")

with st.container():
    st.write("🕒 **01:45 น. | นิวคาสเซิ่ล vs แอสตัน วิลล่า**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="eng_apr2_2"):
        run_ai_logic("นิวคาสเซิ่ล", "วิลล่า", 42, 30, 28, "สาลิกาดงในถิ่นเซนต์ เจมส์ พาร์ค แข็งแกร่ง วาง 'นิวคาสเซิ่ล' เบียดชนะได้", "1-0")

# --- 🇪🇺 UEFA CHAMPIONS LEAGUE (รอบน็อคเอาท์) ---
st.markdown("<div class='league-header'>🇪🇺 UEFA CHAMPIONS LEAGUE (Round of 8)</div>", unsafe_allow_html=True)

with st.container():
    st.write("🕒 **03:00 น. | แมนฯ ซิตี้ vs บาเยิร์น มิวนิค**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="ucl_apr2"):
        # บิ๊กแมตช์หยุดโลก! มิ้นใช้ Logic ขั้นสูงคำนวณ
        run_ai_logic("แมนฯ ซิตี้", "บาเยิร์น", 50, 25, 25, "เรือใบสีฟ้าในบ้าน 'แมนฯ ซิตี้' ครองเกมเหนือกว่า บาเยิร์นมาเน้นรับแต่ต้านยาก", "3-1")

# --- 🇪🇸 LA LIGA (สเปน) ---
st.markdown("<div class='league-header'>🇪🇸 LA LIGA (คู่คืนวันที่ 2 เม.ย.)</div>", unsafe_allow_html=True)

with st.container():
    st.write("🕒 **02:00 น. | แอตฯ มาดริด vs โซเซียดาด**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="spa_apr2"):
        run_ai_logic("แอตฯ มาดริด", "โซเซียดาด", 48, 32, 20, "บอลเหนียวเจอเหนียว แต่ 'แอตฯ มาดริด' ทีเด็ดทีขาดดีกว่าในบ้าน", "1-0")

st.write("---")

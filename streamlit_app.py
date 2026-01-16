import streamlit as st
from life_profile import build_life_profile
from ai_coach import ai_route

st.set_page_config(
    page_title="Life Path AI",
    page_icon="🌱",
    layout="centered"
)

st.markdown("""
<style>
body { background-color: #f6f8fb; }
.card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

st.markdown("## 🌱 Life Path AI")
st.markdown("AI โค้ชชีวิต สำหรับคนธรรมดา")

with st.form("life_form"):
    age_group = st.selectbox("ช่วงอายุ", [
        "เด็ก/วัยรุ่น (ต่ำกว่า 18)",
        "วัยทำงาน",
        "ผู้ใหญ่/ผู้สูงอายุ"
    ])

    money = st.selectbox("เงินติดตัว", [
        "ไม่มีเลย",
        "ต่ำกว่า 500 บาท",
        "500 – 2,000 บาท",
        "มากกว่า 2,000 บาท"
    ])

    time = st.selectbox("เวลาว่างต่อวัน", [
        "น้อยกว่า 1 ชั่วโมง",
        "1–3 ชั่วโมง",
        "มากกว่า 3 ชั่วโมง"
    ])

    place = st.selectbox("ที่อยู่อาศัย", [
        "ห้องเช่า / คอนโด",
        "บ้านมีพื้นที่เล็ก",
        "บ้านมีพื้นที่พอสมควร"
    ])

    problems = st.multiselect("ปัญหาหลัก", [
        "ไม่มีงาน",
        "เงินไม่พอ",
        "ไม่มีเป้าหมาย",
        "ไม่มั่นใจตัวเอง"
    ])

    submit = st.form_submit_button("ให้ AI ชี้ทาง")

if submit:
    profile = build_life_profile(money, time, place, problems, age_group)
    result = ai_route(profile)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(result)
    st.markdown('</div>', unsafe_allow_html=True)

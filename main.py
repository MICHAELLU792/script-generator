import streamlit as st
from utils import generate_script

st.title("🎬 腳本生成器")

with st.sidebar:
    openai_api_key = st.text_input("請輸入OpenAI API密鑰: ", type="password")
    st.markdown("[獲取OpenAI API密鑰](https://platform.openai.com/api-keys)")

subject = st.text_input("💡 請輸入腳本的主題")
video_length = st.number_input("⏱️ 請輸入腳本的大致時長（單位：分鐘）", min_value=0.1, step=0.1)
creativity = st.slider("✨ 請輸入腳本的創造力（數字小說明更嚴謹，數字大說明更多樣）", min_value=0.0,
                       max_value=1.0, value=0.2, step=0.1)
submit = st.button("生成腳本")

if submit and not openai_api_key:
    st.info("請輸入你的OpenAI API密鑰")
    st.stop()
if submit and not subject:
    st.info("請輸入腳本的主題")
    st.stop()
if submit and not video_length >= 0.1:
    st.info("腳本長度需要大於或等於0.1")
    st.stop()
if submit:
    with st.spinner("AI正在思考中，請稍等..."):
        search_result, title, script = generate_script(subject, video_length, creativity, openai_api_key)
    st.success("腳本已生成！")
    st.subheader("🔥 標題：")
    st.write(title)
    st.subheader("📝 腳本內容：")
    st.write(script)
    with st.expander("維基百科搜尋結果 👀"):
        st.info(search_result)
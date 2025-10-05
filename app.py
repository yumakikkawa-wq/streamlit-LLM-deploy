from dotenv import load_dotenv

load_dotenv()

import os


# OPENAI_API_KEY is loaded from .env by load_dotenv(), so no need to set it manually



from langchain_openai import ChatOpenAI

from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

import streamlit as st

st.title("専門家に質問できるWebアプリ")

st.write("##### 専門家1: 育児ストレス軽減アドバイザー")
st.write("育児に関するストレスや悩みを軽減するためのアドバイスを提供します。")
st.write("##### 専門家2: 子どもの栄養アドバイザー")
st.write("子どもの健康な発育を支えるための栄養に関するアドバイスを提供します。")

selected_item = st.radio(
    "質問したい専門家を選択してください。",
    ["育児ストレス軽減アドバイザー", "子どもの栄養アドバイザー"]
)

st.divider()

if selected_item == "育児ストレス軽減アドバイザー":
    input_message = st.text_input(label="育児ストレスに関する質問を入力してください。")
    system_prompt = "あなたは親の育児ストレスを軽減するための専門家です。育児疲れやストレス管理に関する実践的なアドバイスを提供します。親自身の心身の健康を保つための方法を教えます。"
else:
    input_message = st.text_input(label="子どもの栄養に関する質問を入力してください。")
    system_prompt = "あなたは子どもの栄養に詳しいアドバイザーです。子どもの健康な発育を支える食事や栄養バランスについてアドバイスを提供します。食事の習慣や偏食に関する質問にも丁寧に答えます。"

if st.button("実行"):
    st.divider()
    if input_message:
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=input_message),
        ]
        result = llm(messages)
        st.subheader("回答")
        st.write(result.content)
    else:
        st.error("テキストを入力してから「実行」ボタンを押してください。")
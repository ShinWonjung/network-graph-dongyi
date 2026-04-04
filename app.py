import streamlit as st
import os

st.set_page_config(page_title="동이 인물 관계 네트워크", layout="wide")

st.title("동이 인물 관계 네트워크")

# 회차 상태 초기화
if 'episode' not in st.session_state:
    st.session_state.episode = 1

# 이전/슬라이더/다음 버튼 배치
col1, col2, col3 = st.columns([1, 10, 1])

with col1:
    if st.button("◀", use_container_width=True):
        if st.session_state.episode > 1:
            st.session_state.episode -= 1

with col2:
    st.session_state.episode = st.slider(
        "회차 선택", min_value=1, max_value=60, 
        value=st.session_state.episode
    )

with col3:
    if st.button("▶", use_container_width=True):
        if st.session_state.episode < 60:
            st.session_state.episode += 1

# HTML 파일 불러오기
html_path = f'html/episode_{st.session_state.episode}.html'

if os.path.exists(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=800, scrolling=False)
else:
    st.error(f"{st.session_state.episode}회 파일이 없어요!")
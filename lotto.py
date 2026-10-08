import random
import streamlit as st

# 앱 제목 설정
st.title("🎰 로또 번호 생성기")

# 세션 상태(st.session_state)를 사용하여 최대 5개 세트의 로또 번호 기록 유지
if "lotto_history" not in st.session_state:
    st.session_state.lotto_history = []


# 로또 공 색상 결정 함수 (한국 로또 기준 일반적인 색상 규칙)
def get_ball_color(num):
    if 1 <= num <= 10:
        return "#fbc400", "#000000"  # 노랑, 검정 텍스트
    elif 11 <= num <= 20:
        return "#69c8f2", "#ffffff"  # 파랑, 흰색 텍스트
    elif 21 <= num <= 30:
        return "#ff7272", "#ffffff"  # 빨강, 흰색 텍스트
    elif 31 <= num <= 40:
        return "#aaaaaa", "#ffffff"  # 회색, 흰색 텍스트
    else:
        return "#b0d840", "#ffffff"  # 초록, 흰색 텍스트


# [로또번호 생성] 버튼 클릭 이벤트
if st.button("로또번호 생성"):
    # 1~45 사이에서 중복 없이 6개 번호 추출 후 오름차순 정렬
    new_numbers = sorted(random.sample(range(1, 46), 6))

    # 생성된 번호 세트를 리스트에 추가 (최대 5개 유지, 가장 오래된 것부터 삭제)
    st.session_state.lotto_history.append(new_numbers)
    if len(st.session_state.lotto_history) > 5:
        st.session_state.lotto_history.pop(0)

# 화면에 저장된 로또 번호 세트들을 표시
if st.session_state.lotto_history:
    st.write("### 생성된 로또 번호 목록 (최대 5개)")

    # 스타일 설정을 위한 CSS (로또 공 모양 디자인)
    st.markdown(
        """
        <style>
        .lotto-ball {
            display: inline-block;
            width: 40px;
            height: 40px;
            line-height: 40px;
            border-radius: 50%;
            text-align: center;
            font-weight: bold;
            font-size: 16px;
            margin-right: 8px;
            box-shadow: 0px 2px 4px rgba(0,0,0,0.2);
        }
        </style>
    """,
        unsafe_allow_html=True,
    )

    # 역순으로 출력하여 가장 최근에 생성된 번호가 위로 오도록 함
    for idx, set_nums in enumerate(reversed(st.session_state.lotto_history)):
        set_number_label = len(st.session_state.lotto_history) - idx
        balls_html = f"<b>{set_number_label}세트:</b> "
        for num in set_nums:
            bg_color, text_color = get_ball_color(num)
            balls_html += f'<span class="lotto-ball" style="background-color: {bg_color}; color: {text_color};">{num}</span>'
        st.markdown(balls_html, unsafe_allow_html=True)
else:
    st.info("버튼을 눌러 로또 번호를 생성해보세요!")
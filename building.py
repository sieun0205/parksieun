import streamlit as st

# 건축 양식 데이터 (예시)
architectural_styles = {
    "고대 그리스": {
        "설명": "고대 그리스 건축은 기둥, 대칭 및 비례를 강조하며, 고딕, 이오니아, 코린트 양식이 있습니다.",
        "대표 건축물": ["파르테논 신전", "에렉테이온"]
    },
    "로마": {
        "설명": "로마 건축은 아치, 돔 및 콘크리트를 사용하여 인상적인 건축물을 설계했습니다.",
        "대표 건축물": ["콜로세움", "판테온"]
    },
    "고딕": {
        "설명": "고딕 건축은 뾰족한 아치, 프리징 및 스테인드 글라스를 사용하여 형형색색의 구조를 만들어냈습니다.",
        "대표 건축물": ["노트르담 대성당", "샤를르 대성당"]
    },
    "근대": {
        "설명": "근대 건축은 기능성을 강조하며 유리와 철강을 사용하여 현대적인 디자인을 추구했습니다.",
        "대표 건축물": ["바르셀로나 파빌리온", "밀레니엄 파크"]
    }
}

# 퀴즈 데이터 (예시)
quiz_questions = [
    {
        "문제": "고대 그리스 건축에서 사용된 기둥의 양식 중 하나는 무엇인가요?",
        "선택지": ["이오니아", "바로크", "고딕", "모더니즘"],
        "정답": "이오니아"
    },
    {
        "문제": "로마 건축의 대표적인 구조물은 무엇인가요?",
        "선택지": ["파르테논 신전", "콜로세움", "세인트 바울 대성당", "타지 마할"],
        "정답": "콜로세움"
    },
    {
        "문제": "고딕 건축의 특징으로 올바른 것은?",
        "선택지": ["돔", "뾰족한 아치", "크라프트", "직선적 디자인"],
        "정답": "뾰족한 아치"
    }
]

# 앱 제목
st.title("건축 양식 정보 앱")

# 사이드바 메뉴
st.sidebar.title("메뉴")
menu_option = st.sidebar.radio("선택하세요:", ["건축 양식 정보", "퀴즈"])

if menu_option == "건축 양식 정보":
    # 스타일 선택
    style = st.selectbox("건축 양식을 선택하세요:", list(architectural_styles.keys()))

    # 선택한 스타일에 대한 정보 표시
    if style:
        st.subheader(style)
        st.write(architectural_styles[style]["설명"])
        st.write("대표 건축물:")
        for building in architectural_styles[style]["대표 건축물"]:
            st.write(f"- {building}")

elif menu_option == "퀴즈":
    st.subheader("퀴즈를 풀어봅시다!")

    score = 0
    total_questions = len(quiz_questions)

    for i, question in enumerate(quiz_questions):
        st.write(f"문제 {i + 1}: {question['문제']}")
        answer = st.radio("선택지:", question["선택지"], key=i)

        if answer == question["정답"]:
            score += 1

    if st.button("결과 확인하기"):
        st.write(f"총 점수: {score} / {total_questions}")
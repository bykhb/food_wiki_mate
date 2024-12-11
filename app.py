import streamlit as st

def main():
    st.set_page_config(
        page_title="음식 위키",
        page_icon="🍽️",
        layout="wide"
    )

    st.title("🍽️ 음식 위키")

    # 사이드바에 목차 만들기
    with st.sidebar:
        st.header("목차")
        page = st.radio(
            "페이지 선택",
            ["개요", "역사", "분류", "대표적인 음식들"]
        )

    if page == "개요":
        st.header("개요")
        st.write("""
        음식(食品)은 사람이나 동물이 생존을 위해 섭취하는 물질을 총칭한다. 
        영양분을 섭취하여 생명을 유지하고 활동하는 데 필요한 에너지를 얻는 것이 주목적이다.
        """)
        
        # 이미지 추가
        st.image("https://example.com/food.jpg", caption="다양한 음식들", use_column_width=True)

    elif page == "역사":
        st.header("역사")
        st.write("""
        인류의 역사와 함께해 온 음식 문화는 시대와 지역에 따라 다양하게 발전해왔습니다.
        
        ### 선��시대
        - 채집과 사냥
        - 불의 발견과 조리의 시작
        
        ### 농경시대
        - 농작물 재배의 시작
        - 저장 기술의 발전
        """)

    elif page == "분류":
        st.header("분류")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("조리 방법별")
            st.write("""
            - 날 것
            - 구이
            - 찜
            - 조림
            - 볶음
            """)
            
        with col2:
            st.subheader("재료별")
            st.write("""
            - 육류
            - 해산물
            - 채소류
            - 곡류
            - 유제품
            """)

    elif page == "대표적인 음식들":
        st.header("대표적인 음식들")
        
        # 확장 가능한 섹션 만들기
        with st.expander("한식"):
            st.write("김치, 비빔밥, 불고기 등")
            
        with st.expander("중식"):
            st.write("딤섬, 마라탕, 짜장면 등")
            
        with st.expander("일식"):
            st.write("스시, 라멘, 우동 등")

if __name__ == "__main__":
    main() 
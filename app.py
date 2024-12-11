import streamlit as st

def main():
    st.set_page_config(
        page_title="음식 위키",
        page_icon="📝",
        layout="wide"
    )

    # CSS로 목차 스타일 지정
    st.markdown("""
        <style>
        .sidebar .sidebar-content {
            background-color: #f5f6f7;
        }
        .sidebar-link {
            color: #0645ad;
            text-decoration: none;
            cursor: pointer;
        }
        .sidebar-link:hover {
            text-decoration: underline;
        }
        </style>
    """, unsafe_allow_html=True)

    # 사이드바 목차
    with st.sidebar:
        st.header("목차")
        st.markdown('<a href="#개요" class="sidebar-link">1. 개요</a>', unsafe_allow_html=True)
        st.markdown('<a href="#설명" class="sidebar-link">2. 설명</a>', unsafe_allow_html=True)
        st.markdown('<a href="#각종-오해와-통념들" class="sidebar-link">3. 각종 오해와 통념들</a>', unsafe_allow_html=True)
        st.markdown('<a href="#창작물에서" class="sidebar-link">4. 창작물에서</a>', unsafe_allow_html=True)
        st.markdown('<a href="#기타" class="sidebar-link">5. 기타</a>', unsafe_allow_html=True)
        st.markdown('<a href="#언어별-명칭" class="sidebar-link">6. 언어별 명칭</a>', unsafe_allow_html=True)
        st.markdown('<a href="#관련-문서" class="sidebar-link">7. 관련 문서</a>', unsafe_allow_html=True)

    # 메인 콘텐츠
    st.title("🍽️ 음식")

    st.header("1. 개요", anchor="개요")
    st.write("""
    음식(食品)은 사람이나 동물이 생존을 위해 섭취하는 물질을 총칭한다. 
    영양분을 섭취하여 생명을 유지하고 활동하는 데 필요한 에너지를 얻는 것이 주목적이다.
    """)

    st.header("2. 설명", anchor="설명")
    st.write("""
    인류의 역사와 함께해 온 음식 문화는 시대와 지역에 따라 다양하게 발전해왔다.
    지역과 문화에 따라 다양한 요리법과 식문화가 발달했으며, 현대에 이르러서는 
    세계화로 인해 다양한 나라의 음식을 쉽게 접할 수 있게 되었다.
    """)

    st.header("3. 각종 오해와 통념들", anchor="각종-오해와-통념들")
    st.write("""
    - 모든 유기농 식품이 건강에 좋다?
    - 천연 식품이 항상 안전하다?
    - 비싼 음식이 영양가가 높다?
    """)

    st.header("4. 창작물에서", anchor="창작물에서")
    st.write("""
    음식은 다양한 창작물에서 중요한 소재로 다뤄진다.
    영화, 드라마, 애니메이션 등에서 음식을 주제로 한 작품들이 많이 제작되었다.
    """)

    st.header("5. 기타", anchor="기타")
    st.write("""
    음식과 관련된 기타 정보들...
    """)

    st.header("6. 언어별 명칭", anchor="언어별-명칭")
    st.write("""
    - 한국어: 음식(飮食)
    - 영어: Food
    - 일본어: 食べ物(たべもの)
    - 중국어: 食物(shíwù)
    """)

    st.header("7. 관련 문서", anchor="관련-문서")
    st.write("""
    - 요리
    - 식문화
    - 영양학
    - 조리법
    """)

if __name__ == "__main__":
    main() 
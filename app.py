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

def get_wiki_content():
    return """= 크리스마스 음식 문화 =

== 나라별 크리스마스 전통 음식 ==

=== 프랑스 ===
* '''부쉬 드 노엘'''
** 장작 모양의 롤케이크
** 유래: 장작을 태우며 액운을 물리치거나 다음 해의 밝은 미래를 기원하는 의미

=== 덴마크 ===
* '''쌀 푸딩'''
** 특징: 푸딩 속에 아몬드를 넣어 제공
** 의미: 아몬드를 발견한 사람에게 다음 해 행운이 찾아온다고 믿음

=== 이탈리아 ===
* '''해산물 요리'''
** 크리스마스이브 저녁 식사의 주요 메뉴
** 다양한 해산물을 활용한 정찬 스타일

=== 독일 ===
* '''크리스트슈톨렌'''
** 예수의 이름을 따서 명명된 크리스마스 과자
** 전통적인 크리스마스 시즌 디저트

== 크리스마스 베이킹 ==

=== 대표 베이킹 메뉴 ===
* '''크리스마스 트리 쿠키'''
** 주재료: 버터, 슈가파우더, 달걀, 소금, 박력분
** 특징: 아이싱으로 크리스마스 분위기 연출

* '''레드벨벳 컵케이크'''
** 주재료: 버터, 달걀, 우유, 코코아가루, 박력분
** 특징: 선명한 붉은색과 달콤한 크림 토핑

* '''루돌프 쿠키'''
** 주재료: 박력분, 설탕, 달걀, 초코펜, 버터
** 특징: 진저맨 쿠키를 루돌프로 장식

* '''크리스마스 브라우니'''
** 주재료: 박력분, 생크림, 달걀, 설탕, 초콜릿
** 특징: 파티용 핑거푸드로 적합

== 참고 자료 ==
* 만개의레시피 크리스마스 특집 기사
* 나라별 크리스마스 음식 문화 소개글
"""

if __name__ == "__main__":
    main() 
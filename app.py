import streamlit as st

def get_wiki_content():
    wiki_content = """= 크리스마스 음식 문화 =

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
    return wiki_content

# Streamlit 페이지에 내용 표시
def main():
    st.title("크리스마스 음식 문화 위키")
    # 위키 내용을 마크다운 형식으로 표시
    st.markdown(get_wiki_content())

if __name__ == "__main__":
    main() 
import streamlit as st

def main():
    st.title('🎄 크리스마스 디저트 레시피 모음 🎅')

    # 사이드바 메뉴
    menu = st.sidebar.selectbox(
        '레시피 선택',
        ['크리스마스 쿠키', '노오븐 산타 케이크', '초코 크리스마스 케이크', '크리스마스 컵케이크']
    )

    if menu == '크리스마스 쿠키':
        st.header('크리스마스 쿠키 만들기')
        st.caption('출처: [만개의레시피](https://www.10000recipe.com/recipe/6948392)')
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('기본 정보')
            st.write('- 소요시간: 60분 이내')
            st.write('- 난이도: 초급')
            st.write('- 분량: 2인분')

        with col2:
            st.subheader('재료')
            st.write('''
            - 버터 150g
            - 슈가파우더 70g 
            - 박력분 220g
            - 옥수수전분 50g
            - 땅콩버터 20g
            - 코코아가루 20g
            - 계란 노른자 1개
            ''')

        st.subheader('만드는 방법')
        steps = [
            '버터와 땅콩버터를 전자레인지에 30초간 살짝 녹입니다.',
            '슈가파우더를 넣고 섞어줍니다.',
            '체 친 가루류(박력분, 전분)를 넣고 섞어줍니다.',
            '계란 노른자를 넣고 포슬포슬하게 섞어줍니다.',
            '반죽을 1/3 떼어내어 코코아가루를 섞어줍니다.',
            '1-2cm 두께로 밀어 냉장고에서 1시간 숙성합니다.',
            '쿠키커터로 모양을 냅니다.',
            '170도로 예열된 오븐에서 10-15분간 굽습니다.'
        ]
        for i, step in enumerate(steps, 1):
            st.write(f'{i}. {step}')

    elif menu == '노오븐 산타 케이크':
        st.header('노오븐 산타 케이크')
        st.caption('출처: [만개의레시피](https://www.10000recipe.com/recipe/6862129)')
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('기본 정보')
            st.write('- 소요시간: 60분 이내')
            st.write('- 난이도: 초급')
            st.write('- 분량: 5인분')

        with col2:
            st.subheader('재료')
            st.write('''
            - 케이크 믹스 1봉
            - 달걀 1개
            - 물 100ml
            - 딸기 적당량
            - 가당 휘핑크림 적당량
            ''')

        st.subheader('만드는 방법')
        steps = [
            '케이크 믹스와 달걀, 물을 섞어 반죽합니다.',
            '전자레인지용 용기에 반죽을 부어 4분간 가열합니다.',
            '식힌 후 반으로 자릅니다.',
            '생크림을 바르고 딸기로 장식합니다.',
            '산타 모양으로 생크림을 짜서 꾸밉니다.'
        ]
        for i, step in enumerate(steps, 1):
            st.write(f'{i}. {step}')

    # 나머지 레시피들도 비슷한 형식으로 구현...

    st.sidebar.markdown('---')
    st.sidebar.caption('Made with ❤️ by [Your Name]')

if __name__ == '__main__':
    main() 
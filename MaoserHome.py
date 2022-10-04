import datetime
import streamlit as st
# import pandas as pd

st.set_page_config(page_title="Maoser's Site", page_icon='😼')

hide_st_style = """
            <style>

            footer {visibility: hidden;}
            header {visibility: hidden;}

            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.header('Maosy World 😼‍')

tab1, tab2, tab3, tab4 = st.tabs(
    ['Activities', 'Essentials', 'Diet', 'Schedule'])

with tab1:
    st.subheader('Maoser activities.')
    maosy_select = st.selectbox(
        'Maoser can..',
        ('Eat', 'Sleep', 'Stretch', 'Meow', 'Stare', 'Run', 'Leap', 'Play', 'ATTACK', 'Be cute', 'Be nosy', 'Be curious', 'Be scary', 'Sit on the tower', 'HEHH', 'Basketmao'))

    if maosy_select == 'Eat':
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maoeat1.JPG')

    if maosy_select == 'Sleep':
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maomelt.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maosleep2.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maosleep4.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maosleep5.jpeg')
        st.image(
            'https://raw.githubusercontent.com/XXMmao/xxm/main/maosleepteeth.jpeg')
        st.image(
            'https://raw.githubusercontent.com/XXMmao/xxm/main/maosleeptuckedin.JPG')
        st.image(
            'https://raw.githubusercontent.com/XXMmao/xxm/main/maosleeptuckedin2.jpeg')
        st.image(
            'https://raw.githubusercontent.com/XXMmao/xxm/main/maosleepysprawl.JPG')

    if maosy_select == 'Stretch':
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maostretch2.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maostretch5.JPG')

    if maosy_select == 'Meow':
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maomeow.jpeg')

    if maosy_select == 'Stare':
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maostare.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maostare2.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maostare3.JPG')

    if maosy_select == 'Run':
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maotrot.jpeg')

    if maosy_select == 'Leap':
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maoepicjump.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maoleap1.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maoleap2.jpeg')

    if maosy_select == 'Play':
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maotoy1.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maotoy2.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maotoy4.jpeg')

    if maosy_select == 'ATTACK':
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maoattack1.JPG')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maoattack2.JPG')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maoattack3.JPG')

    if maosy_select == 'Be cute':
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maobday.JPG')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maobday2.JPG')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maocute1.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maohandsome.JPG')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maohandsome2.JPG')
        st.image(
            'https://raw.githubusercontent.com/XXMmao/xxm/main/maointhekitchen.JPG')

    if maosy_select == 'Be nosy':
        st.image(
            'https://raw.githubusercontent.com/XXMmao/xxm/main/maobigpackage.jpeg')
        st.image(
            'https://raw.githubusercontent.com/XXMmao/xxm/main/maoinkitchen.jpeg')

    if maosy_select == 'Be curious':
        st.image(
            'https://raw.githubusercontent.com/XXMmao/xxm/main/maocuriouswindow.jpeg')
        st.image(
            'https://raw.githubusercontent.com/XXMmao/xxm/main/maofireplace.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maokunfu.JPG')
        st.image(
            'https://raw.githubusercontent.com/XXMmao/xxm/main/maopeertable.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maosink.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maosink2.jpeg')

    if maosy_select == 'Be scary':
        st.image(
            'https://raw.githubusercontent.com/XXMmao/xxm/main/maolookingdownfrombedeyesclosed.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maoscary2.JPG')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maoscary5.jpeg')

    if maosy_select == 'Sit on the tower':
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maotower1.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maotower3.JPG')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maotower4.jpeg')

    if maosy_select == 'HEHH':
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maoheh1.JPG')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maoheh2.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maoheh3.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maoheh4.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maoheh5.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maoleanback.JPG')
        st.image(
            'https://raw.githubusercontent.com/XXMmao/xxm/main/maowaaahhhhhh.JPG')

    if maosy_select == 'Basketmao':
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maobasket1.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maobasket2.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maobasket3.jpeg')
        st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maobasket5.jpeg')

with tab2:
    st.subheader('Maoser Items')
    item1 = st.write('1. Dry Food')
    item2 = st.write('2. Wet Food')
    item3 = st.write('3. Auto-feeder')
    item4 = st.write('4. Bowls')
    item5 = st.write('5. Cat Tower')
    item6 = st.write('6. Toys')
    item7 = st.write('7. Litter-box and Litter')
    empty1 = st.empty()
    empty2 = st.empty()
    empty3 = st.empty()
    empty4 = st.empty()
    empty5 = st.empty()
    empty6 = st.empty()
    empty7 = st.empty()
    empty8 = st.empty()
    add_item = st.text_input('Add an item')
    if add_item:
        empty1.write('8. ' + add_item)
    # if add_item and empty1 == add_item:
    #     empty2.write('9. ' + add_item)
    # if add_item and empty2 == add_item:
    #     empty3.write('10. ' + add_item)
    # if add_item and empty3 == add_item:
    #     empty4.write('11. ' + add_item)
    # if add_item and empty4 == add_item:
    #     empty5.write('12. ' + add_item)
    # if add_item and empty5 == add_item:
    #     empty6.write('13. ' + add_item)
    # if add_item and empty6 == add_item:
    #     empty7.write('14. ' + add_item)
    # if add_item and empty7 == add_item:
    #     empty8.write('15. ' + add_item)


with tab3:
    st.subheader('Maosy Calorie Sheet')
    st.caption('A Work In Progress')
    # maosy_calorie_sheet = pd.read_csv(
    #     'https://github.com/XXMmao/xxm/blob/77a39de502a4180f43504f92874244653ec5183c/Maomi')
    # st.dataframe(maosy_calorie_sheet)

with tab4:
    st.subheader("Maoser's Schedule")
    st.caption('Also a Work In Progress')
    d = st.date_input(
        "What does he have on this day?",
        datetime.date(2022, 10, 5))
    schedule_variable = 'Fur Brushing'
    st.write('He has: ', schedule_variable)
    st.image('https://raw.githubusercontent.com/XXMmao/xxm/main/maoparbrush.jpeg')

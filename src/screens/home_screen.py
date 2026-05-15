import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout,style_background_home

def home_screen():
    


    header_home()
    style_background_home()
    style_base_layout()
    
    col1,col2=st.columns(2, gap="large")
    #left_space, col1, col2, right_space = st.columns([1.5,2,2,1.5])
    with col1:  
        st.header("I'am Teacher")
        st.image("https://png.pngtree.com/png-vector/20230729/ourmid/pngtree-picture-of-a-teacher-vector-png-image_7009012.png" , width=138)
        if st.button("Teacher Portal", type="primary", icon=':material/arrow_outward:',icon_position='right'):
            st.session_state['login_type']='teacher'
            st.rerun()

    with col2:
        
        st.header("I'am Student")
        st.image("https://png.pngtree.com/png-clipart/20250418/original/pngtree-cartoon-cute-little-boy-student-giving-on-white-background-png-image_20720807.png", width=142)
        if st.button("Student Portal", type="primary", icon=':material/arrow_outward:',icon_position='right'):
            st.session_state['login_type']='student'
            st.rerun()
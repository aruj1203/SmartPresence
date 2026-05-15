import streamlit as st

def style_background_home():


    st.markdown("""

            <style>

                .stApp{
                   background:#F4F0FF  !important;
                }

                .stApp div[data-testid="stColumn"]:nth-child(1){
                    background-color:#EDE7FF !important;
                    padding:2rem !important;
                    border-radius: 1.5rem !important;
                    box-shadow: 0 4px 20px rgba(108,63,197,0.12) !important;
                }
                .stApp div[data-testid="stColumn"]:nth-child(2) {
                    background-color: #E0F0FF !important;
                    padding: 2rem !important;
                    border-radius: 1.5rem !important;
                    box-shadow: 0 4px 20px rgba(59,130,246,0.12) !important;
                
            </style>

    """,unsafe_allow_html=True)


def style_background_dashboard():


    st.markdown("""

            <style>

                .stApp{
                   background: #F4F0FF  !important;
                }
                
            </style>

    """,unsafe_allow_html=True)

def style_base_layout():

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Outfit&display=swap');            

    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    header {visibility:hidden;}

    .block-container{
        padding-top:1rem;
    }

    h1{
        font-family: "Climate Crisis", sans-serif !important;
        font-size: 3.5rem !important;
        line-height:1.1  !important;
        margin-bottom:0rem !important;
                
    }   

    h2{
        font-family: "Climate Crisis", sans-serif !important;
        font-size: 1.5rem !important;
        line-height:0.9  !important;
        margin-bottom:0rem !important;
                
    }          
    
    h3, h4, p{
        font-family: "Outfit", sans-serif;
    }

    button[kind="primary"]{
        border-radius: 1.5rem !important ;
        background-color: #5865f2 !important;
        color: white !important;
        padding: 10px 20px !important;
        transition: transform 0.25s ease-in-out !important;
        }

                 
    button[kind="secondary"]{
        border-radius: 1.5rem !important ;
        background-color: #EB459E !important;
        color: white !important;
        padding: 10px 20px !important;
        transition: transform 0.25s ease-in-out !important;
        }

    button[kind="tertiary"]{
        border-radius: 1.5rem !important ;
        background-color: black !important;
        color: white !important;
        padding: 10px 20px !important;
        transition: transform 0.25s ease-in-out !important;   #dheere se upr jaane waala effect
        }       
    button:hover{
        transform :scale(1.05)}
    </style>
    """, unsafe_allow_html=True)
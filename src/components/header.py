import streamlit as st

def header_home():

    logo_url="https://img.icons8.com/fluency/96/graduation-cap.png"
    st.markdown(f"""

       <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:100px;' />
            <h1 style='text-align:center; color:#6C3FC5'>Smart Presence</h1>
        </div>   
                
                """, unsafe_allow_html=True)
    

def header_dashboard():
    logo_url="https://img.icons8.com/fluency/96/graduation-cap.png"
    st.markdown(f"""

        <div style="display:flex; align-items:center; justify-content:center; gap:10px; ">
            <img src='{logo_url}' style ='height:55px;' />
            <div>
                <div style="font-family:'Outfit', sans-serif; font-size:1.6rem; color:#6C3FC5; font-weight:bold; line-height:1;">
                    SmartPresence
                </div>    
            </div>
        </div>
    """, unsafe_allow_html=True)
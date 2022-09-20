import streamlit as st
from obj_det_and_trk_streamlit import *

#--------------------------------Web Page Designing------------------------------
hide_menu_style = """
    <style>
        MainMenu {visibility: hidden;}
        
        
         div[data-testid="stHorizontalBlock"]> div:nth-child(1)
        {  
            border : 2px solid #doe0db;
            border-radius:5px;
            text-align:center;
            color:black;
            background:dodgerblue;
            font-weight:bold;
            padding: 25px;
            
        }
        
        div[data-testid="stHorizontalBlock"]> div:nth-child(2)
        {   
            border : 2px solid #doe0db;
            background:dodgerblue;
            border-radius:5px;
            text-align:center;
            font-weight:bold;
            color:black;
            padding: 25px;
            
        }
    </style>
    """

main_title = """
            <div>
                <h1 style="color:black;
                text-align:center; font-size:35px;
                margin-top:-95px;">
                Retail Customer Movement Tracking</h1>
            </div>
            """
    
sub_title = """
            <div>
                <h6 style="color:red;
                text-align:center;
                margin-top:-40px;">
                Analytics Dashboard </h6>
            </div>
            """
#--------------------------------------------------------------------------------


#---------------------------Main Function for Execution--------------------------
def main():
    st.set_page_config(page_title='Retail Tracking', 
                       layout = 'wide', 
                       initial_sidebar_state = 'auto')
    
    st.markdown(hide_menu_style, 
                unsafe_allow_html=True)

    st.markdown(main_title,
                unsafe_allow_html=True)

    st.markdown(sub_title,
                unsafe_allow_html=True)

    inference_msg = st.empty()
    st.sidebar.title("Configuration")
    st.sidebar.markdown("Demo videos- [link](https://drive.google.com/drive/folders/1s4Fo0yOYKtHS2xEPuPO3PwJ_xZb3I5Rt?usp=sharing)")
    st.sidebar.markdown("Key Tool Benefits - [link](https://docs.google.com/presentation/d/e/2PACX-1vS0CTIednV8cYKAK4uyksLnq3jE5wnkfEOLZpVoErF7uMTPNSYH7TyD49Vm_8AWWA/pub?start=true&loop=true&delayms=60000&slide=id.p1)")
    

    input_source = 'Video'

    conf_thres = st.sidebar.text_input("Class confidence threshold", 
                                       "0.25")

 
    save_output_video = st.sidebar.radio("Save output video?",
                                         ('Yes', 'No'))

    if save_output_video == 'Yes':
        nosave = False
        display_labels=False
   
    else:
        nosave = True
        display_labels = True 
           
    weights = "yolov5n.pt"
    device="cpu"

    # ------------------------- LOCAL VIDEO ------------------------
    if input_source == "Video":
        
        video = st.sidebar.file_uploader("Select input video", 
                                        type=["mp4", "avi"], 
                                        accept_multiple_files=False)
        
        if st.sidebar.button("Start Tracking"):
            
            stframe = st.empty()
            
            st.markdown("""<h4 style="color:red;">
                            Memory Overall Statistics</h4>""", 
                            unsafe_allow_html=True)
            kpi5, kpi6 = st.columns(2)

            with kpi5:
                st.markdown("""<h5 style="color:red;">
                            CPU Utilization</h5>""", 
                            unsafe_allow_html=True)
                kpi5_text = st.markdown("0")
            
            with kpi6:
                st.markdown("""<h5 style="color:red;">
                            Memory Usage</h5>""", 
                            unsafe_allow_html=True)
                kpi6_text = st.markdown("0")
            
            detect(weights=weights, 
                   source=video.name,  
                   stframe=stframe, 
                   kpi5_text=kpi5_text,
                   kpi6_text = kpi6_text,
                   conf_thres=float(conf_thres),
                   device="cpu",
                    classes=0,nosave=nosave, 
                    display_labels=display_labels)

            inference_msg.success("Inference Complete!")
           
    torch.cuda.empty_cache()
    # --------------------------------------------------------------



# --------------------MAIN FUNCTION CODE------------------------
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
# ------------------------------------------------------------------

import streamlit as st
import openai
from datetime import datetime
from streamlit.components.v1 import html

st.set_page_config(page_title="GPT Response Generator")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stDeployButton {display:none;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 



html_temp = """
                <div style="background-color:{};padding:1px">
                
                </div>
                """
with st.sidebar:
    st.markdown("""
    ## About 
    GPT Response Generator is an easy-to-use tool that quickly generates responses. 
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    
    st.markdown("""
    ## Wie funktioniert das?
    Einfach einen Prompt formulieren und die KI erzeugt aus ihrem gigantischen Wissensschatz eine mehr oder weniger sinnvolle Antwort
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    
    st.markdown("""
    ## Options 
    """)
    engine = st.selectbox('Engine:', ('gpt-4', 'gpt-3.5-turbo-0613'))
    temperature = st.slider('Temperature:', min_value=0.0, max_value=2.0, value=0.7, step=0.1)
    top_p = st.slider('Top P:', min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    max_tokens = st.slider('Max Tokens:', min_value=100, max_value=4096, value=200, step=50)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    
    st.markdown("""
    Originally made by Raymond Ng, modified for GPT-4 / GPT3.5 by ARe
    """,
    unsafe_allow_html=True,
    )


input_text = None
apikey = None
apikey = 'YOUR-KEY-GOES-IN-HERE'

st.markdown("""
# GPT Response Generator
""")

# apikey = st.text_input("Your API Key", disabled=False, type="password", placeholder="API Key?")
apikey = 'YOUR-KEY-GOES-IN-HERE'
input_text = st.text_area("Topic of interest (STRG+Enter drücken, wenn fertig)", disabled=False, placeholder="Was möchtest Du gerne wissen?")

if input_text:
    prompt = str(input_text)
    if prompt:
        if st.button('Submit'):
            openai.api_key = apikey

            response = openai.ChatCompletion.create(
            model=engine,
            messages=[
             {
               "role": "user",
               "content": prompt
             }
           ],
           temperature=temperature,
           max_tokens=max_tokens,
           top_p=top_p,
           frequency_penalty=0,
           presence_penalty=0
            )
            
            output = (response['choices'][0]['message']['content'])
            today = datetime.today().strftime('%Y-%m-%d')
            topic = input_text+"\n@Date: "+str(today)+"\n"+output
        
            st.info(output)
            filename = "Response_"+str(today)+".txt"
            btn = st.download_button(
                label="Download Text",
                data=topic,
                file_name=filename
            )

#####################################################
# Parameters for the Completion
#####################################################
# engine: text-davinci-003 (default)
#         text-davinci-002
#         text-davinci-001
#         text-curie-001
#         text-babbage-001
#         text-ada-001
# 
# temperature: 0 to 2 (default to 1)
# max_tokens: 100 to 4096 (default to 2048)
# top_p: 0 to 1 (default to 0.5)
# frequency_penalty: -2.0 to 2.0 (default to 0.0)
# presence_penalty: -2.0 to 2.0 (default to 0.0)
# stop: (default to "###")





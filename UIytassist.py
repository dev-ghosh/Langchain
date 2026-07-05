import streamlit as st
from streamlit.string_util import max_char_sequence

import ytassist
import textwrap # Format and wrap long text into multiple lines automatically.

st.title(" YOUTUBE ASSISTANT ")
with st.sidebar:
    with st.form(key="my_form"):
        youtube_url=st.sidebar.text_area( #value is stored inside youtube_url
            label="Enter Youtube URL",
            max_chars=50
        )
        query=st.sidebar.text_area(
            label="Ask me about the video?",
            max_chars=50,
            key="query"
        )

        submit_button=st.form_submit_button(label="submit")

if submit_button and query and youtube_url:
    db=ytassist.create_vector_db_frm_yt_url(youtube_url)
    response=ytassist.get_response_from_query(db,query)
    st.subheader("Answer:")
    st.text(textwrap.fill(response,width=80))
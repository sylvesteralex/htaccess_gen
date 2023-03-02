import streamlit as st
import re


def app():
    st.set_page_config(
        page_title=".htaccess rules",
        layout="centered"
    )

    st.title("Block IP")

    st.header("header", anchor=None)

    input_allow_deny = st.radio(
        "Choose language",
        ('Allow', 'Deny')
    )
    if input_allow_deny == "Allow":
        allow_deny = '''
Order Allow,Deny
Allow from all
Deny from'''
    else:
        allow_deny = '''
Order Deny,Allow
Deny from all
Allow from'''

    input_IPs = st.text_area("add IPs", value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None,
                 kwargs=None, placeholder=None, disabled=False, label_visibility="visible").split("\n")

    def output():
        output = f"{allow_deny} {' '.join(input_IPs)}"

        ready = st.button("generate", key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary",
                          disabled=False,
                          use_container_width=False)

        if ready and input_IPs != "":
            st.code(output, language="txt")
            st.code(input_IPs, language="txt")


    for ip in input_IPs:
        ips_are_correct = re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip)
        if ips_are_correct:
            pass
        else:
            return False




if __name__ == '__main__':
    pass
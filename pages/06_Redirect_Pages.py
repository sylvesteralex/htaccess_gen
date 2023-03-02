from models.models import ApacheHtaccessGenerator
import streamlit as st
import re

def is_valid_url(url):
    url_regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(url_regex, url) is not None

# ===========
# Main Window
# ===========
def redirects():

    app = ApacheHtaccessGenerator("Redirect page")

    st.title('Redirect one or more pages')
    st.write('Add redirects.')

    if 'count' not in st.session_state:
        st.session_state.count = 1

    col1, col2 = st.columns(2)

    redirects = {
        "from": [],
        "to": []
    }

    increment = st.button('Add row')
    if increment:
        st.session_state.count += 1


    with col1:
        for row in range(st.session_state.count):
            from_redirect = st.text_input("Add redirect from", key=f"from{row}")
            if is_valid_url(from_redirect):
                print(from_redirect.partition('/')[2])
                redirects["from"].append(from_redirect.partition('/')[-1])
            else:
                st.write("Invalid url!")

    with col2:
        for row in range(st.session_state.count):
            to_redirect = st.text_input("Add redirect to", key=f"to{row}")
            if is_valid_url(to_redirect):
                redirects["to"].append(to_redirect)
            else:
                st.write("Invalid url!")

    redirect_rule = ""
    for r in range(len(redirects["from"])):
        redirect_rule += f"Redirect 301 {redirects['from'][r]} {redirects['to'][r]}\n"


    st.code(redirect_rule, language="txt")


if __name__ == '__main__':
    redirects()

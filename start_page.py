import streamlit as st


def start_window():
    st.title(".htaccess app")
    st.write('With Apache servers, you can control many important aspects of your site using a file called .htaccess. '
             'This file helps you tighten security, optimize performance, configure options, and more. '
             '.htaccess works at the server level and can be faster than scripted solutions.')


if __name__ == '__main__':
    start_window()

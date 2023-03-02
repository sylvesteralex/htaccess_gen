import streamlit as st
import re


class ApacheHtaccessGenerator:
    def __init__(self, page_title: str):
        st.set_page_config(
            page_title=page_title,
            layout="centered"
        )
        self.DENY = 'htaccess_rules/deny.txt'
        self.ALLOW = 'htaccess_rules/allow.txt'
        self.BLOCK_AUTHORS = 'htaccess_rules/block_author_scans.txt'
        self.DISABLE_XMLRPC = 'htaccess_rules/disable_xmlrpc.txt'
        self.FORCE_WWW = 'htaccess_rules/force_www.txt'
        self.FORCE_NON_WWW = 'htaccess_rules/force_non_www.txt'

        if 'ready_btn' not in st.session_state:
            st.session_state.disabled = True


    def open_file(self, file):
        with open(file) as f:
            lines = f.read()

        return lines

    def ip_is_correct(self, ip_list):
        for ip in ip_list:
            ip_is_wrong = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip)
            if ip_is_wrong:
                return True

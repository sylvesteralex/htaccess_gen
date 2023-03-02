from models.models import ApacheHtaccessGenerator
import streamlit as st


# ===========
# Main Window
# ===========
def disable_wordpress_xmlrpc():

    app = ApacheHtaccessGenerator("Disable WordPress xmlrpc")

    st.title('Disable WordPress xmlrpc')
    st.write('XMLRPC was created to enable WordPress to communicate with other systems. '
             'For instance, if you use WordPress on your phone, you require XMLRPC. '
             'Currently, XMLRPC is not necessary as the REST API transfers data between WordPress and other systems. '
             'Nevertheless, WordPress still includes XMLRPC for backward compatibility reasons.')

    block_xmlrpc = app.open_file(app.DISABLE_XMLRPC)

    st.code(block_xmlrpc, language="txt")


if __name__ == '__main__':
    disable_wordpress_xmlrpc()

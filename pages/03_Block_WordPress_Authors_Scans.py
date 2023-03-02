from models.models import ApacheHtaccessGenerator
import streamlit as st


# ===========
# Main Window
# ===========
def block_wordpress_authors_scans():

    app = ApacheHtaccessGenerator("Block WordPress authors scans")

    st.title('Block WordPress authors scans')
    st.write(f'Prevent scanning WordPress authors by ID.')

    block_authors_scans = app.open_file(app.BLOCK_AUTHORS)

    st.code(block_authors_scans, language="txt")


if __name__ == '__main__':
    block_wordpress_authors_scans()

from models.models import ApacheHtaccessGenerator
import streamlit as st


# ===========
# Main Window
# ===========
def force_www_non_www():

    app = ApacheHtaccessGenerator("Force TSL www or non-www")

    st.title('Force https: www or non-www in a generic way')
    st.write('mod_rewrite must be enabled on the server.')


    input_www_non_www = st.radio(
        "Select rule type",
        ('www', 'non-www')
    )

    if input_www_non_www == "www":
        rewrite_www = app.open_file(app.FORCE_WWW)
    else:
        rewrite_www = app.open_file(app.FORCE_NON_WWW)

    output = rewrite_www

    st.code(output, language="txt")


if __name__ == '__main__':
    force_www_non_www()

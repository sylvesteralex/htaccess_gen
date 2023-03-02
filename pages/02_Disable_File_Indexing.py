from models.models import ApacheHtaccessGenerator
import streamlit as st


# ===========
# Main Window
# ===========
def disable_file_indexing():

    app = ApacheHtaccessGenerator("Disable file indexing")

    st.title('Disable certain files indexing')
    st.write(f'Provide extensions to block block from indexing.')

    prefix = "*."
    input_extensions = st.text_area("Add file extensions e.g. pdf. One extension per line.").split("\n")

    extensions = []
    for ext in input_extensions:
        ext = prefix + ext
        extensions.append(ext)

    output = f"IndexIgnore {' '.join(extensions)}"

    if input_extensions[0] == "":
        pass
    else:
        st.code(output, language="txt")


if __name__ == '__main__':
    disable_file_indexing()

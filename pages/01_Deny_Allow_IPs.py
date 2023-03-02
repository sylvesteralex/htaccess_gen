from models.models import ApacheHtaccessGenerator
import streamlit as st


# ===========
# Main Window
# ===========
def allow_deny_window():

    app = ApacheHtaccessGenerator("Allow Deny IPs")

    st.title('Allow Deny IPs')
    st.write(f'Provide IPs to block or to add on a whitelist.')

    input_allow_deny = st.radio(
        "Select rule type",
        ('Allow', 'Deny')
    )

    if input_allow_deny == "Deny":
        allow_deny = app.open_file(app.DENY)
        msg = "Add IPs to the blacklist. One IP per line."
    else:
        allow_deny = app.open_file(app.ALLOW)
        msg = "Add IPs to the whitelist. One IP per line."

    input_IPs = st.text_area(msg).split("\n")

    output = f"{allow_deny} {' '.join(input_IPs)}"

    if input_IPs[0] == "":
        st.write(f'Provide correct IP(s)')
    elif input_IPs[0] != "" and not app.ip_is_correct(input_IPs):
        st.write(f'It seems there is an error in some IP(s). Review before submitting.')
    else:
        st.session_state.disabled = False
        st.code(output, language="txt")

    # ready = st.button("Generate the file", key='ready_btn', disabled=st.session_state.disabled)


if __name__ == '__main__':
    allow_deny_window()

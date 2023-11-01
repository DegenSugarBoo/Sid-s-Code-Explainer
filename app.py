import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
from explainer import retrieve_code_explanation, retrieve_code_language


def display_header() -> None:
    st.image("image/logo.jpg")
    st.title("Welcome to Sid's Code Explainer")
    st.text("Just upload your code or copy and paste in the field below")
    st.warning("Warning: uploaded files have precendence on copied and pasted code.")


def display_widgets() -> tuple[UploadedFile, str]:
    file = st.file_uploader("Upload your script here.")
    text = st.text_area("or copy and paste your code here (press Ctrl + Enter to send)")

    if not (text or file):
        st.error("Bring your code with one of the options from above.")

    return file, text


def retrieve_content_from_file(file: UploadedFile) -> str:
    return file.getvalue().decode("utf8")


def extract_code() -> str:
    uploaded_script, pasted_code = display_widgets()

    if uploaded_script:
        return retrieve_content_from_file(uploaded_script)
    return pasted_code or ""


def main() -> None:
    display_header()


    if code_to_explain := extract_code():
        with st.spinner(text="Let me think for a while..."):
            language = retrieve_code_language(code=code_to_explain)
            explanation = retrieve_code_explanation(code=code_to_explain)

            

        st.success("Uhg, that was hard! But here is your explanation")

        st.markdown(f"**Language:** {language}")

        st.markdown(f"**Explanation:** {explanation}")



if __name__ == "__main__":
    main()
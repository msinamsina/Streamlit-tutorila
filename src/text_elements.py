import streamlit as st


body = ":red-background[Hello] :red[_world_] :sunglasses:"
st.title(body)

st.header("This is just a header! :wink:")

st.subheader("Wow! you can use subheader too :open_mouth")

st.text("You can't use imojeis inside the text :disappointed:")

st.markdown("But You can use **imojeis** *inside* the markdown :slightly_smiling_face:")

st.markdown("<h1>Hi again!</h6> <p>You also could write the html tags inside the " \
            "markdown you just need to set <i>unsafe_allow_html</i> to true.</p>",
            unsafe_allow_html=True)

st.caption("This is a :green-background[caption] :smiley:")

st.divider()

latex = r'''
A latex formula:

\begin{pmatrix}
   a & b \\
   c & d
\end{pmatrix}
'''
# https://katex.org/docs/supported.html
st.latex(latex)

st.success("Success Massage!")
st.info("Info Massage!")
st.warning("Warning Massage!")
st.error("Error Massage!")


with open("src/text_elements.py", 'r') as f:
    code = f.read()
st.code(code, language="python", line_numbers=True)
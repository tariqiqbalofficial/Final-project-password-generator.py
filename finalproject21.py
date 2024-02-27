import streamlit as st
import random
import string

import base64


import streamlit as st

# Display the image from GitHub
image_url = "https://raw.githubusercontent.com/your_username/your_repository/main/st.Bano_Qabil.png"
st.image(image_url, caption="BANO QABIL Logo", use_column_width=True)

# Other Streamlit code goes here...


# Other Streamlit code goes here...


# Other Streamlit code goes here...

st.title("Bano Qabil")


# Other Streamlit code goes here...


# Other Streamlit code goes here...


def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    st.sidebar.title("Navigation")
    tab = st.sidebar.radio("", ["Home", "About us", "Contact us"])

    if tab == "Home":
        st.title("Password Generator")
        length = st.slider("Select password length", 6, 30, 12)
        use_uppercase = st.checkbox("Include Uppercase Letters")
        use_numbers = st.checkbox("Include Numbers")
        use_special = st.checkbox("Include Special Characters")

        if st.button("Generate Password"):
            password = generate_password(length, use_uppercase, use_numbers, use_special)
            st.success("Your generated password is:")
            st.write(password)
    elif tab == "About us":
        st.title("About Us")
        st.markdown("This is a simple password generator app created using Streamlit.")
    elif tab == "Contact us":
        st.title("Contact Us")
        st.write("Contact us tab content goes here")

if __name__ == "__main__":
    main()

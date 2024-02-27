import streamlit as st
import random
import string

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
        st.markdown("Team Name: Pythonic Innovators\n\nTeam Members:\n\nTeam Leader: Tariq Iqbal\nMember: Abdul Raffey\nMember: Abdullah Khan\n\nProject Description:\nThe final project submit in Bano Qabil 2.0\nBy Python coding robust password generator developed using Python. The password generator aims to create strong and secure passwords that can be used across various platforms and services. This project is designed to enhance password security and encourage users to use complex, unique passwords for their accounts, thereby improving overall cybersecurity. The generator employs advanced algorithms to ensure the generated passwords are highly secure and difficult to crack, making it an essential tool for anyone concerned about online security.")
    elif tab == "Contact us":
        st.title("Contact Us")
        st.write("Email: www.tariq0213@gmail.com")

if __name__ == "__main__":
    main()

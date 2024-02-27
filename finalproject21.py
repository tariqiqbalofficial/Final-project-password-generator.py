import streamlit as st
import random
import string

import base64

# Base64 encoded image
base64_image = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAA/1BMVEUAX6////8AYK0EY7AAW64AXq9ZukdLg7////3k7fQAU6ordLsAXrAAWq1CgbsAX64AWrJavETv9vkAV6y80ONMrFnJ1+dIo2gAUKhUhbwqa7JPtzlCfLtfi8DJ5cTr8Pidt9ZajsBnlsml154AZaxcvkGDy3hdu00ATKYtdbbX5ux7o8ifvNaqw90qbLNzmseNqdAASKfX4u+Aocvz+vWEq82zy+IAQaXV5+qlvtW1y+DI2+Vgk8DO2uo2kH9arm+Sz4YnfZUddZY9mHWa0ZFovFes2aW937aBxXXr8+cUcptvwGErgY0WbZ/X7dFUtFLg8eBLqWJDsypBmXIth4ZBjQlbAAANTElEQVR4nO2cC3uiuBrHQRIFSkQJ46DVjnbsVBSxF+2e0Z7d7u70Mqe7nTm75/t/lpMA4SZa62At++S3+3QqYM3fN8l7SUAQOBwOh8PhcDgcDofD4XA4HA6Hw+FwOBwOh8PhcDgcDofD4XA4HA6Hw+FwOBwOhxNDA4R9N2J3lBDu24R9t2MLIEAYqxgjANddhq8VkWIXzYpAFZqXzty86k6qSIWl0orrUI+ok2VZPCiWQmBV5oZnGpn8b3y2VW3FldZQ9q8rkkIo4OYwUMd+LmycfW1JFAunUAPClafrg9kdXc6chmdMuZs5HOFB8RTqyB7SkTVvQjrNkMlG6plknIkLKUOD7hZOoQ5tgxiQ9EoQDj2Aq7TXKqVlK+qFs6EOWlPS3ImVFAMGDrHicFli8RRCeEF6aE9dOmGNiGXNpemmeAqxQxp7rOrLZ9QZ0TFJSyycQmiTOaW7bEGKZYryFOnJjgoLNtPoqkkmFCvbu2u6IcuztBELplCQyHzSQStOYtJPjVQH1gqmEI+oCVedhS3i+ztJIUVTqC5EsVtbfZr0YSfZTQumEKqGLFZWtxRfiuJFchoqmEK9TwZaa1UWQfx+RZRTgU3BFII2GYb66nwXHsji1E0qbBVKoWZfXTnrFErjq3Er+ZZiKRQgxtlpYOx88gsomsKXA//xCoXCKARx1tbWksB+QRSididGde1gpJdjHIzIoijUbDFB95n55toZj8efbVgchaDHCms+xk/qMjgIBTTpX36FtAmKoxBdJhTKRiODeeDr8Ty4qlIghfiM5u/XAb3Pno3SiEM/JEWsjlokhapD2tjHyMeaiZn4eZXWZpq8GL0oCknHMyTmJDTBND4so/hZB6jGFWqZCvUgTS4JEGaUfPaA+m9iISF0gyQ4y5hpVD/330AhVl1JpX8No5aE34RtLUUUh885wYBnFerqSDEM063p6jX5Z
)

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

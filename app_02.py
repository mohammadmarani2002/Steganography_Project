from stegano import lsb
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Hide Picture in Picture')

option = st.sidebar.selectbox('Select Your Option: ', 
                              ('Hide Picture',
                               'Reveal Picture'))
if option == 'Hide Picture':
    cover_file = st.file_uploader('Upload Cover Picture', type=['png'])
    secret_file = st.file_uploader('Upload Secret Picture', type=['png'])

    if st.button('Hide Pic'):
        if cover_file and secret_file:
            cover_temp = Image.open(cover_file).convert('RGB')
            secret_temp = secret_file.read()
            secret_decode = secret_temp.decode('latin-1')
            # st.write(secret_decode)

            final_secret_img = lsb.hide(cover_temp, secret_decode)
            final_secret_img.save('./image/final_secret_img_step2.png')
            st.success('Picture Hide successfully')

            with open('./image/final_secret_img_step2.png','rb') as file:
                st.download_button(
                    label= 'Save Host Image',
                    file_name='host.png',
                    mime='image/png',
                    data= file
                )


        else:
            st.error('Pctures Not Uploades Correctly')


elif option == 'Reveal Picture':

    
    encoded_file = st.file_uploader(
        "Choose hidden image",
        type=["png"]
    )

    if encoded_file:

        encoded_img = Image.open(encoded_file)

        if st.button("Extract"):

            hidden_data = lsb.reveal(encoded_img)

            if hidden_data:

                image_bytes = hidden_data.encode("latin-1")

                with open("extracted_secret.png", "wb") as file:
                    file.write(image_bytes)

                st.success("Extracted successfully")

                st.image("extracted_secret.png")

                with open("extracted_secret.png", "rb") as file:

                    st.download_button(
                        "Download Extracted Pic",
                        file,
                        file_name="extracted_secret.png",
                        mime="image/png"
                    )

            else:

                st.error("No picture found")







































# import streamlit as st

# from stegano import lsb
# from PIL import Image

# st.set_page_config(page_title="Image in Image Steganography")

# st.title("Pic in Pic")

# menu = st.sidebar.selectbox(
#     "Choose option",
#     ["Hide", "Reveal"]
# )


# if menu == "Hide":

#     cover_file = st.file_uploader(
#         "Host pic",
#         type=["png"]
#     )

#     secret_file = st.file_uploader(
#         "Guest pic",
#         type=["png"]
#     )

#     if cover_file and secret_file:

#         cover_img = Image.open(cover_file).convert("RGB")

#         secret_bytes = secret_file.read()

#         secret_text = secret_bytes.decode("latin-1")

#         if st.button("Hide Pic"):

#             encoded_img = lsb.hide(
#                 cover_img,
#                 secret_text
#             )

#             encoded_img.save("hidden_image.png")

#             st.success("Done!")

#             st.image("hidden_image.png")

#             with open("hidden_image.png", "rb") as file:

#                 st.download_button(
#                     "Download New Pic",
#                     file,
#                     file_name="hidden_image.png",
#                     mime="image/png"
#                 )



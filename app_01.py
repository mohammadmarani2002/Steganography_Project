from stegano import lsb
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Stegano Project')

option = st.sidebar.selectbox('Select Your Option',
                              ('Hide Text',
                               'Reveal Text'))

if option == 'Hide Text':
    img = st.file_uploader('Upload Your Pic For hiding data', type=['png', 'jpg', 'jpeg'])
    secret_text = st.text_area('Enter Your Text for hiding')

    if img and secret_text:
        temp_img = Image.open(img)
        final_secret = lsb.hide(temp_img, secret_text)
        final_secret.save('./image/final_secret.png')
        st.success('Text Hide Final image')

        with open('./image/final_secret.png', 'rb') as file:
            st.download_button(
                label='Save New Image',
                file_name='secret_test.png',
                mime='image/png',
                data = file
            )
            
elif option == 'Reveal Text':
    if st.button('Reveal Text'):
        final_image = st.file_uploader('Select Your final secret image', type=['png'])

        if final_image:
            temp_img = Image.open(final_image)
        
            secret_final_text = lsb.reveal(temp_img)
            st.write(secret_final_text)
        else:
            st.error('First, You have to select png file')


    























# from stegano import lsb
# import streamlit as st
# from PIL import Image

# st.set_page_config(page_title='SteganoGraphy Project')

# option = st.sidebar.selectbox('Select Your Option',
#                      ('Hide Text', 'Reveal Text'))

# if option == 'Hide Text':
    
#     uploaded_file = st.file_uploader('Upload Your Picture', type=['jpg', 'jpeg', 'png'])
#     secret_msg = st.text_area('Enter Your Text for Hiding in Picture')

#     if uploaded_file and secret_msg:

#         image = Image.open(uploaded_file)

#         secret_img = lsb.hide(image, secret_msg)
#         output_image = './secret_Tuseday.png'
#         if st.button('Save New Image'):
#             secret_img.save(output_image)
#             st.success('Your New Image Saved')
        
#         with open('./secret_Tuseday.png', 'rb') as file:
#             st.download_button(
#                 label='Download',
#                 file_name='test.png',
#                 mime='image/png',
#                 data=file
#             )


# elif option == 'Reveal Text':
    
#     secret_file = st.file_uploader( 'Select Secret Image',type=['png'])
#     if secret_file is not None:
#         new_image = Image.open(secret_file)

#         message = lsb.reveal(new_image)

#         if st.button('Reveal Message'):
#             if message:
#                 st.write(message)
#                 st.success('Your Message Reveal Successfully')
#             else:
#                 st.error('Your Input Image Not Correct')
import streamlit as st
from stegano import lsb
from PIL import Image
import json
import os

st.set_page_config(page_title="Hide JSON in Image", page_icon="📁")
st.title("📁 Hide & Reveal JSON File in Image")

option = st.sidebar.selectbox(
    "Select Option",
    ("Hide JSON", "Reveal JSON")
)

# ================================================
if option == "Hide JSON":
    st.subheader("🔒 Hide a JSON File Inside an Image")

    # آپلود تصویر پوشش
    cover_img = st.file_uploader("Upload Cover Image", type=["png", "jpg", "jpeg"])

    # آپلود فایل JSON
    json_file = st.file_uploader("Upload JSON File", type=["json"])

    if cover_img and json_file:
        try:
            # خواندن محتوای فایل JSON
            json_content = json_file.read().decode("utf-8")

            # بررسی اعتبار JSON
            json.loads(json_content)  # اگر JSON نامعتبر باشه، خطا میده

            # باز کردن تصویر
            img = Image.open(cover_img).convert("RGB")

            # مخفی کردن JSON در تصویر
            stego_img = lsb.hide(img, json_content)

            # ذخیره تصویر نهایی
            save_path = "hidden_json_image.png"
            stego_img.save(save_path)

            st.success("✅ JSON file hidden successfully!")

            # نمایش اطلاعات
            st.write(f"📄 JSON size: {len(json_content)} characters")

            # دکمه دانلود
            with open(save_path, "rb") as file:
                st.download_button(
                    label="📥 Download Image with Hidden JSON",
                    data=file,
                    file_name="hidden_json_image.png",
                    mime="image/png"
                )

        except json.JSONDecodeError:
            st.error("❌ Invalid JSON file. Please upload a valid JSON.")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# ================================================
elif option == "Reveal JSON":
    st.subheader("🔓 Extract JSON from Image")

    stego_img = st.file_uploader("Upload Image with Hidden JSON", type=["png"])

    if stego_img:
        st.image(stego_img, caption="Uploaded Image", use_container_width=True)

        if st.button("🔎 Extract JSON"):
            try:
                img = Image.open(stego_img)
                hidden_data = lsb.reveal(img)

                if hidden_data:
                    # بررسی اینکه داده‌ی استخراج‌شده JSON معتبر هست یا نه
                    try:
                        json_data = json.loads(hidden_data)
                        st.success("✅ JSON extracted successfully!")

                        # نمایش JSON به صورت فرمت‌شده
                        st.json(json_data)

                        # دکمه دانلود فایل JSON
                        with open("extracted_data.json", "w", encoding="utf-8") as f:
                            json.dump(json_data, f, indent=4, ensure_ascii=False)

                        with open("extracted_data.json", "rb") as f:
                            st.download_button(
                                label="📥 Download Extracted JSON",
                                data=f,
                                file_name="extracted_data.json",
                                mime="application/json"
                            )

                    except json.JSONDecodeError:
                        st.warning("⚠️ Data extracted but it's not a valid JSON.")
                        st.code(hidden_data, language="text")
                else:
                    st.warning("⚠️ No hidden data found in this image.")

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
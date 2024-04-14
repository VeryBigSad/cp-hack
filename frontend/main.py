from io import BytesIO

import pandas as pd
import streamlit as st
from PIL import Image
from requests import post


# Placeholder for your model (Replace this with your actual model)
def sim_predict(image_id):
    predictions = post(f'http://85.192.33.132:8000/api/v1/similar-images?image_id={image_id}').json()['probabilities']
    return predictions

def class_predict(image_id):
    predictions = post(f'http://85.192.33.132:8000/api/v1/classify-image?image_id={image_id}').json()['probabilities']
    return predictions


uploaded_images = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"],
                                   accept_multiple_files=True)

images = []
images_id = []
images_dict = []
if uploaded_images:
    for uploaded_file in uploaded_images:
        image = Image.open(uploaded_file)
        images.append(image)

        img_bytes = BytesIO()
        image.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()

        image_id = post(f'http://85.192.33.132:8000/api/v1/upload-image', files={"image": img_bytes}).json()
        images_id.append(image_id)

    if st.button('Predict'):
        for image_id in images_id:
            sim_prediction = sim_predict(image_id['image_id'])
            sim_prediction = pd.DataFrame(sim_prediction)
            class_prediction = class_predict(image_id['image_id'])
            class_prediction = pd.DataFrame(class_prediction)
            name = sim_prediction.iloc[sim_prediction['probability'].idxmax()]['name']
            image_dict = {
                'name': name,
                'image_id': image_id['image_id'],
                'image_url': image_id['image_url'],
                'probability': class_prediction['probability'],
                'category': class_prediction['category'], # что тут то блять
                'suggestions': sim_prediction
            }
            images_dict.append(image_dict)

        images_df = pd.DataFrame(images_dict)

        st.markdown('### Экспонат относится к одной из категорий:')

        cats = pd.DataFrame(zip(images_dict[0]['category'], images_dict[0]['probability']),
                            columns=['category', 'probability'])

        st.bar_chart(cats, x='category', y='probability')

        suggestion = images_dict[0]['suggestions']
        highest = images_df['category'].iloc[0][images_df['probability'].values[0].idxmax()]
        st.markdown(f"### Скорее всего это {highest}, посмотреть все варианты:")

        table = st.data_editor(
            suggestion,
            column_config={
                "name": st.column_config.Column(
                    "Предложение",
                    width="medium",
                ),
                "image_url": st.column_config.ImageColumn(
                    "Фотография"
                ),
                "category": st.column_config.Column(),
                "probability": st.column_config.ProgressColumn(
                    "Вероятности",
                    format="%.3f",
                    min_value=0,
                    max_value=1,
                ),
            },
            hide_index=True,
        )

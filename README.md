# End-to-end-Waste-Detection-Using-Yolo-v5
This project involves training a YOLOv5 model on a custom dataset of 13 classes. The classes represent various waste items, and the model was trained on Google Colab for object detection. Additionally, a Flask app was developed with three routes for different functionalities.

![image](https://github.com/user-attachments/assets/7f82711f-db46-4670-a1a2-39c2e711e424)

![image](https://github.com/user-attachments/assets/19c0480b-665d-44cd-a0bd-57f2bf0ad3d7)


## Description

This project involves training the YOLOv5 model on a custom dataset with 13 waste detection classes. The model was trained on Google Colab, and the results are shown in the image below.

The classes used in this project are:

| Class ID | Class Name     |
|----------|----------------|
| 1        | Banana         |
| 2        | Chilli         |
| 3        | Drink Can      |
| 4        | Drink Pack     |
| 5        | Food Can       |
| 6        | Lettuce        |
| 7        | Paper Bag      |
| 8        | Plastic Bag    |
| 9        | Plastic Bottle |
| 10       | Plastic Container |
| 11       | Sweet Potato   |
| 12       | Tea Bag        |
| 13       | Tissue Roll    |

The model was trained using custom data ingested, validated, and processed using three dedicated classes for each task.

## Classes

The following classes were implemented for handling the different stages of the project:

- **Data Ingestion**: This class loads the custom dataset for training and validation.
- **Validation**: The validation class ensures data is loaded successfully.
- **Training**: This class contains the training of the YOLOv5 model using the custom dataset.

## Training Process

The training process was conducted on Google Colab using the YOLOv5 repository. The training was carried out with a custom dataset of 13 classes and was fine-tuned for optimal performance. The model was trained for 200 epochs to ensure sufficient learning and convergence.

### Results

The trained model achieved good results, which can be seen in the image below:

![image](https://github.com/user-attachments/assets/bcb070ab-293c-497f-b9fe-a717ab4347d4)


## Flask App

A Flask application was developed for integrating the trained YOLOv5 model. The Flask app exposes three routes to interact with the model:

### Routes

- **Home Route (`/`)**: A simple home route that renders the homepage of the app.
- **Predict Route (`/predict`)**: This route allows users to upload an image and get predictions from the YOLOv5 model. The model detects objects and returns the results.
- **Predict Live Route (`/live`)**: This route allows users to interact with the model in real-time using a camera.

## Getting Started

To run the project locally:

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

3. Create a conda environment
    ```bash
    conda create -n waste python=3.11 -y
    ```
    ```bash
    conda activate waste
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:
    ```bash
    python app.py
    ```

4. Access the app via `http://localhost:5000







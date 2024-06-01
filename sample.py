import os
from src.utils import load_object  # Importing your load_object function from your module
from src.exception import CustomException

if __name__ == "__main__":
    # Assuming the preprocessor.pkl file is located in the 'artifacts' folder
    file_path = r'artifacts\preprocessor.pkl'

    # Load the object
    try:
        loaded_object = load_object(file_path)
        print("Object loaded successfully.")
        # You can print or perform any further operations with the loaded object here
    except CustomException as ce:
        print("Custom Exception occurred:", ce)

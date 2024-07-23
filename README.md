# Hand Tracking Interface

This project uses OpenCV and the cvzone library to create a hand tracking interface. It can detect the number of fingers held up and open specific websites based on the number of fingers detected.

## Features
- Detects 0 to 5 fingers.
- Opens specific websites based on the number of fingers detected.

## Requirements

- Python 3.x
- OpenCV
- cvzone
- Pillow
- webbrowser (part of the Python standard library)

## Installation

1. **Clone the Repository**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a Virtual Environment (Optional but recommended)**

    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Application**

    ```bash
    python <your_script_name>.py
    ```

2. **Functionality**

    - Hold up 1 finger: Opens YouTube.
    - Hold up 2 fingers: Opens Instagram.
    - Hold up 3 fingers: Opens LinkedIn.
    - Hold up 4 fingers: Opens Portfolio.
    - Hold up 5 fingers: Reserved for future use.

## File Structure


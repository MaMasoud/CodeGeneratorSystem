# Image Code Generator using Flask

This is a simple web application built using Flask that allows users to generate images with codes from a CSV file.

## Features

- Upload an input image and a CSV file containing codes.
- Customize font size, font color, and code position on the image.
- Process the CSV file and generate images with codes embedded.

## Prerequisites

- Python 3.x
- Flask
- Pillow (PIL)

## Installation

1. Clone the repository or download the ZIP file.
2. Install the required packages by running:

pip install Flask Pillow


## Usage

1. Run the Flask application:

python app.py

markdown
Copy code

2. Open a web browser and navigate to `http://localhost:5000`.

3. Follow the on-screen instructions to upload an input image and a CSV file, and customize font settings.

4. Click "Process" to generate images with embedded codes.

5. Check the "Result" page to view and download the generated images.

## Project Structure

- `app.py`: The main Flask application file.
- `static/`: Static assets including uploaded files and generated images.
- `templates/`: HTML templates for rendering pages.

## Acknowledgments

This project uses the Flask web framework and the Pillow library for image manipulation.

## License

This project is licensed under the [MIT License](LICENSE).

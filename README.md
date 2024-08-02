# Gemini Q&A App

This is a simple Q&A web application built with Streamlit, utilizing the Gemini Free API to provide answers to user queries. The application allows users to input a question and receive an informative response.

## Features

- User-friendly interface for asking questions
- Utilizes the Gemini Free API to fetch and display responses
- Lightweight and easy to deploy

## Screenshot

![Gemini Q&A App Screenshot](./image.png)

## Installation

To run this application locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/gemini-qa-app.git
   cd gemini-qa-app
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

## Usage

1. Open your web browser and navigate to the local host.
2. Enter your question in the input box.
3. Click the "Ask the question" button.
4. The response will be displayed below the button.

## File Structure

- `app.py`: The main Streamlit application file.
- `requirements.txt`: List of dependencies required to run the app.
- `README.md`: This is readme file.
- `.gitigore`: This is gitignore file

## Dependencies

- `streamlit`: Streamlit library for building the web interface.
- `requests`: Library for making HTTP requests to the Gemini API.

You can install these dependencies using the `requirements.txt` file provided.

Link: https://llmdemossv27.streamlit.app/

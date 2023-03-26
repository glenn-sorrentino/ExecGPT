# ExecGPT Setup

This README provides instructions for setting up the ChatGPT web app in a development environment.

## Prerequisites

- Python 3.8 or higher
- A code editor (e.g., Visual Studio Code)

## Step 1: Clone the repository

1. Clone the repository containing the ChatGPT web app to your local machine.

```
git clone https://github.com/glenn-sorrentino/ExecGPT.git
```

## Step 2: Set up a virtual environment

1. Open a terminal/command prompt and navigate to the repository's root directory.
2. Create a virtual environment:

```
python3 -m venv venv
```

3. Activate the virtual environment:
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```
- On Windows:
  ```
  venv\Scripts\activate
  ```

## Step 3: Install the required packages

1. Install the required packages using the `requirements.txt` file:

```
pip install -r requirements.txt
```


## Step 4: Configure environment variables

1. Create a file named `.env` in the root directory of the project to store your environment variables. This file should not be committed to the repository, so add it to your `.gitignore` file if necessary.
2. Open the `.env` file and add the following line to set up the API key for OpenAI:

```
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenAI API key.
3. Save the `.env` file.

4. In the `app.py` file, add the following lines at the beginning to load the environment variables from the `.env` file:
```
from dotenv import load_dotenv
load_dotenv()
```

Make sure to install the python-dotenv package if you haven't already:

```
pip install python-dotenv
```

## Step 5: Run the application locally

1. Start the Flask development server:

```
python app.py
```

2. Open a web browser and navigate to `http://localhost:5000` to test the application.

## Step 6: Make changes to the code

1. Use your preferred code editor to make changes to the application's code.
2. Save your changes and restart the Flask development server to see the updates.

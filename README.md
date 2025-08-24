# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server

## Project Structure

- **frontend/**: Contains the Stramlit application code
- **backend/**: Contains the FastAPI backend server code
- **tests/**: Contains test cases
- **requirements/**: Lists required Python Packages
- **README.md/**: Provides an overview and instructions for the project.

## Setup Instructions

1. **Clone the repository**:
    ```bash
   git clone https://github.com/kvicky110202/Expense-Tracking-System.git
   cd expense-management-system
    ```
   
1. **Install dependencies**:
    ```commandline
   pip install -r requirements.txt
    ```
   
1. **Run the FastAPI server**:
    ```commandline
   uvicorn server.server:app --reload
    ```

1. **Run the Streamlit app**:
   ```commandline
   streamlit run frontend/app.py

   ```


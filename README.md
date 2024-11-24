# Good Buy's API Documentation 

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yogaputrap/Good-Buy.git
   ```

2. **Navigate to the project directory:**

   ```bash
   Good-Buy
   ```

3. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

   On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

5. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the FastAPI development server:**

   ```bash
   python -m uvicorn app.main:app --reload 
   ```

   The API will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

2. **Access the Swagger UI and ReDoc:**

   - Swagger UI: [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/)
   - ReDoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

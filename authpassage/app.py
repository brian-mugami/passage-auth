from main import create_app
from dotenv import find_dotenv,load_dotenv

load_dotenv(find_dotenv())

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=7000)
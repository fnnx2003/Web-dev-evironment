from flask import Flask
from flask_cors import CORS
import os
from sqlalchemy import create_engine, text
db_url = os.environ.get('DATABASE_URL')
engine = create_engine(db_url)

app = Flask(__name__)
CORS(app)
@app.route('/health')
def health():
    return {"status": "ok"}
@app.route('/db-check')
def db_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"database": "connected"}
    except Exception as e:
        return {"database": "error", "message": str(e)}, 500
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

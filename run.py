from main.config import app, db

# only true if run from run.py
if __name__ == '__main__':
    db.create_all()
    app.run(port=5000, debug=True)

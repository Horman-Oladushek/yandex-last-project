from app import app 


#все роуты для приложения
@app.route('/')
def index():
    return 'Hello, World!'

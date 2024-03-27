from app import app 


# Здесь ты уже пишешь все роуты для приложения
@app.route('/')
def index():
    return 'Hello, World!'

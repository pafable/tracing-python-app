from myapp import models, app
import os

print(os.getcwd())
print(os.listdir())
print(os.listdir('myapp'))

if __name__ == "__main__":
    with app.app_context():
        import setup
    app.run(debug=False, threaded=True)
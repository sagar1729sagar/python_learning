"""
This file contains the definition of  our Flask application.

It also runs the app if the file is executed
"""
# from flask import Flask
#
# app = Flask(__name__)
#
# if __name__ == '__main__':
#     app.run()

movies = ['The Matrix', 'Fast & Furious', 'Frozen', 'The life of Pi']

for movie in movies:
    print(movie)

print('We\'re done here!')

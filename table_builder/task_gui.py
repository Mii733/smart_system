# from flaskwebgui import FlaskUI  # import FlaskUI class

#You can also call the run function on FlaskUI class instantiation

# proc = subprocess.run('E:\\AccountingSystem\\venv\Scripts\\activate.bat',
#                         shell=True,
#                         stdin=subprocess.PIPE,
#                         stdout=subprocess.PIPE,
#                         )
# os.system('cmd /k "E:\\AccountingSystem\\venv\Scripts\\activate.bat"')
# time.sleep(11)

# FlaskUI(server='django',port=9000).run()



#################
from flaskwebgui import FlaskUI
from table_builder.wsgi import application as app
# from task_gui import app

if __name__ == "__main__":
    FlaskUI(app=app,server="django",port=9000).run()
###############################



# FlaskUI(server='django',port=9000).run()
# from flask import Flask

# # @app.route("/")
# def create_app():
#     app = Flask(__name__)


#     def index():
#         return "Hello World!"

#     return app

# if __name__ == '__main__':
#     app = create_app()
#     app.run() 




#################


# from flaskwebgui import FlaskUI
# from task.wsgi import application as app


# def start_django(**server_kwargs):

#     import waitress

#     waitress.serve(**server_kwargs)


# if __name__ == "__main__":

#     # Default start django

#     # FlaskUI(
#     #     app=app,
#     #     server="django",
#     #     width=800,
#     #     height=600,
#     # ).run()

#     # Default start django with custom kwargs

#     FlaskUI(
#         server="django",
#         server_kwargs={
#             "app": app,
#             "port": 9000,
#         },
#         width=800,
#         height=600,
#     ).run()
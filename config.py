"""gunicorn WSGI server configuration."""

from multiprocessing import cpu_count
from os import environ
from os import path
from os import popen

def max_workers():
    return cpu_count()


def env_variables():
    dir_path = path.dirname(path.realpath(__file__))
    environ["DIALOGFLOW_PROJECT_ID"] = "my-project-1534013250767"
    environ["GOOGLE_APPLICATION_CREDENTIALS"] = path.join(dir_path, "Project-e3414b3959c6.json")
    command = popen('echo $GOOGAUTH | base64 --decode > /app/Project-e3414b3959c6.json')
    return


env_variables()

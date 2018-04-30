from behave import *
import subprocess
import os

def before_scenario(context, scenario):
    context.server = subprocess.Popen('Python .\\features\\srv.py')

def after_scenario(context, scenario):
    context.server.terminate()
    try:
        os.remove(context.PATH)
    except:
        pass

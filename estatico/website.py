from flask import Blueprint
from flask import render_template
from pathlib import Path


blueprint_name = Path(__file__).stem
blueapp = Blueprint(blueprint_name, __name__)


@blueapp.route('/')
def index():
    return render_template(f'{blueprint_name}/hello.html')

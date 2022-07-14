from flask import Blueprint

from ..extensions import db
from ..models.video import Viedo

api = Blueprint('api', __name__)

@api.route('/video/<name>')
def create_user(name):
    # Viedo.query.filter_by(name= 'prokanzik').first()

 
    return 'Create User11'
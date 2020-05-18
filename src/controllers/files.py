from flask import render_template, Blueprint
from ..routes.files import routes_files

# ======
# CONTROLLER: FILES and potentially serve a REACT APP
# ======

files = Blueprint(
            'documentation',
            __name__,
            static_folder='../../static/templates',
            template_folder='../../static/templates',
        )

@files.route(**(routes_files['documentation']))
def documentation():
    return render_template('documentation.html', title='Mbrella documentation')

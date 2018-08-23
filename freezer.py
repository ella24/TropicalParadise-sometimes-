from flask_frozen import Freezer
from app import app, Beach

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

freezer = Freezer(app)

@freezer.register_generator
def show():
    for beach in Beach.query.all():
        yield { 'index': beach.index }

if __name__ == '__main__':
    freezer.freeze()
from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import URLmapForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLmapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    short = form.custom_id.data or get_unique_short_id()
    url_map = URLMap(
        original=form.original_link.data,
        short=short
    )
    db.session.add(url_map)
    db.session.commit()
    flash(url_for('redirect_original', short=short, _external=True))
    return render_template('index.html', url=url_map, form=form)


@app.route('/<string:short>')
def redirect_original(short):
    return redirect(URLMap.get_url_map_or_404(short).original)
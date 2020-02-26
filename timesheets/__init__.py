import os

from pyramid.config import Configurator

from bin import load_base_data
from data.db_session import DbSession


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()

    init_db()

    return config.make_wsgi_app()


def init_db():
    db_file = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'db',
        'timesheets.sqlite'
    )
    DbSession.global_init(db_file)
    load_base_data.load_starter_data()

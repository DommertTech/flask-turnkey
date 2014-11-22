from distutils.core import setup

setup(
    name='flask-turnkey',
    version='0.0.1',
    packages=['flask_starter.flask_rum', 'flask_starter.flask_turboduck', 'flask_starter.flask_turboduck.tests'],
    url='http://github.com/dommerttech/flask-turnkey',
    license='mit',
    author='Dommert',
    author_email='Dommert@Gmail.com',
    description='Provides starting point for flask projects. includes themes, templates,Database ORM, admin, user system, rest api.'
)

from setuptools import setup, find_packages

setup(
    name='api_julian',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-Login',
        'PyMySQL',
        'Werkzeug',
    ],
    entry_points={
        'console_scripts': [
            'runserver=run:app.run',
        ],
    },
)

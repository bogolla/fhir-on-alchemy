import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='fhir-server',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='SIL',
    description='FHIR Profiling and Slicing.',
    long_description=README,
    install_requires=[
        'alembic==0.8.5',
        'cryptography==1.3',
        'Flask==0.10.1',
        'Flask-Migrate==1.8.0',
        'Flask-Script==2.0.5',
        'Flask-SQLAlchemy==2.1',
        'gunicorn==19.4.5',
        'isodate==0.5.4',
        'itsdangerous==0.24',
        'Jinja2==2.8',
        'Mako==1.0.4',
        'MarkupSafe==0.23',
        'psycopg2==2.6.1',
        'python-editor==0.5',
        'requests==2.9.1',
        'six==1.10.0',
        'SQLAlchemy==1.0.12',
        'SQLAlchemy-Utils==0.32.0',
        'Werkzeug==0.11.4',

        'Sphinx==1.3.6',
        'sphinx-autobuild==0.6.0'
    ],
    url='https://github.com/bogolla/fhir-server',
    author='Brian Ogollah',
    author_email='brian.ogollah@savannahinformatics.com',
    keywords='FHIR Profiling Slicing',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: SIL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Clinical Informatics :: Interoperability',
    ],
)

from setuptools import setup, find_packages

VERSION = '0.1.0'

setup(
    name = 'django-goodies',
    version = VERSION,
    description = '**TESTING** useful goodies for use in multiple Django apps.',
    author = 'Micky Hulse',
    author_email = 'micky@hulse.me',
    maintainer = 'Micky Hulse',
    maintainer_email = 'micky@hulse.me',
    url = 'https://github.com/mhulse/django-goodies',
    license = 'http://www.gnu.org/copyleft/gpl.html',
    platforms = ['any'],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
)
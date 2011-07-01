from setuptools import setup, find_packages

setup(
    name='django-goodies',
    version='0.1.1',
    description='**TESTING** django-goodies',
    long_description=open('README.md').read(),
    author='Micky Hulse',
    author_email='micky@hulse.me',
    url='https://github.com/mhulse/django-goodies',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
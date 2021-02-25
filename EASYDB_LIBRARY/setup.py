from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: POSIX :: Linux',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='Easy DB',
    version='0.1dev',
    description='Creates Databases',
    author='Immanuel Fowler',
    author_email='immanuelfowlerr@gmail.com',
    url='',
    packages=find_packages(),
    license='MIT',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    install_requires=['os']
)
from setuptools import setup

setup(
    name='tally',
    version='0.1.0',    
    description='CLI Tally Counter',
    url='https://github.com/lacanlale/cli-tally',
    author='Jonathan Lacanlale',
    author_email='jonathanlacanlale98@gmail.com',
    packages=['tally'],
    entry_points = {
        'console_scripts': [
            'tally = tally.__main__:main'
        ]
    },
    install_requires=['pyfiglet>=0.8.post'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.5',
    ],
)
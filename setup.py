import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements-repl.txt', 'r') as f:
    requirements = f.read().split('\n')

setuptools.setup(
    name='makeit',
    version='0.1.0',
    author='DandyDrop',
    description='Helps when you need to hear what somebody said in telegram voice note',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/DandyDrop/make_voices_louder_tg',
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    keywords='make voice note louder telegram',
    install_requires=requirements
)

import setuptools

with open('requirements-repl.txt', 'r') as f:
    requirements = f.read().split('\n')

setuptools.setup(
    name='make_voices_louder_tg',
    version='0.1.0',
    install_requires=requirements,
    packages=setuptools.find_packages()
)

from setuptools import setup, find_packages

setup(
    name='meu_projeto',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        generate-lambda-routes=cli:generate_lambda_routes
    '''
)
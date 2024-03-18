from setuptools import setup, find_packages

setup(
    name='lambda_aws_creator',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        generate-lambda-routes=lambda_decorators.cli:generate_lambda_routes
    '''
)
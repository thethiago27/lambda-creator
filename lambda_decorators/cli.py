import click
import os
import json

from lambda_decorators.decorators import LambdaFunction


@click.command()
@click.option('--directory', default='.', help='The directory to search for Lambda functions. Defaults to the current '
                                               'directory.')
def generate_lambda_routes(directory):
    lambda_routes = []

    def find_decorated_functions(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if '@LambdaFunction' in line:
                    filename = os.path.basename(file_path)
                    function_name = lines[lines.index(line) + 1].strip().split()[1].split('(')[0]
                    lambda_routes.append({'filename': filename, 'function': function_name})

    def find_decorated_functions_in_directory(directory_path):
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    find_decorated_functions(file_path)

    find_decorated_functions_in_directory(directory)

    click.echo(json.dumps(lambda_routes, indent=2))


if __name__ == '__main__':
    generate_lambda_routes()

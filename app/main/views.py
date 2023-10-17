from . import main_blueprint


@main_blueprint.route('/')
def main():
    return 'Hello World!'
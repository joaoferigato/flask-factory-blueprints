from . import functionality_blueprint


@functionality_blueprint.route('/')
def functionality():
    return 'Hello World 2!'
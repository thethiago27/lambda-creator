def LambdaFunction(settings):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Aqui você pode adicionar lógica adicional antes ou depois de chamar a função decorada, se necessário
            result = func(*args, **kwargs)
            return result

        wrapper.name = settings.get('name', '')
        wrapper.description = settings.get('description', '')
        wrapper.timeout = settings.get('timeout', 10)
        wrapper.memorySize = settings.get('memorySize', 256)
        wrapper.environment = settings.get('environment', {})
        return wrapper

    return decorator

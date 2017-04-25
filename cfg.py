import os


def get_env(name, proto, fallback_name):
    val = os.environ.get(name)
    if val:
        return val
    fallback = os.environ.get(fallback_name)
    if not fallback:
        raise Error('Either {} or {} environment variables must be set'.format(name, fallback_name))
    return proto + fallback


def get_broker():
    return get_env('BROKER', 'amqp://', 'MASTER_IP')


def get_backend():
    return get_env('BACKEND', 'redis://', 'MASTER_IP')
import importlib

class BaseRegistry(type):

    CONTAINERS = {}

    def __new__(cls, name, bases, attrs):
        # instantiate a new type corresponding to the type of class being defined
        # this is currently RegisterBase but in child classes will be the child class
        new_cls = type.__new__(cls, name, bases, attrs)
        cls.CONTAINERS[new_cls.__name__.replace('Registry', '').lower()] = new_cls
        return new_cls

    @classmethod
    def get_registry(cls):
        return dict(cls.REGISTRY)


def get_benchmark(container_name: str, benchmark_name: str):
    importlib.import_module(f'benchsuite.{container_name}')
    benchmark_class = BaseRegistry.CONTAINERS[container_name].BENCHMARKS[benchmark_name]
    return benchmark_class()
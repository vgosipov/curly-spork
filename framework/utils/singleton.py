class Singleton(type):
    _instances = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in Singleton._instances:
            Singleton._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return Singleton._instances[cls]

    @staticmethod
    def get_instance():
        raise NotImplementedError

from datetime import datetime, timezone


def logger_factory(path):
    def logger(func):
        def wrapper(*args, **kwargs):
            called_at = datetime.now(timezone.utc)
            result = func(*args, **kwargs)
            with open(path, 'w') as f:
                f.write(f' Logged at: {called_at}')
                f.write(f' Name: {func.__name__}')
                f.write(f' Args: {args}')
                f.write(f' Kwargs: {kwargs}')
                f.write(f' Result: {result}')
                f.write("\n")
            return result
        return wrapper
    return logger


@logger_factory('log.txt')
def example(a, b, c=None):
    return 1


if __name__ == '__main__':
    example('1','2', c=1)





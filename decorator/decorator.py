def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Try again, please"
        except ValueError:
            return "Try again, please"
        except TypeError:
            return "Try again, please"

    return inner

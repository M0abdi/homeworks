def retry_on_exception(exceptions, max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
          #  return None ****
        return wrapper
    return decorator







retry_on_exception((ValueError, ZeroDivisionError), max_attempts=3)
def problematic_function(x):
    if x == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return 10 / x

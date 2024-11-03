def counter():
    count = 0  # 状態を保持

    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            print(f"{func.__name__}が{count}回呼ばれました")
            return func(*args, **kwargs)
        return wrapper

    return decorator

@counter()
def greet():
    print("こんにちは！")

greet()
greet()

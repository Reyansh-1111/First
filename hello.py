"""Simple greeting script."""

def greet(name: str = "world") -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("What's your name? ").strip() or "world"
    print(greet(user_name))
  

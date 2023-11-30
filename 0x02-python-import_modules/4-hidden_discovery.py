#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for func in dir(hidden_4):
        if func[1] != "_":
            print(func)

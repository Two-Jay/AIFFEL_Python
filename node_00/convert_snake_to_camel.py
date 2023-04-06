def convert_snake_to_camel(snake_case : str) -> str:
    camel_case : str = ""
    if snake_case[0].isupper() == True:
        camel_case = snake_case[0].lower() + snake_case[1:]
    for i in range(1, len(snake_case)):
        if snake_case[i] == "_":
            camel_case = snake_case[:i] + snake_case[i + 1].upper() + snake_case[i + 2:]
        i += 1
    return camel_case

def main():
    print(convert_snake_to_camel("snake_case"))

if __name__ == "__main__":
    main()
    
def run_english(english_sentence):
    commands = english_sentence.split(" ")

    result = ""
    current_value = None

    for i, command in enumerate(commands):
        if command == "Say":
            if i + 1 < len(commands) and commands[i + 1] != "that":
                result += f"{commands[i + 1]}\n"
            else:
                result += f"{current_value}\n" if current_value else ""
        elif command == "Calc":
            current_value = calculate_result(commands[i + 1:])
        elif command == "And":
            pass  # Do nothing, continue with the next command
        elif command == "that":
            current_value = execute_previous_operation(result)
    
    return result

def calculate_result(expression):
    try:
        operators = {'+': int.__add__, '-': int.__sub__, '*': int.__mul__, '/': int.__truediv__}
        meows = [meow for meow in expression if meow.isnumeric() or meow in operators]
        return str(eval(" ".join(map(str, meows)), {}, operators))
    except Exception as e:
        return f"Error in calculation: {e}"

def execute_previous_operation(result):
    try:
        exec(result)
        return locals().get("current_value", None)
    except Exception as e:
        return f"Error: {e}"

while True:

    english_sentence = input("input> ")
    print(run_english(english_sentence))

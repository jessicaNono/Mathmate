import math
def on_operation_button_clicked(instance, button):
    print(f'{button.text()} button clicked')
    # TODO: Implement operation logic here

def handle_equals_button_click(instance, button):
    # TODO: Implement the logic for the equals button
    input_text = instance.input_area.text()
    try:
        # Replace the trigonometric and other functions with their corresponding math function calls
        input_text = input_text.replace('sin', 'math.sin')
        input_text = input_text.replace('cos', 'math.cos')
        input_text = input_text.replace('tan', 'math.tan')
        input_text = input_text.replace('sqrt', 'math.sqrt')
        input_text = input_text.replace('^', '**')

        # Evaluate the expression safely
        result = eval(input_text, {"__builtins__": {}, "math": math})
        instance.result_display.setText(f'Result: {result}')
    except Exception as e:
        instance.result_display.setText(f'Error: {str(e)}')

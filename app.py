from flask import Flask, render_template, request, jsonify
from venn_visual import plot_venn
from sets_logic import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    img = None
    result_text = ""
    if request.method == 'POST':
        # получаем множества из формы
        raw_a = request.form.get('set_a', '')
        raw_b = request.form.get('set_b', '')
        operation = request.form.get('operation', 'union')  # получаем выбранную операцию

        # преобразование в Python set
        a = set(raw_a.replace(' ', '').split(',')) if raw_a else set()
        b = set(raw_b.replace(' ', '').split(',')) if raw_b else set()

        # Выбор операции
        if operation == 'union':
            result = union(a, b)
            operation_name = "объединения"
        elif operation == 'intersection':
            result = intersection(a, b)
            operation_name = "пересечения"
        elif operation == 'difference':
            result = difference(a, b)
            operation_name = "разности A\\B"
        elif operation == 'sym_diff':
            result = sym_diff(a, b)
            operation_name = "симметрической разности"
        elif operation == 'cartesian':
            result = cartesian(a, b)
            operation_name = "декартового произведения"
        
        # Форматирование результата
        if operation == 'cartesian':
            result_text = f"Результат {operation_name}: {', '.join(str(x) for x in result)}"
        else:
            result_text = f"Результат {operation_name}: {', '.join(str(x) for x in sorted(result))}"

        # генерируем диаграмму только для операций с 2-мя множествами
        if a and b:
            img = plot_venn(a, b)

    return render_template('index.html', img=img, result_text=result_text)

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    a = set(data.get('setA', '').replace(' ', '').split(',')) if data.get('setA') else set()
    b = set(data.get('setB', '').replace(' ', '').split(',')) if data.get('setB') else set()
    operation = data.get('operation', 'union')

    # Выбор операции
    if operation == 'union':
        result = union(a, b)
    elif operation == 'intersection':
        result = intersection(a, b)
    elif operation == 'difference':
        result = difference(a, b)
    elif operation == 'sym_diff':
        result = sym_diff(a, b)
    elif operation == 'cartesian':
        result = cartesian(a, b)
    else:
        result = set()

    # Если результат — множество кортежей (для декартового произведения), конвертируем в список строк
    if operation == 'cartesian':
        result_list = [str(t) for t in result]
    else:
        result_list = list(result)

    return jsonify({'result': result_list})

if __name__ == '__main__':
    app.run(debug=True)

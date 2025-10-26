# venn_visual.py
import matplotlib
matplotlib.use('Agg')  # <- критично! Без оконного backend
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import io
import base64

def plot_venn(a, b, set_labels=('A', 'B')):
    """
    Создаёт диаграмму Венна для двух множеств и возвращает изображение в base64 для вставки в HTML.
    
    :param a: множество A (set)
    :param b: множество B (set)
    :param set_labels: подписи множеств
    :return: base64 строка с изображением
    """
    # Создаём фигуру
    plt.figure(figsize=(5,5))
    
    # Строим диаграмму Венна
    v = venn2([a, b], set_labels=set_labels)

    # Подписи элементов каждого сектора (если не пусто)
    for idx, subset in enumerate(v.subset_labels):
        if subset:
            subset.set_text(subset.get_text())

    # Сохраняем в буфер PNG
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()  # закрываем фигуру, чтобы не создавались окна
    buf.seek(0)
    
    # Конвертируем в base64 для вставки в HTML <img>
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return img_base64

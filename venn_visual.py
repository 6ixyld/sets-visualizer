# venn_visual.py
import matplotlib
matplotlib.use('Agg')  # <- критично! Без оконного backend
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import io
import base64

def plot_venn(a, b, set_labels=('A', 'B')):
    """
    Создаёт красивую диаграмму Венна для двух множеств с отображением элементов.
    """
    # Создаём фигуру с современным дизайном
    plt.figure(figsize=(8, 8), facecolor='#f8f9fa')
    ax = plt.gca()
    ax.set_facecolor('#f8f9fa')
    
    # Цветовая схема
    colors = ['#ff6b6b', '#4ecdc4']
    text_color = '#2d3436'
    
    # Строим диаграмму Венна
    v = venn2([a, b], set_labels=set_labels, 
              set_colors=colors, alpha=0.8)
    
    # Очищаем стандартные подписи с количествами и добавляем элементы
    for label in v.subset_labels:
        if label:
            label.set_text('')
    
    # Добавляем элементы множества A только (левая часть)
    if a - b:
        elements_a = sorted(a - b)
        v.get_label_by_id('10').set_text('\n'.join(map(str, elements_a)))
    
    # Добавляем элементы пересечения A∩B (центральная часть)
    if a & b:
        elements_intersect = sorted(a & b)
        v.get_label_by_id('11').set_text('\n'.join(map(str, elements_intersect)))
    
    # Добавляем элементы множества B только (правая часть)
    if b - a:
        elements_b = sorted(b - a)
        v.get_label_by_id('01').set_text('\n'.join(map(str, elements_b)))
    
    # Настраиваем подписи множеств
    for label in v.set_labels:
        if label:
            label.set_fontsize(16)
            label.set_fontweight('bold')
            label.set_color(text_color)
    
    # Настраиваем подписи элементов
    for subset_label in v.subset_labels:
        if subset_label:
            subset_label.set_fontsize(12)
            subset_label.set_fontweight('normal')
            subset_label.set_color(text_color)
    
    # Настраиваем внешний вид окружностей
    for patch in v.patches:
        if patch:
            patch.set_edgecolor('#2d3436')
            patch.set_linewidth(2)
            patch.set_linestyle('-')
    
    # УБРАЛ ЗАГОЛОВОК ДИАГРАММЫ
    # plt.title('Диаграмма Венна', color=text_color, fontsize=18, pad=20, fontweight='bold')
    
    # Убираем оси для чистого вида
    ax.axis('off')
    
    # Сохраняем с высоким качеством
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', 
                facecolor=ax.get_facecolor(), dpi=150, 
                transparent=False, edgecolor='none')
    plt.close()
    
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return img_base64

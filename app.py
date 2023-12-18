from flask import Flask, render_template
import io
import base64
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def espiral_matplotlib(n):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    ax.axis('off')

    fib_sequence = fibonacci(n)

    # Calcular las coordenadas para la espiral de Fibonacci con un ángulo gradual y desfase
    x = []
    y = []
    for i in range(n):
        angle = i * 0.3 + i * 0.1  # Ajustar el ángulo y el desfase para obtener una espiral asimétrica
        x.append(i * np.cos(angle))
        y.append(i * np.sin(angle))

    ax.plot(x, y, color='SteelBlue', linewidth=2)

    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight', pad_inches=0)
    img.seek(0)

    encoded_img = base64.b64encode(img.read()).decode('utf-8')
    plt.close()

    return encoded_img

@app.route('/')
def index():
    n = 20
    encoded_img = espiral_matplotlib(n)
    return render_template('index.html', image=encoded_img)

if __name__ == '__main__':
    app.run(debug=True)






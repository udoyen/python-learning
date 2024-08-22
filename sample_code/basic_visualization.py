import matplotlib.pyplot as plt

def plot_graph(x, y, title, x_label, y_label):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()
    
    
# Usage
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]
plot_graph(x, y, 'Sample Line Graph', 'X-Axis', 'Y-Axis')

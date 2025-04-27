import matplotlib.pyplot as plt


def plot_best_tour(coords, tour, length=None):
    # tüm şehir noktaları
    all_x = [c[0] for c in coords.values()]
    all_y = [c[1] for c in coords.values()]
    # tur sırasına göre çizim
    xs = [coords[i][0] for i in tour]
    ys = [coords[i][1] for i in tour]

    plt.figure(figsize=(8, 6))
    plt.scatter(all_x, all_y, s=30, label='Cities', alpha=0.5)
    plt.plot(xs, ys, marker='o', linewidth=1.5, label='Best tour')
    for node, (x, y) in coords.items():
        plt.text(x, y, str(node), fontsize=7, ha='right', va='bottom')

    title = "Best TSP Tour"
    if length is not None:
        title += f" (len={length:.2f})"
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

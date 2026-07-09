from pathlib import Path
import matplotlib.pyplot as plt


def save_bar_chart(data, title, xlabel, ylabel, filename, output_dir):
    output_dir.mkdir(exist_ok=True)

    plt.figure(figsize=(10, 6))

    data.plot(kind="bar")

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig(output_dir / filename)

    plt.close()
import math
from pathlib import Path
import random
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from termcolor import colored

COLORS = [
    # "black",
    "red",
    "yellow",
    "green",
    "cyan",
    "blue",
    "magenta",
    # "white",
    "light_grey",
    "dark_grey",
    "light_red",
    "light_yellow",
    "light_green",
    "light_cyan",
    "light_blue",
    "light_magenta",
]
__counter = 0


def cprint(*vals):
    """Log values, highlighting any prefixed by a color tag (e.g., 'red:error')."""
    global __counter
    __counter = 0

    def fmt(v):
        if isinstance(v, (int, float)):
            v = f"blue:{v:,}"
        if isinstance(v, tuple):
            v = f"blue:{v}"
        else:
            v = str(v)

        if v.startswith("rand:"):
            global __counter
            # v = v.replace("rand:", f"{random.choice(COLORS)}:")
            v = v.replace("rand:", f"{COLORS[__counter%len(COLORS)]}:")
            __counter += 1
        for c in COLORS:
            tag = f"{c}:"
            if v.startswith(tag):
                return colored(v[len(tag) :], c, attrs=["bold"])
        return v

    vals = map(fmt, vals)
    print(*vals)


def imshow(
    images: (
        list[Image.Image | np.ndarray | str | Path]
        | dict[str, Image.Image | np.ndarray | str | Path]
    ),
    size=4,
    cols: int = None,
    cmap="grey",
    vrange=(None, None),
):
    """Plot a list of PIL images in a grid

    Args:
        images (list[Image.Image]): the list of images to show
        size (int, optional): the size in inch of the images
        col (int, optional): The number of columns of the grid. Defaults to 1.
    """
    if isinstance(images, (Image.Image, str, Path, np.ndarray)):
        images = [images]
    titles = None
    if isinstance(images, dict):
        titles, images = list(images.keys()), list(images.values())
    else:
        images = list(images)
        if not images:
            return
    for i in range(len(images)):
        if not isinstance(images[i], (Image.Image, np.ndarray)):
            images[i] = Image.open(images[i])

    if not cols:
        cols = min(10, len(images))
    rows = math.ceil(len(images) / cols)
    max_ratio = max(
        (
            image.size[0] / image.size[1]
            if isinstance(image, (Image.Image))
            else image.shape[0] / image.shape[1]
        )
        for image in images
    )
    _, axes = plt.subplots(
        rows, cols, figsize=(cols * size, int(rows * size * max_ratio))
    )
    if rows > 1 or cols > 1:
        axes = axes.flatten()
    else:
        axes = [axes]
    for i, img in enumerate(images):
        axes[i].imshow(img, cmap=cmap, vmin=vrange[0], vmax=vrange[1])
        if titles:
            axes[i].set_title(titles[i])
        axes[i].axis("off")
    plt.tight_layout()
    plt.show()

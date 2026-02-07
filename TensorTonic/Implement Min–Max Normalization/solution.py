import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    if X:
        x_array = np.asarray(X)
        min_x = np.min(X, axis=axis, keepdims=True)
        max_x = np.max(X, axis=axis, keepdims=True)
        denominator = (x_array - min)/(max-min)
        top = x_array - min_x
        bot = max_x - min_x
        bot_x = np.maximum(bot, eps)
        return top/bot_x
    return None
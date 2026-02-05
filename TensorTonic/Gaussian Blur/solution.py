import math 

def gaussian(x, y, sigma):

    top = -1 * (x**2+y**2)/(2*(sigma**2))
    return math.exp(top)
    
def gaussian_kernel(size, sigma):
    """
    Generate a normalized 2D Gaussian blur kernel.
    """
    # Write code here
    height = size 
    width = size
    center = size // 2
    total = 0 
    out = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            x = j - center 
            y = i - center 
            value = gaussian(x, y, sigma)
            out[i][j] = value
            total += value

    for i in range(height):
        for j in range(width):
            out[i][j] /= total
    return out



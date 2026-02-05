def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    # Write code here
    H = len(X)
    W = len(X[0])

    out_h =  (H - pool_size) // stride + 1
    out_w =  (W - pool_size) // stride + 1

    output = [[0 for _ in range(out_w)] for _ in range(out_h)]

    for i in range(out_h):
        for j in range(out_w):
            max__value = X[i*stride][j*stride]
            for m in range(pool_size):
                for n in range(pool_size):
                    if X[i*stride + m][j*stride + n] > max__value:
                        max__value = X[i*stride + m][j*stride + n]
            output[i][j] = max__value
    return output
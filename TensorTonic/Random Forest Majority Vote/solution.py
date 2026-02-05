def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    samples = len(predictions[0])
    predicts = []
    for i in range(samples):
        counter = {}
        for pred in predictions: 
            counter[pred[i]] = counter.get(pred[i], 0) + 1
        highest = find_max(counter)
        predicts.append(highest)
    return predicts

def find_max(fred: dict):
    max_value = max(fred.values())
    max_keys = []
    for key, value in fred.items():
        if value == max_value:
            max_keys.append(key)
    return min(max_keys)
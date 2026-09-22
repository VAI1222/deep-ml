def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    samples = list(samples)
    if not samples:
        return []

    counts = {}
    for sample in samples:
        counts[sample] = counts.get(sample,0) + 1

    total_count = len(samples)

    return [(val, count / total_count) for val, count in sorted(counts.items())]
    pass
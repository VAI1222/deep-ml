import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    arr = np.array(data)
    mean_val = float(np.mean(arr))
    median_val = float(np.median(arr))
    values, counts=np.unique(arr, return_counts=True)
    mode_val = float(values[np.argmax(counts)])
    variance_val = float(np.var(arr, ddof=0))
    std_val = float(np.std(arr, ddof=0))
    p25 = float(np.percentile(arr, 25))
    p50 = float(np.percentile(arr, 50))
    p75 = float(np.percentile(arr, 75))
    iqr_val = float(p75 - p25)
    return{
        'mean' : mean_val,
        'median' : median_val,
        'mode' : mode_val,
        'variance' : variance_val,
        'standard_deviation' : std_val,
        "25th_percentile" : p25,
        "50th_percentile" : p50,
        "75th_percentile" : p75,
        "interquartile_range" : iqr_val
    }
import math
import numpy as np

def safe_float(x, default=0.0):
    try:

        if x is None:
            return default

        if isinstance(x, (float, int)):
            if math.isnan(x) or math.isinf(x):
                return default
            return float(x)

        if isinstance(x, np.floating):
            if np.isnan(x) or np.isinf(x):
                return default
            return float(x)

        return float(x)

    except:
        return default

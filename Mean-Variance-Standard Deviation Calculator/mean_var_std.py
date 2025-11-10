import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 NumPy array
    arr = np.array(lst).reshape(3,3)
    
    # Create dictionary with all calculations
    calculations = {
        'mean': [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean().tolist()],
        'variance': [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var().tolist()],
        'standard deviation': [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.std().tolist()],
        'max': [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max().tolist()],
        'min': [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min().tolist()],
        'sum': [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum().tolist()]
    }
    
    return calculations

if __name__ == "__main__":
    example = [0,1,2,3,4,5,6,7,8]
    print(calculate(example))

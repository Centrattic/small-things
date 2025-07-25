import numpy as np

d = 10000  # High dimension
num_trials = 1000

angles = []
for _ in range(num_trials):
    x = np.random.randn(d)
    y = np.random.randn(d)

    # True of non unit vectors too, but more true if vectors are normalized.
    
    x /= np.linalg.norm(x)
    y /= np.linalg.norm(y)
    cos_theta = np.dot(x, y)
    angle = np.arccos(np.clip(cos_theta, -1.0, 1.0)) * 180 / np.pi
    angles.append(angle)

print(f"Average angle: {np.mean(angles)} degrees")  # Should be close to 90


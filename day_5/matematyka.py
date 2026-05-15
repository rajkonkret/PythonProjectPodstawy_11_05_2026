import math

print(math.pi)  # 3.141592653589793
print(len(str(math.pi)))  # 17

print(math.sqrt(25))  # 5.0
# SciPy, nympy, pandas

# sin 30 stopni
angle_radians = math.radians(30)
print(math.sin(angle_radians))  # 0.49999999999999994

angles = [0, 30, 45, 60, 90]
sin_values = [math.sin(math.radians(a)) for a in angles]
print(sin_values)
# [0.0, 0.49999999999999994, 0.7071067811865476, 0.8660254037844386, 1.0]

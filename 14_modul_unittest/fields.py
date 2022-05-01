# fields.py

def rectangle(a, b):
  return a * b

def triangle(a, h):
  return 0.5 * a * h

print(rectangle(4, 6))
print(triangle(4, 6))

print(rectangle(4, 6) == 24)
print(triangle(4, 6) == 12)
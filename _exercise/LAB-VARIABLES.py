#<h1> "LAB-VARIABLES"

box = 'cola:9 bottles:1 liter'
print(box)

box = box.upper()
print(box)

box = box.lower()
print(box)

box_splited = box.split(':')
print(box_splited)

helloMessage = "Hello %s!"

print(helloMessage % ("Kate"))
print(helloMessage % ("Chris"))

helloMessage = "Hello {0:s}!"

print(helloMessage.format("Kate"))
print(helloMessage.format("Chris"))

helloMessage = "%s has %d %s"

print(helloMessage % ("Kate", 1, "animal"))
print(helloMessage % ("Chris", 100000, "$"))

helloMessage = "{0:s} has {1:d} {2:s}"

print(helloMessage.format("Kate", 1, "animal"))
print(helloMessage.format("Chris", 100000, "$"))

line = "{0:20s} costs {1:6d} €"

print(line.format('ICE CREAM', 3))
print(line.format('TRIP TO VENICE', 119))
print(line.format('PIZZA HAWAII', 6))

line = '{0:s} {1:d}'

print(line.format('ICE CREAM', 3))
print(line.format('TRIP TO VENICE', 119))
print(line.format('PIZZA HAWAII', 6))
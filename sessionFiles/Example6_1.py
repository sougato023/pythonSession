#tuple - immutable
dimensions = (200,20,78)
for dimension in dimensions:
    print("Dimension : "+str(dimension))

print("x-coordinate: "+str(dimensions[0]))

#dimensions[0] = 100

print("New Dimensions")
dimensions = (100,20,78)
for dimension in dimensions:
    print("Dimension : "+str(dimension))

dimensions = ["sougato", "michale","xi"]
for dimension in dimensions:
    print("Dimension : "+dimension)
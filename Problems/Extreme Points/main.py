# The following line creates a dictionary from the input. Do not modify it, please
# test_dict = {"a": 43, "b": 1233, "c": 8}
test_dict = json.loads(input())

# Work with the 'test_dict'
minimum = min(test_dict.items(), key=lambda item: item[1])
maximum = max(test_dict.items(), key=lambda item: item[1])
print("min:", minimum[0])
print("max:", maximum[0])


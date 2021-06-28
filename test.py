import ast
import json

# initializing string 
test_string = '{"s": 0.6, "h": -1}'

res = ast.literal_eval(test_string)

print("The converted dictionary : " + str(res))

print(type(res))

res = json.loads(test_string)

print("The converted dictionary : " + str(res))

print(type(res))

res = dict(test_string)

print("The converted dictionary : " + str(res))

print(type(res))

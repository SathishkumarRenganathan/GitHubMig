import pickle

class writePickling:
    a_number = 12
    a_string = 'welcome'
    a_list = ['Hello', 'welcome', 'to', 'python']
    a_tuple = ('Hi','welcome','to','data science')
    a_set = {'python','bigdata','GCP'}
    a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}

myObj = writePickling()
myPickledObject = pickle.dumps(myObj)
print(f"This is my pickled object:\n{myPickledObject}\n")

myUnPickledObject = pickle.loads(myPickledObject)
print(f"This is a_dict of the unpickled object:\n{myUnPickledObject.a_dict}\n")
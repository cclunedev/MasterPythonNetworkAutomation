def serialize(targetObject, outputFile, pickleOrJson='json'):
#This function takes an input object and serializes it into a JSON text or Pickle binary file 

  if pickleOrJson == 'json':
    with open(outputFile, 'w') as file:
      import json
      jsonString = json.dumps(targetObject)
      file.write(jsonString)


  elif pickleOrJson == 'pickle':
    import pickle
    with open(outputFile, 'wb') as file:
      pickle.dump(targetObject, file)


def deserialize(inputFile, pickleOrJson='json'):
#This function deserializes data from a Pickle or JSON data file
#If pickleOrJson = json, the function takes a JSON string text file and returns a dict
#If pickleOrJson = pickle, the function takes a pickled binary file and returns the file's object

  if pickleOrJson == 'json':
    import json
    with open(inputFile, 'r') as file:
      jsonOutput = json.load(file)
    return jsonOutput

  elif pickleOrJson == 'pickle':
    import pickle
    with open(inputFile, 'rb') as file:
      pickleOutput = pickle.load(file)
    return pickleOutput

# FileJson

**This is a small library for conveniently working with json format files, adding, removing ...**

The programming language here is python, and the json library.
The main class is **FileJson**, which takes 1 parameter, this is the name of the file **(without json extension)**

```python
   from FileJson import FileJson

   FJ = FileJson("NameFile")
```

The class has a **temp** variable to which you can add an object of type dict, this will be the template of our json object in the file.
**This is an optional parameter**!

```python
	...
	FJ.temp = {
		"data": {},
		"outdata": {}
	}

```

**There are several methods to work with:**

- add
- delete
- relocate
- if_read
- read
- create
- addDex



## Add

Accepts one required parameter and three optional parameters
This method allows you to add or change data in an object

**required parameter:**
An array of dict objects to be added to the main or secondary
Example:
```python
	...
	data = [
		{
			"key": "value"
		}
	]
	FJ.add(data)

	print(FJ.temp) # {"data": {},"outdata": {}, "key": "value"}
```

**Optional Parameters:**
**1**
It is in the second parameter that you can pass the name of the object key in the main object, which will be the secondary one.
Example:
```python
	...
	data = [
		{
			"key": "value"
		}
	]
	FJ.add(data, 'data')

	print(FJ.temp) # {"data": {"key": "value"},"outdata": {}}
```
**2**
If you pass 3 parameter to true you can achieve the following. You don't need to specify an array of objects, but you can only provide one dict in the first parameter
Example:
```python
	...
	data = {
		"key": "value"
	}
	FJ.add(data, 'data', True)

	print(FJ.temp) # {"data": {"key": "value"},"outdata": {}}
```
**3**
The fourth default argument in the "True" position is necessary in order to limit the consciousness of the file, namely not to create it
Example:
```python
	...
	data = {
		"key": "value"
	}
	FJ.add(data, 'data', True, False) # The file will not be created or modified

	print(FJ.temp) # {"data": {"key": "value"},"outdata": {}}
```


## delete

Accepts one required parameter and three optional parameters
This method allows you to delete by keys from an object

**required parameter:**
Array of keys of an object of type "dict"
Example:
```python
	...
	FJ.delete(['data'])

	print(FJ.temp) # {'outdata': {}}
```

**Optional Parameters:**
**1**
It is in the second parameter that you can pass the name of the object key in the main object, which will be the secondary one.
Example:
```python
	...
	FJ.delete(['key'], 'data')

	print(FJ.temp) # {"data": {},"outdata": {}}
```

**2**
If you pass 3 parameter to true you can achieve the following. You don't need to specify an array of objects, but you can only provide one dict in the first parameter
Example:
```python
	...
	FJ.delete('key', 'data', True)

	print(FJ.temp) # {"data": {},"outdata": {}}
```

**3**
The fourth default argument in the "True" position is necessary in order to limit the consciousness of the file, namely not to create it
Example:
```python
	...
	FJ.delete('key', 'data', True, False) # The file will not be created or modified

	print(FJ.temp) # {"data": {},"outdata": {}}
```

## relocate

Accepts three required parameters and one optional parameter
This method allows you to transfer from one object by keys to another

**required parameter:**
**1**
Under which key to put the copied object
```python
	...
	FJ.relocate('outdata', 'data', ['key'])

	print(FJ.temp) # {"data": {},"outdata": {'key': 'value'}}
```

**2**
From which key will the objects be taken
```python
	...
	FJ.relocate('outdata', 'data', ['key'])

	print(FJ.temp) # {"data": {},"outdata": {'key': 'value'}}
```

**2**
Array of keys which keys values will be copied copied
```python
	...
	FJ.relocate('outdata', 'data', ['key'])

	print(FJ.temp) # {"data": {},"outdata": {'key': 'value'}}
```

**Optional Parameters:**
The fourth default argument in the "True" position is necessary in order to limit the consciousness of the file, namely not to create it
Example:
```python
	...
	FJ.relocate('outdata', 'data', ['key'], False) # The file will not be created or modified

	print(FJ.temp) # {"data": {},"outdata": {'key': 'value'}}
```


## addDex
It works as the "add" method, but in this case it is made as a decorator
Example:
```python
	...
	data = [
		{
			"key": "value"
		}
	]
	@FJ.addDex(data)
	def creates (temp):
		print(temp) # {"data": {},"outdata": {}, "key": "value"}

	creates()
```

**Methods "if_read", "read", "create" auxiliary**


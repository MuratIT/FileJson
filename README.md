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



## Add

Takes one required parameter and two optional

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
```

**Optional Parameters:**
##### 1
It is in the second parameter that you can pass the name of the object key in the main object, which will be the secondary one.
Example:
```python
	...
	FJ.add(data, 'namekey')
```
##### 2
If you pass 3 parameter to true you can achieve the following. You don't need to specify an array of objects, but you can only provide one dict in the first parameter
Example:
```python
	...
	data = {
		"key": "value"
	}
	FJ.add(data, 'namekey', True)
```





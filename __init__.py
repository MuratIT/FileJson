from FileJson import FileJson

if __name__ == '__main__':
	FJ = FileJson("data")
	FJ.temp = {
		"data": {},
		"outdata": {} 
	}


	data = [
		{
			"09.09.2021": {
				"text": "Hello!",
				"image": False
			}
		},
		{
			"10.09.2021": {
				"text": "Hello1!",
				"image": False
			}
		}
	]

	@FJ.addDex(data)
	def creates (temp):
		print(temp)

	creates()

	# FJ.add(data, 'data')

	# FJ.delete(["data", "outdata"])

	# FJ.relocate('outdata', 'data', ["10.09.2021", "09.09.2021"])
	# print(FJ.temp )
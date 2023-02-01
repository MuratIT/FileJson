import json


class FileJson:
    def __init__(self, file_name):
        self.file_name = file_name
        self.temp = {}

    def create(self, data, path=False):
        if not path:
            file_name = self.file_name
        else:
            file_name = path

        with open(f"{file_name}.json", "w") as write_file:
            json.dump(data, write_file)

    def read(self, path=False):
        if not path:
            file_name = self.file_name
        else:
            file_name = path

        with open(f"{file_name}.json", "r", encoding="utf-8") as read_file:
            data = json.load(read_file)
        return data

    def if_read(self, create=True):
        try:
            read_data = self.read()
        except:
            if create:
                self.create(self.temp)
                read_data = self.read()
            else:
                try:
                    read_data = self.read()
                except:
                    read_data = self.temp

        return read_data

    def relocate(self, item1, item2, array, create=True):
        read_datas = self.if_read()
        self.temp[item1] = read_datas[item1]

        for keyp, valuep in read_datas[item2].items():
            if keyp in array:
                self.temp[item1][keyp] = valuep
            else:
                self.temp[item2][keyp] = valuep

        if create:
            self.create(self.temp)

    def __intdict_data(self, item, dict_data):
        for key, value in dict_data.items():
            if item:
                self.temp[item][key] = value
            else:
                self.temp[key] = value

    def add(self, dict_datas, item=False, ifArray=True, create=True):
        read_datas = self.if_read(create)

        for key, value in read_datas.items():
            self.temp[key] = value

        if ifArray:
            for dict_data in dict_datas:
                self.__intdict_data(item, dict_data)
        elif not ifArray:
            self.__intdict_data(item, dict_datas)

        if create:
            self.create(self.temp)

    def addDex(self, dict_datas, item=False, ifArray=True, create=True):
        def add_dex(func):
            def dex():
                self.add(dict_datas=dict_datas, item=item, ifArray=ifArray, create=create)
                func(self.temp)

            return dex

        return add_dex

    def delete(self, keys, item=False, ifArray=True, create=True):
        read_datas = self.if_read(create)
        for key, value in read_datas.items():
            self.temp[key] = value

        if ifArray:
            for key in keys:
                if not item:
                    self.temp.pop(key, 'ERROR')
                else:
                    self.temp[item].pop(key, 'ERROR')
        else:
            if not item:
                self.temp.pop(keys, 'ERROR')
            else:
                self.temp[item].pop(keys, 'ERROR')

        if create:
            self.create(self.temp)

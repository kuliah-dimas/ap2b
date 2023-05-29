import json


def program1():
    data_json = open("data.json")
    data = json.loads(data_json.read())

    for i in range(len(data)):
        print(f"Nama: {data[i]['name']}")
        print(f"NPM: {data[i]['npm']}")
        print(f"Kelas: {data[i]['kelas']}")
        print(f"Fakultas: {data[i]['fakultas']}")
        print(f"Jurusan: {data[i]['jurusan']}")
        print()


program1()

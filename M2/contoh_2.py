import json


def program2():
    json_data = {
        "profiles": [
            {
                "name": "Muharomarrizki Viandra",
                "npm": "51422176",
                "kelas": "1IA24",
                "fakultas": "FTI",
                "jurusan": "Teknik Informatika"
            },
            {
                "name": "Reihan Saputra",
                "npm": "50422012",
                "kelas": "1IA27",
                "fakultas": "FTI",
                "jurusan": "Teknik Informatika"
            },
            {
                "name": "Ucok Babi",
                "npm": "504220123",
                "kelas": "1IA24",
                "fakultas": "FTI",
                "jurusan": "Teknik Informatika"
            },
            {
                "name": "Dimaskul",
                "npm": "5042201123",
                "kelas": "1IA24",
                "fakultas": "FTI",
                "jurusan": "Teknik Informatika"
            },
            {
                "name": "Putri Indo",
                "npm": "504220112",
                "kelas": "1IA24",
                "fakultas": "FTI",
                "jurusan": "Teknik Informatika"
            }
        ]
    }

    read_json = json.dumps(json_data, indent=3)

    print(read_json)


program2()

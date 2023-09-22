import json

import requests

# headers = {
#     'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Connection': 'keep-alive',
#     'Origin': 'https://dk.mosreg.ru',
#     'Referer': 'https://dk.mosreg.ru/',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-site',
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
#     'accept': '*/*',
#     'content-type': 'application/json',
#     'front-end-version': '2023-09-18 09:00',
#     'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
#     'sec-ch-ua-mobile': '?1',
#     'sec-ch-ua-platform': '"Android"',
# }
#
# json_data = {
#     'operationName': 'TeachersCatalog',
#     'variables': {
#         'page': 1,
#         'limit': 12,
#         'houseOfCultureId': 'e7e5fd86-fd26-4c25-a31f-e2ecbe1f7586',
#     },
#     'query': 'query TeachersCatalog($houseOfCultureId: [String], $limit: Int, $page: Int, $listUrbanDistrictId: [String], $gender: String, $workshopCategoryId: [String], $order: [OrderInput], $minAge: Int, $maxAge: Int) {\n  TeachersCatalog(\n    hasWorkshopInHouseOfCulture: true\n    houseOfCultureId: $houseOfCultureId\n    workshopCategoryId: $workshopCategoryId\n    limit: $limit\n    page: $page\n    listUrbanDistrictId: $listUrbanDistrictId\n    gender: $gender\n    order: $order\n    minAge: $minAge\n    maxAge: $maxAge\n    statusId: [1]\n  ) {\n    data {\n      id: userStaffId\n      middleName\n      lastName\n      firstName\n      imageCoverObject {\n        imageId\n        value\n        __typename\n      }\n      fullLengthOfWork\n      workshopCategories\n      rating\n      workshopCategory {\n        name\n        id: workshopCategoryId\n        __typename\n      }\n      workshops {\n        name\n        workshopCategoryId\n        __typename\n      }\n      age\n      workshopsInHousesOfCulture {\n        id: houseOfCultureId\n        name\n        slug\n        city {\n          id: cityId\n          name\n          __typename\n        }\n        __typename\n      }\n      housesOfCulture {\n        id: houseOfCultureId\n        name\n        slug\n        city {\n          id: cityId\n          name\n          __typename\n        }\n        __typename\n      }\n      isPrivatePractice\n      __typename\n    }\n    hasMorePages: has_more_pages\n    currentPage: current_page\n    __typename\n  }\n}',
# }
#
# response = requests.post('https://api.dk.mosreg.ru/graphql', headers=headers, json=json_data).json()
#
#
#
# with open(f"new.json", "w", encoding="utf-8") as file:
#     json.dump(response, file, indent=4, ensure_ascii=False)

with open('new.json', 'r', encoding="utf-8") as fcc_file:
    fcc_data = json.load(fcc_file)

fcc_data = fcc_data['data']['TeachersCatalog']['data']

teachers_dict = {}

for i in range(len(fcc_data)):
    for house in range(len(fcc_data[i]['housesOfCulture'])):
        if fcc_data[i]['housesOfCulture'][house]['name'] == 'ЦДК «Созвездие»':
            teacher_desc = {}
            teacher_name = f"{fcc_data[i]['firstName']} {fcc_data[i]['middleName']} {fcc_data[i]['lastName']}"
            teacher_photo = fcc_data[i]['imageCoverObject']['value']
            teacher_age = fcc_data[i]['age']
            teacher_id = fcc_data[i]['id']
            teacher_list = []
            for workshop in range(len(fcc_data[i]['workshops'])):
                teacher_list.append(fcc_data[i]['workshops'][workshop]['name'])

            teacher_desc = {}
            teacher_desc['Имя'], teacher_desc['Фото'], teacher_desc['Возраст'], teacher_desc['Список'] = teacher_name, teacher_photo, teacher_age, teacher_list

            teachers_dict[teacher_id] = teacher_desc


with open(f"answer.json", "w", encoding="utf-8") as file:
    json.dump(teachers_dict, file, indent=4, ensure_ascii=False)


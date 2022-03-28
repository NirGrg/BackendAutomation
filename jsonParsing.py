import json

# courses = '{"name":"Rahul","languages":["Java", "python"]}'
#
# dict_courses = json.loads(courses)
# print(type(dict_courses))
# print(dict_courses['languages'])
#
# list_languages = dict_courses['languages']
# print(type(list_languages))
# print(list_languages[0])

with open("C:\\Users\\nir.gurung\\Downloads\\course.json") as f:
    data = json.load(f)
    print(data['courses'][1]['title'])
    print(type(data))
    print(data['dashboard']['website'])
    for i in data['courses']:
        print(i)
        if (i['title']=='RPA'):
            print(i['price'])
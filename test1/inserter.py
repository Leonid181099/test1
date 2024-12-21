from tinydb import TinyDB

def insert_forms():
    db = TinyDB('db.json')
    db.insert({
    "name": "Form template name",
    "field_name_1": "email",
    "field_name_2": "phone"
})
    db.insert({
        "name": "Form template name1",
        "field_name_1": "date",
        "field_name_2": "text",
        "field_name_3": "phone"
})
#     db.insert({
#         "name": "Form template name2",
# })


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    insert_forms()
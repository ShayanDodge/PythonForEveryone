contacts={"alex": "0217520","sarah":"0315530","mary":"0212221"}
code="021"

def contact_tehrani(contacts,code):
    contact_new={}
    for item in contacts.items():
        if code in item[1]:
            contact_new[item[0]]=item[1]
    return contact_new

contact_new=contact_tehrani(contacts,code)
for key in sorted(contact_new):
    print(key,contact_new[key])
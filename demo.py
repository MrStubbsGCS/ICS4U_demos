school_rooms = {174: "cotaught class and break out rooms", 230: "small breakoutroom, warm", 412:"fourth floor lab"}
ex_dictionary = {True: "yes", False: "No"}
print(school_rooms.keys())
test = school_rooms.keys()
for key in test:
    del school_rooms[key]
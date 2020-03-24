class Building:

    def __init__(self):
        self.stories = []
        self.address = ""
        self.total_floors = len(self.stories)
        self.modifiable_floors = 0
        self.current_floors_modified = 0
        # This will always be 0 while cur_flo_mod != mod_flo.
        self.construction_progress = 0
        self.total_cost = 0

    def mod_story(self, story, mode):
        if (mode == "add"):
            self.stories.append(story)
        else:
            self.stories.remove(story)
        
        return 

class Story:

    def __init__(self):
        # {'Bathroom': 3, 'Conference Room': 5, ...}
        self.rooms = {}
        self.num_rooms = len(self.rooms)
        self.total_cost = 0
    
    def add_room(self, room, amt):
        if (room in self.rooms):
            self.rooms[room] = self.rooms[room] + amt
        else:
            self.rooms[room] = amt
        
        return
    
    def remove_rooms(self, room, amt):
        if (room in self.rooms):
            self.rooms[room] = self.rooms[room] - amt
        else:
            print("That room does not exist.")
            
        return

class Room:
    def __init__(self, room_type, size, location):
        self.room_type = room_type
        self.room_size = size
        self.room_location = location
        self.total_cost = 0
        # {'Office Chair': 25, 'Conference Table': 1, ...}
        self.furniture = {}

    def add_furniture(self, furniture, amt):
        if (furniture in self.furniture):
            self.furniture[furniture] = self.furniture[furniture] + amt
        else:
            self.furniture[furniture] = amt
        
        return
    
    def remove_furniture(self, furniture, amt):
        if (furniture in self.furniture):
            self.furniture[furniture] = self.furniture[furniture] - amt
        else:
            print("That furniture is not present in this room.")
        
        return

class Model:
    def __init__(self, controller, mode):
        self.controller = controller
        
        if (mode == "new file"):
            # Use self.controller.building_details to:
            #         Set the Building and Story attributes appropriately.
            # DO NOT modify buildings.csv with new building entry. This will be
            # done at save time (in case user decides not to save).
            pass
        elif (mode == "open file"):
            # Use self.controller.chosen_building to:
            #        Open buildings.csv and read the right entry. Set Building 
            #        attributes.
            #        Find and open floors.csv and rooms.csv (using Building Num)
            #        to set the Story and Room attributes.
            # See Controller.py -> csavefile() for filename formats.
            pass
        
        return

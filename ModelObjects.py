class Building:

    def __init__(self):
        self.stories = []


    def add_story(self, story):
        self.stories.append(story)
    
    def get_num_floors(self):
        return len(self.stories)
   


class Story:

    def __init__(self):
        self.rooms = []
    
    def add_room(self, room):
        self.rooms.append(room)
    
    def get_num_rooms(self):
        return len(self.rooms)

class Room:
    def __init__(self, room_type, size):
        self.room_type = room_type
        self.furniture = []
        self.room_size = size

    def add_furniture(self, furniture):
        self.furniture.append(furniture)

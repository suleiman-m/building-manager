from View import *
from Controller import *

import csv
import string

class Building:

    def __init__(self, address, region, postalCode):
        self.stories = []
        self.address = address
        self.region = region
        self.postalCode = postalCode
        self.total_floors = len(self.stories)
        self.total_cost = ""
        self.modifiable_floors = 0
        self.current_floors_modified = 0
        print("Created new building with address ", self.address)

    def mod_story(self, story, mode):
        if (mode == "add"):
            self.stories.append(story)
        elif (mode == "del"):
            self.stories.remove(story)
        
        return 

class Story:

    def __init__(self, totalCost, floorNum, sqft):
        # {'Bathroom': 3, 'Conference Room': 5, ...}
        self.rooms = {}
        self.roomsList = []
        self.total_rooms = len(roomsList)
        self.num_rooms = len(self.rooms)
        self.total_cost = totalCost
        self.floor = floorNum
        self.area = sqft
    
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
            print("That room does not exist yet.")
            
        return

class Room:
    def __init__(self, room_type, size, location, cost, number):
        ''' 
        Example Initation:
        room204 = Room("conference room", 50, "north-west")
        '''
        self.room_type = room_type
        self.room_size = size
        self.room_location = location
        self.room_number = number
        self.total_cost = cost
        # Default not furnished.
        self.furnish_status = 0
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
        ''' DO NOT MODIFY BUILDING.CSV with NEW building ID# at time of creation,
        in case user does NOT want to save changes.
        
        Instantiation format for Building, Story and Room classes:
             self.b# = Building(...)
             self.b#s# = Story(...)
             self.b#s#r# = Room(...)
        View can call self.controller.model.(b#/b#s#/b#s#r#) to access
        values and functions (e.g. Building.mod_story)
        '''
        self.controller = controller
        
        if (mode == "new file"):
            # Use self.controller.building_details to:
            #         Set the Building and Story attributes appropriately.
            # DO NOT modify buildings.csv with new building entry. This will be
            # done at save time (in case user decides not to save).
            info = self.controller.building_details
            self.building = Building(info[0], info[1], info[2])

        elif (mode == "open file"):
            # See Controller.py -> csavefile() for filename formats.
            # Assumes user entered valid number.
            
            with open("/buildings/buildings.csv") as topfile:
                readCSV = csv.reader(topfile, delimiter=',')
                for row in readCSV:
                    if (row[0] == controller.chosen_building):
                        self.currBuild = Building()
                        self.currBuild.address = row[1]
                        self.currBuild.region = row[2]
                        self.currBuild.postalCode = row[3]
                        self.currBuild.total_cost = row[7]
                        
                        floorFile = "/buildings/b" + str(row[0]) + "_floors.csv"
                        with open(floorFile) as floors:
                            readFloors = csv.reader(floors, delimiter=',')
                            # Setting up dictionary keys.
                            headers = next(readFloors)
                            for header in headers:
                                temp = header.split()
                                header = temp[0]
                            
                            floor_count = 0
                            for floor in readFloors:
                                story = Story(floor[2], floor[0], floor[1])
                                
                                # Assigning parsed dictionary values.
                                # Splitting includes all digits, not just first.
                                for i in range(3, 8):
                                    amt = floor[i].split()
                                    story.rooms[headers[i]] = amt[0]                                   
                                
                                floor_count += 1
                                # File naming convention: b3f23_rooms.csv
                                # Each floor must have a .CSV for its rooms
                                rfile = "/buildings/b" + str(row[0]) + "f" + str(floor[0]) + "_rooms.csv"
                                with open(rfile) as roomFile:
                                    readRooms = csv.reader(roomFile, delimiter=",")
                                    '''
                                    # CSV HEADERS
                                    roomHeaders = next(readRooms)
                                    for roomHeader in roomHeaders:
                                        temp1 = roomHeader.split()
                                        roomHeader = temp1[0]
                                    '''
                                
                                    for room in readRooms:
                                        room = Room(room[3], room[1], room[5], room[2], room[0])
                                        if (room[6] != "Not Furnished"):
                                            room.furnish_status = 1
                                            
                                            furniture_list = room[6].split(",")
                                            for furniture in furniture_list:
                                                items = furniture.split(" ", 1)
                                                # Smaple field value format: 
                                                # 25 Office Chairs
                                                room.furniture[items[1]] = items[0]
                                        
                                        story.roomsList.append(room)
                                
                                # Retroactively fill array for Building
                                # Accessibile by currBuild.stories[0...]
                                self.currBuild.mod_story(story, "add")                                 
              
                        return
        return

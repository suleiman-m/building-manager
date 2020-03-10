# building-manager
A user-friendly GUI to help bridge the gap between corporations and construction companies for the creation or modification of office and commercial buildings and/or floor spaces.

# Introduction
This program is a GUI of three windows - one window has options to add, delete, or re-organize floors throughout a building - this can include the entire building itself, or just a range of specific floors (i.e. a rented-out office space). 

The second window allows the user to add, modify, or delete different kinds of rooms from the currently selected floor. By modify, we mean adding different types of pre-approved furniture, scaling the size up and down (e.g. a toilet bathroom upscaled to a toilet+shower bathroom, or a conference room of 10 seats to 25), or changing the direction and/or placement of the specific room on that floor (e.g. moving an office from the east end of the floor to the west end). 

Finally the third window will allow the user to see a real-time blueprint of the current floor with their modifications. This window is divided up into two separate frames - the top frame has the blueprint visual, and the bottom frame has the cost-price analysis of the selected floor, as well as the current total with all the floors combined (or the entire building if it is a fresh construction case and not just an office-space renovation).

# The Goal
This project aims to help unify office managers and corporations with their specific needs and costs, and a medium to display and present that information in a relevant manner to the actual construction agency in charge of the product. We hope that the interface helps alleviate some of the issues that may arise in an otherwise email-only correspondence state of affairs, and also avoid any problems at all.

# The Future
In the future, this project can be upscaled to a framework that connects both the client (the corporation/company) and the construction team with a single-sign-on online interface that provides real-time updates pushed by the client to the server, so that any changes can be easily and quickly conveyed - this will also help keep a record of all demands, agreed-upon prices, deals, as well as provide a quick and efficient way to respond to any construction problems that may arise and that require client input or verification before continuing.

# The Current State
As of now, the program is just a python project that interacts with the user via command-line - it’s only goal is to collect information about the number of rooms, floors, types of rooms, and use an arbitrary pricing sheet to provide the costs. 

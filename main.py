class Star_Cinema:
    __hall_list = []
 
    def _entry_hall(self, hall):
        self.__hall_list.append(hall)
 
 
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        self._entry_hall(self)
 
    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))

        allSeats = [[True for i in range(self.__cols)]
                   for j in range(self.__rows)]
        self.__seats[id] = allSeats
 
    def book_seats(self, name, phono, id, seat_list):
        flag = 1
        show = ()
        for item in self.__show_list:
            if item[0] == id:
                flag = 0
                show = item
                break
 
        if flag:
            print(f"\n\n{'-'*15}\nId didn't match with any show!\n{'-'*15}\n\n")
        else:
            bookedSeat = ""
            for item in seat_list:
                if self.__rows > item[0] and self.__cols > item[1]:
                    if self.__seats[id][item[0]][item[1]] == True:
                        self.__seats[id][item[0]][item[1]] = False
                        bookedSeat += f'{chr(65+item[0])}{item[1]} '
                    else:
                        print(
                            f"\n\n{'-'*15}\nTHESE SEATS WERE BOOKED - {chr(65+item[0])}{item[1]}\n{'-'*15}\n\n")
                else:
                    print(
                        f"\n\n{'-'*15}\nINVALID SEAT NO - {chr(65+item[0])}{item[1]}. TRY AGAIN\n{'-'*15}\n\n")
            if bookedSeat != "":
                print(
                    f"\n{'#'*5} TICKET BOOKED SUCCESSFULLY!! {'#'*5}\n{'-'*65}\n\nNAME: {name}\nPHONE NUMBER: {phono}\n\nMOVIE NAME: {show[1]}\t\tMOVIE TIME: {show[2]}\nTICKETS: {bookedSeat}\nHALL:{self.__hall_no}\n\n{'-'*65}\n")
 

    def view_show_list(self):
        print(f'\n\n{"-"*70}\n')
        for item in self.__show_list:
            print(f'MOVIE NAME: {item[1]}\tSHOW ID: {item[0]}\tTIME: {item[2]}')
        print(f'\n{"-"*70}\n\n')
 

    def view_available_seats(self, id):
        flag = 1
        for item in self.__show_list:
            if item[0] == id:
                flag = 0
                print(f'\n\nMOVIE NAME: {item[1]}\tTIME: {item[2]}')
                break
        if flag:
            print(f"\n\n{'-'*15}\nId didn't match with any show!\n{'-'*15}\n\n")
        else:
            print(f'X for already booked seats\n{"-"*50}\n')
            for i, seatCol in enumerate(self.__seats[id]):
                for j, val in enumerate(seatCol):
                    if val:
                        print(f'{chr(65+i)}{j}', end="\t")
                    else:
                        print("X", end="\t")
                print()
            print(f'\n{"-"*50}\n\n')
 
 
hall = Hall(4, 5, "A10")
hall.entry_show("mov1", "Black Adam", "Oct 30 2022, 10:00 PM")
hall.entry_show("mov2", "Superman", "Nov 01 2022, 11:00 PM")
 
 
while True:
    userInput = int(input(
        "1. VIEW ALL SHOWS TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET\nENTER OPTION: "))
    if userInput == 1:
        hall.view_show_list()
    elif userInput == 2:
        showId = input("ENTER SHOW ID: ")
        hall.view_available_seats(showId)
    elif userInput == 3:
        name = input("ENTER CUSTOMER NAME: ")
        phono = input("ENTER CUSTOMER PHONE NUMBER: ")
        showId = input("ENTER SHOW ID: ")
        numsOfTicket = int(input("ENTER NUMBER OF TICKETS: "))
        seat_list = []
        if numsOfTicket < 1:
            print(f"\n\n{'-'*15}\nNumber of tickets not valid!\n{'-'*15}\n\n")
        else:
            for i in range(1,numsOfTicket):
                seat = input(f"ENTER SEAT NO {i} :")
                seat_list.append((ord(seat[0])-65, int(seat[1:])))
            hall.book_seats(name, phono, showId, seat_list)
    else:
        break
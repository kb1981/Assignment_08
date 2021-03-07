#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# KBrock, 2021-Mar-07, completed adding code to use classes
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID   \n
        cd_title: (string) with the title of the CD   \n
        cd_artist: (string) with the artist of the CD   \n

    methods:
    """
    # -- construtor -- #
    def __init__(self, ID, title, artist):
        self.__cd_id = None
        self.__cd_title = None
        self.__cd_artist = None
        self.cd_id = ID
        self.cd_title = title
        self.cd_artist = artist

    # -- properties -- #
    @property
    def cd_id(self):
        return self.__cd_id
    @cd_id.setter
    def cd_id(self, value):
        if type(value) == int:
            self.__cd_id = value
        else:
            raise Exception ('Numbers Only!')

    @property
    def cd_title(self):
        return self.__cd_title
    @cd_title.setter
    def cd_title(self, value):
        self.__cd_title = value

    @property
    def cd_artist(self):
        return self.__cd_artist
    @cd_artist.setter
    def cd_artist(self, value):
        self.__cd_artist = value

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)
    """

# -- methods -- #
    @staticmethod
    def save_inventory(file_name, cdsave):
        with open (file_name, 'w') as objFile:
            for row in cdsave:
                strRow = ''
                for item in row:
                    strRow +=str(item) + ','
                strRow = strRow[:-1] + '\n'
                objFile.write(strRow)

    @staticmethod
    def load_inventory(file_name, cdload):
        cdload.clear()
        try:
            with open (file_name, 'r') as objFile:
                for row in objFile:
                    data = row.strip().split(',')
                    cdload.append(data)
            return cdload
        except FileNotFoundError:
            print('Looks like you are just getting started!')
            objFile = open(file_name, 'w')
            print('The file', strFileName, 'was created for you to use! Select [a] to add inventory.\n')
        except EOFError:
            print('Lets add some CDs!  Select [a] to get started! \n')

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Takes Input from the User and produces Output:

    properties:

    methods: 
        print_menu(): -> (prints a list of options)   \n
        menu_choice() -> (a lower case sting of the users input out of the choices l, a, i, s or x)   \n
        show_inventory(lstInvenotry) -> (prints a list of the current CD inventory)   \n
        cd_intake() -> (returns user input of ID, Title, and Artist for the CD)  \n
    """

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user"""
        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] Exit')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection"""
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Please choose from: [l, a, i, s or x]: ').lower().strip()
        print()
        return choice

    @staticmethod
    def show_inventory(cdlist):
        """Shows the current input from the user"""
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in cdlist:
            print('{}\t{} (by:{})'.format(*row))
        print('======================================\n')

    @staticmethod
    def cd_intake():
        """Gets information from user for CD input"""
        while True:
            try:
                ID = int(input('Enter ID: ').strip())
                break
            except ValueError:
                print ('Numbers Only Please ... Try Again!')
        Title = input('What is the CD\'s title? ').strip()
        Artist = input('What is the Artist\'s name? ').strip()
        print()
        return ID, Title, Artist

# -- Main Body of Script -- #
print('\nWelcome to the Magic CD Inventory!\n') 

FileIO.load_inventory(strFileName, lstOfCDObjects)

while True: 
    IO.print_menu()  #Display Menu to user and get choice
    strChoice = IO.menu_choice()

    if strChoice == 'x':  #Selection 'x' exits the program
        print ('"CD" ya later! Bye!')
        break

    if strChoice == 'l':  #Selection 'l' loads the CD Inventory from CDInventory.txt
          print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
          strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled:  ')
          if strYesNo.lower() == 'yes':
              print('reloading...\n')
              lstOfCDObjects = FileIO.load_inventory(strFileName, lstOfCDObjects)
              IO.show_inventory(lstOfCDObjects)
          else:
              input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.\n')
              IO.show_inventory(lstOfCDObjects)
              continue

    elif strChoice == 'a':  #Selection 'a' allows user to add a CD to inventory list
        intID, strTitle, strArtist = IO.cd_intake()
        objCD = CD(intID, strTitle, strArtist)
        lstCD = [objCD.cd_id, objCD.cd_title, objCD.cd_artist]
        lstOfCDObjects.append(lstCD)
        IO.show_inventory(lstOfCDObjects)

    elif strChoice == 'i':  #Selection 'i' displays the current inventory in the list
        IO.show_inventory(lstOfCDObjects)
        continue

    elif strChoice == 's':  #Selection 's' saves the current CD Inventory list to a text file
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
            print('Your Inventory has been saved!\n')
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue

    else:
        print("You've fa la la la lost me ...Try Again!")




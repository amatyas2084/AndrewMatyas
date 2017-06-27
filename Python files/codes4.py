'''
Author: Andrew Matyas
Date: 2/21


Description:
This program is used to run a social person class 
collaborated with Jacob Hiniker
'''
from hw3 import Person

class SocialPerson:

    def __init__(self,sfile=None):
        self.friends = {}
        if sfile == None:
            self.me = Person()
            self.status = input("Enter my status: ")	
        else:
            ifile = open(sfile,"r")
            first = ifile.readline().strip()
            last = ifile.readline().strip()
            bday = ifile.readline().strip()
            email = ifile.readline().strip()
            self.me = Person(first,last,bday,email)
            self.status = ifile.readline().strip()
            line = ifile.readline().strip()
            while line != "" :
                first = line
                last = ifile.readline().strip()
                bday = ifile.readline().strip()
                email = ifile.readline().strip()
                self.friends[email] = Person(first,last,bday,email)
                line = ifile.readline().strip()

    def friends_str(self):
        fs = ""
        count = 1
        for key in sorted(self.friends):
            fs += str(count) + ")  " + repr(self.friends[key]) + "\n"
            count += 1
        return fs

    def __repr__(self):
        str_rep = "---------- me ----------\n"
        str_rep += repr(self.me) + "\n"
        str_rep += "My status is: " + str(self.status) + "\n\n"
        str_rep += "------- friends --------\n"
        str_rep += str(self.friends_str())
        return str_rep

    def add_friend(self):
        newP = Person()
        self.friends[newP.email] = newP

    def get_key(self):

        print('------- friends --------\n' + self.friends_str() + '------------------------')
        choice = input('Enter friend number or 0 to cancel: ')

        if str(choice).isdigit() == False:
            print('Not a friend number: ' + str(choice))
            return ''
        elif int(choice) <= 0:
            return ''
        elif int(choice) > len(self.friends):
            print('Not a friend number: ' + str(choice))
            return ''
        else:
            temp = sorted(self.friends.keys())
            return temp[int(choice)-1]


    def unfriend(self):
        unf = self.get_key()

        if len(unf) > 0:
            self.friends.pop(unf)

    def write_sp(self, fname):
        f = open(fname, 'w+')
        f.write(self.me.first + "\n")
        f.write(self.me.last + "\n")
        f.write(self.me.bday + "\n")
        f.write(self.me.email + "\n")
        f.write(self.status + "\n")
        if len(self.friends) > 0:
            count = 1
            for key in sorted(self.friends):
                f.write(self.friends[key].first + "\n")
                f.write(self.friends[key].last + "\n")
                f.write(self.friends[key].bday + "\n")
                f.write(self.friends[key].email + "\n")
                count += 1
        f.close()

    @staticmethod
    def get_sp():
        print("---------- SocialPerson Options ----------")
        print("1) Create a new SocialPerson")
        print("2) Load a SocialPerson from file")
        print("3) Cancel")
        choice = input("Enter option number: ")
        if choice == '1':
            return SocialPerson()
        elif choice == '2':
            return SocialPerson(input("Enter filename: "))
        elif choice == '3':
            return None
        else:
            return None

    @staticmethod
    def get_option():

        print('---------- SocialPerson Options ----------')
        print('1) Add a friend\n' + '2) Unfriend someone\n' + '3) Print to screen\n' + '4) Save\n' + '5) Exit')
        choice = input("Enter option number: ")
        while choice != '5':
            if choice.isdigit():
                choice = int(choice)
                if 5 > choice > 0:
                    return choice
                else:
                    print('Invalid option: ' + str(choice) + ', try again')
                    choice = input('Enter option number: ')
            else:
                print('Invalid option: ' + str(choice) + ', try again')
                choice = input('Enter option number: ')
        return 5

def main():
    sp = SocialPerson.get_sp()
    while sp:
        option = SocialPerson.get_option()
        if option == 1:
            sp.add_friend()
        elif option == 2:
            sp.unfriend()
        elif option == 3:
            print(sp)
        elif option == 4:
            sp.write_sp(input("Enter save filename: "))
        else:
            return

if __name__ == '__main__':
    main()
'''
Author: Andrew Matyas
Date: 2/5

Description:
This program does stuff with binary
'''
class Binary():
    def __init__(self, arg='0'):
        """ Each Binary object has one instance variable, a list called
            num_list. num_list has integers 0 or 1 in the same order as
            the corresponding characters in the argument. If the string
            is less than 16 characters long, num_list should be padded by
            repeating the leftmost digit until the list has 16 elements.
            This is done by calling the pad() method.

            Args:
                self
                arg -- (str) 0's and 1's, 16 or less chars. Default is 0

            returns:
                n/a
        """
        num_list = []
        if len(arg) > 16:
            raise RuntimeError
        elif len(arg) == 0:
            num_list.append(0)
        else:
            arg = list(arg)
            for i in arg:
                if not(i is '0' or i is '1'):
                    raise RuntimeError
                num_list.append(int(i))

        self.num_list = num_list

        if len(num_list) < 16: 
            self.pad()

        

    def pad(self):
        """ Pad num_list by repeating the leftmost digit until the list
            has 16 elements.

            Args:
                self

            returns:
                none
        """
        to_repeat = self.num_list[0]
        self.num_list.reverse()

        for i in range(len(self.num_list), 16):
            self.num_list.append(to_repeat)
        self.num_list.reverse()

    def __repr__(self):
        """ Returns a 16-character string representing the fixed-width
            binary number.

            Args:
                self -- (Binary) containing a 16-digit list

            returns:
                (string) representation on Binary object
        """
        r = ""
        for i in self.num_list:
            r += str(i)
        return r

    def __add__(self, to_add):
        """ Returns a new Binary instance that represents the sum of self
            and the argument. If the sum requires more than 16 digits,
            raise a RuntimeError.

            Args:
                self -- (Binary) base object
                to_add -- (Binary) an object to add to base

            returns:
                (Binary) result of added objects.
                (RuntimeError) if results cannot be added
        """
        first_neg = (self.num_list[0] == 1)
        second_neg = (to_add.num_list[0] == 1)
        added = []
        total = 0
        carry = 0
        for i in range(16):
            total = self.num_list[15 - i] + to_add.num_list[15 - i] + carry
            if total == 0 or total == 1:
                added.append(total)
                carry = 0
            elif total == 2:
                added.append(0)
                carry = 1
            else:
                added.append(1)
                carry = 1
        added.reverse()

        
        if added[0] == 1 and (not first_neg and not second_neg):
            raise RuntimeError("Overflow!")

        
        if carry != 0 and (first_neg and second_neg) and added[0] == 0:
            raise RuntimeError("Overflow!")

        new_nums = Binary("")
        new_nums.num_list = added
        return new_nums

    def __neg__(self):
        """ Return a new Binary instance that equals -self.

            Args:
                self

            returns:
                (Binary) negative of self
        """
        flip = Binary("")
        for i in range(16):
            if self.num_list[i] == 0:
                flip.num_list[i] = 1
            else:
                flip.num_list[i] = 0

        flip = flip + Binary("01")
        return flip

    def __sub__(self, to_subtract):
        """ Takes a Binary object as an argument. Returns a new Binary
            instance that represents self – the argument.

            Args:
                self
                to_subtract -- (Binary) to subtract from self

            returns:
                (Binary)
        """
        return self + -to_subtract

    def __int__(self):
        """ Return the decimal value of the Binary object. This method
            should never raise a RuntimeError due to overflow. It is not
            used anywhere else in this program

            Args:
                self

            returns:
                (int) corresponding to the Binary object
        """
        digits = self
        if self.num_list == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            return -32768
        int_num = 0
        neg = False
        if self.num_list[0] == 1 :
            neg = True
            digits = (-digits)
        for i in range(16):
            if digits.num_list[15-i] == 1:
                int_num += 2**i
        if neg:
            int_num = -int_num
        return int_num

    def __eq__(self, other):
        """ Takes a Binary object. Returns True if self == the argument,
            False otherwise.

            Args:
                self
                other: (Binary) object to be compared

            returns:
                Boolean representing equality of objects

        """
        return self.num_list == other.num_list

    def __lt__(self, compare):
        """ Takes a Binary object as an argument. Return True if
            self < the argument, False otherwise. This method should
            never raise a RuntimeError due to overflow.

            Args:
            self
                compare -- (Binary) object to compare to self

            returns:
                (Boolean) is 'self' less than 'compare'?
        """
        
		
        if self.num_list[0] == 0 and compare.num_list[0] == 1:
            return False
        elif self.num_list[0] == 1 and compare.num_list[0] == 0:
            return True
        else:
            return (self - compare).num_list[0] == 1

    def __abs__(self):
        """ Return a new instance that is the absolute value of self.

            Args:
                self

            returns:
                (Binary) absolute value of self
        """
        if self.num_list[0] == 1:
            return -self
        return self+Binary()



def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    
    
    

if __name__ == '__main__':
    main()

'''
Author: Andrew Matyas
Date: 4/27

Description:
<summary of this program>
'''
from bs4 import BeautifulSoup
import requests

class Person:

    def __init__(self, last, first, ptype, email, phone, unit, position, addr, bldg, rm):
            self.last = last
            self.first = first
            self.ptype = ptype
            self.email = email
            self.phone = phone
            self.unit = unit
            self.position = position
            self.addr = addr
            self.bldg = bldg
            self.rm = rm
    
    @classmethod
    def from_soup(cls, soup):
        name = soup.find("h3").get_text().strip().split(",")
        
        last = name[0].strip()
        first = name[1].strip()
        ptype = soup.find("span",class_= "type").get_text().strip()
        email = soup.find("a", class_="mailto").get_text().strip()
        
        if len(soup.find_all("a", class_="phoneto")) == 0 :
            phone = ""
        else:
            phone = soup.find("a", class_="phoneto").get_text().strip()
            
        
        
        unit = soup.find("div", class_="degree").get_text().strip()
        job = soup.find("div", class_="department").get_text().strip().split("\n")
        position = job[0].strip()
        location = soup.find_all("div")
        addr = location[-3].get_text().strip()
        bldg = location[-2].get_text().strip()[10:]
        rm = location[-1].get_text().strip()[8:]
        
        return Person(last,first,ptype,email,phone,unit,position,addr,bldg,rm)
        
    def generator(self):
        nlst = []
        nlst.append(self.last+", "+self.first)
        nlst.append(self.ptype)
        nlst.append(self.email)
        nlst.append(self.phone)
        nlst.append(self.unit)
        nlst.append(self.position)
        nlst.append(self.addr)
        nlst.append(self.bldg+" rm "+self.rm)
        return (x for x in nlst)
        
    def __repr__(self):
        return(self.first+" "+self.last+", "+self.email+", "+self.position)

    def __eq__(self,other):
        return self.email == other.email
    
    def __hash__(self):
        return hash(self.email)
        
    def __lt__(self,other):
        if self == other:
            return False
        else:
            if self.last == other.last:
                if self.first == other.first:
                    return self.first[-1] > other.first[-1]
                      
                else:
                    return self.first < other.first
            else:
                return self.last < other.last

class People:

    def __init__(self,ppl = None,fname=None):
        
        self.missing = []
        if not ppl:
            self.people = []
        else:
            self.people = ppl
        
        if fname:
            iperson = []
            file = open(fname,"r")
            for line in file:
                line = line.strip().split(",")
                url = "http://directory.arizona.edu/phonebook?type_2=&lastname="+line[1]+"&firstname="+line[0]+"&email=&phone=&attribute_7="
                page = requests.get(url)
                soup = BeautifulSoup(page.content)
                people = soup.find_all("span",class_="field-content")
                if len(people) == 0:
                    self.missing.append("".join(line))
                else:
                    for person in people:
                        iperson.append(Person.from_soup(person))
                    self.select_people(iperson,line)
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    
    
    
    
    
    
if __name__ == '__main__':
    main()
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        avg = sum(self.scores) / len(self.scores)        
        if avg > 89:
            result = 'O'
        elif avg < 90 and avg >= 80:
            result = 'E'
        elif avg >= 70 and avg < 80:
            result = 'A'
        elif avg >= 55 and avg < 70:
            result = 'P'
        elif avg >= 40 and avg < 55:
            result = 'D'    
        elif avg < 40:
            result = 'T'
        return result


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
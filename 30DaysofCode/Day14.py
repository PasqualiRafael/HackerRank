class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        min_element = 101
        max_element = 0
        self.__elements.sort()
        for elements in self.__elements:
            if elements < min_element:
                min_element = elements
            elif elements > max_element:
                max_element = elements
        
        self.maximumDifference = max_element - min_element

        
	

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
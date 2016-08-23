class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3
    def check_angles(self):
        if (self.angle1+self.angle2+self.angle3) == 180:
            return True
        else:
            return False
my_triangle = Triangle(90, 30, 60)
print (my_triangle.number_of_sides)
print (my_triangle.check_angles())



grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print (grade)

def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(grades):
    variance = 0
    for g in grades:
        variance += ((grades_average(grades) - g) ** 2)
    return variance / len(grades)
print (grades_variance(grades))

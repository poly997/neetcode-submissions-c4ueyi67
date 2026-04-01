class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        students_1 = sum(students)
        students_0 = len(students) - students_1
        #print(students_1,students_0)

        index = 0
        while students_0 or students_1 > 0:

            print("beginning of the cycle",students_1,students_0)
            if sandwiches[index] == 1:
                students_1 -= 1
                print("std_1", students_1)
            else:
                students_0 -= 1
                print("std_0", students_0)
            if students_0 < 0 or students_1 < 0:
                print("return len-index")
                print("values", students_1,students_0)
                return len(students) - index
            
            index += 1
            print("index", index)

        return 0
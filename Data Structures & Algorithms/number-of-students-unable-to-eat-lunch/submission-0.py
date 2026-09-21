class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentCounter = Counter(students)
        
        print(studentCounter)

        for sandwich in sandwiches:

            if(studentCounter[sandwich]==0):
                break;
            else:
                studentCounter[sandwich] -= 1;

        return studentCounter.total();      

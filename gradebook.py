#creating the data

students = ["Noelia", "Genesis", "Paul", "Rich", "Juan"]
scores = [85, 100, 60, 80, 70]

print ("=" *35)
print ("       Students Gradebook")
print ("=" *35)

#Display each student with their score
for i in range(len(students)):
    print(f"{students[i]:<12} {scores[i]}")

#calculates statistics 
total = sum (scores)  #Built in function add all items
average = total/len(scores) #Total divided by count
highest = (max(scores)) # Built in function: finds the largest value
lowest = (min(scores)) # Built in function : finds the lowest value

print ("=" *35)
print (f"Total scores {total}")
print (f"average is {average}")
print (f"highest scores is {highest}")
print (f"lowest scores is {lowest}")

highest_index = scores.index(highest) #.index returns the position of a value
top_student = students [highest_index]

print(f"the winner is {top_student} with {highest}")

#add a new student

new_name = input ("Student name: ")
try:
    new_score = int(input ("Test score: "))
except ValueError:
    print ("Invalid score. Using 0.")
    new_score =0 

students.append(new_name)
scores.append(new_score)

#recalculate
new_average = sum(scores)/len(scores)

#Output 
print(f"{len(students)} students")


print (f"new average is {new_average:.1f} ")



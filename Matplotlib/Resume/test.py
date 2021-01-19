from matplotlib import pylab as plt

from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
fig,ax = plt.subplots()
arr_code = mpimg.imread('rtest.jpg')
imagebox = OffsetImage(arr_code)
ab = AnnotationBbox(imagebox, (0.84, 0.9)) # middle of picture
ax.add_artist(ab)


fig.set_facecolor('grey')
ax.set_facecolor('grey')
# plt.savefig('resumeexample.png', dpi=300, bbox_inches='tight')
# plt.axhline(x=.99, color='purple', alpha=0.5, linewidth=2) # beware of the parameters
# plt.axhline(y=.88, xmin=0, xmax=1, color='black', linewidth=1)
plt.axis('off')


# plt.show()

# In digital signal processing, spatial anti-aliasing is a technique for minimizing the distortion artifacts known as aliasing when representing a high-resolution image at a lower resolution.

Job_1_responsibilities = [['Provide explanation and visualization about Math concepts such as: Linear programming, Probability distributions, differentiation, and Introduction to Linear Algebra.'],
                          ['Supervise two to three students for a 90 minute session on their respective work including school assignments and contest preperation.'],
                          ["Write and review students' monthly reports and execute plans and tutoring for improvements."],
                          ["Perform other duties and tasks as assigned such as moving all students' information to another website and re-creating study plans for most students due to technical issues."]]

Job_2_responsibilities = [['Teach children who span the age of 6-12 on speed counting and the use of abacus.'],
                          ["Grade students's weekly assignments and analyse what the problem was that resulted in an error."],
                          ["Engage in discussion with my supervisor as to how we can improve a student's skill on a daily basis."]]

Job_3_responsibilities = [["Provide help to the first year students in my university in their Introduction to Python course by explaining concepts such as: dictionaries, sets, recursion, as well as the os and random module."],
                          ["For stronger students, I would introduce topics such as linked list, OOP, searching and sorting, and the analysis of time and space complexity for basic functions."],
                          ["Encourage them to read the documentation or turn to stack overflow whenever there is doubts."]]

Project_Descriptions = [["xxx", "Tools: Pandas, Flask ", "xxx"],
                        ['Built a website on a development server using Flask with the goal of reducing the use of phone calls for a reservation.',
                    'Tools: Bootstrap, sqlalchemy, html/css, ', 'Currently testing some Machine Learning models to maximise revenue while maintaining user satisfaction.'],
                    ['Used Beautifulsoup to scrap all the cases of Covid-19 in my home country.','Users have the option to filter the results based on states and order.']
                        ]

def xxx(x):
    b = 39
    # split strings that are longer than b to 2 or more elements inside the current list so that it fits in the resume
    # example [['0123456789'],['01234567']] -> [['01234','56789'],['01234','567']] when b is 5
    for i in range(len(x)):
        for j in range(len(x[i])):
                if len(x[i][j]) > b:
                    temp = len(x[i][j])
                    start = 0
                    end = b
                    for _ in range(int(temp/b)):
                        x[i].append(x[i][j][start:end])
                        start += b
                        end += b
                    if len(x[i][j][start:]) > 0:
                        x[i].append(x[i][j][start:])
                    x[i].remove(x[i][j]) # cannot remove
                    # x[i][j] = 'None'
                    # return l2
    return x
x = [['0123456789'], ['01234567']]
# print(xxx(x))
# print(xxx(x)==[['01234','56789'],['01234','567']])
# c = xxx(Job_1_responsibilities)
# for i in c:
#     print(len(i),i)
for i in Job_1_responsibilities:
    print(i[0])
print()
for i in Job_3_responsibilities:
    print(i[0])
print()
for i in Job_2_responsibilities:
    print(i[0])
print()
for i in Project_Descriptions:
    print(i[0])
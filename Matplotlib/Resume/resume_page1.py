from matplotlib import pyplot as plt
from pylab import rcParams

rcParams['figure.figsize'] = 6, 6.5

fig, ax = plt.subplots(nrows=1, ncols=1)
fig.patch.set_facecolor('#808080')
ax.set_facecolor('black')

Name = 'JASON LEONG'
My_Role = ['Student in Cognitive Science and','Artificial Intelligence']

Experience_title = 'EXPERIENCE'

Job_1_company_name = 'Mathnasium'
Job_1_position = 'Mathematics Instructor'
Job_1_responsibilities = [['Provide explanation and visualization about Math concepts such as: Linear programming,','Probability distributions, differentiation, and Introduction to Linear Algebra.'],['Supervise two to three students for a 90 minute session on their respective work including','school assignments and contest preperation.'], "Write and review students' monthly reports and execute plans and tutoring for improvements.", ["Perform other duties and tasks as assigned such as moving all students' information","to another website and re-creating study plans for most students due to technical issues."]]
Job_1_duration = '2019-01-01-2019-07-01'

Job_2_company_name = "Global Math"
Job_2_position = "Speed Counting and Abacus Tutor"
Job_2_responsibilities = ['Teach children who span the age of 6-12 on speed counting and the use of abacus.', "Grade students's weekly assignments and analyse what the problem was that resulted in an error.", "Engage in discussion with my supervisor as to how we can improve a student's skill on a daily basis."]
Job_2_duration = '2016-03-01-2016-06-01'

Job_3_company_name = 'Flow'
Job_3_position = 'Part-Time Python Tutor'
Job_3_responsibilities = [["Provide help to the first year students in my university in their Introduction to Python course", "by explaining concepts such as: dictionaries, sets, recursion, as well as the os and random module."], ["For stronger students, I would introduce topics such as linked list, OOP, searching and sorting,", "and the analysis of time and space complexity for basic functions."], ["Encourage them to read the documentation or turn to stack overflow whenever there is doubts."]]
Job_3_duration = '2020-01-01-Present'

Skills_Title = 'SKILLS'
Skills = ["Python", "Flask", "Pandas", "Numpy", "Matplotlib", "Beautifulsoup", "Netlogo", "Git", "SQL", "HTML/CSS (Basic)"]

Languages_Title = 'LANGUAGES'
Languages = ["English", "Chinese", "Cantonese"]

Achivement_Title = 'ACHIVEMENT'
Achivements = ['A level Mathematics Competition']
A_Description = [['Represented Asia Pacific International School in the Advanced-Level','Mathematics Competition at district round.'],
                 ['Advanced to the national round of the competition after winning the','district round.']]

Education_Title = 'EDUCATION'
Education = ['BSc Cognitive Science and Artificial Intelligence (CSAI)']
University = ['Tilburg University']
Education_Duration = ['2019-present']
E_Description = ['Currently at the end of my 2nd year study at Tilburg University.', 'Overall Grade so far : 8/10']

Projects_Title = 'PROJECTS'
Project_Names = ['Data Science Project', 'Badminton Court Booking Website', 'Web-Scraping of Covid-19 cases in every state of Malaysia']
Project_Links = ['link', 'link', 'link']
Project_Descriptions = [["xxx", "Tools: Pandas, Flask ", "xxx"], [['Built a website on a development server using Flask','with the goal of reducing the use of phone calls for a reservation.'], 'Tools: Bootstrap, sqlalchemy, html/css, ', ['Currently testing some Machine Learning models to maximise revenue','while maintaining user satisfaction.']], ['Used Beautifulsoup to scrap all the cases of Covid-19 in my home country.', 'Users have the option to filter the results based on states and order.']]

Contact_Title = 'Contact Me'
Contact_ID = ['Email: ', 'Phone: ', 'LinkedIN: ']
Contact = ['leongjason3781@gmail.com', '+60123292658', 'https://www.linkedin.com/in/jason-leong-65333a196/']


Extra_Title = 'Find Me Online'
Extra_ID = ['GitHub: ','Facebook: ','Instagram: ','Discord: ','Kaggle: ']
Extra = ['https://github.com/JasonLeong81','https://www.facebook.com/JasonLeong81/','https://www.instagram.com/Jason_Leong_81/','https://discord.com/users/Jasonn#0350','https://www.kaggle.com/jasonleongchoryew']

x_line_width_right_min = 0.5
x_line_width_right_max = 0.9
x_line_width_left_min = 0
x_line_width_left_max = 0.45

### Begin Coding :) ####################################################################################################

def resume_page_1():
    # Introduction

    plt.annotate(Name, (0,0.95), weight='regular', fontsize=18, alpha=.6,color='white')
    plt.annotate(My_Role[0], (0,0.90), weight='regular', fontsize=8, alpha=.6,color='blue')
    plt.annotate(My_Role[1], (0,0.88), weight='regular', fontsize=8, alpha=.6,color='blue')

    # Picture
    from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
    import matplotlib.image as mpimg
    # fig, ax = plt.subplots()
    arr_code = mpimg.imread('rtest.jpg')
    imagebox = OffsetImage(arr_code)
    ab = AnnotationBbox(imagebox, (0.7, 1))  # middle of picture
    ax.add_artist(ab)

    # Experience

    plt.annotate(Experience_title , (0,0.80), weight='bold', fontsize=12, alpha=.6,color='white')

    plt.axhline(y=.795, xmin=x_line_width_left_min, xmax=x_line_width_left_max, color='black', linewidth=1)

    plt.annotate(Job_3_position , (0,0.75), weight='regular', fontsize=10, alpha=.6,color='white')
    plt.annotate(Job_3_company_name , (0,0.73), weight='regular', fontsize=8, alpha=.6,color='blue')
    plt.annotate(Job_3_duration , (0,0.71), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.69), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_3_responsibilities[0][0] , (0.01,0.69), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_3_responsibilities[0][1], (0.01, 0.67), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate('-' , (0,0.65), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_3_responsibilities[1][0] , (0.01,0.65), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_3_responsibilities[1][1] , (0.01,0.63), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.61), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_3_responsibilities[2][0] , (0.01,0.61), weight='regular', fontsize=8, alpha=.6,color='white')

    plt.annotate(Job_1_position , (0,0.56), weight='regular', fontsize=10, alpha=.6,color='white')
    plt.annotate(Job_1_company_name , (0,0.54), weight='regular', fontsize=8, alpha=.6,color='blue')
    plt.annotate(Job_1_duration , (0,0.52), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.50), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_1_responsibilities[0][0] , (0.01,0.50), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_1_responsibilities[0][1] , (0.01,0.48), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.46), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_1_responsibilities[1][0] , (0.01,0.46), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_1_responsibilities[1][1], (0.01, 0.44), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate('-' , (0,0.42), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_1_responsibilities[2] , (0.01,0.42), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.40), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_1_responsibilities[3][0] , (0.01,0.40), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_1_responsibilities[3][1], (0.01, 0.38), weight='regular', fontsize=8, alpha=.6, color='white')

    plt.annotate(Job_2_position , (0,0.33), weight='regular', fontsize=10, alpha=.6,color='white')
    plt.annotate(Job_2_company_name , (0,0.31), weight='regular', fontsize=8, alpha=.6,color='blue')
    plt.annotate(Job_2_duration , (0,0.29), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.27), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_2_responsibilities[0] , (0.01,0.27), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.25), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_2_responsibilities[1] , (0.01,0.25), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.23), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_2_responsibilities[2] , (0.01,0.23), weight='regular', fontsize=8, alpha=.6,color='white')

    # Education

    plt.annotate(Education_Title, (0.5,0.80), weight='bold', fontsize=12, alpha=.6,color='white')

    plt.axhline(y=.795, xmin=x_line_width_right_min, xmax=x_line_width_right_max, color='black', linewidth=1)

    plt.annotate(Education[0], (0.5,0.75), weight='regular', fontsize=10, alpha=.6,color='white')
    plt.annotate(University[0] , (0.5,0.73), weight='regular', fontsize=8, alpha=.6,color='blue')
    plt.annotate(Education_Duration[0] , (0.5,0.71), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ' , (0.5,0.69), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(E_Description[0] , (0.51,0.69), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ' , (0.5,0.67), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(E_Description[1] , (0.51,0.67), weight='regular', fontsize=8, alpha=.6,color='white')

    # Achivement

    plt.annotate(Achivement_Title , (0.5,0.62), weight='bold', fontsize=12, alpha=.6,color='white')

    plt.axhline(y=.615, xmin=x_line_width_right_min, xmax=x_line_width_right_max, color='black', linewidth=1)

    plt.annotate(Achivements[0] , (0.5,0.57), weight='regular', fontsize=10, alpha=.6,color='white')
    plt.annotate("- " , (0.5,0.55), weight='regular', fontsize=12, alpha=.6,color='white')
    plt.annotate(A_Description[0][0] , (0.51,0.55), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(A_Description[0][1] , (0.51,0.53), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate("- " , (0.5,0.51), weight='regular', fontsize=12, alpha=.6,color='white')
    plt.annotate(A_Description[1][0] , (0.51,0.51), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(A_Description[1][1], (0.51, 0.49), weight='regular', fontsize=8, alpha=.6, color='white')

    # Projects

    plt.annotate(Projects_Title , (0.5,0.44), weight='bold', fontsize=12, alpha=.6,color='white')

    plt.axhline(y=.430, xmin=x_line_width_right_min, xmax=x_line_width_right_max, color='black', linewidth=1)

    plt.annotate(Project_Names[0] , (0.5,0.39), weight='bold', fontsize=10, alpha=.6,color='white')
    plt.annotate(Project_Links[0] , (0.5,0.37), weight='regular', fontsize=8, alpha=.6,color='blue')
    plt.annotate( '-', (0.5,0.35), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[0][0] , (0.51,0.35), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0.5,0.33), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[0][1] , (0.51,0.33), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-'  , (0.5,0.31), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[0][2] , (0.51,0.31), weight='regular', fontsize=8, alpha=.6,color='white')

    plt.annotate(Project_Names[1] , (0.5,0.26), weight='bold', fontsize=10, alpha=.6,color='white')
    plt.annotate(Project_Links[1] , (0.5,0.24), weight='regular', fontsize=8, alpha=.6,color='blue')
    plt.annotate( '-', (0.5,0.22), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[1][0][0] , (0.51,0.22), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[1][0][1], (0.51, 0.20), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate('-' , (0.5,0.18), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[1][1] , (0.51,0.18), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-'  , (0.5,0.16), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[1][2][0] , (0.51,0.16), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[1][2][1] , (0.51,0.14), weight='regular', fontsize=8, alpha=.6,color='white')


    plt.annotate(Project_Names[2] , (0.5,0.09), weight='bold', fontsize=10, alpha=.6,color='white')
    plt.annotate(Project_Links[2] , (0.5,0.07), weight='regular', fontsize=8, alpha=.6,color='blue')
    plt.annotate( '-', (0.5,0.05), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[2][0] , (0.51,0.05), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0.5,0.03), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[2][1] , (0.51,0.03), weight='regular', fontsize=8, alpha=.6,color='white')

    # Skills

    plt.annotate(Skills_Title , (0,0.18), weight='bold', fontsize=12, alpha=.6,color='white')

    plt.axhline(y=.175, xmin=x_line_width_left_min, xmax=x_line_width_left_max, color='black', linewidth=1)

    c = 0.13
    for i in range(5):
        plt.annotate('- ', (0,c), weight='regular', fontsize=8, alpha=.6,color='white')
        plt.annotate(Skills[i] , (0.01,c), weight='regular', fontsize=8, alpha=.6,color='white')
        c -= 0.02
    c = 0.13
    for i in range(5,10):
        plt.annotate('- ', (0.09,c), weight='regular', fontsize=8, alpha=.6,color='white')
        plt.annotate(Skills[i] , (0.1,c), weight='regular', fontsize=8, alpha=.6,color='white')
        c -= 0.02

    plt.axis('off')
    plt.savefig('resume_page_1.png',facecolor=("#808080"))
    plt.show()


### Done :) ####################################################################################################

if __name__ == '__main__':
    resume_page_1()


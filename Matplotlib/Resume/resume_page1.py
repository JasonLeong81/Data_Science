from matplotlib import pyplot as plt
from pylab import rcParams

rcParams['figure.figsize'] = 6, 6.5

fig, ax = plt.subplots(nrows=1, ncols=1)
fig.patch.set_facecolor('#808080')
ax.set_facecolor('black')

Name = 'JASON LEONG'
My_Role = 'Student in Cognitive Science and Artificial Intelligence'

Experience_title = 'EXPERIENCE'

Job_1_company_name = 'Mathnasium'
Job_1_position = 'Mathematics tutor'
Job_1_responsibilities = ['Provide explanation and visualization about Math concepts such as: Linear programming, Probability distributions, differentiation, and Introduction to Linear Algebra.','Supervise two to three students for a 90 minute session on their respective work including school assignments and contest preperation.', "Write and review students' monthly reports and execute plans and tutoring for improvements.", "Perform other duties and tasks as assigned such as moving all students' information to another website and re-creating study plans for most students due to technical issues.","Participate in meetings where we discussed about potentially successful teaching methods that we tried on students, students' progress and problems, and any special requests from students or parents."]
Job_1_duration = 'duration'

Job_2_company_name = "Global Math"
Job_2_position = "Speed counting and abacus tutor"
Job_2_responsibilities = ['Teach children who span the age of 6-12 on speed counting and the use of abacus for basic Math operations.', "Grade students's weekly assignments and analyse what the problem was that resulted in an error, if there was any.", "Engage in discussion with my supervisor as to how we can improve a student's skill on a daily basis."]
Job_2_duration = 'duration'

Job_3_company_name = 'Flow'
Job_3_position = 'Python tutor'
Job_3_responsibilities = ["Provide help to the first year students in my university in their Introduction to Python course by explaining concepts such as: dictionaries, sets, recursion, as well as the os and random module.", "For stronger students, I would introduce new topics based on what they have learned. Some of these are: linked list, OOP, searching and sorting, and the analysis of time and space complexity for basic functions.", "Encourage them to read the documentation or turn to stack overflow whenever there is doubts."]
Job_3_duration = 'duration'

Skills_Title = 'SKILLS'
Skills = ["Python", "Flask", "Pandas", "Numpy", "Matplotlib", "Beautifulsoup", "Netlogo", "Git", "SQL", "Basic HTML/CSS"]

Languages_Title = 'LANGUAGES'
Languages = ["English", "Chinese", "Cantonese"]

Achivement_Title = 'ACHIVEMENT'
Achivements = ['A level Mathematics Competition']
A_Description = ['Represented Asia Pacific International School in the Advanced-Level Mathematics Competition at district round.',
                 'Advanced to the national round of the competition after winning the district round.']

Education_Title = 'EDUCATION'
Education = ['BSc Cognitive Science and Artificial Intelligence (CSAI)']
University = ['Tilburg University']
Education_Duration = ['2019-present']
E_Description = ['Currently at the end of my 2nd year study at Tilburg University.', 'Overall Grade so far : 8/10']

Projects_Title = 'PROJECTS'
Project_Names = ['Data Science Project', 'Badminton Court Booking Website', 'Web-Scraping of Covid-19 cases in every state of Malaysia.']
Project_Links = ['link', 'link', 'link']
Project_Descriptions = [["xxx", "Tools: Pandas, ", "xxx"], ['Built a website using Flask for a Badminton Court so that people can reserve a court online rather than the traditional way of calling to the place and hoping that someone would pick up.', 'Tools: Bootstrap, sqlalchemy, html/css, ', 'Currently testing some Machine Learning models that would charge different prices to maximise revenue while maintaining user satisfaction.'], ['Used Beautifulsoup to scrap all the cases of Covid-19 in my home country.', 'Users have the option to filter the results based on states and order.', 'Used the QuickSort algorithm for sorting and the datetime module for filtering as ways to improve time and space complexity.']]

Contact_Title = 'Contact Me'
Contact_ID = ['Email: ', 'Phone: ', 'LinkedIN: ']
Contact = ['leongjason3781@gmail.com', '+60123292658', 'https://www.linkedin.com/in/jason-leong-65333a196/']


Extra_Title = 'Find Me Online'
Extra_ID = ['GitHub: ','Facebook: ','Instagram: ','Discord: ','Kaggle: ']
Extra = ['https://github.com/JasonLeong81','https://www.facebook.com/JasonLeong81/','https://www.instagram.com/Jason_Leong_81/','https://discord.com/users/Jasonn#0350','https://www.kaggle.com/jasonleongchoryew']


### Begin Coding :) ####################################################################################################

def resume_page_1():
    # Introduction

    plt.annotate(Name, (0,0.95), weight='regular', fontsize=18, alpha=.6,color='white')
    plt.annotate(My_Role, (0,0.90), weight='regular', fontsize=8, alpha=.6,color='blue')

    # Picture



    # Experience

    plt.annotate(Experience_title , (0,0.80), weight='bold', fontsize=12, alpha=.6,color='white')

    plt.annotate(Job_1_position , (0,0.75), weight='regular', fontsize=10, alpha=.6,color='white')
    plt.annotate(Job_1_company_name , (0,0.73), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_1_duration , (0,0.71), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.69), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_1_responsibilities[0] , (0.01,0.69), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.67), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_1_responsibilities[1] , (0.01,0.67), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.65), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_1_responsibilities[2] , (0.01,0.65), weight='regular', fontsize=8, alpha=.6,color='white')

    plt.annotate(Job_2_position , (0,0.58), weight='regular', fontsize=10, alpha=.6,color='white')
    plt.annotate(Job_2_company_name , (0,0.56), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_2_duration , (0,0.54), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.52), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_2_responsibilities[0] , (0.01,0.52), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.50), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_2_responsibilities[1] , (0.01,0.50), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.48), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_2_responsibilities[2] , (0.01,0.48), weight='regular', fontsize=8, alpha=.6,color='white')

    plt.annotate(Job_3_position , (0,0.41), weight='regular', fontsize=10, alpha=.6,color='white')
    plt.annotate(Job_3_company_name , (0,0.39), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_3_duration , (0,0.37), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.35), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_3_responsibilities[0] , (0.01,0.35), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.33), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_3_responsibilities[1] , (0.01,0.33), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0,0.31), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Job_3_responsibilities[2] , (0.01,0.31), weight='regular', fontsize=8, alpha=.6,color='white')

    # Education

    plt.annotate(Education_Title, (0.5,0.80), weight='bold', fontsize=12, alpha=.6,color='white')
    plt.annotate(Education[0], (0.5,0.75), weight='regular', fontsize=10, alpha=.6,color='white')
    plt.annotate(University[0] , (0.5,0.73), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Education_Duration[0] , (0.5,0.71), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ' , (0.5,0.69), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(E_Description[0] , (0.52,0.69), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ' , (0.5,0.67), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(E_Description[1] , (0.52,0.67), weight='regular', fontsize=8, alpha=.6,color='white')

    # Achivement

    plt.annotate(Achivement_Title , (0.5,0.60), weight='bold', fontsize=12, alpha=.6,color='white')
    plt.annotate(Achivements[0] , (0.5,0.55), weight='regular', fontsize=10, alpha=.6,color='white')
    plt.annotate("- " , (0.5,0.53), weight='regular', fontsize=12, alpha=.6,color='white')
    plt.annotate(A_Description[0] , (0.52,0.53), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate("- " , (0.5,0.51), weight='regular', fontsize=12, alpha=.6,color='white')
    plt.annotate(A_Description[1] , (0.52,0.51), weight='regular', fontsize=8, alpha=.6,color='white')

    # Projects

    plt.annotate(Projects_Title , (0.5,0.44), weight='bold', fontsize=12, alpha=.6,color='white')

    plt.annotate(Project_Names[0] , (0.5,0.39), weight='bold', fontsize=10, alpha=.6,color='white')
    plt.annotate(Project_Links[0] , (0.5,0.37), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate( '-', (0.5,0.35), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[0][0] , (0.52,0.35), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0.5,0.33), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[0][1] , (0.52,0.33), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-'  , (0.5,0.31), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[0][2] , (0.52,0.31), weight='regular', fontsize=8, alpha=.6,color='white')

    plt.annotate(Project_Names[1] , (0.5,0.24), weight='bold', fontsize=10, alpha=.6,color='white')
    plt.annotate(Project_Links[1] , (0.5,0.22), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate( '-', (0.5,0.20), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[1][0] , (0.52,0.20), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0.5,0.18), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[1][1] , (0.52,0.18), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-'  , (0.5,0.16), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[1][2] , (0.52,0.16), weight='regular', fontsize=8, alpha=.6,color='white')

    plt.annotate(Project_Names[2] , (0.5,0.09), weight='bold', fontsize=10, alpha=.6,color='white')
    plt.annotate(Project_Links[2] , (0.5,0.07), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate( '-', (0.5,0.05), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[2][0] , (0.52,0.05), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-' , (0.5,0.03), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[2][1] , (0.52,0.03), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('-'  , (0.5,0.01), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Project_Descriptions[2][2] , (0.52,0.01), weight='regular', fontsize=8, alpha=.6,color='white')

    # Skills

    plt.annotate(Skills_Title , (0,0.24), weight='bold', fontsize=12, alpha=.6,color='white')
    plt.annotate('- ', (0,0.22), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Skills[0] , (0.01,0.22), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0,0.2), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Skills[1] , (0.01,0.2), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0,0.18), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Skills[2] , (0.01,0.18), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0,0.16), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Skills[3] , (0.01,0.16), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0,0.14), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Skills[4] , (0.01,0.14), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0,0.12), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Skills[5] , (0.01,0.12), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0,0.1), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Skills[6] , (0.01,0.1), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0,0.08), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Skills[7] , (0.01,0.08), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0,0.06), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Skills[8] , (0.01,0.06), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0,0.04), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(Skills[9] , (0.01,0.04), weight='regular', fontsize=8, alpha=.6,color='white')

    plt.axis('off')
    plt.savefig('resume_page_1.png',facecolor=("#808080"))
    plt.show()


### Done :) ####################################################################################################

if __name__ == '__main__':
    resume_page_1()


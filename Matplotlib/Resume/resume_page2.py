from matplotlib import pyplot as plt
from pylab import rcParams
import resume_page1 as r1

Strength_Title = 'STRENGTHS'
Strengths = ['1','2','3']
Strength_Descriptions = [['11','12'],['21','22'],['31','32']]

Hobby_Title = 'HOBBIES'
Hobbies = ['Badminton','Basketball','Chess','Coding','Travelling','Stamp Collection']

def resume_page_2():

    # Languages
    plt.annotate(r1.Languages_Title, (0,0.95), weight='bold', fontsize=12, alpha=.6,color='white')
    plt.annotate('- ', (0,0.90), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(r1.Languages[0], (0.02,0.90), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0,0.88), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(r1.Languages[1], (0.02,0.88), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0,0.86), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(r1.Languages[2], (0.02,0.86), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0,0.84), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(r1.Languages[3], (0.02,0.84), weight='regular', fontsize=8, alpha=.6,color='white')

    # Strengths
    plt.annotate(Strength_Title, (0.5,0.95), weight='bold', fontsize=12, alpha=.6,color='white')
    plt.annotate(Strengths[0], (0.5, 0.90), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate('- ', (0.5, 0.88), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate(Strength_Descriptions[0][0], (0.52,0.88), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0.5, 0.86), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate(Strength_Descriptions[0][1], (0.52,0.86), weight='regular', fontsize=8, alpha=.6,color='white')

    plt.annotate(Strengths[1], (0.5, 0.79), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate('- ', (0.5, 0.77), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate(Strength_Descriptions[1][0], (0.52,0.77), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0.5, 0.75), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate(Strength_Descriptions[1][1], (0.52,0.75), weight='regular', fontsize=8, alpha=.6,color='white')

    plt.annotate(Strengths[2], (0.5, 0.68), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate('- ', (0.5, 0.66), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate(Strength_Descriptions[2][0], (0.52,0.66), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0.5, 0.64), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate(Strength_Descriptions[2][1], (0.52,0.64), weight='regular', fontsize=8, alpha=.6,color='white')

    # Hobbies
    plt.annotate(Hobby_Title, (0,0.77), weight='bold', fontsize=12, alpha=.6,color='white')
    plt.annotate('- ', (0, 0.72), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate(Hobbies[0], (0.02,0.72), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0, 0.70), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate(Hobbies[1], (0.02,0.70), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0, 0.68), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate(Hobbies[2], (0.02,0.68), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0, 0.66), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate(Hobbies[3], (0.02,0.66), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0, 0.64), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate(Hobbies[4], (0.02,0.64), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate('- ', (0, 0.62), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate(Hobbies[5], (0.02,0.62), weight='regular', fontsize=8, alpha=.6,color='white')

    # Extra
    plt.annotate(r1.Extra_Title, (0.5,0.55), weight='bold', fontsize=12, alpha=.6,color='white')
    plt.annotate(r1.Extra_ID[0] + r1.Extra[0], (0.5,0.50), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(r1.Extra_ID[1] + r1.Extra[1], (0.5, 0.48), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate(r1.Extra_ID[2] + r1.Extra[2], (0.5, 0.46), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate(r1.Extra_ID[3] + r1.Extra[3], (0.5, 0.44), weight='regular', fontsize=8, alpha=.6, color='white')
    plt.annotate(r1.Extra_ID[4] + r1.Extra[4], (0.5, 0.42), weight='regular', fontsize=8, alpha=.6, color='white')



    # Contacts
    plt.annotate(r1.Contact_Title, (0,0.55), weight='bold', fontsize=12, alpha=.6,color='white')
    plt.annotate(r1.Contact_ID[0] + r1.Contact[0], (0,0.50), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(r1.Contact_ID[1] + r1.Contact[1], (0,0.48), weight='regular', fontsize=8, alpha=.6,color='white')
    plt.annotate(r1.Contact_ID[2] + r1.Contact[2], (0,0.46), weight='regular', fontsize=8, alpha=.6,color='white')




    plt.axis('off')
    plt.savefig('resume_page_2.png',facecolor=("#808080"))
    plt.show()

if __name__ == '__main__':
    resume_page_2()




from matplotlib import pylab as plt

from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
fig,ax = plt.subplots()
arr_code = mpimg.imread('rtest.jpg')
imagebox = OffsetImage(arr_code)
ab = AnnotationBbox(imagebox, (0.84, 0.2)) # middle of picture
ax.add_artist(ab)
fig.set_facecolor('grey')
ax.set_facecolor('grey')
# plt.savefig('resumeexample.png', dpi=300, bbox_inches='tight')
# plt.show()

# In digital signal processing, spatial anti-aliasing is a technique for minimizing the distortion artifacts known as aliasing when representing a high-resolution image at a lower resolution.




import pandas as pd
from matplotlib import pyplot as plt

# Matplotlib Marker Styles : https://www.youtube.com/redirect?q=http%3A%2F%2Fbit.ly%2FMatplotlib-Fmt-Str&v=zZZ_RCwp49g&redir_token=QUFFLUhqbGgtTHY2bk1OeHZIdmhKM0tTeEJxaUJrTTU2Z3xBQ3Jtc0tucURqTjQ1Vl9Pa0RwdEx6VmNzRHBVMW4xTVdtdnVfUEpmM25oRGthaVNYUEJBU01rc0hjVFBMMjdoT3NMX1VseFdMbVVSOGFVcm9reGlBYXNLVzVCTW5fSFJBSmEtR1lvdWJnU2tmOXAxSHFkMHk0WQ%3D%3D&event=video_description
# Matplotlib color maps: https://www.youtube.com/redirect?q=https%3A%2F%2Fmatplotlib.org%2F3.1.0%2Ftutorials%2Fcolors%2Fcolormaps.html&v=zZZ_RCwp49g&redir_token=QUFFLUhqbkVYbmdrbFctNVZCVHhpcWRPU0Y1M1d4SkRCd3xBQ3Jtc0tuZ3otNmx2QUlhSWF3TUZIWWpxZXpuZER3emFHNnF4bmdrTXlPazh4eFVzVGRGdlh4ZWZOYnliVWZtdmpDVTM5M2stclFjUm5sLTVqWGNxb3k4dDRHZXlsdi1hR0h2cVdBYUd2QlRMeEdQU3NEd08tZw%3D%3D&event=video_description
plt.style.use('seaborn')
x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174, 538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

# plt.scatter(x,y,s=100,c='green',marker='X',edgecolor='black',linewidth=1,alpha=0.75) # s for size, c for color, alpha is the transparency
# plt.scatter(x,y,s=sizes,cmap='Greens',c=colors,marker='X',edgecolor='black',linewidth=1,alpha=0.75) # pay attention to cmap
# cbar = plt.colorbar()
# cbar.set_label('Satisfaction')

data = pd.read_csv('data3.csv') # most famous youtube videos
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, c=ratio, cmap='summer', edgecolor='black', linewidth=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

plt.xscale('log')
plt.yscale('log')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')
plt.tight_layout()
plt.show()
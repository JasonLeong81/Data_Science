from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9] # in ther first minute, player 1 scored 8 points, player 2 and 3 scored 0 point.
player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [1, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]
labels = ['player1', 'player2', 'player3']
colors = ['#6d904f', '#fc4f30', '#008fd5']


# plt.pie([1, 1, 1], labels=["Player 1", "Player2", "Player3"]) # pie chart can show you the scores of players at one point in time but not the whole time

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors) # stack plot shows you the scores of players over a period of time. not just one time
plt.legend(loc=(0.07, 0.05)) # location for legend to appear on the plot : loc=(x,y)


plt.title('My Awesome Stack Plot')
plt.tight_layout()
plt.show()
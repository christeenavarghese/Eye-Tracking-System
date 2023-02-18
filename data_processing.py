import pandas as pd
from matplotlib import pyplot as plt


df_game = pd.read_excel("./game_2.xlsx", header= None)
df_eye = pd.read_excel("./Output_5.xlsx", header=None)

# dropping the first row because it is just the header, will add it later on!
df_game = df_game.tail(-1)
df_eye = df_eye.tail(-1)

# taking each column from the game excel files to process it into 1 file 
x_game = df_game.iloc[:, 0]
x_game_updated = x_game[::15]
x_game_updated.reset_index(inplace=True, drop=True)

y_game = df_game.iloc[:, 1]
y_game_updated = y_game[::15]
y_game_updated.reset_index(inplace=True, drop=True)

game_time = df_game.iloc[:, 3]
game_time_updated = game_time[::15]
game_time_updated.reset_index(inplace=True, drop=True)

game_left = df_game.iloc[:, 5]
game_left.reset_index(inplace=True, drop=True)
game_center = df_game.iloc[:, 6]
game_center.reset_index(inplace=True, drop=True)
game_right = df_game.iloc[:, 7]
game_right.reset_index(inplace=True, drop=True)
game_up = df_game.iloc[:, 9]
game_up.reset_index(inplace=True, drop=True)
game_down = df_game.iloc[:, 10]
game_down.reset_index(inplace=True, drop=True)



# taking each column from the eye tracking excel files to process into 1 file
x_eye = df_eye.iloc[:, 1]
x_eye.reset_index(inplace=True, drop=True)

y_eye = df_eye.iloc[:, 2]
y_eye.reset_index(inplace=True, drop=True)

eye_time = df_eye.iloc[:, 0]
eye_time.reset_index(inplace=True, drop=True)

eye_left = df_eye.iloc[:, 4]
eye_left.reset_index(inplace=True, drop=True)

eye_center = df_eye.iloc[:, 5]
eye_center.reset_index(inplace=True, drop=True)

eye_right = df_eye.iloc[:, 6]
eye_right.reset_index(inplace=True, drop=True)

eye_up = df_eye.iloc[:, 8]
eye_up.reset_index(inplace=True, drop=True)

eye_down = df_eye.iloc[:, 9]
eye_down.reset_index(inplace=True, drop=True)

# concat everything into 1 potential excel file
combine = pd.concat([game_time_updated, x_game_updated, y_game_updated, eye_time, x_eye, y_eye, 
                     game_left, game_center, game_right, game_up, game_down, 
                     eye_left, eye_center, eye_right, eye_up, eye_down], axis = 1, ignore_index=True)
new = pd.DataFrame(combine)

# new.fillna(0, inplace=True)
new.rename(columns={new.columns[0]: "game_timer",
                    new.columns[1]: "game_x_coor",
                    new.columns[2]: "game_y_coor",
                    new.columns[3]: "eye_timer",
                    new.columns[4]: "eye_x_coor",
                    new.columns[5]: "eye_y_coor", 
                    new.columns[6]: "game_left", 
                    new.columns[7]: "game_center", 
                    new.columns[8]: "game_right", 
                    new.columns[9]: "game_up", 
                    new.columns[10]: "game_down",
                    new.columns[11]: "eye_left", 
                    new.columns[12]: "eye_center", 
                    new.columns[13]: "eye_right", 
                    new.columns[14]: "eye_up", 
                    new.columns[15]: "eye_down", 
                    }, inplace = True)

new.to_excel('./Data.xlsx')

# make the graph 
fig, ax = plt.subplots(figsize=(10, 5), layout='constrained')
ax.plot(new.iloc[:, 0], new.iloc[:, 1], label='Game X Coordinate')  # Plot some data on the axes.
ax.plot(new.iloc[:, 0], new.iloc[:, 2], label='Game Y Coordinate')  # Plot more data on the axes...
ax.plot(new.iloc[:, 3], new.iloc[:, 4], label='Eye X Coordinate')  # ... and some more.
ax.plot(new.iloc[:, 3], new.iloc[:, 5], label='Eye Y Coordinate')  # ... and some more.
ax.set_xlabel('Time')  # Add an x-label to the axes.
ax.set_ylabel('Value')  # Add a y-label to the axes.
ax.set_title("Comparison")  # Add a title to the axes.
ax.legend();  # Add a legend.
plt.show()
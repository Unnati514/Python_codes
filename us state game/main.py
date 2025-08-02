import turtle
import pandas



screen = turtle.Screen()
screen.title("U.S , States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
# for the x and y coordinate on the map
# def get_mouse_click_coor(x,y):
#     print(x,y)   

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?") # for pop-up box

    # if answer_state is one of the states in all the states of the 50_states.csv
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # create a new data frame with the states that were not guessed
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

# for the user to click on the screen to exit the game




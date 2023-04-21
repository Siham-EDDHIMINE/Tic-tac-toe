import tkinter as tk

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] and buttons[i][0]['text'] != '':
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] and buttons[0][i]['text'] != '':
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] and buttons[0][0]['text'] != '':
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] and buttons[0][2]['text'] != '':
        return True
    return False

def on_click(i,j):
    global player
    if player == 'X' and buttons[i][j]['text'] == '':
        buttons[i][j].configure(text='X')
        player = 'O'
    elif player == 'O' and buttons[i][j]['text'] == '':
        buttons[i][j].configure(text='O')
        player = 'X'
    if check_winner():
        print(player + " wins!")
        window.destroy()

window = tk.Tk()
player = 'X'
buttons = [[tk.Button(window, text='', command=lambda i=i, j=j: on_click(i,j)) for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j, ipadx=50, ipady=50)
window.mainloop()
from tkinter import *

class TTT_Label(Label):
    def __init__(self, row, col, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.row = row
        self.col = col
        

class Tic_Tac_Toe:
    def __init__(self):
        window = Tk()
        window.title("Tic Tac Toe")
        window["background"] = "black"
        
        #game state
        self.labels = []
        self.turn = "X"

        for i in range(3):
            row = []
            for j in range(3):
                label = TTT_Label(i, j, text=" ",
                                  width = 3, height = 1,
                                  font = ("Helvetica", "100"))
                label.grid(row = i, column = j, padx = 1, pady = 1)
                label.bind("<Button-1>", self.handle_mouse_click)
                row.append(label)
            self.labels.append(row)

        self.win_label = Label(window, text= " ", font = ("Helvetica", "40"))
        self.win_label.grid(row = 3, column= 0, columnspan = 3, sticky=W+E)
        

        window.mainloop()

    def handle_mouse_click(self, event):
        label = event.widget
        if label["text"] == " ":
            label["text"] = self.turn

            self.check_win(label.row, label.col)

            if self.turn == "X":
                self.turn = "O"
            else:
                self.turn = "X"

    def check_win(self, row, col):
        #win across a row
        if self.labels[row][0]["text"] == \
           self.labels[row][1]["text"] == \
           self.labels[row][2]["text"]:
            self.win_label["text"] = str("Winner: " + self.turn)

        #win down a col
        elif self.labels[0][col]["text"] == \
           self.labels[1][col]["text"] == \
           self.labels[2][col]["text"]:
            print("Winner: ", self.turn)
            self.win_label["text"] = str("Winner: " + self.turn)

        #win down diagonal
        elif self.labels[0][0]["text"] == \
           self.labels[1][1]["text"] == \
           self.labels[2][2]["text"] \
           != " ":
            print("Winner: ", self.turn)
            self.win_label["text"] = str("Winner: " + self.turn)

        elif self.labels[2][0]["text"] == \
           self.labels[1][1]["text"] == \
           self.labels[0][2]["text"] \
           != " ":
            print("Winner: ", self.turn)
            self.win_label["text"] = str("Winner: " + self.turn)

     
def main():
    ttt = Tic_Tac_Toe()

if __name__ == "__main__":
    main()

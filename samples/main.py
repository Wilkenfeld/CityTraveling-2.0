from tkinter import *
from tkinter import filedialog
import classes.graph as graph

# Main Window
root = Tk()

class GUI():

    def main(self):
        # Creation of the main elements of the page
        cityModel = Canvas(master=root, bg="grey", width=500, height=680)
        menu = Frame(master=root, borderwidth=3, height="680", width="700", padx="200")
        title = Label(master=menu, text="CitySim! (ALPHA RELEASE 1.0)")
        JSONMenu = Button(master=menu, text="Open File", padx="5", pady="5", command=self.openJSONFile)

        # Layout of the window
        root.title("CitySim")
        title.pack(side="top")
        JSONMenu.pack(side="top")
        cityModel.grid(sticky="NSEW", rowspan=4)
        menu.grid(column="1", row="1", padx="30")
        root.geometry("1200x680")

        # Execution
        if __name__ == "__main__": root.mainloop()

    def openJSONFile(self):
        self.JSONFilePath = filedialog.askopenfilename(title="Select JSON file", 
                                                        filetypes=[("JSON Files", ".json")])

gui = GUI()
gui.main()
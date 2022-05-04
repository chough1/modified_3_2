from rps_gui import *

def main():
    window = Tk()
    window.title('Rock, Paper, Scissors')
    window.geometry('1000x400')
    window.resizable(False, False)
    window.config(bg="#69cdd6")
    widgets = GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()
# following video tutorial at https://www.youtube.com/watch?v=dlRXp4YSuG4


#frontend 

from tkinter import*
import tkinter.messagebox

class Student:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry("1350x7500+0+0")
        self.root.config(bg="cadet blue")

        stdId = StringVar()
        firstName = StringVar()
        lastName = StringVar()
        surName = StringVar()
        dob = StringVar()
        age = StringVar()
        address = StringVar()
        mobile = StringVar()

        #################################### Frames ####################################
        mainFrame = Frame(self.root, bg="cadet blue")
        mainFrame.grid()


        titFrame = Frame(mainFrame, bd=2, padx=54, pady=8 , bg="Ghost White", relief = RIDGE)
        titFrame.pack(side=TOP)

        self.lblTit = Label(titFrame, font=('arial', 47,'bold'), text="Student Database Management Systems", bg="Ghost White")
        self.lblTit.grid()

        buttonFrame = Frame(mainFrame, bd=2, width=1350, height=70, padx=18, pady=10 , bg="Ghost White", relief = RIDGE)
        buttonFrame.pack(side=BOTTOM)

        dataFrame = Frame(mainFrame, bd=1, width=1300, height=400, padx=20, pady=20 , bg="cadet blue", relief = RIDGE)
        dataFrame.pack(side=BOTTOM)

        dataFrameLeft = LabelFrame(mainFrame, bd=1, width=1000, height=600, padx=20, pady=20, bg="Ghost White", relief = RIDGE, font=('arial', 20,'bold'), text="Student Info\n")
        dataFrameLeft.pack(side=LEFT)

        dataFrameRight = LabelFrame(mainFrame, bd=1, width=450, height=300, padx=31, pady=3 , bg="Ghost White", relief = RIDGE, font=('arial', 20,'bold'), text="Student Details\n" )
        dataFrameRight.pack(side=RIGHT)

        #################################### lables and widgets ####################################
        self.lblTitStdId = Label(dataFrameLeft, font=('arial', 20,'bold'), text="Student ID", padx=2,pady=2, bg="Ghost White")
        self.lblTitStdId.grid(row = 0, column = 0, sticky=W )
        self.txtStdId = Entry(dataFrameLeft, font=('arial', 20,'bold'), textvariable=stdId, width=39)
        self.txtStdId.grid(row = 0, column = 1 )

        self.lblTitStdFirstName = Label(dataFrameLeft, font=('arial', 20,'bold'), text="Student First Name", padx=2,pady=2, bg="Ghost White")
        self.lblTitStdFirstName.grid(row = 1, column = 0, sticky=W )
        self.txtFirstName = Entry(dataFrameLeft, font=('arial', 20,'bold'), textvariable=firstName, width=39)
        self.txtFirstName.grid(row = 1, column = 1 )

        self.lblTitSurName = Label(dataFrameLeft, font=('arial', 20,'bold'), text="Student Last Name", padx=2,pady=2, bg="Ghost White")
        self.lblTitSurName.grid(row = 2, column = 0, sticky=W )
        self.txtSurName = Entry(dataFrameLeft, font=('arial', 20,'bold'), textvariable=surName, width=39)
        self.txtSurName.grid(row = 2, column = 1 )

if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
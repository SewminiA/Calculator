import tkinter
from tkinter import *


root = Tk()
root.title('my cal')
root.resizable(width=0,height=0)


add_value = StringVar()
x=5
y=2
backColor = 'black'
fontColor = 'gray'
display = ''

def butclick(num):
    global display
    display = display+str(num)
    add_value.set(display)

def butclear():
    global  display
    display = ''
    add_value.set(display)

def butequal():
    global  display
    equal = str(round(eval(display),5))
    add_value.set(equal)
    display=equal

screen = Entry(root,bg = 'white',width=25,bd=3,textvariable=add_value,font=('Arial',16,'bold'),fg='blue')
but_7 = Button(root,text=7,font=('Times New roman',20,'bold'),bg=backColor,width=x,height=y,fg=fontColor,command=lambda :butclick(7))
but_8 = Button(root,text=8,font=('Times New roman',20,'bold'),bg=backColor,width=x,height=y,fg=fontColor,command=lambda :butclick(8))
but_9 = Button(root,text=9,font=('Times New roman',20,'bold'),bg=backColor,width=x,height=y,fg=fontColor,command=lambda :butclick(9))
but_4 = Button(root,text=4,font=('Times New roman',20,'bold'),bg=backColor,width=x,height=y,fg=fontColor,command=lambda :butclick(4))
but_5 = Button(root,text=5,font=('Times New roman',20,'bold'),bg=backColor,width=x,height=y,fg=fontColor,command=lambda :butclick(5))
but_6 = Button(root,text=6,font=('Times New roman',20,'bold'),bg=backColor,width=x,height=y,fg=fontColor,command=lambda :butclick(6))
but_1 = Button(root,text=1,font=('Times New roman',20,'bold'),bg=backColor,width=x,height=y,fg=fontColor,command=lambda :butclick(1))
but_2 = Button(root,text=2,font=('Times New roman',20,'bold'),bg=backColor,width=x,height=y,fg=fontColor,command=lambda :butclick(2))
but_3 = Button(root,text=3,font=('Times New roman',20,'bold'),bg=backColor,width=x,height=y,fg=fontColor,command=lambda :butclick(3))
but_0 = Button(root,text=0,font=('Times New roman',20,'bold'),bg=backColor,width=10,padx=6,height=y,fg=fontColor,command=lambda :butclick(0))

but_plus = Button(root,text='+', font=('Times New roman',20,'bold'),bg='black',width=x,height=y,fg='white',command=lambda :butclick('+'))
but_minus = Button(root,text='-', font=('Times New roman',20,'bold'),bg='black',width=x,height=y,fg='white',command=lambda :butclick('-'))
but_product = Button(root,text='*', font=('Times New roman',20,'bold'),bg='black',width=x,height=y,fg='white',command=lambda :butclick('*'))
but_devision = Button(root,text='/', font=('Times New roman',20,'bold'),bg='black',width=x,height=y,fg='white',command=lambda :butclick('/'))



but_equal = Button(root,text='=', font=('Times New roman',20,'bold'),bg='orange',width=x,height=y,fg='green',command=lambda :butequal())
but_clear = Button(root,text='C', font=('Times New roman',20,'bold'),bg='orange',width=15,padx=11,height=y,fg='green',command=lambda :butclear())
but_dot = Button(root,text='.', font=('Times New roman',20,'bold'),bg='black',width=x,height=y,fg='white',command=lambda :butclick('.'))

screen.grid(row=0,column=0,columnspan=4,rowspan=2)
but_7.grid(row=2,column=0)
but_8.grid(row=2,column=1)
but_9.grid(row=2,column=2)
but_4.grid(row=3,column=0)
but_5.grid(row=3,column=1)
but_6.grid(row=3,column=2)
but_1.grid(row=4,column=0)
but_2.grid(row=4,column=1)
but_3.grid(row=4,column=2)
but_0.grid(row=5,column=0,columnspan=2)
but_plus.grid(row=2,column=3)
but_minus.grid(row=3,column=3)
but_product.grid(row=4,column=3)
but_devision.grid(row=5,column=3)
but_equal.grid(row=6,column=3)
but_clear.grid(row=6,column=0,columnspan=3)
but_dot.grid(row=5,column=2)


root.mainloop()

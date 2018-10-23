import tkinter as tk



window = tk.Tk()
#************** 关于RadioButtton×××××××××
# def print_selection():
#     I.config(text='you are have selected'+var.get())
# var  = tk.StringVar()
# I = tk.Label(window,bg = 'yellow',width = 20 ,text = 'empty')
# I.pack()
#
# r1 = tk.Radiobutton(window,text = 'Option A',
#                     #其中variable=var, value='A'的意思就是，
#                     # 当我们鼠标选中了其中一个选项，
#                     # 把value的值A放到变量var中，然后赋值给variable
#                     variable = var,value ='A',
#                     command = print_selection)
# r1.pack()
#×××××××××××××××××××scale控件×××××××××××××××××××××
# def print_selection(v):
#     I.config(text ="you have selected"+v)
# s = tk.Scale(window,label='try me',from_=5,to = 11,orient = tk.HORIZONTAL,
#              length=200,showvalue =0,tickinterval=2,resolution=0.01,command=print_selection)
# s.pack()
# I = tk.Label(window,bg='red',width = 20,text = 'empty')
# I.pack()
#####################checkbutton 控件##################
# def print_selection():
#     if (var1.get()==1)&(var2.get()==0):
#         I.config(text='i love only python')
#     elif (var1.get()==0)&(var2.get()==1):
#         I.config(text='i love only c++')
#     elif (var1.get()==1)&(var2.get()==1):
#         I.config(text='i love both')
#     else :
#         I.config(text='i heat them')
#
# I = tk.Label(window,bg='red',width =20,text ='empty')
# I.pack()
# var1 = tk.IntVar()
# var2 = tk.IntVar()
# c1 = tk.Checkbutton(window,text='python',variable=var1,onvalue=1,offvalue=0,
#                     command=print_selection)
# c1.pack()
# c2 = tk.Checkbutton(window,text='c++',variable=var2,onvalue=1,offvalue=0,
#                     command=print_selection)
# c2.pack()
######################canvas 控件###################
# canvas = tk.Canvas(window,bg='blue',height=100,width=200)
# canvas.pack()
# image_file = tk.PhotoImage(file='ins.gif')
# image = canvas.create_image(10,10,anchor='nw',image=image_file)
# x0,y0,x1,y1=50,50,80,80
# line =canvas.create_line(x0,y0,x1,y1)
# oval = canvas.create_oval(x0,y0,x1,y1,fill = 'red')
# arc = canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start =0,extent=180)
# rect = canvas.create_rectangle(300,30,100+20,30+20)
# def moveit():
#     canvas.move(rect,0,2)
# button = tk.Button(window,text = 'move',command=moveit)
# button.pack()
######################menubar 控件#################
#创建一个菜单栏，理解成一个容器，在窗口的上方
# menubar = tk.Menu(window)
# filemenu = tk.Menu(menubar,tearoff =0)
#
# counter =0
# def do_job():
#     global counter
#     I.config(text = 'do'+str(counter))
#     counter+=1
# I = tk.Label(window,text = "empty")
# I.pack()
# menubar.add_cascade(label='File',menu = filemenu)
#
# filemenu.add_command(label = 'new',command=do_job)
# filemenu.add_command(label = 'open',command=do_job)
# filemenu.add_command(label = 'save',command=do_job)
# filemenu.add_separator()
# filemenu.add_command(label='exit',command = window.quit)
# submenu = tk.Menu(filemenu)
# filemenu.add_cascade(label='import',menu = submenu,underline =0)
# submenu.add_command(label='submenu1',command=do_job)
# window.config(menu=menubar)

window.title("my window")
window.geometry('200x200')
window.mainloop()
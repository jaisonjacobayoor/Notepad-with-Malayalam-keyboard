from tkinter import *
from tkinter import filedialog #this is imported to load a dialog letting user select and open a file from your local drive
from tkinter import font
#import ttk for notebook
from tkinter import ttk

root = Tk()
root.title('Malayalam Keypad V1.0')
root.geometry("1200x800")
root.resizable(0,0)


global open_status_name #from Save File function
open_status_name = False #from Save File function

#functions that define what happens when each button is clicked 


# f1 \  row a
def button_space_clicked():
    my_text.insert(END, " ")

def button_ക_clicked():
    my_text.insert(END, "ക")

def button_enter_clicked():
    my_text.insert(END, "\n")

def button_ച_clicked():
    my_text.insert(END, "ച")

def button_ട_clicked():
    my_text.insert(END, "ട")

def button_ത_clicked():
    my_text.insert(END, "ത")

def button_പ_clicked():
    my_text.insert(END, "പ")

def button_യ_clicked():
    my_text.insert(END, "യ")
    
def button_ഷ_clicked():
    my_text.insert(END, "ഷ")

def button_ൺ_clicked():
    my_text.insert(END, "ൺ")

def button_റ_clicked():
    my_text.insert(END, "റ")


# f1 \  row b

def button_അ_clicked():
    my_text.insert(END, "അ")

def button_ഉ_clicked():
    my_text.insert(END, "ഉ")

def button_ഒ_clicked():
    my_text.insert(END, "ഒ")

def button_അം_clicked():
    my_text.insert(END, "അം")

def button_ഖ_clicked():
    my_text.insert(END, "ഖ")

def button_ഛ_clicked():
    my_text.insert(END, "ഛ")

def button_ഠ_clicked():
    my_text.insert(END, "ഠ")

def button_ഥ_clicked():
    my_text.insert(END, "ഥ")

def button_ഫ_clicked():
    my_text.insert(END, "ഫ")

def button_ര_clicked():
    my_text.insert(END, "ര")

def button_സ_clicked():
    my_text.insert(END, "സ")

def button_ൻ_clicked():
    my_text.insert(END, "ൻ")

def button_question_clicked():
    my_text.insert(END, "?")

# f1 \  row c

def button_ആ_clicked():
    my_text.insert(END, "ആ")

def button_ഊ_clicked():
    my_text.insert(END, "ഊ")

def button_ഓ_clicked():
    my_text.insert(END, "ഓ")

def button_അഃ_clicked():
    my_text.insert(END, "അഃ")
#
def button_ഗ_clicked():
    my_text.insert(END, "ഗ")

def button_ജ_clicked():
    my_text.insert(END, "ജ")

def button_ഡ_clicked():
    my_text.insert(END, "ഡ")

def button_ദ_clicked():
    my_text.insert(END, "ദ")

def button_ബ_clicked():
    my_text.insert(END, "ബ")

def button_ല_clicked():
    my_text.insert(END, "ല")

def button_ഹ_clicked():
    my_text.insert(END, "ഹ")

def button_ർ_clicked():
    my_text.insert(END, "ർ")

def button_fullstop_clicked():
    my_text.insert(END, ".")


# f1 \  row d

def button_ഇ_clicked():
    my_text.insert(END, "ഇ")

def button_എ_clicked():
    my_text.insert(END, "എ")

def button_ഐ_clicked():
    my_text.insert(END, "ഐ")

def button_ഋ_clicked():
    my_text.insert(END, "ഋ")

def button_ഘ_clicked():
    my_text.insert(END, "ഘ")

def button_ഝ_clicked():
    my_text.insert(END, "ഝ")

def button_ഢ_clicked():
    my_text.insert(END, "ഢ")

def button_ധ_clicked():
    my_text.insert(END, "ധ")

def button_ഭ_clicked():
    my_text.insert(END, "ഭ")

def button_വ_clicked():
    my_text.insert(END, "വ")

def button_ള_clicked():
    my_text.insert(END, "ള")

def button_ൽ_clicked():
    my_text.insert(END, "ൽ")

def button_comma_clicked():
    my_text.insert(END, ",")

# f1 \  row e

def button_ഈ_clicked():
    my_text.insert(END, "ഈ")

def button_ഏ_clicked():
    my_text.insert(END, "ഏ")

def button_ഔ_clicked():
    my_text.insert(END, "ഔ")

def button_്_clicked():
    my_text.insert(END, "്")

def button_ങ_clicked():
    my_text.insert(END, "ങ")

def button_ഞ_clicked():
    my_text.insert(END, "ഞ")

def button_ണ_clicked():
    my_text.insert(END, "ണ")

def button_ന_clicked():
    my_text.insert(END, "ന")

def button_മ_clicked():
    my_text.insert(END, "മ")

def button_ശ_clicked():
    my_text.insert(END, "ശ")

def button_ഴ_clicked():
    my_text.insert(END, "ഴ")

def button_ൾ_clicked():
    my_text.insert(END, "ൾ")

def button_quote_clicked():
    my_text.insert(END, "'")

#f2 \ row b (vowels)
def button_ു_clicked():
    my_text.insert(END, "ു")

def button_ൊ_clicked():
    my_text.insert(END, "ൊ")

def button_ം_clicked():
    my_text.insert(END, "ം")

#f2 \ row c (vowels)
def button_ാ_clicked():
    my_text.insert(END, "ാ")

def button_ൂ_clicked():
    my_text.insert(END, "ൂ")

def button_ോ_clicked():
    my_text.insert(END, "ോ")

def button_ഃ_clicked():
    my_text.insert(END, " ഃ")

#f2 \ row d (vowels)

def button_ി_clicked():
    my_text.insert(END, "ി")

def button_െ_clicked():
    my_text.insert(END, "െ")

def button_ൈ_clicked():
    my_text.insert(END, "ൈ")

def button_ൃ_clicked():
    my_text.insert(END, "ൃ")

#f2 \ row e (vowels)

def button_ീ_clicked():
    my_text.insert(END, "ീ")

def button_േ_clicked():
    my_text.insert(END, "േ")

def button_ൌ_clicked():
    my_text.insert(END, "ൌ")

def new_file(): #take all the contents of file and delete it
    my_text.delete("1.0", END) #delete from first line (1.0) to the last line (END)
    root.title('New_File_Malayalam Keypad V1.0') #update the title of window
    Status_bar.config(text = "    New File opened") #update the status bar

    global open_status_name #declaring again to prevent some old values stored to interrupt the save and Save us process
    open_status_name = False #declaring again to prevent some old values stored to interrupt the save and Save us process

def open_file(): #open a file thats located in your folder structure
    my_text.delete("1.0", END) #delete from first line (1.0) to the last line (END)
    text_file = filedialog.askopenfilename(initialdir="", title ="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*") )) #open the window and grab a file name
    
    #for saving purposes //// jump to the //  def save_file():
    if text_file: #if a file name exist
            global open_status_name #know the status of the opened file; now we have to make open_status_name global, so that we could access it from anywhere 
            open_status_name = text_file


    name = text_file #add all the contents of text_file to 'name'
    Status_bar.config(text = f'    {name} ') #update the status bar with the f'string' name // this is to fetch the file name
    name = name.replace("/Users/i321150/Desktop/", "")
    root.title(f'{name}_Malayalam Keypad V1.0') #update the title of window with the f{name} fetched from the filename
    
    

    #open the file 
    text_file = open(text_file, 'r') #r means open the file only for reading
    stuff = text_file.read()

    my_text.insert(END, stuff) #add file to textbox
    text_file.close() #close the opened file

def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension = ".*", initialdir ="", title = "Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")) )
    if text_file: #if user chooses a .txt extension
        #update the statusbar
        name = text_file 
        Status_bar.config(text = f'    Saved: {name} ') #update the status bar with the f'string' name // this is to fetch the file name
        name = name.replace("/Users/i321150/Desktop/", "") #remove the local address from name
        root.title(f'{name}_Malayalam Keypad V1.0') #update the title of window with the f{name} fetched from the filename

        #save the file
        text_file = open(text_file, 'w') #open the text file, this time we'll write instead of 'r'
        text_file.write(my_text.get(1.0, END)) #whatever you 'get' from the text box (my_text), from first line to the last line, then write them into text_file
        text_file.close() #close the file as a best practice

def save_file():
    global open_status_name
    if open_status_name: #if exists // Have we already opened the file with this filename?
        #save the file
        text_file = open(open_status_name, 'w') #open the text file, this time we'll write instead of 'r'
        text_file.write(my_text.get(1.0, END)) #whatever you 'get' from the text box (my_text), from first line to the last line, then write them into text_file
        text_file.close() #close the file as a best practice

        Status_bar.config(text = f'    Saved: {open_status_name} ') #update the status bar with the f'string' name // this is to fetch the file name
    else: #if the file doesnt exist, 'save it as' a new file
        save_as_file()

#///////////////////////////Cut,Copy,Paste//////////////////////////////////////////////////////////////////////////

def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get(): #if somethings highlighted, do something with it:
            selected = my_text.selection_get() #this selection.get() will isolate the highlighted or selected text and..
            my_text.delete("sel.first", "sel.last") #..delete selected text from the textbox, first highlighted + last selected and everything in between 

            root.clipboard_clear() #clear whatever is saved already there in the clipboard..
            root.clipboard_append(selected) #.. and copy whats the latest in "selected"
            Status_bar.config(text = "    Cut from the selected location")

def copy_text(e):
    global selected
    if e: #a check to see if we've used keyboard shortcuts to trigger the coppy
        selected = root.clipboard_get() # when you copy something, copy it to the clipboard


        
    if my_text.selection_get(): #if somethings highlighted, then do this with it:
        selected = my_text.selection_get() #copy is same as cut, only that it doesnt delete the content from the textbox
        
        root.clipboard_clear() #clear whatever is saved already there in the clipboard..
        root.clipboard_append(selected) #.. and copy whats the latest in "selected"
        Status_bar.config(text = "    Copied to Clipboard")
        

def paste_text(e):
    global selected
    if e: #check to see if the keyboard shortcuts are bing used
        selected = root.clipboard_get() #copy whatever is there in clipboard to selected

    else: #else
        if selected: #something is 'selected', then do all these stuff:
            position = my_text.index(INSERT) #grab where the cursor is sittingin text box and assign it to position
            my_text.insert(position, selected) #paste whatever was'selected' in this position
            Status_bar.config(text = "    Pasted to the new location")

#/////////////////////////////////////////////////////////////////  

def button_backspace_clicked():   #http://effbot.org/tkinterbook/text.htm How to perform a backspace event in Text widget
    my_text.delete("%s-1c" % INSERT, INSERT)
    Status_bar.config(text = "    Deleted the last character") #update the status bar


#create main frame
my_frame = Frame(root)
my_frame.pack()

#create Menu / New, Open, Save
my_menu = Menu(root)
root.config(menu = my_menu)

#add a file to the menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label = "File", menu = file_menu )
file_menu.add_command(label = "New", command = new_file)
file_menu.add_command(label = "Open", command = open_file )
file_menu.add_command(label = "Save", command = save_file )
file_menu.add_command(label = "Save As", command = save_as_file )
file_menu.add_command(label = "Exit", command = root.quit)



#create rows
row1 = Frame(root, bg="#ffffff")
row1.pack(expand=True, fill = "both")


#Statusbar at the end of the screen
Status_bar = Label(row1, text = "    I'm ready, Jaison!", anchor=W, bg = "#000000", fg = "#b7cfa5")
Status_bar.pack(fill = X, side = BOTTOM, ipady =5)

#create scrollbar first
text_scroll =Scrollbar(my_frame)
text_scroll.pack(side = RIGHT, expand = True, fill=Y)

#textfield to enter text
my_text = Text(my_frame, width = 1200, font =("Verdana", 26), undo = True, yscrollcommand = text_scroll.set, bg ="#1e1e1e", fg = "#ffffff", height = 14, padx =20,pady = 20, )
my_text.pack(side= RIGHT, expand = True, fill ="both")

#configure the scrollbar for myframe
text_scroll.config(command = my_text.yview)

#making a tabstyle notebook which goes in row 1

style = ttk.Style(row1) #always remember to 'import ttk' in the begining, else there will be a lot of errors
style.configure('lefttab.TNotebook', tabposition  = 'WS')

notebook = ttk.Notebook(row1, style = 'lefttab.TNotebook')
f1 = Frame(notebook, bg = 'white', width = 1200, height = 400)
notebook.add(f1, text = 'Regular')
f2 = Frame(notebook, bg = 'white', width = 1200, height = 400)
notebook.add(f2, text = 'SHIFT')

notebook.pack(expand = True, fill="both")



#GUI starts here::

#now fill f1 tab with buttonrows
btnrow1a = Frame(f1, bg = "#000000")
btnrow1a.pack(expand = True, fill ="both")

btnrow1b = Frame(f1, bg = "#808080")
btnrow1b.pack(expand = True, fill ="both")

btnrow1c = Frame(f1, bg = "#000000")
btnrow1c.pack(expand = True, fill ="both")

btnrow1d = Frame(f1, bg = "#808080")
btnrow1d.pack(expand = True, fill ="both")

btnrow1e = Frame(f1, bg = "#000000")
btnrow1e.pack(expand = True, fill ="both")

#now fill f2 tab with buttonrows
btnrow2a = Frame(f2, bg = "#000000")
btnrow2a.pack(expand = True, fill ="both")

btnrow2b = Frame(f2, bg = "#808080")
btnrow2b.pack(expand = True, fill ="both")

btnrow2c = Frame(f2, bg = "#000000")
btnrow2c.pack(expand = True, fill ="both")

btnrow2d = Frame(f2, bg = "#808080")
btnrow2d.pack(expand = True, fill ="both")

btnrow2e = Frame(f2, bg = "#000000")
btnrow2e.pack(expand = True, fill ="both")


#fill f1> buttonrow 1a with buttons 

btn2=Button(btnrow1a, text ="Undo", font = ("Verdana", 18), command = my_text.edit_undo) 
btn2.pack(side=LEFT, expand=True, fill="both")

btn3=Button(btnrow1a, text ="Redo", font = ("Verdana", 18), command = my_text.edit_redo) 
btn3.pack(side=LEFT, expand=True, fill="both")

btn4=Button(btnrow1a, text ="Space", font = ("Verdana", 18), command = button_space_clicked) 
btn4.pack(side=LEFT, expand=True, fill="both")

btn5=Button(btnrow1a, text ="Enter", font = ("Verdana", 18), command = button_enter_clicked) 
btn5.pack(side=LEFT, expand=True, fill="both")

btn6=Button(btnrow1a, text ="ക", font = ("Verdana", 22), command =button_ക_clicked) 
btn6.pack(side=LEFT, expand=True, fill="both")

btn7=Button(btnrow1a, text ="ച", font = ("Verdana", 22), command =button_ച_clicked) 
btn7.pack(side=LEFT, expand=True, fill="both")

btn8=Button(btnrow1a, text ="ട", font = ("Verdana", 22), command =button_ട_clicked) 
btn8.pack(side=LEFT, expand=True, fill="both")

btn9=Button(btnrow1a, text ="ത", font = ("Verdana", 22), command =button_ത_clicked) 
btn9.pack(side=LEFT, expand=True, fill="both")

btn10=Button(btnrow1a, text ="പ", font = ("Verdana", 22), command =button_പ_clicked) 
btn10.pack(side=LEFT, expand=True, fill="both")

btn11=Button(btnrow1a, text ="യ", font = ("Verdana", 22), command =button_യ_clicked) 
btn11.pack(side=LEFT, expand=True, fill="both")

btn12=Button(btnrow1a, text ="ഷ", font = ("Verdana", 22), command =button_ഷ_clicked) 
btn12.pack(side=LEFT, expand=True, fill="both")

btn13=Button(btnrow1a, text ="ൺ", font = ("Verdana", 22), command =button_ൺ_clicked) 
btn13.pack(side=LEFT, expand=True, fill="both")

btn14=Button(btnrow1a, text ="റ", font = ("Verdana", 22), command =button_റ_clicked) 
btn14.pack(side=LEFT, expand=True, fill="both")

#fill f1> buttonrow 1b with buttons 
btn1=Button(btnrow1b, text ="Cut", font = ("Verdana", 18), command =lambda: cut_text(False)) 
btn1.pack(side=LEFT, expand=True, fill="both")

btn2=Button(btnrow1b, text ="അ", font = ("Verdana", 22), command =button_അ_clicked) 
btn2.pack(side=LEFT, expand=True, fill="both")

btn3=Button(btnrow1b, text ="ഉ", font = ("Verdana", 22), command =button_ഉ_clicked) 
btn3.pack(side=LEFT, expand=True, fill="both")

btn4=Button(btnrow1b, text ="ഒ", font = ("Verdana", 22), command =button_ഒ_clicked) 
btn4.pack(side=LEFT, expand=True, fill="both")

btn5=Button(btnrow1b, text ="അം", font = ("Verdana", 22), command =button_അം_clicked) 
btn5.pack(side=LEFT, expand=True, fill="both")

btn6=Button(btnrow1b, text ="ഖ", font = ("Verdana", 22), command =button_ഖ_clicked) 
btn6.pack(side=LEFT, expand=True, fill="both")

btn7=Button(btnrow1b, text ="ഛ", font = ("Verdana", 22), command =button_ഛ_clicked) 
btn7.pack(side=LEFT, expand=True, fill="both")

btn8=Button(btnrow1b, text ="ഠ", font = ("Verdana", 22), command =button_ഠ_clicked) 
btn8.pack(side=LEFT, expand=True, fill="both")

btn9=Button(btnrow1b, text ="ഥ", font = ("Verdana", 22), command =button_ഥ_clicked) 
btn9.pack(side=LEFT, expand=True, fill="both")

btn10=Button(btnrow1b, text ="ഫ", font = ("Verdana", 22), command =button_ഫ_clicked) 
btn10.pack(side=LEFT, expand=True, fill="both")

btn11=Button(btnrow1b, text ="ര", font = ("Verdana", 22), command =button_ര_clicked) 
btn11.pack(side=LEFT, expand=True, fill="both")

btn12=Button(btnrow1b, text ="സ", font = ("Verdana", 22), command =button_സ_clicked) 
btn12.pack(side=LEFT, expand=True, fill="both")

btn13=Button(btnrow1b, text ="ൻ", font = ("Verdana", 22), command =button_ൻ_clicked) 
btn13.pack(side=LEFT, expand=True, fill="both")

btn14=Button(btnrow1b, text ="?", font = ("Verdana", 18), command =button_question_clicked) 
btn14.pack(side=LEFT, expand=True, fill="both")

#fill f1> buttonrow 1c with buttons 
btn1=Button(btnrow1c, text ="Copy", font = ("Verdana", 18), command =lambda: copy_text(False)) 
btn1.pack(side=LEFT, expand=True, fill="both")

btn2=Button(btnrow1c, text ="ആ", font = ("Verdana", 22), command =button_ആ_clicked) 
btn2.pack(side=LEFT, expand=True, fill="both")

btn3=Button(btnrow1c, text ="ഊ", font = ("Verdana", 22), command =button_ഊ_clicked) 
btn3.pack(side=LEFT, expand=True, fill="both")

btn4=Button(btnrow1c, text ="ഓ", font = ("Verdana", 22), command =button_ഓ_clicked) 
btn4.pack(side=LEFT, expand=True, fill="both")

btn5=Button(btnrow1c, text ="അഃ", font = ("Verdana", 22), command =button_അഃ_clicked) 
btn5.pack(side=LEFT, expand=True, fill="both")

btn6=Button(btnrow1c, text ="ഗ", font = ("Verdana", 22), command =button_ഗ_clicked) 
btn6.pack(side=LEFT, expand=True, fill="both")

btn7=Button(btnrow1c, text ="ജ", font = ("Verdana", 22), command =button_ജ_clicked) 
btn7.pack(side=LEFT, expand=True, fill="both")

btn8=Button(btnrow1c, text ="ഡ", font = ("Verdana", 22), command =button_ഡ_clicked) 
btn8.pack(side=LEFT, expand=True, fill="both")

btn9=Button(btnrow1c, text ="ദ", font = ("Verdana", 22), command =button_ദ_clicked) 
btn9.pack(side=LEFT, expand=True, fill="both")

btn10=Button(btnrow1c, text ="ബ", font = ("Verdana", 22), command =button_ബ_clicked) 
btn10.pack(side=LEFT, expand=True, fill="both")

btn11=Button(btnrow1c, text ="ല", font = ("Verdana", 22), command =button_ല_clicked) 
btn11.pack(side=LEFT, expand=True, fill="both")

btn12=Button(btnrow1c, text ="ഹ", font = ("Verdana", 22), command =button_ഹ_clicked) 
btn12.pack(side=LEFT, expand=True, fill="both")

btn13=Button(btnrow1c, text ="ർ", font = ("Verdana", 22), command =button_ർ_clicked) 
btn13.pack(side=LEFT, expand=True, fill="both")

btn14=Button(btnrow1c, text =".", font = ("Verdana", 18), command =button_fullstop_clicked) 
btn14.pack(side=LEFT, expand=True, fill="both")

#fill f1> buttonrow 1d with buttons 
btn1=Button(btnrow1d, text ="Paste", font = ("Verdana", 18), command =lambda: paste_text(False)) 
btn1.pack(side=LEFT, expand=True, fill="both")

btn2=Button(btnrow1d, text ="ഇ", font = ("Verdana", 22), command =button_ഇ_clicked) 
btn2.pack(side=LEFT, expand=True, fill="both")

btn3=Button(btnrow1d, text ="എ", font = ("Verdana", 22), command =button_എ_clicked) 
btn3.pack(side=LEFT, expand=True, fill="both")

btn4=Button(btnrow1d, text ="ഐ", font = ("Verdana", 22), command =button_ഐ_clicked) 
btn4.pack(side=LEFT, expand=True, fill="both")

btn5=Button(btnrow1d, text ="ഋ", font = ("Verdana", 22), command =button_ഋ_clicked) 
btn5.pack(side=LEFT, expand=True, fill="both")

btn6=Button(btnrow1d, text ="ഘ", font = ("Verdana", 22), command =button_ഘ_clicked) 
btn6.pack(side=LEFT, expand=True, fill="both")

btn7=Button(btnrow1d, text ="ഝ", font = ("Verdana", 22), command =button_ഝ_clicked) 
btn7.pack(side=LEFT, expand=True, fill="both")

btn8=Button(btnrow1d, text ="ഢ", font = ("Verdana", 22), command =button_ഢ_clicked) 
btn8.pack(side=LEFT, expand=True, fill="both")

btn9=Button(btnrow1d, text ="ധ", font = ("Verdana", 22), command =button_ധ_clicked) 
btn9.pack(side=LEFT, expand=True, fill="both")

btn10=Button(btnrow1d, text ="ഭ", font = ("Verdana", 22), command =button_ഭ_clicked) 
btn10.pack(side=LEFT, expand=True, fill="both")

btn11=Button(btnrow1d, text ="വ", font = ("Verdana", 22), command =button_വ_clicked) 
btn11.pack(side=LEFT, expand=True, fill="both")

btn12=Button(btnrow1d, text ="ള", font = ("Verdana", 22), command =button_ള_clicked) 
btn12.pack(side=LEFT, expand=True, fill="both")

btn13=Button(btnrow1d, text ="ൽ", font = ("Verdana", 22), command =button_ൽ_clicked) 
btn13.pack(side=LEFT, expand=True, fill="both")

btn14=Button(btnrow1d, text =",", font = ("Verdana", 18), command =button_comma_clicked) 
btn14.pack(side=LEFT, expand=True, fill="both")

#fill f1> buttonrow 1e with buttons 
btn1=Button(btnrow1e, text ="Delete", font = ("Verdana", 18), command =button_backspace_clicked) 
btn1.pack(side=LEFT, expand=True, fill="both")

btn2=Button(btnrow1e, text ="ഈ", font = ("Verdana", 22), command =button_ഈ_clicked) 
btn2.pack(side=LEFT, expand=True, fill="both")

btn3=Button(btnrow1e, text ="ഏ", font = ("Verdana", 22), command =button_ഏ_clicked) 
btn3.pack(side=LEFT, expand=True, fill="both")

btn4=Button(btnrow1e, text ="ഔ", font = ("Verdana", 22), command =button_ഔ_clicked) 
btn4.pack(side=LEFT, expand=True, fill="both")

btn5=Button(btnrow1e, text ="്", font = ("Verdana", 22), command =button_്_clicked) 
btn5.pack(side=LEFT, expand=True, fill="both")

btn6=Button(btnrow1e, text ="ങ", font = ("Verdana", 22), command =button_ങ_clicked) 
btn6.pack(side=LEFT, expand=True, fill="both")

btn7=Button(btnrow1e, text ="ഞ", font = ("Verdana", 22), command =button_ഞ_clicked) 
btn7.pack(side=LEFT, expand=True, fill="both")

btn8=Button(btnrow1e, text ="ണ", font = ("Verdana", 22), command =button_ണ_clicked) 
btn8.pack(side=LEFT, expand=True, fill="both")

btn9=Button(btnrow1e, text ="ന", font = ("Verdana", 22), command =button_ന_clicked) 
btn9.pack(side=LEFT, expand=True, fill="both")

btn10=Button(btnrow1e, text ="മ", font = ("Verdana", 22), command =button_മ_clicked) 
btn10.pack(side=LEFT, expand=True, fill="both")

btn11=Button(btnrow1e, text ="ശ", font = ("Verdana", 22), command =button_ശ_clicked) 
btn11.pack(side=LEFT, expand=True, fill="both")

btn12=Button(btnrow1e, text ="ഴ", font = ("Verdana", 22), command =button_ഴ_clicked) 
btn12.pack(side=LEFT, expand=True, fill="both")

btn13=Button(btnrow1e, text ="ൾ", font = ("Verdana", 22), command =button_ൾ_clicked) 
btn13.pack(side=LEFT, expand=True, fill="both")

btn14=Button(btnrow1e, text ="'", font = ("Verdana", 18), command =button_quote_clicked) 
btn14.pack(side=LEFT, expand=True, fill="both")




#fill f2> buttonrow 2a with buttons 

btn2=Button(btnrow2a, text ="Undo", font = ("Verdana", 18), command = my_text.edit_undo) 
btn2.pack(side=LEFT, expand=True, fill="both")

btn3=Button(btnrow2a, text ="Redo", font = ("Verdana", 18), command = my_text.edit_redo) 
btn3.pack(side=LEFT, expand=True, fill="both")

btn4=Button(btnrow2a, text ="Space", font = ("Verdana", 18), command =button_space_clicked) 
btn4.pack(side=LEFT, expand=True, fill="both")

btn5=Button(btnrow2a, text ="Enter", font = ("Verdana", 18), command =button_enter_clicked) 
btn5.pack(side=LEFT, expand=True, fill="both")

btn6=Button(btnrow2a, text ="ക", font = ("Verdana", 22), command =button_ക_clicked ) 
btn6.pack(side=LEFT, expand=True, fill="both")

btn7=Button(btnrow2a, text ="ച", font = ("Verdana", 22), command =button_ച_clicked ) 
btn7.pack(side=LEFT, expand=True, fill="both")

btn8=Button(btnrow2a, text ="ട", font = ("Verdana", 22), command =button_ട_clicked ) 
btn8.pack(side=LEFT, expand=True, fill="both")

btn9=Button(btnrow2a, text ="ത", font = ("Verdana", 22), command =button_ത_clicked ) 
btn9.pack(side=LEFT, expand=True, fill="both")

btn10=Button(btnrow2a, text ="പ", font = ("Verdana", 22), command =button_പ_clicked) 
btn10.pack(side=LEFT, expand=True, fill="both")

btn11=Button(btnrow2a, text ="യ", font = ("Verdana", 22), command =button_യ_clicked ) 
btn11.pack(side=LEFT, expand=True, fill="both")

btn12=Button(btnrow2a, text ="ഷ", font = ("Verdana", 22), command =button_ഷ_clicked ) 
btn12.pack(side=LEFT, expand=True, fill="both")

btn13=Button(btnrow2a, text ="ൺ", font = ("Verdana", 22), command =button_ൺ_clicked) 
btn13.pack(side=LEFT, expand=True, fill="both")

btn14=Button(btnrow2a, text ="റ", font = ("Verdana", 22), command =button_റ_clicked ) 
btn14.pack(side=LEFT, expand=True, fill="both")

#fill f1> buttonrow 1b with buttons 
btn1=Button(btnrow2b, text ="Cut", font = ("Verdana", 18), command =lambda: cut_text(False)) 
btn1.pack(side=LEFT, expand=True, fill="both")

btn2=Button(btnrow2b, text ="അ", font = ("Verdana", 22), command =button_അ_clicked ) 
btn2.pack(side=LEFT, expand=True, fill="both")

btn3=Button(btnrow2b, text =" ു", font = ("Verdana", 22), command =button_ു_clicked ) 
btn3.pack(side=LEFT, expand=True, fill="both")

btn4=Button(btnrow2b, text =" ൊ", font = ("Verdana", 22), command =button_ൊ_clicked ) 
btn4.pack(side=LEFT, expand=True, fill="both")

btn5=Button(btnrow2b, text =" ം", font = ("Verdana", 22), command =button_ം_clicked ) 
btn5.pack(side=LEFT, expand=True, fill="both")

btn6=Button(btnrow2b, text ="ഖ", font = ("Verdana", 22), command =button_ഖ_clicked ) 
btn6.pack(side=LEFT, expand=True, fill="both")

btn7=Button(btnrow2b, text ="ഛ", font = ("Verdana", 22), command =button_ഛ_clicked ) 
btn7.pack(side=LEFT, expand=True, fill="both")

btn8=Button(btnrow2b, text ="ഠ", font = ("Verdana", 22), command =button_ഠ_clicked ) 
btn8.pack(side=LEFT, expand=True, fill="both")

btn9=Button(btnrow2b, text ="ഥ", font = ("Verdana", 22), command =button_ഥ_clicked ) 
btn9.pack(side=LEFT, expand=True, fill="both")

btn10=Button(btnrow2b, text ="ഫ", font = ("Verdana", 22), command =button_ഫ_clicked) 
btn10.pack(side=LEFT, expand=True, fill="both")

btn11=Button(btnrow2b, text ="ര", font = ("Verdana", 22), command =button_ര_clicked) 
btn11.pack(side=LEFT, expand=True, fill="both")

btn12=Button(btnrow2b, text ="സ", font = ("Verdana", 22), command =button_സ_clicked ) 
btn12.pack(side=LEFT, expand=True, fill="both")

btn13=Button(btnrow2b, text ="ൻ", font = ("Verdana", 22), command =button_ൻ_clicked ) 
btn13.pack(side=LEFT, expand=True, fill="both")

btn14=Button(btnrow2b, text ="?", font = ("Verdana", 18), command =button_question_clicked) 
btn14.pack(side=LEFT, expand=True, fill="both")

#fill f1> buttonrow 1c with buttons 
btn1=Button(btnrow2c, text ="Copy", font = ("Verdana", 18), command =lambda: copy_text(False)) 
btn1.pack(side=LEFT, expand=True, fill="both")

btn2=Button(btnrow2c, text =" ാ", font = ("Verdana", 22), command =button_ാ_clicked ) 
btn2.pack(side=LEFT, expand=True, fill="both")

btn3=Button(btnrow2c, text =" ൂ", font = ("Verdana", 22), command =button_ൂ_clicked ) 
btn3.pack(side=LEFT, expand=True, fill="both")

btn4=Button(btnrow2c, text =" ോ", font = ("Verdana", 22), command =button_ോ_clicked ) 
btn4.pack(side=LEFT, expand=True, fill="both")

btn5=Button(btnrow2c, text =" ഃ", font = ("Verdana", 22), command =button_ഃ_clicked) 
btn5.pack(side=LEFT, expand=True, fill="both")

btn6=Button(btnrow2c, text ="ഗ", font = ("Verdana", 22), command =button_ഗ_clicked) 
btn6.pack(side=LEFT, expand=True, fill="both")

btn7=Button(btnrow2c, text ="ജ", font = ("Verdana", 22), command =button_ജ_clicked) 
btn7.pack(side=LEFT, expand=True, fill="both")

btn8=Button(btnrow2c, text ="ഡ", font = ("Verdana", 22), command =button_ഡ_clicked) 
btn8.pack(side=LEFT, expand=True, fill="both")

btn9=Button(btnrow2c, text ="ദ", font = ("Verdana", 22), command =button_ദ_clicked ) 
btn9.pack(side=LEFT, expand=True, fill="both")

btn10=Button(btnrow2c, text ="ബ", font = ("Verdana", 22), command =button_ബ_clicked ) 
btn10.pack(side=LEFT, expand=True, fill="both")

btn11=Button(btnrow2c, text ="ല", font = ("Verdana", 22), command =button_ല_clicked ) 
btn11.pack(side=LEFT, expand=True, fill="both")

btn12=Button(btnrow2c, text ="ഹ", font = ("Verdana", 22), command =button_ഹ_clicked ) 
btn12.pack(side=LEFT, expand=True, fill="both")

btn13=Button(btnrow2c, text ="ർ", font = ("Verdana", 22), command =button_ർ_clicked ) 
btn13.pack(side=LEFT, expand=True, fill="both")

btn14=Button(btnrow2c, text =".", font = ("Verdana", 18), command =button_fullstop_clicked) 
btn14.pack(side=LEFT, expand=True, fill="both")

#fill f1> buttonrow 1d with buttons 
btn1=Button(btnrow2d, text ="Paste", font = ("Verdana", 18), command =lambda: paste_text(False)) 
btn1.pack(side=LEFT, expand=True, fill="both")

btn2=Button(btnrow2d, text =" ി", font = ("Verdana", 22), command =button_ി_clicked) 
btn2.pack(side=LEFT, expand=True, fill="both")

btn3=Button(btnrow2d, text =" െ", font = ("Verdana", 22), command =button_െ_clicked) 
btn3.pack(side=LEFT, expand=True, fill="both")

btn4=Button(btnrow2d, text =" ൈ", font = ("Verdana", 22), command =button_ൈ_clicked) 
btn4.pack(side=LEFT, expand=True, fill="both")

btn5=Button(btnrow2d, text =" ൃ", font = ("Verdana", 22), command =button_ൃ_clicked) 
btn5.pack(side=LEFT, expand=True, fill="both")

btn6=Button(btnrow2d, text ="ഘ", font = ("Verdana", 22), command =button_ഘ_clicked ) 
btn6.pack(side=LEFT, expand=True, fill="both")

btn7=Button(btnrow2d, text ="ഝ", font = ("Verdana", 22), command =button_ഝ_clicked ) 
btn7.pack(side=LEFT, expand=True, fill="both")

btn8=Button(btnrow2d, text ="ഢ", font = ("Verdana", 22), command =button_ഢ_clicked ) 
btn8.pack(side=LEFT, expand=True, fill="both")

btn9=Button(btnrow2d, text ="ധ", font = ("Verdana", 22), command =button_ധ_clicked ) 
btn9.pack(side=LEFT, expand=True, fill="both")

btn10=Button(btnrow2d, text ="ഭ", font = ("Verdana", 22), command =button_ഭ_clicked ) 
btn10.pack(side=LEFT, expand=True, fill="both")

btn11=Button(btnrow2d, text ="വ", font = ("Verdana", 22), command =button_വ_clicked ) 
btn11.pack(side=LEFT, expand=True, fill="both")

btn12=Button(btnrow2d, text ="ള", font = ("Verdana", 22), command =button_ള_clicked ) 
btn12.pack(side=LEFT, expand=True, fill="both")

btn13=Button(btnrow2d, text ="ൽ", font = ("Verdana", 22), command =button_ൽ_clicked) 
btn13.pack(side=LEFT, expand=True, fill="both")

btn14=Button(btnrow2d, text =",", font = ("Verdana", 18), command =button_comma_clicked) 
btn14.pack(side=LEFT, expand=True, fill="both")

#fill f1> buttonrow 1e with buttons 
btn1=Button(btnrow2e, text ="Delete", font = ("Verdana", 18), command =button_backspace_clicked) 
btn1.pack(side=LEFT, expand=True, fill="both")

btn2=Button(btnrow2e, text =" ീ", font = ("Verdana", 22), command =button_ീ_clicked ) 
btn2.pack(side=LEFT, expand=True, fill="both")

btn3=Button(btnrow2e, text =" േ", font = ("Verdana", 22), command =button_േ_clicked ) 
btn3.pack(side=LEFT, expand=True, fill="both")

btn4=Button(btnrow2e, text =" ൌ", font = ("Verdana", 22), command =button_ൌ_clicked ) 
btn4.pack(side=LEFT, expand=True, fill="both")

btn5=Button(btnrow2e, text ="്", font = ("Verdana", 22), command =button_്_clicked ) 
btn5.pack(side=LEFT, expand=True, fill="both")

btn6=Button(btnrow2e, text ="ങ", font = ("Verdana", 22), command =button_ങ_clicked ) 
btn6.pack(side=LEFT, expand=True, fill="both")

btn7=Button(btnrow2e, text ="ഞ", font = ("Verdana", 22), command =button_ഞ_clicked) 
btn7.pack(side=LEFT, expand=True, fill="both")

btn8=Button(btnrow2e, text ="ണ", font = ("Verdana", 22), command =button_ണ_clicked ) 
btn8.pack(side=LEFT, expand=True, fill="both")

btn9=Button(btnrow2e, text ="ന", font = ("Verdana", 22), command =button_ന_clicked ) 
btn9.pack(side=LEFT, expand=True, fill="both")

btn10=Button(btnrow2e, text ="മ", font = ("Verdana", 22), command =button_മ_clicked) 
btn10.pack(side=LEFT, expand=True, fill="both")

btn11=Button(btnrow2e, text ="ശ", font = ("Verdana", 22), command =button_ശ_clicked ) 
btn11.pack(side=LEFT, expand=True, fill="both")

btn12=Button(btnrow2e, text ="ഴ", font = ("Verdana", 22), command =button_ഴ_clicked ) 
btn12.pack(side=LEFT, expand=True, fill="both")

btn13=Button(btnrow2e, text ="ൾ", font = ("Verdana", 22), command =button_ൾ_clicked ) 
btn13.pack(side=LEFT, expand=True, fill="both")

btn14=Button(btnrow2e, text ="'", font = ("Verdana", 18), command =button_quote_clicked ) 
btn14.pack(side=LEFT, expand=True, fill="both")



#////// making the cut copy paste compliant with the shortcuts from windows keyboard and to fix copy to clipboard
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-x>', paste_text)
#////// making the cut copy paste compliant with the shortcuts from Mac keyboard and to fix copy to clipboard
root.bind('<Command-Key-x>', cut_text)
root.bind('<Command-Key-c>', copy_text)
root.bind('<Command-Key-x>', paste_text)

root.mainloop()
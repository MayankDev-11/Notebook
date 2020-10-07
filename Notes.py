import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import pyttsx3 #pip install pyttsx3
import os


# This is defined to speak

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# This the start point of the application.
main_application = tk.Tk()
main_application.iconbitmap("Images\download.ico")
main_application.title("Notes")
main_application.geometry("1200x800")

main_menu = tk.Menu()
# These are some of the images required,which you can access from the images file if you want.

new_icon = tk.PhotoImage(file=r'C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\new.png')
open_icon = tk.PhotoImage(file=r'C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\open.png')
save_icon = tk.PhotoImage(file=r'C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\save_as.png')
exit_icon = tk.PhotoImage(file=r'C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\exit.png')

# These are the menu that are being defined now but be used in the lower part of the code.

file = tk.Menu(main_menu,tearoff=False)

copy_icon = tk.PhotoImage(file=r'C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\copy.png')
paste_icon = tk.PhotoImage(file=r'C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\paste.png')
cut_icon = tk.PhotoImage(file=r'C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\cut.png')
find_icon = tk.PhotoImage(file=r'C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\search.png')

edit = tk.Menu(main_menu,tearoff=False)

view = tk.Menu(main_menu,tearoff=False)

light_default_icon = tk.PhotoImage(file=r'C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\light.png')
light_plus_icon = tk.PhotoImage(file=r'C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\light1.png')
dark_icon = tk.PhotoImage(file=r'C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\dark.png')
red_icon = tk.PhotoImage(file=r'C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\red.png')
monkai_icon = tk.PhotoImage(file=r'C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\monkai.png')
night_blue_icon = tk.PhotoImage(file=r'C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\dark.png')


color_theme = tk.Menu(main_menu,tearoff=False)

theme_choice = tk.StringVar()

# This is a tuple to change color themes in the background

color_icons = (light_default_icon,light_plus_icon,dark_icon,red_icon,monkai_icon,night_blue_icon)

# This is the color dict and color codes

color_dict = {

    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#d3b774','#ffe8e8'),
    'Monkai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2')

}


# This is to add the menus which we defined earlier to get into the main_menu

main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label ='Edit',menu=edit)
main_menu.add_cascade(label = "View",menu=view)
main_menu.add_cascade(label = "ColorTheme",menu=color_theme)


# Tool Bar

tool_bar = ttk.Label(main_application)
tool_bar.pack(side = tk.TOP,fill = tk.X)

# Font

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width = 30,textvariable = font_family,state = 'readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('@MS Mincho'))
font_box.grid(row = 0,column = 0, padx = 5)

# Size box

size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width = 14, textvariable = size_var, state = 'readonly')
font_size['values'] = tuple(range(8,81))
font_size.current(1)
font_size.grid(row = 0,column = 1,padx = 5)


# Bold button

bold_icon = tk.PhotoImage(file = r"C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\bold.png")
bold_btn = tk.Button(tool_bar,image = bold_icon)
bold_btn['border'] = '0'
bold_btn.grid(row = 0,column = 2,padx = 5)


# Italic button
italic_icon = tk.PhotoImage(file=r"C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\italic.png")
italic_btn = tk.Button(tool_bar,image=italic_icon)
italic_btn['border'] = '0'
italic_btn.grid(row = 0,column =3,padx = 5)

# underline button

underline_icon = tk.PhotoImage(file = r"C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\underline.png")
underline_btn = tk.Button(tool_bar,image = underline_icon)
underline_btn['border'] = '0'
underline_btn.grid(row = 0,column =4,padx = 5)

# font color button
font_color_icon = tk.PhotoImage(file = r"C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\font_color.png")
font_color_btn = tk.Button(tool_bar,image = font_color_icon)
font_color_btn['border'] = '0'
font_color_btn.grid(row = 0,column = 8,padx = 5 )

# align left

align_left_icon = tk.PhotoImage(file=r'C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\align_left.png')
align_left_btn = tk.Button(tool_bar, image=align_left_icon)
align_left_btn['border'] = '0'
align_left_btn.grid(row=0, column=5, padx=5)

# align center
align_center_icon = tk.PhotoImage(file = r"C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\align_center.png")
align_center_btn = tk.Button(tool_bar, image=align_center_icon)
align_center_btn['border'] = '0'
align_center_btn.grid(row=0, column=6, padx=5)

# align right
align_right_icon = tk.PhotoImage(file = r"C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\align_right.png")
align_right_btn = tk.Button(tool_bar, image=align_right_icon)
align_right_btn['border'] = '0'
align_right_btn.grid(row=0, column=7, padx=5)



# audio
audio_icon = tk.PhotoImage(file =r'C:\Users\Mayank\OneDrive\Documents\Python\Python projects\Images\audio.png')
audio_btn = tk.Button(tool_bar, image = audio_icon)
audio_btn['border'] = '0'
audio_btn.grid(row = 0, column = 10, padx = 5)


# This is the area where the user will write the text.

text_editor = tk.Text(main_application)
text_editor.config(wrap = 'word',relief = tk.FLAT)

# This is the scroll bar to see the text

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT,fill = tk.Y)
text_editor.pack(fill=tk.BOTH, expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)


current_font_family = '@MS Mincho'
current_font_size = 12

# These are the options to change fonts and size

def change_font(event = None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font = (current_font_family,current_font_size))

def change_size(event = None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font = (current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_size)


# This is to change the boldness of the text.

def change_bold():

    text_property = tk.font.Font(font = text_editor['font'])

    if text_property.actual()['weight'] == 'normal':

        text_editor.configure(font =(current_font_family,current_font_size,'bold'))
    else:
        text_editor.configure(font = (current_font_family,current_font_size,'normal'))

bold_btn.configure(command = change_bold)

# This function is to change the text from normal to italic

def change_italic():

    text_property = tk.font.Font(font = text_editor['font'])

    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font = (current_font_family,current_font_size,'italic'))

    else:

        text_editor.configure(font=(current_font_family, current_font_size, 'roman'))

italic_btn.configure(command = change_italic)

# This function is to underline the text

def change_underline():
    text_property = tk.font.Font(font = text_editor['font'])

    if text_property.actual()['underline'] == 0:

        text_editor.configure(font = (current_font_family,current_font_size,'underline'))

    else:

        text_editor.configure(font = (current_font_family,current_font_size,'normal'))

underline_btn.configure(command = change_underline)

# This is to change the color of your text

def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg = color_var[1])

font_color_btn.configure(command = change_font_color)

# These all 3 functions are alignments

def align_left():

    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify = tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')


align_left_btn.configure(command = align_left)

def align_center():

    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify = tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_btn.configure(command = align_center)

def align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify = tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_btn.configure(command = align_right)

# This function is to make your text speak out by your pc

def speak():
    audio = text_editor.get(1.0, 'end')
    engine.say(audio)
    engine.runAndWait()

audio_btn.configure(command = speak)

# These is the status bar which count the number of charectors and words

status_bar = ttk.Label(main_application,text = 'Status Bar')
status_bar.pack(side = tk.BOTTOM)

text_changed = False

# Charector count

def changed(event = None):

    global text_changed
    if text_editor.edit_modified() or True:
        text_changed = True
        words = len(text_editor.get(1.0,'end-1c').split())
        charectors = len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text = f' Charectors : {charectors} Words : {words}')

    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',changed)

url = ""

# Create a new file

# This option is deprecated to clear the things you have written and clear the text

def newFile(event = None):
    global url
    main_application.title("Notes")
    url = None
    text_editor.delete(1.0, tk.END)


file.add_command(label = 'New',image = new_icon,compound = tk.LEFT,accelerator = "Ctrl+N",command = new_icon)

# Open File

# This is to open a file from your pc

def open_file(event = None):

    global url
    url = filedialog.askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if url == "":
        url = None
    else:
        main_application.title(os.path.basename(url) + " - Notes")
        text_editor.delete(1.0, 'end')
        f = open(url, "r")
        text_editor.insert(1.0, f.read())
        f.close()


file.add_command(label = "Open",image = open_icon,compound = tk.LEFT,accelerator = "Ctrl+O",command = open_file)


# Save a file

# This option is to save a file.

def save_file(event = None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0.tk.END))
            with open(url,'w',encoding="utf-8") as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w',defaultextension = '.txt',
                                           filetypes = (("Text File,*txt"),("All Files","*.*")))
            content2 = text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

file.add_command(label = "Save",image = save_icon,compound = tk.LEFT,accelerator = "Ctrl+S",command = save_file)



# This is to exit

def exit_func():
    global url,text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel("Warning", "Do you want to save this file?")
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url,"w",encoding="utf-8") as fw:
                        fw.write(content)
                        main_application.destroy()

                else:
                    content2 = str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode = "w",defaultextension = ".txt",filetypes = (("Text File","*.txt"),("All Files","*.*")))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file.add_command(label = "Exit",image = exit_icon,compound = tk.LEFT,accelerator = "Ctrl+Q",command = exit_func)

# Edit menu

# These are some edit options like cut,copy,paste

edit.add_command(label = "Copy",image = copy_icon,compound = tk.LEFT,accelerator ="Ctrl+C",command = lambda : text_editor.event_generate("<Control-c>"))
edit.add_command(label = "Paste",image = paste_icon,compound = tk.LEFT,accelerator ="Ctrl+V",command = lambda : text_editor.event_generate("<Control-v>"))
edit.add_command(label = "Cut",image = cut_icon,compound = tk.LEFT,accelerator ="Ctrl+X",command = lambda : text_editor.event_generate("<Control-x>"))

# This function is to find a word in your editor and replace

def find_func(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break

                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0, 0)

    ## frame
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text='Replace')

    ## entry
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)

    ## label grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()


edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F')

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

# These are some functions to show status bar if you want or hide it

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side = tk.TOP,fill = tk.X)
        text_editor.pack(fill = tk.BOTH,expand = True)
        status_bar.pack(side = tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side = tk.BOTTOM)
        show_statusbar = True

view.add_checkbutton(label = "Tool Bar",onvalue = True, offvalue = 0,variable = show_toolbar,compound = tk.LEFT,command = hide_toolbar)
view.add_checkbutton(label = "Status Bar",onvalue = 1, offvalue = False,variable = show_statusbar,compound = tk.LEFT,command = hide_statusbar)

# This is to change the theme.

def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(background = bg_color,fg = fg_color)

count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i,image = color_icons[count],variable = theme_choice,compound = tk.LEFT,command = change_theme)
    count += 1

# This is the command which says to put all the menus in main_application

main_application.config(menu = main_menu)


# This is to define all the shortcut keys.

main_application.bind("<Control-n>",newFile)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-q>",exit_func)
main_application.bind("<Control-f>",find_func)

main_application.mainloop()

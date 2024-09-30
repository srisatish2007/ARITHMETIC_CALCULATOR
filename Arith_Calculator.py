from customtkinter import *
from math import *

# import time

set_appearance_mode("system")
set_default_color_theme("blue")
lst = []
lst_oper = []
global big_disp_text, lbl_dis_big, lbl_dis_small, text_Var
big_disp_text = ""
# text_var=""
append_text = ""
big_disp_text2 = ""
global i, solution
solution = 0
arith_animate_x = 0
sci_animate_x = -350

def button_press(button_name):
    global big_disp_text, lbl_dis_big, lbl_dis_small
    button_name_disp = str(button_name)

    def displaying_text():
        global big_disp_text, lbl_dis_big, lbl_dis_small, big_disp_text2
        if len(big_disp_text) <= 17:
            big_disp_text2 = big_disp_text2 + str(button_name)
            # big_disp_text2 = big_disp_text
        if button_name != "=":
            if len(big_disp_text) <= 16:
                big_disp_text = big_disp_text + str(button_name)
                # big_disp_text2=big_disp_text
                lbl_dis_big.configure(text=big_disp_text)
            if len(big_disp_text) > 10:
                lbl_dis_big.configure(
                    font=("Helvetica 24 bold", 40, "bold"),
                )
            if len(big_disp_text) >= 15:
                lbl_dis_big.configure(
                    font=("Helvetica 24 bold", 32, "bold"),
                )
            if len(big_disp_text) > 15:
                lbl_dis_big.configure(
                    font=("Helvetica 24 bold", 22, "bold"),
                )

    displaying_text()


def Creating_list():

    global append_text, big_disp_text, big_disp_text2

    # print(big_disp_text)

    for i in big_disp_text2:

        if i != "*" and i != "-" and i != "/" and i != "+" and i != "=" and i != "^":
            append_text = append_text + i
        elif i == "*" or i == "-" or i == "/" or i == "+" or i == "=" or i == "^":
            lst.append(float(append_text))
            append_text = ""
            if i != "=":
                lst.append(i)
    # print(lst)
    if solution != 0:
        Calculation()
        pass  #################


#
def Calculation():  # DMAS
    global lst
    global big_disp_text, lbl_dis_big, lbl_dis_small, big_disp_text2
    # print("hello")
    if "^" in lst:
        for n in range(0, len(lst)):
            if lst[n] == "^":
                solution = lst[n - 1] ** lst[n + 1]
                lst.pop(n + 1)
                lst[n] = solution
                solution = 0
                lst.pop(n - 1)
                # print(lst)
                break
            else:
                continue
    elif "/" in lst:
        # print("1")
        # if lst.index('/')<lst.index("*"):
        for i in range(0, len(lst), 1):
            if lst[i] == "/":
                # print("2")

                solution = lst[i - 1] / lst[i + 1]
                lst.pop((i + 1))
                lst[i] = solution
                # print(lst)
                solution = 0
                lst.pop(i - 1)
                # print(lst)
                break
            else:
                continue
    elif "*" in lst:
        for j in range(0, len(lst)):
            if lst[j] == "*":
                solution = lst[j - 1] * lst[j + 1]
                lst.pop(j + 1)
                lst[j] = solution
                solution = 0
                lst.pop(j - 1)
                # print(lst)
                break
            else:
                continue

    elif "+" in lst:
        for k in range(0, len(lst)):
            if lst[k] == "+":
                solution = lst[k - 1] + lst[k + 1]
                lst.pop(k + 1)
                lst[k] = solution
                solution = 0
                lst.pop(k - 1)
                # print(lst)
                break
            else:
                continue

    elif "-" in lst:
        for m in range(0, len(lst)):
            if lst[m] == "-":
                solution = lst[m - 1] - lst[m + 1]
                lst.pop(m + 1)
                lst[m] = solution
                solution = 0
                lst.pop(m - 1)
                # print(lst)
                break
            else:
                continue
    if len(lst) != 1:
        Calculation()
    if len(lst) == 1:
        print_solution()


def print_solution():
    global big_disp_text, lbl_dis_big, lbl_dis_small, big_disp_text2

    final_solution = round(lst[0], 7)
    lst.pop(0)
    dis_small_text = big_disp_text
    big_disp_text = str(final_solution)
    lbl_dis_big.configure(text=big_disp_text)
    lbl_dis_small.configure(text=dis_small_text)
    global big_disp_text2
    big_disp_text2 = str(final_solution)


def clear_all():
    global lst, big_disp_text2, big_disp_text, lbl_dis_big
    big_disp_text = ""
    dis_small_text = big_disp_text
    big_disp_text2 = ""
    lbl_dis_big.configure(text=big_disp_text)
    lbl_dis_small.configure(text=dis_small_text)
    for row in lst:
        lst.remove(row)
    lbl_dis_big.configure(font=("Helvetica 24 bold", 40, "bold"))


def back_delete():
    global lst, big_disp_text2, big_disp_text, lbl_dis_big
    big_disp_text = big_disp_text[: len(big_disp_text) - 1]
    big_disp_text2 = big_disp_text2[: len(big_disp_text2) - 1]
    lbl_dis_big.configure(text=big_disp_text)


root = CTk()
root.title("Calculator")
# root.iconbitmap(
#     r"C:\Users\Admin\Downloads\Visual Studio Code\calculate_w_icon\calculate_OO9_icon.ico"
# )
root.geometry("500x650+300+54")
ligth_grey = "#324D50"
dark_grey = "#1B2C2E"
butt_col = "#5AE1FF"
orange = "#FF7B01"
f = 27
HOV_COL_1 = "#9fff01"
HOV_COL_2 = "#fff501"
lbl_root = CTkFrame(
    root,
    # text="",
    width=350,
    height=605.7,
    fg_color=ligth_grey,
    corner_radius=23,
)
lbl_root.place(x=74.7, y=22.2)
lbl2_root = CTkFrame(
    lbl_root,
    # text="",
    width=350.1,
    height=383.8,
    fg_color=dark_grey,
    corner_radius=23,
)
lbl2_root.place(x=0, y=245)


def clear_button_all_function():
    clear_all()


def back_del_all_func():
    back_delete()
    Creating_list


buttonC = CTkButton(
    lbl2_root,
    text="C",
    text_color=orange,
    width=54.2,
    height=55.8,
    hover_color="#2bff00",
    fg_color=butt_col,
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
    command=clear_button_all_function,
)
buttonC.place(x=20.9, y=27)


buttonX = CTkButton(
    lbl2_root,
    text="X",
    hover_color="#2bff00",
    width=54.2,
    text_color=orange,
    height=55.8,
    fg_color=butt_col,
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
    command=back_del_all_func,
)
buttonX.place(x=105.6, y=27)

buttonP = CTkButton(
    lbl2_root,
    text="^",
    width=34.2,
    hover_color="#2bff00",
    text_color=orange,
    height=55.8,
    fg_color=butt_col,
    corner_radius=23,
    command=lambda: button_press("^"),
    font=("Helvetica 24 bold", f + 2, "bold"),
)
buttonP.place(
    x=190.3,
    y=27,
)

buttonD = CTkButton(
    lbl2_root,
    text="/",
    width=64.2,
    hover_color=HOV_COL_1,
    text_color=dark_grey,
    fg_color=orange,
    height=55.8,
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
    command=lambda: button_press("/"),
)
buttonD.place(x=275, y=27)
#
button7 = CTkButton(
    lbl2_root,
    text="7",
    text_color=dark_grey,
    hover_color=HOV_COL_1,
    width=54.2,
    height=55.8,
    fg_color=butt_col,
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
    command=lambda: button_press(7),
)
button7.place(x=20.9, y=91.2)


button8 = CTkButton(
    lbl2_root,
    text="8",
    width=54.2,
    height=55.8,
    hover_color=HOV_COL_1,
    text_color=dark_grey,
    fg_color=butt_col,
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
    command=lambda: button_press(8),
)
button8.place(x=105.6, y=91.2)

button9 = CTkButton(
    lbl2_root,
    text="9",
    text_color=dark_grey,
    width=54.2,
    height=55.8,
    command=lambda: button_press(9),
    hover_color=HOV_COL_1,
    fg_color=butt_col,
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
)
button9.place(x=190.3, y=91.2)

buttonM = CTkButton(
    lbl2_root,
    text="*",
    width=54.2 + 10,
    height=55.8,
    text_color=dark_grey,
    hover_color=HOV_COL_1,
    fg_color=orange,
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
    command=lambda: button_press("*"),
)
buttonM.place(x=275, y=91.2)


button4 = CTkButton(
    lbl2_root,
    text="4",
    width=54.2,
    hover_color=HOV_COL_1,
    height=55.8,
    fg_color=butt_col,
    text_color=dark_grey,
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
    command=lambda: button_press(4),
)
button4.place(x=20.9, y=156.1)

button5 = CTkButton(
    lbl2_root,
    text="5",
    width=54.2,
    height=55.8,
    text_color=dark_grey,
    hover_color=HOV_COL_1,
    fg_color=butt_col,
    command=lambda: button_press(5),
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
)
button5.place(x=105.6, y=156.1)

button6 = CTkButton(
    lbl2_root,
    text="6",
    width=54.2,
    hover_color=HOV_COL_1,
    height=55.8,
    text_color=dark_grey,
    fg_color=butt_col,
    command=lambda: button_press(6),
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
)
button6.place(x=190.3, y=156.1)


buttonS = CTkButton(
    lbl2_root,
    text="-",
    width=64.2,
    height=55.8,
    hover_color=HOV_COL_1,
    text_color=dark_grey,
    fg_color=orange,
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
    command=lambda: button_press("-"),
)
buttonS.place(x=275, y=156.1)


button1 = CTkButton(
    lbl2_root,
    text="1",
    width=54.2,
    height=55.8,
    text_color=dark_grey,
    hover_color=HOV_COL_1,
    fg_color=butt_col,
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
    command=lambda: button_press(1),
)
button1.place(x=20.9, y=220.6)



button2 = CTkButton(
    lbl2_root,
    text="2",
    width=54.2,
    height=55.8,
    text_color=dark_grey,
    fg_color=butt_col,
    hover_color=HOV_COL_1,
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
    command=lambda: button_press(2),
)
button2.place(x=105.6, y=220.6)

button3 = CTkButton(
    lbl2_root,
    text="3",
    width=54.2,
    height=55.8,
    hover_color=HOV_COL_1,
    fg_color=butt_col,
    text_color=dark_grey,
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
    command=lambda: button_press(3),
)
button3.place(x=190.3, y=220.6)

buttonA = CTkButton(
    lbl2_root,
    hover_color=HOV_COL_1,
    text="+",
    width=64.2,
    height=55.8,
    text_color=dark_grey,
    fg_color=orange,
    command=lambda: button_press("+"),
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
)
buttonA.place(x=275, y=220.6)


buttonDOT = CTkButton(
    lbl2_root,
    text=".",
    width=54.2,
    height=55.8,
    hover_color="#2bff00",
    fg_color=butt_col,
    text_color=orange,
    anchor=CENTER,
    corner_radius=23,
    font=("Helvetica 24 bold", f + 10, "bold"),
    command=lambda: button_press("."),
)
buttonDOT.place(x=20.9, y=285.1)

button0 = CTkButton(
    lbl2_root,
    text="0",
    width=54.2,
    height=55.8,
    anchor=CENTER,
    fg_color=butt_col,
    text_color=dark_grey,
    hover_color=HOV_COL_1,
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
    command=lambda: button_press(0),
)
button0.place(x=105.6, y=285.1)


def multi_fun_equal():
    button_press("=")
    Creating_list()
    Calculation()
buttonE = CTkButton(
    lbl2_root,
    text="=",
    text_color=dark_grey,
    width=149.4,
    hover_color=HOV_COL_1,
    anchor=CENTER,
    height=55.8,
    fg_color=orange,
    corner_radius=23,
    font=("Helvetica 24 bold", f, "bold"),
    command=multi_fun_equal,
)
buttonE.place(x=190.3, y=285.1)
lbl_opt = CTkLabel(
    lbl_root,
    text="",
    width=184.5 + 15,
    height=37.4,
    fg_color=butt_col,
    bg_color=ligth_grey,
    corner_radius=13,
)
lbl_opt.place(x=73.7, y=27)


lbl_dis_base = CTkLabel(
    lbl_root,
    width=332.5,
    text="",
    height=135,
    fg_color=dark_grey,
    bg_color=ligth_grey,
    corner_radius=17,
)
lbl_dis_base.place(x=9.3, y=71.8 + 17 + 1.7)

lbl_dis_big = CTkLabel(
    lbl_dis_base,
    width=315.4,
    text="",
    height=70,
    fg_color=dark_grey,
    bg_color=dark_grey,
    anchor=E,
    font=("Helvetica 24 bold", 50, "bold"),
    corner_radius=10,
)
lbl_dis_big.place(x=3, y=70 - 15)


lbl_dis_small = CTkLabel(
    lbl_dis_base,
    width=306.4,
    text="",
    height=5,
    fg_color=dark_grey,
    bg_color=dark_grey,
    anchor=E,
    font=("Helvetica 24 bold", 20, "bold"),
    corner_radius=10,
)
lbl_dis_small.place(x=15, y=9)
lbl_sci_root = CTkFrame(
    lbl_root,
    # text="",
    width=350.1,
    height=383.8,
    fg_color=dark_grey,
    corner_radius=23,
)
lbl_sci_root.place(x=-350, y=245)


def sci_animate():

    global lbl_sci_root, opt_but_2
    opt_but_1.configure(fg_color=dark_grey, text_color=orange)
    opt_but_2.configure(fg_color=orange, text_color=dark_grey)
    global sci_animate_x
    global lbl2_root
    global arith_animate_x
    if arith_animate_x <= 364:
        lbl2_root.place(x=arith_animate_x)
        root.after(5, sci_animate)
        arith_animate_x += 15

    else:
        if sci_animate_x <= -10:
            sci_animate_x += 12.5

            lbl_sci_root.place(x=sci_animate_x)
            root.after(5, sci_animate)


def arith_animate():
    global lbl_sci_root
    global sci_animate_x, opt_but_1
    # sci_animate_x=0
    opt_but_1.configure(fg_color=orange, text_color=dark_grey)
    opt_but_2.configure(fg_color=dark_grey, text_color=orange)

    global lbl2_root
    global arith_animate_x
    if sci_animate_x >= -363:
        sci_animate_x -= 15

        lbl_sci_root.place(x=sci_animate_x)
        root.after(5, arith_animate)
    else:
        if arith_animate_x >= 15:
            arith_animate_x -= 15

            lbl2_root.place(x=arith_animate_x)
            root.after(5, arith_animate)


opt_but_1 = CTkButton(
    lbl_opt,
    text="ARITHMETIC CALCULATER",
    text_color=dark_grey,
    width=88.6 + 100,
    height=28.1,
    fg_color=orange,
    bg_color=butt_col,
    hover_color=HOV_COL_1,
    corner_radius=23,
    font=("Helvetica 24 bold", 12, "bold"),
    command=arith_animate,
)
opt_but_1.place(x=5.35, y=4.2)




root.mainloop()

from tkinter import font as tkFont;import datetime; from tkinter.ttk import *;from tkinter import messagebox;import requests;import openpyxl;from openpyxl import Workbook;from tkinter import *;from tkinter import filedialog;from tkinter import messagebox;from tkinter.ttk import *;import os;import math;import tkinter as tk
def callback(): 
    link1.grid_forget(); root.filename = ''
    XlsLocation['state'] = 'active'
def info():
    if a == True:
        now = datetime.datetime.now()
        x = str(Birth.get())
        date = x.split("/")
        month = int(date[1])
        year = int(date[2])
        month = (12 - month) + (2021-year)*12
    if a == False:
        month = int(Month.get())
    if month < 0:
        messagebox.showinfo("Lỗi tháng tuổi","Tháng tuổi không có hoặc chưa hỗ trợ")
    if 0 <= month <= 60:
        Confirm.grid_forget()
        Delete.grid(row=9,column=1,pady=2,padx=2)
        global Info
        global Underline
        nameq = str(Name.get())
        name = nameq.split(' ')
        inf = 'Tên: ' + name[len(name)-1] + '  Tháng tuổi: ' + str(month) + '  Chiều cao: ' + Height.get() + ' cm' + '  Cân nặng: ' + Weight.get() + ' kg'
        Info = Label(root, text=inf, font=('Arial',11))
        Underline = Label(root, text='- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -', font=('Arial',11))
        Info.grid(row=5,column=3,pady=2,padx=2)
        Underline.grid(row=6,column=3,pady=2,padx=2)
class result():
    def weight1():
        global a
        if a == False:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[Name.get()]
                    if sheet.cell(row = i, column = 1).value == None and sheet.cell(row = i-1, column = 1).value == 'Tháng tuổi':
                        break
                    try: int(sheet.cell(row = i-1, column = 1).value)
                    except: b = False
                    else: b = True
                    if sheet.cell(row = i, column = 1).value == None and b == True:
                        break
                sheet.cell(row = i, column = 5).value = 'Trẻ suy dinh dưỡng thể nhẹ cân mức độ nặng'
                wb.save(root.filename)
                wb.close()
            except: pass
        if a == True:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[ClassName.get()]
                    if sheet.cell(row = i, column = 9).value == None and sheet.cell(row = i-1, column = 1).value == i - 2:
                        break
                    if sheet.cell(row = i, column = 12).value == None and sheet.cell(row = i-1, column = 1).value == 'TT':
                        break
                if sheet.cell(row = i-1, column = 2).value != Name.get():
                    sheet.cell(row = i, column = 9).value = 'X'
                    #sheet.cell(row = i, column = 8).value = ' '
                    #sheet.cell(row = i, column = 7).value = ' '
                    #sheet.cell(row = i, column = 6).value = ' '
                wb.save(root.filename)
                wb.close()
            except: pass
        global WLabel
        WLabel = Label(root, text="[Câng nặng]: Trẻ suy dinh dưỡng thể nhẹ cân mức độ nặng", font=('Arial',11))
        WLabel.grid(row=7,column=3,pady=2,padx=2)
    def weight2():
        global a
        if a == False:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[Name.get()]
                    if sheet.cell(row = i, column = 1).value == None and sheet.cell(row = i-1, column = 1).value == 'Tháng tuổi':
                        break
                    try: int(sheet.cell(row = i-1, column = 1).value)
                    except: b = False
                    else: b = True
                    if sheet.cell(row = i, column = 1).value == None and b == True:
                        break
                sheet.cell(row = i, column = 5).value = 'Trẻ suy dinh dưỡng thể nhẹ cân'
                wb.save(root.filename)
                wb.close()
            except: pass
        if a == True:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[ClassName.get()]
                    if sheet.cell(row = i, column = 8).value == None and sheet.cell(row = i-1, column = 1).value == i - 2:
                        break
                    if sheet.cell(row = i, column = 12).value == None and sheet.cell(row = i-1, column = 1).value == 'TT':
                        break
                if sheet.cell(row = i-1, column = 2).value != Name.get():
                    sheet.cell(row = i, column = 8).value = 'X'
                    #sheet.cell(row = i, column = 6).value = ' '
                    #sheet.cell(row = i, column = 7).value = ' '
                    #sheet.cell(row = i, column = 9).value = ' '
                wb.save(root.filename)
                wb.close()
            except:
                pass
        global WLabel
        WLabel = Label(root, text="[Câng nặng]: Trẻ suy dinh dưỡng thể nhẹ cân", font=('Arial',11))
        WLabel.grid(row=7,column=3,pady=2,padx=2)
    def weight3():
        if a == False:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[Name.get()]
                    if sheet.cell(row = i, column = 1).value == None and sheet.cell(row = i-1, column = 1).value == 'Tháng tuổi':
                        break
                    try: int(sheet.cell(row = i-1, column = 1).value)
                    except: b = False
                    else: b = True
                    if sheet.cell(row = i, column = 1).value == None and b == True:
                        break
                sheet.cell(row = i, column = 5).value = 'Trẻ bình thường'
                wb.save(root.filename)
                wb.close()
            except: pass
        if a == True:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[ClassName.get()]
                    if sheet.cell(row = i, column = 7).value == None and sheet.cell(row = i-1, column = 1).value == i - 2:
                        break
                    if sheet.cell(row = i, column = 12).value == None and sheet.cell(row = i-1, column = 1).value == 'TT':
                        break
                if sheet.cell(row = i-1, column = 2).value != Name.get():
                    sheet.cell(row = i, column = 7).value = 'X'
                    #sheet.cell(row = i, column = 6).value = ' '
                    #sheet.cell(row = i, column = 8).value = ' '
                    #sheet.cell(row = i, column = 9).value = ' '
                wb.save(root.filename)
                wb.close()
            except: pass
        global WLabel
        WLabel = Label(root, text="[Câng nặng]: Trẻ bình thường", font=('Arial',11))
        WLabel.grid(row=7,column=3,pady=2,padx=2)
    def weight4():
        global a
        if a == False:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[Name.get()]
                    if sheet.cell(row = i, column = 1).value == None and sheet.cell(row = i-1, column = 1).value == 'Tháng tuổi':
                        break
                    try: int(sheet.cell(row = i-1, column = 1).value)
                    except: b = False
                    else: b = True
                    if sheet.cell(row = i, column = 1).value == None and b == True:
                        break
                sheet.cell(row = i, column = 5).value = 'Trẻ thừa cân'
                wb.save(root.filename)
                wb.close()
            except: pass
        if a == True:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[ClassName.get()]
                    if sheet.cell(row = i, column = 6).value == None and sheet.cell(row = i-1, column = 1).value == i - 2:
                        break
                    if sheet.cell(row = i, column = 12).value == None and sheet.cell(row = i-1, column = 1).value == 'TT':
                        break
                if sheet.cell(row = i-1, column = 2).value != Name.get():
                    sheet.cell(row = i, column = 6).value = 'X'
                    #sheet.cell(row = i, column = 7).value = ' '
                    #sheet.cell(row = i, column = 8).value = ' '
                    #sheet.cell(row = i, column = 9).value = ' '
                wb.save(root.filename)
                wb.close()
            except: pass
        global WLabel
        WLabel = Label(root, text="[Câng nặng]: Trẻ thừa cân", font=('Arial',11))
        WLabel.grid(row=7,column=3,pady=2,padx=2)
    def weight5():
        if a == False:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[Name.get()]
                    if sheet.cell(row = i, column = 1).value == None and sheet.cell(row = i-1, column = 1).value == 'Tháng tuổi':
                        break
                    try: int(sheet.cell(row = i-1, column = 1).value)
                    except: b = False
                    else: b = True
                    if sheet.cell(row = i, column = 1).value == None and b == True:
                        break
                sheet.cell(row = i, column = 5).value = 'Trẻ béo phì'
                wb.save(root.filename)
                wb.close()
            except: pass
        if a == True:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[ClassName.get()]
                    if sheet.cell(row = i, column = 6).value == None and sheet.cell(row = i-1, column = 1).value == i - 2:
                        break
                    if sheet.cell(row = i, column = 12).value == None and sheet.cell(row = i-1, column = 1).value == 'TT':
                        break
                if sheet.cell(row = i-1, column = 2).value != Name.get():
                    sheet.cell(row = i, column = 6).value = 'X'
                    #sheet.cell(row = i, column = 7).value = ' '
                    #sheet.cell(row = i, column = 8).value = ' '
                    #sheet.cell(row = i, column = 9).value = ' '
                wb.save(root.filename)
                wb.close()
            except: pass
        global WLabel
        WLabel = Label(root, text="[Câng nặng]: Trẻ béo phì", font=('Arial',11))
        WLabel.grid(row=7,column=3,pady=2,padx=2)
    def height1():
        if a == False:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[Name.get()]
                    if sheet.cell(row = i, column = 1).value == None and sheet.cell(row = i-1, column = 1).value == 'Tháng tuổi':
                        break
                    try: int(sheet.cell(row = i-1, column = 1).value)
                    except: b = False
                    else: b = True
                    if sheet.cell(row = i, column = 1).value == None and b == True:
                        break
                sheet.cell(row = i, column = 4).value = 'Trẻ suy dinh dưỡng thể thấp còi mức độ nặng'
                wb.save(root.filename)
                wb.close()
            except: pass
        if a == True:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[ClassName.get()]
                    if sheet.cell(row = i, column = 14).value == None and sheet.cell(row = i-1, column = 1).value == i - 2:
                        break
                    if sheet.cell(row = i, column = 12).value == None and sheet.cell(row = i-1, column = 1).value == 'TT':
                        break
                if sheet.cell(row = i-1, column = 2).value != Name.get():
                    sheet.cell(row = i, column = 14).value = 'X'
                    #sheet.cell(row = i, column = 13).value = ' '
                    #sheet.cell(row = i, column = 12).value = ' '
                    #sheet.cell(row = i, column = 11).value = ' '
                wb.save(root.filename)
                wb.close()
            except: pass
        global HLabel
        HLabel = Label(root, text="[Chiều cao]: Trẻ suy dinh dưỡng thể thấp còi mức độ nặng", font=('Arial',11))
        HLabel.grid(row=8,column=3,pady=2,padx=2)
    def height2():
        global HLabel
        HLabel = Label(root, text="[Chiều cao]: Trẻ suy dinh dưỡng thể thấp còi", font=('Arial',11))
        HLabel.grid(row=8,column=3,pady=2,padx=2)
        if a == False:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[Name.get()]
                    if sheet.cell(row = i, column = 1).value == None and sheet.cell(row = i-1, column = 1).value == 'Tháng tuổi':
                        break
                    try: int(sheet.cell(row = i-1, column = 1).value)
                    except: b = False
                    else: b = True
                    if sheet.cell(row = i, column = 1).value == None and b == True:
                        break
                sheet.cell(row = i, column = 4).value = 'Trẻ suy dinh dưỡng thể thấp còi'
                wb.save(root.filename)
                wb.close()
            except: pass
        if a == True:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[ClassName.get()]
                    if sheet.cell(row = i, column = 13).value == None and sheet.cell(row = i-1, column = 1).value == i - 2:
                        break
                    if sheet.cell(row = i, column = 12).value == None and sheet.cell(row = i-1, column = 1).value == 'TT':
                        break
                if sheet.cell(row = i-1, column = 2).value != Name.get():
                    sheet.cell(row = i, column = 13).value = 'X'
                    #sheet.cell(row = i, column = 14).value = ' '
                    #sheet.cell(row = i, column = 12).value = ' '
                    #sheet.cell(row = i, column = 11).value = ' '
                wb.save(root.filename)
                wb.close()
            except: pass
    def height3():
        if a == False:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[Name.get()]
                    if sheet.cell(row = i, column = 1).value == None and sheet.cell(row = i-1, column = 1).value == 'Tháng tuổi':
                        break
                    try: int(sheet.cell(row = i-1, column = 1).value)
                    except: b = False
                    else: b = True
                    if sheet.cell(row = i, column = 1).value == None and b == True:
                        break
                sheet.cell(row = i, column = 4).value = 'Trẻ bình thường'
                wb.save(root.filename)
                wb.close()
            except: pass
        if a == True:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[ClassName.get()]
                    if sheet.cell(row = i, column = 12).value == None and sheet.cell(row = i-1, column = 1).value == i - 2:
                        break
                    if sheet.cell(row = i, column = 12).value == None and sheet.cell(row = i-1, column = 1).value == 'TT':
                        break
                if sheet.cell(row = i-1, column = 2).value != Name.get():
                    sheet.cell(row = i, column = 12).value = 'X'
                    #sheet.cell(row = i, column = 11).value = ' '
                    #sheet.cell(row = i, column = 14).value = ' '
                    #sheet.cell(row = i, column = 13).value = ' '
                wb.save(root.filename)
                wb.close()
            except: pass
        global HLabel
        HLabel = Label(root, text="[Chiều cao]: Trẻ bình thường", font=('Arial',11))
        HLabel.grid(row=8,column=3,pady=2,padx=2)
    def height4():
        if a == False:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[Name.get()]
                    if sheet.cell(row = i, column = 1).value == None and sheet.cell(row = i-1, column = 1).value == 'Tháng tuổi':
                        break
                    try: int(sheet.cell(row = i-1, column = 1).value)
                    except: b = False
                    else: b = True
                    if sheet.cell(row = i, column = 1).value == None and b == True:
                        break
                sheet.cell(row = i, column = 4).value = 'Trẻ cao hơn so với tuổi'
                wb.save(root.filename)
                wb.close()
            except: pass
        if a == True:
            try:
                wb = openpyxl.load_workbook(root.filename)
                for i in range(1, 1048576): 
                    sheet = wb[ClassName.get()]
                    if sheet.cell(row = i, column = 11).value == None and sheet.cell(row = i-1, column = 1).value == i - 2:
                        break
                    if sheet.cell(row = i, column = 12).value == None and sheet.cell(row = i-1, column = 1).value == 'TT':
                        break
                    if sheet.cell(row = i-1, column = 2).value != Name.get():
                        sheet.cell(row = i, column = 11).value = 'X'
                        #sheet.cell(row = i, column = 13).value = ' '
                        #sheet.cell(row = i, column = 12).value = ' '
                        #sheet.cell(row = i, column = 14).value = ' '
                    wb.save(root.filename)
                    wb.close()
            except: pass
        global HLabel
        HLabel = Label(root, text="[Chiều cao]: Trẻ cao hơn so với tuổi", font=('Arial',11))
        HLabel.grid(row=8,column=3,pady=2,padx=2)
def main():
    info()
    global a
    if a == False:
        month = int(Month.get())
        weight = float(Weight.get().replace(',','.'))
        height = float(Height.get().replace(',','.'))
    if a == True:
        now = datetime.datetime.now()
        x = str(Birth.get())
        date = x.split("/")
        month = int(date[1])
        year = int(date[2])
        month = (12 - month) + (2021-year)*12
        weight = float(Weight.get().replace(',','.'))
        height = float(Height.get().replace(',','.'))
    if a == False:
        try:
            if root.filename != None:
                wb = openpyxl.load_workbook(root.filename)
                if Name.get() in wb.sheetnames:
                    sheetsetup = wb[Name.get()]
                    for i in range(1, 1048576): 
                        if sheetsetup.cell(row = i, column = 1).value == None and sheetsetup.cell(row = i-1, column = 1).value == i - 2:
                            break
                    sheetsetup.cell(row = i, column = 1).value = month
                    sheetsetup.cell(row = i, column = 2).value = height
                    sheetsetup.cell(row = i, column = 3).value = weight
                    if sheetsetup['A1'].value == None:
                        if Name.get() == '':
                            sheetsetup['A1'].value = 'Họ và Tên cháu: (Chưa cập nhật)'
                        else:
                            sheetsetup['A1'].value = 'Họ và Tên cháu: '+ Name.get()
                        if Birth.get() == '':
                            sheetsetup['A2'].value = 'Ngày sinh: (Chưa cập nhật)'
                        else:
                            sheetsetup['A2'].value = 'Ngày sinh: '+Birth.get()
                        if Ad.get() == '':
                            sheetsetup['A3'].value = 'Địa chỉ: (Chưa cập nhật)'
                        else:
                            sheetsetup['A3'].value = 'Địa chỉ: '+Ad.get()
                        if PName.get() == '':
                            sheetsetup['A4'].value = 'Họ và Tên người bảo hộ: (Chưa cập nhật)'
                        else:
                            sheetsetup['A4'].value = 'Họ và Tên người bảo hộ: '+PName.get()
                        sheetsetup['A5'].value = 'Giới tính: '+ variable.get()
                        sheetsetup.merge_cells('A1:C1')
                        sheetsetup.merge_cells('A2:C2')
                        sheetsetup.merge_cells('A3:C3')
                        sheetsetup.merge_cells('A4:C4')
                        sheetsetup.merge_cells('A5:C5')
                        sheetsetup['A6'].value = ' '
                        sheetsetup['B6'].value = ' '
                        sheetsetup['C6'].value = ' '
                        sheetsetup['D1'].value = ' '
                        sheetsetup['D2'].value = ' '
                        sheetsetup['D3'].value = ' '
                        sheetsetup['D4'].value = ' '
                        sheetsetup['D5'].value = ' '
                        sheetsetup['D6'].value = ' '
                        sheetsetup['E6'].value = ' '
                        sheetsetup['E5'].value = ' '
                        sheetsetup['E4'].value = ' '
                        sheetsetup['E3'].value = ' '
                        sheetsetup['E2'].value = ' '
                        sheetsetup['E1'].value = ' '
                        sheetsetup['A7'].value = 'Tháng tuổi'
                        sheetsetup['B7'].value = 'Chiều cao'
                        sheetsetup['C7'].value = 'Cân nặng'
                        sheetsetup['D7'].value = 'Kết quả chiều cao theo tuổi'
                        sheetsetup['E7'].value = 'Kết quả cân nặng theo tuổi'
                        sheetsetup['A8'].value = month
                        sheetsetup['B8'].value = height
                        sheetsetup['C8'].value = weight
                    wb.save(root.filename)
                    wb.close()
                else:
                    wb.create_sheet(title = Name.get())
                    sheetsetup = wb[Name.get()]
                    if sheetsetup['A1'].value == None:
                        if Name.get() == '':
                            sheetsetup['A1'].value = 'Họ và Tên cháu: (Chưa cập nhật)'
                        else:
                            sheetsetup['A1'].value = 'Họ và Tên cháu: '+ Name.get()
                        if Birth.get() == '':
                            sheetsetup['A2'].value = 'Ngày sinh: (Chưa cập nhật)'
                        else:
                            sheetsetup['A2'].value = 'Ngày sinh: '+Birth.get()
                        if Ad.get() == '':
                            sheetsetup['A3'].value = 'Địa chỉ: (Chưa cập nhật)'
                        else:
                            sheetsetup['A3'].value = 'Địa chỉ: '+Ad.get()
                        if PName.get() == '':
                            sheetsetup['A4'].value = 'Họ và Tên người bảo hộ: (Chưa cập nhật)'
                        else:
                            sheetsetup['A4'].value = 'Họ và Tên người bảo hộ: '+PName.get()
                        sheetsetup['A5'].value = 'Giới tính: '+ variable.get()
                        sheetsetup.merge_cells('A1:C1')
                        sheetsetup.merge_cells('A2:C2')
                        sheetsetup.merge_cells('A3:C3')
                        sheetsetup.merge_cells('A4:C4')
                        sheetsetup.merge_cells('A5:C5')
                        sheetsetup['A6'].value = ' '
                        sheetsetup['B6'].value = ' '
                        sheetsetup['C6'].value = ' '
                        sheetsetup['D1'].value = ' '
                        sheetsetup['D2'].value = ' '
                        sheetsetup['D3'].value = ' '
                        sheetsetup['D4'].value = ' '
                        sheetsetup['D5'].value = ' '
                        sheetsetup['D6'].value = ' '
                        sheetsetup['E6'].value = ' '
                        sheetsetup['E5'].value = ' '
                        sheetsetup['E4'].value = ' '
                        sheetsetup['E3'].value = ' '
                        sheetsetup['E2'].value = ' '
                        sheetsetup['E1'].value = ' '
                        sheetsetup['A7'].value = 'Tháng tuổi'
                        sheetsetup['B7'].value = 'Chiều cao'
                        sheetsetup['C7'].value = 'Cân nặng'
                        sheetsetup['D7'].value = 'Kết quả chiều cao theo tuổi'
                        sheetsetup['E7'].value = 'Kết quả cân nặng theo tuổi'
                        sheetsetup['A8'].value = month
                        sheetsetup['B8'].value = height
                        sheetsetup['C8'].value = weight
                        wb.save(root.filename)
                        wb.close()
        except: pass
    if a == True:
        try:
            if root.filename != None:
                wb = openpyxl.load_workbook(root.filename)
                if ClassName.get() in wb.sheetnames:
                    sheetsetup = wb[ClassName.get()]
                    for i in range(1, 1048576): 
                        if sheetsetup.cell(row = i, column = 1).value == None and sheetsetup.cell(row = i-1, column = 1).value == i - 2:
                            break
                    if sheetsetup.cell(row = i-1, column = 2).value != Name.get():
                        sheetsetup.cell(row = i, column = 3).value = Birth.get()
                        sheetsetup.cell(row = i, column = 10).value = height
                        sheetsetup.cell(row = i, column = 10).value = height
                        sheetsetup.cell(row = i, column = 5).value = weight
                        sheetsetup.cell(row = i, column = 2).value = Name.get()
                        sheetsetup.cell(row = i, column = 1).value = i - 1
                        sheetsetup.cell(row = i, column = 4).value = variable.get()
                    if sheetsetup['A1'].value != 'TT' or sheetsetup['B1'].value != 'Họ và Tên' or sheetsetup['C1'].value != 'Ngày sinh' or sheetsetup['D1'].value != 'Giới tính' or sheetsetup['E1'].value != 'Cân nặng' or sheetsetup['F1'].value != 'Thừa cân, béo phì' or sheetsetup['G1'].value != 'Bình thường' or sheetsetup['H1'].value != 'SDD vừa' or sheetsetup['I1'].value != 'SDD nặng' or sheetsetup['J1'].value != 'Chiều cao' or sheetsetup['K1'].value != 'Cao hơn so với tuổi' or sheetsetup['L1'].value != 'Bình thường' or sheetsetup['M1'].value != 'Thấp còi độ 1' or sheetsetup['N1'].value != 'Thấp còi độ 2':
                        sheetsetup['A1'].value = 'TT'
                        sheetsetup['B1'].value = 'Họ và Tên'
                        sheetsetup['C1'].value = 'Ngày sinh'
                        sheetsetup['D1'].value = 'Giới tính'
                        sheetsetup['E1'].value = 'Cân nặng'
                        sheetsetup['F1'].value = 'Thừa cân, béo phì'
                        sheetsetup['G1'].value = 'Bình thường'
                        sheetsetup['H1'].value = 'SDD vừa'
                        sheetsetup['I1'].value = 'SDD nặng'
                        sheetsetup['J1'].value = 'Chiều cao'
                        sheetsetup['K1'].value = 'Cao hơn so với tuổi'
                        sheetsetup['L1'].value = 'Bình thường'
                        sheetsetup['M1'].value = 'Thấp còi độ 1'
                        sheetsetup['N1'].value = 'Thấp còi độ 2'
                    wb.save(root.filename)
                    wb.close()
                    
                else:
                    wb.create_sheet(title = ClassName.get())
                    sheetsetup = wb[ClassName.get()]
                    if sheetsetup['A1'].value != 'TT' or sheetsetup['B1'].value != 'Họ và Tên' or sheetsetup['C1'].value != 'Ngày sinh' or sheetsetup['D1'].value != 'Giới tính' or sheetsetup['E1'].value != 'Cân nặng' or sheetsetup['F1'].value != 'Thừa cân, béo phì' or sheetsetup['G1'].value != 'Bình thường' or sheetsetup['H1'].value != 'SDD vừa' or sheetsetup['I1'].value != 'SDD nặng' or sheetsetup['J1'].value != 'Chiều cao' or sheetsetup['K1'].value != 'Cao hơn so với tuổi' or sheetsetup['L1'].value != 'Bình thường' or sheetsetup['M1'].value != 'Thấp còi độ 1' or sheetsetup['N1'].value != 'Thấp còi độ 2':
                        sheetsetup['A1'].value = 'TT'
                        sheetsetup['B1'].value = 'Họ và Tên'
                        sheetsetup['C1'].value = 'Ngày sinh'
                        sheetsetup['D1'].value = 'Giới tính'
                        sheetsetup['E1'].value = 'Cân nặng'
                        sheetsetup['F1'].value = 'Thừa cân, béo phì'
                        sheetsetup['G1'].value = 'Bình thường'
                        sheetsetup['H1'].value = 'SDD vừa'
                        sheetsetup['I1'].value = 'SDD nặng'
                        sheetsetup['J1'].value = 'Chiều cao'
                        sheetsetup['K1'].value = 'Cao hơn so với tuổi'
                        sheetsetup['L1'].value = 'Bình thường'
                        sheetsetup['M1'].value = 'Thấp còi độ 1'
                        sheetsetup['N1'].value = 'Thấp còi độ 2'
                        for i in range(1, 1048576): 
                            if sheetsetup.cell(row = i, column = 1).value == None:
                                break
                        if sheetsetup.cell(row = i-1, column = 2).value != Name.get():
                            sheetsetup.cell(row = i, column = 3).value = Birth.get()
                            sheetsetup.cell(row = i, column = 10).value = height
                            sheetsetup.cell(row = i, column = 5).value = weight
                            sheetsetup.cell(row = i, column = 2).value = Name.get()
                            sheetsetup.cell(row = i, column = 1).value = i - 1
                            sheetsetup.cell(row = i, column = 4).value = variable.get()
                            wb.save(root.filename)
                            wb.close()
        except: pass
    #-------------------- ANALYZE --------------------#
    if variable.get() in ['Nữ']:
        if month == 0:
            if weight <= 2:result.weight1()
            if 2 < weight <= 2.4:result.weight2()
            if 2.4 < weight <= 4.4:result.weight3()
            if 4.4 < weight <= 4.9:result.weight4()
            if weight >= 4.9:result.weight5()
            if height <= 43:result.height1()
            if 43 < height <= 46:result.height2()
            if 46 < height <= 53:result.height3()
            if height > 53:result.height4()
        if month == 1:
            if weight <= 2.8:result.weight1()
            if 2.8 < weight <= 3.4:result.weight2()
            if 3.4 < weight <= 5.7:result.weight3()
            if 5.7 < weight <= 6.5:result.weight4()
            if weight > 6.5:result.weight5()
            if height <= 48:result.height1()
            if 48 < height <= 50:result.height2()
            if 50 < height <= 58:result.height3()
            if height > 58:result.height4()
        if month == 2:
            if weight <= 3.5:result.weight1()
            if 3.5 < weight <= 4:result.weight2()
            if 4 < weight <= 6.8:result.weight3()
            if 6 < weight <= 7.7:result.weight4()
            if weight > 7.7:result.weight5()
            if height <= 51:result.height1()
            if 51 < height <= 53:result.height2()
            if 53 < height <= 62:result.height3()
            if height > 62:result.height4()
        if month == 3:
            if weight <= 4:result.weight1()
            if 4 < weight <= 4.6:result.weight2()
            if 4.6 < weight <= 7.7:result.weight3()
            if 7.7 < weight <= 8.6:result.weight4()
            if weight > 8.6:result.weight5()
            if height <= 54:result.height1()
            if 54 < height <= 56:result.height2()
            if 56 < height <= 64:result.height3()
            if height > 64:result.height4()
        if month == 4:
            if weight <= 4.5:result.weight1()
            if 4.5 < weight <= 5.1:result.weight2()
            if 5.1 < weight <= 8.3:result.weight3()
            if 8.3 < weight <= 9.4:result.weight4()
            if weight > 9.4:result.weight5()
            if height <= 55:result.height1()
            if 55 < height <= 58:result.height2()
            if 58 < height <= 67:result.height3()
            if height > 67:result.height4()
        if month == 5:
            if weight <= 4.8:result.weight1()
            if 4.8 < weight <= 5.5:result.weight2()
            if 5.5 < weight <= 9:result.weight3()
            if 9 < weight <= 10:result.weight4()
            if weight > 10:result.weight5()
            if height <= 57.5:result.height1()
            if 57.5 < height <= 60:result.height2()
            if 60 < height <= 68.5:result.height3()
            if height > 68.5:result.height4()
        if month == 6:
            if weight <= 5.1:result.weight1()
            if 5.1 < weight <= 5.7:result.weight2()
            if 5.7 < weight <= 9.4:result.weight3()
            if 9.4 < weight <= 10.6:result.weight4()
            if weight > 10.6:result.weight5()
            if height <= 59:result.height1()
            if 59 < height <= 61.5:result.height2()
            if 61.5 < height <= 70.5:result.height3()
            if height > 70.5:result.height4()
        if month == 7:
            if weight <= 5.3:result.weight1()
            if 5.3 < weight <= 6:result.weight2()
            if 6 < weight <= 9.9:result.weight3()
            if 9.9 < weight <= 11.1:result.weight4()
            if weight > 11.1:result.weight5()
            if height <= 60.5:result.height1()
            if 60.5 < height <= 63:result.height2()
            if 63 < height <= 72:result.height3()
            if height > 72:result.height4()
        if month == 8:
            if weight <= 5.6:result.weight1()
            if 5.6 < weight <= 6.3:result.weight2()
            if 6.3 < weight <= 10.3:result.weight3()
            if 10.3 < weight <= 11.6:result.weight4()
            if weight > 11.6:result.weight5()
            if height <= 61.5:result.height1()
            if 61.5 < height <= 64:result.height2()
            if 64 < height <= 73.5:result.height3()
            if height > 73.5:result.height4()
        if month == 9:
            if weight <= 5.8:result.weight1()
            if 5.8 < weight <= 6.5:result.weight2()
            if 6.5 < weight <= 10.6:result.weight3()
            if 10.6 < weight <= 12:result.weight4()
            if weight > 12:result.weight5()
            if height <= 63:result.height1()
            if 63 < height <= 65.5:result.height2()
            if 65.5 < height <= 75:result.height3()
            if height > 75:result.height4()
        if month == 10:
            if weight <= 6:result.weight1()
            if 6 < weight <= 6.7:result.weight2()
            if 6.7 < weight <= 11:result.weight3()
            if 11 < weight <= 12.4:result.weight4()
            if weight > 12.4:result.weight5()
            if height <= 64:result.height1()
            if 64 < height <= 67:result.height2()
            if 67 < height <= 76.5:result.height3()
            if height > 76.5:result.height4()
        if month == 11:
            if weight <= 6.1:result.weight1()
            if 6.1 < weight <= 6.9:result.weight2()
            if 6.9 < weight <= 11.3:result.weight3()
            if 11.3 < weight <= 12.7:result.weight4()
            if weight > 12.7:result.weight5()
            if height <= 65:result.height1()
            if 65 < height <= 68:result.height2()
            if 68 < height <= 78:result.height3()
            if height > 78:result.height4()
        if month == 12:
            if weight <= 6.2:result.weight1()
            if 6.2 < weight <= 7.1:result.weight2()
            if 7.1 < weight <= 11.5:result.weight3()
            if 11.5 < weight <= 13:result.weight4()
            if weight > 13:result.weight5()
            if height <= 66:result.height1()
            if 66 < height <= 68:result.height2()
            if 68 < height <= 79:result.height3()
            if height > 79:result.height4()
        if month == 13:
            if weight <= 6.5:result.weight1()
            if 6 < weight <= 7.2:result.weight2()
            if 7.2 < weight <= 11.8:result.weight3()
            if 11.8 < weight <= 13.5:result.weight4()
            if weight > 13.5:result.weight5()
            if height <= 67:result.height1()
            if 67 < height <= 70:result.height2()
            if 70 < height <= 81:result.height3()
            if height > 81:result.height4()
        if month == 14:
            if weight <= 6.7:result.weight1()
            if 6.7 < weight <= 7.5:result.weight2()
            if 7.5 < weight <= 12.1:result.weight3()
            if 12.1 < weight <= 13.8:result.weight4()
            if weight > 13.8:result.weight5()
            if height <= 68:result.height1()
            if 68 < height <= 71:result.height2()
            if 71 < height <= 82:result.height3()
            if height > 82:result.height4()
        if month == 15:
            if weight <= 6.9:result.weight1()
            if 6.9 < weight <= 7.7:result.weight2()
            if 7.7 < weight <= 12.5:result.weight3()
            if 12.5 < weight <= 14.1:result.weight4()
            if weight > 14.1:result.weight5()
            if height <= 69:result.height1()
            if 69 < height <= 72:result.height2()
            if 72 < height <= 83:result.height3()
            if height > 83:result.height4()
        if month == 16:
            if weight <= 7:result.weight1()
            if 7 < weight <= 7.8:result.weight2()
            if 7.8 < weight <= 12.7:result.weight3()
            if 12.7 < weight <= 14.5:result.weight4()
            if weight > 14.5:result.weight5()
            if height <= 70:result.height1()
            if 70 < height <= 73:result.height2()
            if 73 < height <= 84:result.height3()
            if height > 84:result.height4()
        if month == 17:
            if weight <= 7:result.weight1()
            if 7 < weight <= 8:result.weight2()
            if 8 < weight <= 13:result.weight3()
            if 13 < weight <= 14.8:result.weight4()
            if weight > 14.8:result.weight5()
            if height <= 71:result.height1()
            if 71 < height <= 73:result.height2()
            if 73 < height <= 86:result.height3()
            if height > 86:result.height4()
        if month == 18:
            if weight <= 7.2:result.weight1()
            if 7.2 < weight <= 8.1:result.weight2()
            if 8.1 < weight <= 13.3:result.weight3()
            if 13.3 < weight <= 15:result.weight4()
            if weight > 15:result.weight5()
            if height <= 72:result.height1()
            if 72 < height <= 75:result.height2()
            if 75 < height <= 87:result.height3()
            if height > 87:result.height4()
        if month == 19:
            if weight <= 7.4:result.weight1()
            if 7.4 < weight <= 8.3:result.weight2()
            if 8.3 < weight <= 13.5:result.weight3()
            if 13.5 < weight <= 15.5:result.weight4()
            if weight > 15.5:result.weight5()
            if height <= 73:result.height1()
            if 73 < height <= 76:result.height2()
            if 76 < height <= 88:result.height3()
            if height > 88:result.height4()
        if month == 19:
            if weight <= 7.5:result.weight1()
            if 7.5 < weight <= 8.4:result.weight2()
            if 8.4 < weight <= 13.8:result.weight3()
            if 13.8 < weight <= 15.8:result.weight4()
            if weight > 15.8:result.weight5()
            if height <= 74:result.height1()
            if 74 < height <= 77:result.height2()
            if 77 < height <= 89:result.height3()
            if height > 89:result.height4()
        if month == 21:
            if weight <= 7.7:result.weight1()
            if 7.7 < weight <= 8.6:result.weight2()
            if 8.6 < weight <= 14:result.weight3()
            if 14 < weight <= 16:result.weight4()
            if weight > 16:result.weight5()
            if height <= 74.5:result.height1()
            if 75.5 < height <= 78:result.height2()
            if 78 < height <= 90:result.height3()
            if height > 90:result.height4()
        if month == 22:
            if weight <= 7.9:result.weight1()
            if 7.9 < weight <= 8.8:result.weight2()
            if 8.8 < weight <= 14.4:result.weight3()
            if 14.4 < weight <= 16.5:result.weight4()
            if weight > 16.5:result.weight5()
            if height <= 75.5:result.height1()
            if 75.5 < height <= 78.5:result.height2()
            if 78.5 < height <= 91:result.height3()
            if height > 91:result.height4()
        if month == 23:
            if weight <= 8:result.weight1()
            if 8 < weight <= 9:result.weight2()
            if 9 < weight <= 14.6:result.weight3()
            if 14.6 < weight <= 16.7:result.weight4()
            if weight > 16.7:result.weight5()
            if height <= 76:result.height1()
            if 76 < height <= 79:result.height2()
            if 79 < height <= 92:result.height3()
            if height > 92:result.height4()
        if month == 60:
            if weight <= 8:result.weight1()
            if 8 < weight <= 9:result.weight2()
            if 9 < weight <= 15:result.weight3()
            if 15 < weight <= 17:result.weight4()
            if weight > 17:result.weight5()
            if height <= 75.5:result.height1()
            if 75.5 < height <= 80:result.height2()
            if 80 < height <= 93:result.height3()
            if height > 93:result.height4()
        if month == 25:
            if weight <= 8.2:result.weight1()
            if 8.2 < weight <= 9.2:result.weight2()
            if 9.2 < weight <= 15.1:result.weight3()
            if 15.1 < weight <= 17.3:result.weight4()
            if weight > 17.3:result.weight5()
            if height <= 76.8:result.height1()
            if 76.8 < height <= 80:result.height2()
            if 80 < height <= 93.1:result.height3()
            if height > 93.1:result.height4()
        if month == 26:
            if weight <= 8.4:result.weight1()
            if 8.4 < weight <= 9.4:result.weight2()
            if 9.4 < weight <= 15.4:result.weight3()
            if 15.4 < weight <= 17.7:result.weight4()
            if weight > 17.7:result.weight5()
            if height <= 77.5:result.height1()
            if 77.5 < height <= 80.8:result.height2()
            if 80.8 < height <= 94.1:result.height3()
            if height > 94.1:result.height4()
        if month == 27:
            if weight <= 8.5:result.weight1()
            if 8.5 < weight <= 9.5:result.weight2()
            if 9.5 < weight <= 15.7:result.weight3()
            if 15.7 < weight <= 18:result.weight4()
            if weight > 18:result.weight5()
            if height <= 78.1:result.height1()
            if 78.1 < height <= 81.5:result.height2()
            if 81.5 < height <= 95:result.height3()
            if height > 95:result.height4()
        if month == 28:
            if weight <= 8.6:result.weight1()
            if 8.6 < weight <= 9.7:result.weight2()
            if 9.7 < weight <= 16:result.weight3()
            if 16 < weight <= 18.3:result.weight4()
            if weight > 18.3:result.weight5()
            if height <= 78.8:result.height1()
            if 78.8 < height <= 82.2:result.height2()
            if 82.2 < height <= 96:result.height3()
            if height > 96:result.height4()
        if month == 29:
            if weight <= 8.8:result.weight1()
            if 8.8 < weight <= 9.8:result.weight2()
            if 9.8 < weight <= 16.2:result.weight3()
            if 16.2 < weight <= 18.7:result.weight4()
            if weight > 18.7:result.weight5()
            if height <= 79.5:result.height1()
            if 79.5 < height <= 82.9:result.height2()
            if 82.9 < height <= 96.9:result.height3()
            if height > 96.9:result.height4()
        if month == 30:
            if weight <= 8.9:result.weight1()
            if 8.9 < weight <= 10:result.weight2()
            if 10 < weight <= 16.5:result.weight3()
            if 16.5 < weight <= 19:result.weight4()
            if weight > 19:result.weight5()
            if height <= 80.1:result.height1()
            if 80.1 < height <= 83.6:result.height2()
            if 83.6 < height <= 97.7:result.height3()
            if height > 97.7:result.height4()
        if month == 31:
            if weight <= 9:result.weight1()
            if 9 < weight <= 10.1:result.weight2()
            if 10.1 < weight <= 16.8:result.weight3()
            if 16.8 < weight <= 19.3:result.weight4()
            if weight > 19.3:result.weight5()
            if height <= 80.7:result.height1()
            if 80.7 < height <= 84.3:result.height2()
            if 84.3 < height <= 98.6:result.height3()
            if height > 98.6:result.height4()
        if month == 32:
            if weight <= 9.1:result.weight1()
            if 9.1 < weight <= 10.3:result.weight2()
            if 10.3 < weight <= 17.1:result.weight3()
            if 17.1 < weight <= 19.6:result.weight4()
            if weight > 19.6:result.weight5()
            if height <= 81.3:result.height1()
            if 81.3 < height <= 84.9:result.height2()
            if 84.9 < height <= 99.4:result.height3()
            if height > 99.4:result.height4()
        if month == 33:
            if weight <= 9.3:result.weight1()
            if 9.3 < weight <= 10.4:result.weight2()
            if 10.4 < weight <= 17.3:result.weight3()
            if 17.3 < weight <= 20:result.weight4()
            if weight > 20:result.weight5()
            if height <= 81.9:result.height1()
            if 81.9 < height <= 85.6:result.height2()
            if 85.6 < height <= 100.3:result.height3()
            if height > 100.3:result.height4()
        if month == 34:
            if weight <= 9.4:result.weight1()
            if 9.4 < weight <= 10.5:result.weight2()
            if 10.5 < weight <= 17.6:result.weight3()
            if 17.6 < weight <= 20.3:result.weight4()
            if weight > 20.3:result.weight5()
            if height <= 82.4:result.height1()
            if 82.5 < height <= 86.2:result.height2()
            if 86.2 < height <= 101.9:result.height3()
            if height > 101.1:result.height4()
        if month == 35:
            if weight <= 9.5:result.weight1()
            if 9.5 < weight <= 10.7:result.weight2()
            if 10.7 < weight <= 17.9:result.weight3()
            if 17.9 < weight <= 20.6:result.weight4()
            if weight > 20.6:result.weight5()
            if height <= 83.1:result.height1()
            if 83.1 < height <= 86.8:result.height2()
            if 86.8 < height <= 101.9:result.height3()
            if height > 101.9:result.height4()
        if month == 36:
            if weight <= 9.6:result.weight1()
            if 9.6 < weight <= 10.8:result.weight2()
            if 10.8 < weight <= 18.1:result.weight3()
            if 18.1 < weight <= 20.9:result.weight4()
            if weight > 20.9:result.weight5()
            if height <= 83.6:result.height1()
            if 83.6 < height <= 87.4:result.height2()
            if 87.4 < height <= 102.7:result.height3()
            if height > 102.7:result.height4()
        if month == 37:
            if weight <= 9.7:result.weight1()
            if 9.7 < weight <= 10.9:result.weight2()
            if 10.9 < weight <= 18.4:result.weight3()
            if 18.4 < weight <= 21.3:result.weight4()
            if weight > 21.3:result.weight5()
            if height <= 84.2:result.height1()
            if 84.2 < height <= 88:result.height2()
            if 88 < height <= 103.4:result.height3()
            if height > 103.4:result.height4()
        if month == 38:
            if weight <= 9.8:result.weight1()
            if 9.8 < weight <= 11.1:result.weight2()
            if 11.1 < weight <= 18.7:result.weight3()
            if 18.7 < weight <= 21.6:result.weight4()
            if weight > 21.6:result.weight5()
            if height <= 84.7:result.height1()
            if 84.7 < height <= 88.6:result.height2()
            if 88.6 < height <= 104.2:result.height3()
            if height > 104.2:result.height4()
        if month == 39:
            if weight <= 9.9:result.weight1()
            if 9.9 < weight <= 11.2:result.weight2()
            if 11.2 < weight <= 19:result.weight3()
            if 19 < weight <= 22:result.weight4()
            if weight > 22:result.weight5()
            if height <= 85.3:result.height1()
            if 85.3 < height <= 89.2:result.height2()
            if 89.2 < height <= 105:result.height3()
            if height > 105:result.height4()
        if month == 40:
            if weight <= 10.1:result.weight1()
            if 10.1 < weight <= 11.3:result.weight2()
            if 11.3 < weight <= 19.2:result.weight3()
            if 19.2 < weight <= 22.2:result.weight4()
            if weight > 22.3:result.weight5()
            if height <= 85.8:result.height1()
            if 85.8 < height <= 89.8:result.height2()
            if 89.8 < height <= 105.7:result.height3()
            if height > 105.7:result.height4()
        if month == 41:
            if weight <= 10.2:result.weight1()
            if 10.2 < weight <= 11.5:result.weight2()
            if 11.5 < weight <= 19.5:result.weight3()
            if 19.5 < weight <= 22.7:result.weight4()
            if weight > 22.7:result.weight5()
            if height <= 86.3:result.height1()
            if 86.3 < height <= 90.4:result.height2()
            if 90.4 < height <= 106.4:result.height3()
            if height > 106.4:result.height4()
        if month == 42:
            if weight <= 10.3:result.weight1()
            if 10.3 < weight <= 11.6:result.weight2()
            if 11.6 < weight <= 19.8:result.weight3()
            if 19.8 < weight <= 23:result.weight4()
            if weight > 23:result.weight5()
            if height <= 86.8:result.height1()
            if 86.8 < height <= 90.9:result.height2()
            if 90.9 < height <= 107.2:result.height3()
            if height > 107.2:result.height4()
        if month == 43:
            if weight <= 10.4:result.weight1()
            if 10.4 < weight <= 11.7:result.weight2()
            if 11.7 < weight <= 20.1:result.weight3()
            if 20.1 < weight <= 23.4:result.weight4()
            if weight > 23.4:result.weight5()
            if height <= 87.4:result.height1()
            if 87.4 < height <= 91.5:result.height2()
            if 91.5 < height <= 107.9:result.height3()
            if height > 107.9:result.height4()
        if month == 44:
            if weight <= 10.5:result.weight1()
            if 10.5 < weight <= 11.8:result.weight2()
            if 11.8 < weight <= 20.4:result.weight3()
            if 20.4 < weight <= 23.7:result.weight4()
            if weight > 23.7:result.weight5()
            if height <= 87.9:result.height1()
            if 87.9 < height <= 92:result.height2()
            if 92 < height <= 108.6:result.height3()
            if height > 108.6:result.height4()
        if month == 45:
            if weight <= 10.6:result.weight1()
            if 10.6 < weight <= 12:result.weight2()
            if 12 < weight <= 20.7:result.weight3()
            if 20.7 < weight <= 60.1:result.weight4()
            if weight > 60.1:result.weight5()
            if height <= 88.4:result.height1()
            if 88.4 < height <= 92.5:result.height2()
            if 92.5 < height <= 109.3:result.height3()
            if height > 109.3:result.height4()
        if month == 46:
            if weight <= 10.7:result.weight1()
            if 10.7 < weight <= 12.1:result.weight2()
            if 12.1 < weight <= 20.9:result.weight3()
            if 20.9 < weight <= 60.5:result.weight4()
            if weight > 60.5:result.weight5()
            if height <= 88.9:result.height1()
            if 88.9 < height <= 93.1:result.height2()
            if 93.1 < height <= 110:result.height3()
            if height > 110:result.height4()
        if month == 47:
            if weight <= 10.8:result.weight1()
            if 10.8 < weight <= 12.2:result.weight2()
            if 12.2 < weight <= 21.2:result.weight3()
            if 21.2 < weight <= 60.8:result.weight4()
            if weight > 60.8:result.weight5()
            if height <= 89.3:result.height1()
            if 89.3 < height <= 93.6:result.height2()
            if 93.6 < height <= 110.7:result.height3()
            if height > 110.7:result.height4()
        if month == 48:
            if weight <= 10.9:result.weight1()
            if 10.9 < weight <= 12.3:result.weight2()
            if 12.3 < weight <= 21.5:result.weight3()
            if 21.5 < weight <= 25.2:result.weight4()
            if weight > 25.2:result.weight5()
            if height <= 89.8:result.height1()
            if 89.8 < height <= 94.1:result.height2()
            if 94.1 < height <= 111.3:result.height3()
            if height > 111.3:result.height4()
        if month == 49:
            if weight <= 11:result.weight1()
            if 11 < weight <= 12.4:result.weight2()
            if 12.4 < weight <= 21.8:result.weight3()
            if 21.8 < weight <= 25.5:result.weight4()
            if weight > 25.5:result.weight5()
            if height <= 90.3:result.height1()
            if 90.3 < height <= 94.6:result.height2()
            if 94.6 < height <= 112:result.height3()
            if height > 112:result.height4()
        if month == 50:
            if weight <= 11.1:result.weight1()
            if 11.1 < weight <= 12.6:result.weight2()
            if 12.6 < weight <= 22.1:result.weight3()
            if 22.1 < weight <= 25.9:result.weight4()
            if weight > 25.9:result.weight5()
            if height <= 90.7:result.height1()
            if 90.7 < height <= 95.1:result.height2()
            if 95.1 < height <= 112.7:result.height3()
            if height > 112.7:result.height4()
        if month == 51:
            if weight <= 11.2:result.weight1()
            if 11.2 < weight <= 12.7:result.weight2()
            if 12.7 < weight <= 22.4:result.weight3()
            if 22.4 < weight <= 26.3:result.weight4()
            if weight > 26.3:result.weight5()
            if height <= 91.2:result.height1()
            if 91.2 < height <= 95.6:result.height2()
            if 95.6 < height <= 113.3:result.height3()
            if height > 113.3:result.height4()
        if month == 52:
            if weight <= 11.3:result.weight1()
            if 11.3 < weight <= 12.8:result.weight2()
            if 12.8 < weight <= 22.6:result.weight3()
            if 22.6 < weight <= 26.6:result.weight4()
            if weight > 26.6:result.weight5()
            if height <= 91.7:result.height1()
            if 91.7 < height <= 96.1:result.height2()
            if 96.1 < height <= 114:result.height3()
            if height > 114:result.height4()
        if month == 53:
            if weight <= 11.4:result.weight1()
            if 11.4 < weight <= 12.9:result.weight2()
            if 12.9 < weight <= 22.9:result.weight3()
            if 22.9 < weight <= 27:result.weight4()
            if weight > 27:result.weight5()
            if height <= 92.1:result.height1()
            if 92.1 < height <= 96.1:result.height2()
            if 96.6 < height <= 114.4:result.height3()
            if height > 114.4:result.height4()
        if month == 54:
            if weight <= 11.5:result.weight1()
            if 11.5 < weight <= 13:result.weight2()
            if 13 < weight <= 23.2:result.weight3()
            if 23.2 < weight <= 27.4:result.weight4()
            if weight > 27.4:result.weight5()
            if height <= 92.6:result.height1()
            if 92.6 < height <= 96.6:result.height2()
            if 96.6 < height <= 114.6:result.height3()
            if height > 114.6:result.height4()
        if month == 55:
            if weight <= 11.6:result.weight1()
            if 11.6 < weight <= 13:result.weight2()
            if 13 < weight <= 23.2:result.weight3()
            if 23.2 < weight <= 27.4:result.weight4()
            if weight > 27.4:result.weight5()
            if height <= 93:result.height1()
            if 93 < height <= 97.6:result.height2()
            if 97.6 < height <= 115.9:result.height3()
            if height > 115.9:result.height4()
        if month == 56:
            if weight <= 11.7:result.weight1()
            if 11.7 < weight <= 13.3:result.weight2()
            if 13.3 < weight <= 23.8:result.weight3()
            if 23.8 < weight <= 28.1:result.weight4()
            if weight > 28.1:result.weight5()
            if height <= 93.4:result.height1()
            if 93.4 < height <= 98.1:result.height2()
            if 98.1 < height <= 116.5:result.height3()
            if height > 116.5:result.height4()
        if month == 57:
            if weight <= 11.8:result.weight1()
            if 11.8 < weight <= 13.4:result.weight2()
            if 13.4 < weight <= 60.1:result.weight3()
            if 60.1 < weight <= 28.5:result.weight4()
            if weight > 28.5:result.weight5()
            if height <= 93.9:result.height1()
            if 93.9 < height <= 98.5:result.height2()
            if 98.5 < height <= 117.1:result.height3()
            if height > 117.1:result.height4()
        if month == 58:
            if weight <= 11.8:result.weight1()
            if 11.8 < weight <= 13.4:result.weight2()
            if 13.4 < weight <= 60.1:result.weight3()
            if 60.1 < weight <= 28.5:result.weight4()
            if weight > 28.5:result.weight5()
            if height <= 94.3:result.height1()
            if 94.3 < height <= 99:result.height2()
            if 99 < height <= 117.7:result.height3()
            if height > 117.7:result.height4()
        if month == 59:
            if weight <= 11.9:result.weight1()
            if 11.9 < weight <= 13.5:result.weight2()
            if 13.5 < weight <= 60.4:result.weight3()
            if 60.4 < weight <= 28.8:result.weight4()
            if weight > 28.8:result.weight5()
            if height <= 94.7:result.height1()
            if 94.7 < height <= 99.5:result.height2()
            if 99.5 < height <= 117.7:result.height3()
            if height > 118.3:result.height4()
        if month == 60:
            if weight <= 12.1:result.weight1()
            if 12.1 < weight <= 13.7:result.weight2()
            if 13.7 < weight <= 60.9:result.weight3()
            if 60.9 < weight <= 29.5:result.weight4()
            if weight > 29.5:result.weight5()
            if height <= 95.2:result.height1()
            if 95.2 < height <= 99.9:result.height2()
            if 99.9 < height <= 118.9:result.height3()
            if height > 118.9:result.height4()
        if month > 60: messagebox.showinfo("Lỗi tháng tuổi","Tháng tuổi không có hoặc chưa hỗ trợ")
    if variable.get() in ['Nam']:
        if month == 0:
            if weight <= 2:result.weight1()
            if 2 < weight <= 2.4:result.weight2()
            if 2.4 < weight <= 4.4:result.weight3()
            if 4.4 < weight <= 5:result.weight4()
            if weight > 5:result.weight5()
            if height <= 44:result.height1()
            if 44 < height <= 46:result.height2()
            if 46 < height <= 54:result.height3()
            if height > 54:result.height4()
        if month == 1:
            if weight <= 3:result.weight1()
            if 3 < weight <= 3.5:result.weight2()
            if 3.5 < weight <= 6:result.weight3()
            if 6 < weight <= 6.8:result.weight4()
            if weight > 6.8:result.weight5()
            if height <= 49:result.height1()
            if 49 < height <= 51:result.height2()
            if 51 < height <= 59:result.height3()
            if height > 59:result.height4()
        if month == 2:
            if weight <= 3.8:result.weight1()
            if 3.8 < weight <= 4.4:result.weight2()
            if 4.4 < weight <= 7.2:result.weight3()
            if 7.2 < weight <= 8:result.weight4()
            if weight > 8:result.weight5()
            if height <= 53:result.height1()
            if 53 < height <= 55:result.height2()
            if 55 < height <= 63.5:result.height3()
            if height > 63.5:result.height4()
        if month == 3:
            if weight <= 4.4:result.weight1()
            if 4.4 < weight <= 5.1:result.weight2()
            if 5.1 < weight <= 8:result.weight3()
            if 8 < weight <= 9:result.weight4()
            if weight > 9:result.weight5()
            if height <= 55.5:result.height1()
            if 55.5 < height <= 56:result.height2()
            if 56 < height <= 64:result.height3()
            if height > 64:result.height4()
        if month == 4:
            if weight <= 4.5:result.weight1()
            if 4.5 < weight <= 5.1:result.weight2()
            if 5.1 < weight <= 8.3:result.weight3()
            if 8.3 < weight <= 9.4:result.weight4()
            if weight > 9.41:result.weight5()
            if height <= 55:result.height1()
            if 55 < height <= 58:result.height2()
            if 58 < height <= 67:result.height3()
            if height > 67:result.height4()
        if month == 5:
            if weight <= 4.8:result.weight1()
            if 4.8 < weight <= 5.5:result.weight2()
            if 5.5 < weight <= 9:result.weight3()
            if 9 < weight <= 10:result.weight4()
            if weight > 10:result.weight5()
            if height <= 57.5:result.height1()
            if 57.5 < height <= 60:result.height2()
            if 60 < height <= 68.5:result.height3()
            if height > 68.5:result.height4()
        if month == 6:
            if weight <= 5.1:result.weight1()
            if 5.1 < weight <= 5.7:result.weight2()
            if 5.7 < weight <= 9.4:result.weight3()
            if 9.4 < weight <= 10.6:result.weight4()
            if weight > 10.6:result.weight5()
            if height <= 59:result.height1()
            if 59 < height <= 61.5:result.height2()
            if 61.5 < height <= 70.5:result.height3()
            if height > 70.5:result.height4()
        if month == 7:
            if weight <= 5.3:result.weight1()
            if 5.3 < weight <= 6:result.weight2()
            if 6 < weight <= 9.9:result.weight3()
            if 9.9 < weight <= 11.1:result.weight4()
            if weight > 11.1:result.weight5()
            if height <= 60.5:result.height1()
            if 60 < height <= 63:result.height2()
            if 63 < height <= 72:result.height3()
            if height > 72:result.height4()
        if month == 8:
            if weight <= 5.6:result.weight1()
            if 5.6 < weight <= 6.3:result.weight2()
            if 6.3 < weight <= 10.3:result.weight3()
            if 10.3 < weight <= 11.6:result.weight4()
            if weight > 11.6:result.weight5()
            if height <= 61.5:result.height1()
            if 61.5 < height <= 64:result.height2()
            if 64 < height <= 73.5:result.height3()
            if height > 73.5:result.height4()
        if month == 9:
            if weight <= 5.8:result.weight1()
            if 5.8 < weight <= 6.5:result.weight2()
            if 6.5 < weight <= 10.6:result.weight3()
            if 10.6 < weight <= 12:result.weight4()
            if weight >= 12:result.weight5()
            if height <= 63:result.height1()
            if 63 < height <= 65.5:result.height2()
            if 65.5 < height <= 75:result.height3()
            if height > 75:result.height4()
        if month == 10:
            if weight <= 6:result.weight1()
            if 6 < weight <= 6.7:result.weight2()
            if 6.7 < weight <= 11:result.weight3()
            if 11 < weight <= 12.4:result.weight4()
            if weight > 12.4:result.weight5()
            if height <= 64:result.height1()
            if 64 < height <= 67:result.height2()
            if 67 < height <= 76.5:result.height3()
            if height >= 76.5:result.height4()
        if month == 11:
            if weight <= 6.1:result.weight1()
            if 6.1 < weight <= 6.9:result.weight2()
            if 6.9 < weight <= 11.3:result.weight3()
            if 11.3 < weight <= 12.7:result.weight4()
            if weight > 12.7:result.weight5()
            if height <= 65:result.height1()
            if 65 < height <= 68:result.height2()
            if 68 < height <= 78:result.height3()
            if height > 78:result.height4()
        if month == 12:
            if weight <= 7:result.weight1()
            if 7 < weight <= 7.8:result.weight2()
            if 7.8 < weight <= 12:result.weight3()
            if 12 < weight <= 13.4:result.weight4()
            if weight > 13.4:result.weight5()
            if height <= 69:result.height1()
            if 69 < height <= 71:result.height2()
            if 71 < height <= 80.5:result.height3()
            if height > 80.5:result.height4()
        if month == 13:
            if weight <= 7.1:result.weight1()
            if 7.1 < weight <= 8:result.weight2()
            if 8 < weight <= 12.3:result.weight3()
            if 12.3 < weight <= 13.7:result.weight4()
            if weight > 13.7:result.weight5()
            if height <= 70:result.height1()
            if 70 < height <= 72:result.height2()
            if 72 < height <= 82:result.height3()
            if height > 82:result.height4()
        if month == 14:
            if weight <= 7.3:result.weight1()
            if 7.3 < weight <= 8.1:result.weight2()
            if 8.1 < weight <= 12.6:result.weight3()
            if 12.6 < weight <= 14:result.weight4()
            if weight > 14:result.weight5()
            if height <= 71:result.height1()
            if 71 < height <= 73:result.height2()
            if 73 < height <= 85:result.height3()
            if height > 85:result.height4()
        if month == 15:
            if weight <= 7.4:result.weight1()
            if 7.4 < weight <= 8.3:result.weight2()
            if 8.3 < weight <= 12.9:result.weight3()
            if 12.9 < weight <= 14.4:result.weight4()
            if weight > 14.4:result.weight5()
            if height <= 71.5:result.height1()
            if 71.5 < height <= 74:result.height2()
            if 74 < height <= 84:result.height3()
            if height > 84:result.height4()
        if month == 16:
            if weight <= 7.6:result.weight1()
            if 7.6 < weight <= 8.5:result.weight2()
            if 8.5 < weight <= 13.1:result.weight3()
            if 13.1 < weight <= 14.6:result.weight4()
            if weight > 14.6:result.weight5()
            if height <= 72.5:result.height1()
            if 72.5 < height <= 75:result.height2()
            if 75 < height <= 85.5:result.height3()
            if height > 85.5:result.height4()
        if month == 17:
            if weight <= 7.7:result.weight1()
            if 7.7 < weight <= 8.6:result.weight2()
            if 8.6 < weight <= 13.4:result.weight3()
            if 13.4 < weight <= 15:result.weight4()
            if weight > 15:result.weight5()
            if height <= 73.5:result.height1()
            if 73.5 < height <= 76:result.height2()
            if 76 < height <= 86.5:result.height3()
            if height > 86.5:result.height4()
        if month == 18:
            if weight <= 7.8:result.weight1()
            if 7.8 < weight <= 8.7:result.weight2()
            if 8.7 < weight <= 13.7:result.weight3()
            if 13.7 < weight <= 15.3:result.weight4()
            if weight > 15.3:result.weight5()
            if height <= 74:result.height1()
            if 74 < height <= 76:result.height2()
            if 76 < height <= 87.5:result.height3()
            if height > 87.5:result.height4()
        if month == 19:
            if weight <= 8:result.weight1()
            if 8 < weight <= 9:result.weight2()
            if 9 < weight <= 14:result.weight3()
            if 14 < weight <= 15.6:result.weight4()
            if weight > 15.6:result.weight5()
            if height <= 75:result.height1()
            if 75 < height <= 78:result.height2()
            if 78 < height <= 88.5:result.height3()
            if height > 88.5:result.height4()
        if month == 20:
            if weight <= 8.1:result.weight1()
            if 8.1 < weight <= 9:result.weight2()
            if 9 < weight <= 14.2:result.weight3()
            if 14.2 < weight <= 15.9:result.weight4()
            if weight > 15.9:result.weight5()
            if height <= 76:result.height1()
            if 76 < height <= 78.5:result.height2()
            if 78.5 < height <= 90:result.height3()
            if height > 90:result.height4()
        if month == 21:
            if weight <= 8.2:result.weight1()
            if 8.2 < weight <= 9.2:result.weight2()
            if 9.2 < weight <= 14.5:result.weight3()
            if 14.5 < weight <= 16.2:result.weight4()
            if weight > 16.2:result.weight5()
            if height <= 76.5:result.height1()
            if 76.5 < height <= 79:result.height2()
            if 79 < height <= 91:result.height3()
            if height > 91:result.height4()
        if month == 22:
            if weight <= 8.4:result.weight1()
            if 8.4 < weight <= 9.4:result.weight2()
            if 9.4 < weight <= 14.7:result.weight3()
            if 14.7 < weight <= 16.5:result.weight4()
            if weight > 16.5:result.weight5()
            if height <= 77:result.height1()
            if 77 < height <= 80:result.height2()
            if 80 < height <= 92:result.height3()
            if height > 92:result.height4()
        if month == 23:
            if weight <= 8.5:result.weight1()
            if 8.5 < weight <= 9.5:result.weight2()
            if 9.5 < weight <= 15:result.weight3()
            if 15 < weight <= 16.8:result.weight4()
            if weight > 16.8:result.weight5()
            if height <= 78:result.height1()
            if 78 < height <= 81:result.height2()
            if 81 < height <= 93:result.height3()
            if height > 93:result.height4()
        if month == 60:
            if weight <= 8.6:result.weight1()
            if 8.6 < weight <= 9.7:result.weight2()
            if 9.7 < weight <= 15.3:result.weight3()
            if 15.3 < weight <= 17.1:result.weight4()
            if weight > 17.1:result.weight5()
            if height <= 78.5:result.height1()
            if 78.5 < height <= 81.5:result.height2()
            if 81.5 < height <= 94:result.height3()
            if height > 94:result.height4()
        if month == 25:
            if weight <= 8.8:result.weight1()
            if 8.8 < weight <= 9.8:result.weight2()
            if 9.8 < weight <= 15.5:result.weight3()
            if 15.5 < weight <= 17.5:result.weight4()
            if weight > 17.5:result.weight5()
            if height <= 78.6:result.height1()
            if 78.6 < height <= 81.7:result.height2()
            if 81.7 < height <= 94.2:result.height3()
            if height > 94.2:result.height4()
        if month == 26:
            if weight <= 8.9:result.weight1()
            if 8.9 < weight <= 10:result.weight2()
            if 10 < weight <= 15.8:result.weight3()
            if 15.8 < weight <= 17.8:result.weight4()
            if weight > 17.8:result.weight5()
            if height <= 79.3:result.height1()
            if 78.3 < height <= 82.5:result.height2()
            if 82.5 < height <= 95.2:result.height3()
            if height > 95.2:result.height4()
        if month == 27:
            if weight <= 9:result.weight1()
            if 9 < weight <= 10.1:result.weight2()
            if 10.1 < weight <= 16.1:result.weight3()
            if 16.1 < weight <= 18.1:result.weight4()
            if weight > 18.1:result.weight5()
            if height <= 79.9:result.height1()
            if 78.9 < height <= 83.1:result.height2()
            if 83.1 < height <= 96.1:result.height3()
            if height > 96.1:result.height4()
        if month == 28:
            if weight <= 9.1:result.weight1()
            if 9.1 < weight <= 10.2:result.weight2()
            if 10.2 < weight <= 16.3:result.weight3()
            if 16.3 < weight <= 18.4:result.weight4()
            if weight > 18.4:result.weight5()
            if height <= 80.5:result.height1()
            if 80.5 < height <= 83.8:result.height2()
            if 83.8 < height <= 97:result.height3()
            if height > 97:result.height4()
        if month == 29:
            if weight <= 9.2:result.weight1()
            if 9.2 < weight <= 10.4:result.weight2()
            if 10.4 < weight <= 16.6:result.weight3()
            if 16.6 < weight <= 18.7:result.weight4()
            if weight > 18.7:result.weight5()
            if height <= 81.1:result.height1()
            if 81.1 < height <= 84.5:result.height2()
            if 84.5 < height <= 97.9:result.height3()
            if height > 97.9:result.height4()
        if month == 30:
            if weight <= 9.4:result.weight1()
            if 9.4 < weight <= 10.5:result.weight2()
            if 10.5 < weight <= 16.9:result.weight3()
            if 16.9 < weight <= 19:result.weight4()
            if weight > 19:result.weight5()
            if height <= 81.7:result.height1()
            if 81.7 < height <= 85.1:result.height2()
            if 85.1 < height <= 98.7:result.height3()
            if height > 98.7:result.height4()
        if month == 31:
            if weight <= 9.5:result.weight1()
            if 9.5 < weight <= 10.7:result.weight2()
            if 10.7 < weight <= 17.1:result.weight3()
            if 17.1 < weight <= 19.3:result.weight4()
            if weight > 19.3:result.weight5()
            if height <= 82.3:result.height1()
            if 82.3 < height <= 85.7:result.height2()
            if 85.7 < height <= 99.6:result.height3()
            if height > 99.6:result.height4()
        if month == 32:
            if weight <= 9.6:result.weight1()
            if 9.6 < weight <= 10.8:result.weight2()
            if 10.8 < weight <= 17.4:result.weight3()
            if 17.4 < weight <= 19.6:result.weight4()
            if weight > 19.6:result.weight5()
            if height <= 82.8:result.height1()
            if 82.8 < height <= 86.4:result.height2()
            if 86.4 < height <= 100.4:result.height3()
            if height > 100.4:result.height4()
        if month == 33:
            if weight <= 9.7:result.weight1()
            if 9.7 < weight <= 10.9:result.weight2()
            if 10.9 < weight <= 17.6:result.weight3()
            if 17.6 < weight <= 19.9:result.weight4()
            if weight > 19.9:result.weight5()
            if height <= 83.4:result.height1()
            if 83.4 < height <= 86.9:result.height2()
            if 86.9 < height <= 101.2:result.height3()
            if height > 101.2:result.height4()
        if month == 34:
            if weight <= 9.8:result.weight1()
            if 9.8 < weight <= 11:result.weight2()
            if 11 < weight <= 17.8:result.weight3()
            if 17.8 < weight <= 20.2:result.weight4()
            if weight > 20.2:result.weight5()
            if height <= 83.9:result.height1()
            if 83.9 < height <= 87.5:result.height2()
            if 87.5 < height <= 102:result.height3()
            if height > 102:result.height4()
        if month == 35:
            if weight <= 9.9:result.weight1()
            if 9.9 < weight <= 11.2:result.weight2()
            if 11.2 < weight <= 18.1:result.weight3()
            if 18.1 < weight <= 20.4:result.weight4()
            if weight > 20.4:result.weight5()
            if height <= 84.4:result.height1()
            if 84.4 < height <= 88.1:result.height2()
            if 88.1 < height <= 102.7:result.height3()
            if height > 102.7:result.height4()
        if month == 36:
            if weight <= 10:result.weight1()
            if 10 < weight <= 11.3:result.weight2()
            if 11.3 < weight <= 18.3:result.weight3()
            if 18.3 < weight <= 20.7:result.weight4()
            if weight > 20.7:result.weight5()
            if height <= 85:result.height1()
            if 85 < height <= 88.7:result.height2()
            if 88.7 < height <= 103.5:result.height3()
            if height > 103.5:result.height4()
        if month == 37:
            if weight <= 10.1:result.weight1()
            if 10.1 < weight <= 11.4:result.weight2()
            if 11.4 < weight <= 18.6:result.weight3()
            if 18.6 < weight <= 21:result.weight4()
            if weight > 21:result.weight5()
            if height <= 85.5:result.height1()
            if 85.5 < height <= 89.2:result.height2()
            if 89.2 < height <= 104.2:result.height3()
            if height > 104.2:result.height4()
        if month == 38:
            if weight <= 10.2:result.weight1()
            if 10.2 < weight <= 11.5:result.weight2()
            if 11.5 < weight <= 18.8:result.weight3()
            if 18.8 < weight <= 21.3:result.weight4()
            if weight > 21.3:result.weight5()
            if height <= 86:result.height1()
            if 86 < height <= 89.8:result.height2()
            if 89.8 < height <= 105:result.height3()
            if height > 105:result.height4()
        if month == 39:
            if weight <= 10.3:result.weight1()
            if 10.3 < weight <= 11.6:result.weight2()
            if 11.6 < weight <= 19:result.weight3()
            if 19 < weight <= 21.6:result.weight4()
            if weight > 21.6:result.weight5()
            if height <= 86.5:result.height1()
            if 86.5 < height <= 90.3:result.height2()
            if 90.3 < height <= 105.7:result.height3()
            if height > 105.7:result.height4()
        if month == 40:
            if weight <= 10.4:result.weight1()
            if 10.4 < weight <= 11.8:result.weight2()
            if 11.8 < weight <= 19.3:result.weight3()
            if 19.3 < weight <= 21.9:result.weight4()
            if weight > 21.9:result.weight5()
            if height <= 87:result.height1()
            if 87 < height <= 90.9:result.height2()
            if 90.9 < height <= 106.4:result.height3()
            if height > 106.4:result.height4()
        if month == 41:
            if weight <= 10.5:result.weight1()
            if 10.5 < weight <= 11.9:result.weight2()
            if 11.9 < weight <= 19.5:result.weight3()
            if 19.5 < weight <= 22.1:result.weight4()
            if weight > 22.1:result.weight5()
            if height <= 87.5:result.height1()
            if 87.5 < height <= 91.4:result.height2()
            if 91.4 < height <= 107.1:result.height3()
            if height > 107.4:result.height4()
        if month == 42:
            if weight <= 10.6:result.weight1()
            if 10.6 < weight <= 12:result.weight2()
            if 12 < weight <= 19.7:result.weight3()
            if 19.7 < weight <= 22.4:result.weight4()
            if weight > 22.4:result.weight5()
            if height <= 88:result.height1()
            if 88 < height <= 91.9:result.height2()
            if 91.9 < height <= 107.8:result.height3()
            if height > 107.8:result.height4()
        if month == 43:
            if weight <= 10.7:result.weight1()
            if 10.7 < weight <= 12.1:result.weight2()
            if 12.1 < weight <= 20:result.weight3()
            if 20 < weight <= 22.7:result.weight4()
            if weight > 22.7:result.weight5()
            if height <= 88.4:result.height1()
            if 88.4 < height <= 92.4:result.height2()
            if 92.4 < height <= 108.5:result.height3()
            if height > 108.5:result.height4()
        if month == 44:
            if weight <= 10.8:result.weight1()
            if 10.8 < weight <= 12.2:result.weight2()
            if 12.2 < weight <= 20.2:result.weight3()
            if 20.2 < weight <= 23:result.weight4()
            if weight > 23:result.weight5()
            if height <= 88.9:result.height1()
            if 88.9 < height <= 93:result.height2()
            if 93 < height <= 109.1:result.height3()
            if height > 109.1:result.height4()
        if month == 45:
            if weight <= 10.9:result.weight1()
            if 10.9 < weight <= 12.4:result.weight2()
            if 12.4 < weight <= 20.5:result.weight3()
            if 20.5 < weight <= 23.3:result.weight4()
            if weight > 23.3:result.weight5()
            if height <= 89.4:result.height1()
            if 89.4 < height <= 93.5:result.height2()
            if 93.5 < height <= 109.8:result.height3()
            if height > 109.8:result.height4()
        if month == 46:
            if weight <= 11:result.weight1()
            if 11 < weight <= 12.5:result.weight2()
            if 12.5 < weight <= 20.7:result.weight3()
            if 20.7 < weight <= 23.6:result.weight4()
            if weight > 23.6:result.weight5()
            if height <= 89.8:result.height1()
            if 89.8 < height <= 94:result.height2()
            if 94 < height <= 110:result.height3()
            if height > 110:result.height4()
        if month == 47:
            if weight <= 11.1:result.weight1()
            if 11.1 < weight <= 12.6:result.weight2()
            if 12.6 < weight <= 20.9:result.weight3()
            if 20.9 < weight <= 23.9:result.weight4()
            if weight > 23.9:result.weight5()
            if height <= 90.3:result.height1()
            if 90.3 < height <= 94.4:result.height2()
            if 94.4 < height <= 111.1:result.height3()
            if height > 111.1:result.height4()
        if month == 48:
            if weight <= 11.2:result.weight1()
            if 11.2 < weight <= 12.7:result.weight2()
            if 12.7 < weight <= 21.2:result.weight3()
            if 21.2 < weight <= 60.2:result.weight4()
            if weight > 60.2:result.weight5()
            if height <= 90.7:result.height1()
            if 90.7 < height <= 94.9:result.height2()
            if 94.9 < height <= 111.7:result.height3()
            if height > 111.7:result.height4()
        if month == 49:
            if weight <= 11.3:result.weight1()
            if 11.3 < weight <= 12.8:result.weight2()
            if 12.8 < weight <= 21.4:result.weight3()
            if 21.4 < weight <= 60.5:result.weight4()
            if weight > 60.5:result.weight5()
            if height <= 91.2:result.height1()
            if 91.2 < height <= 95.4:result.height2()
            if 95.4 < height <= 112.4:result.height3()
            if height > 112.4:result.height4()
        if month == 50:
            if weight <= 11.4:result.weight1()
            if 11.4 < weight <= 12.9:result.weight2()
            if 12.9 < weight <= 21.7:result.weight3()
            if 21.7 < weight <= 60.8:result.weight4()
            if weight > 60.8:result.weight5()
            if height <= 91.6:result.height1()
            if 91.6 < height <= 95.9:result.height2()
            if 95.9 < height <= 113:result.height3()
            if height > 113:result.height4()
        if month == 51:
            if weight <= 11.5:result.weight1()
            if 11.5 < weight <= 13.1:result.weight2()
            if 13.1 < weight <= 21.9:result.weight3()
            if 21.9 < weight <= 25.1:result.weight4()
            if weight > 25.1:result.weight5()
            if height <= 92.1:result.height1()
            if 92.1 < height <= 96.4:result.height2()
            if 96.4 < height <= 113.6:result.height3()
            if height > 113.6:result.height4()
        if month == 52:
            if weight <= 11.6:result.weight1()
            if 11.6 < weight <= 13.2:result.weight2()
            if 13.2 < weight <= 22.2:result.weight3()
            if 22.2 < weight <= 25.4:result.weight4()
            if weight > 25.4:result.weight5()
            if height <= 92.5:result.height1()
            if 92.5 < height <= 96.9:result.height2()
            if 96.9 < height <= 114.2:result.height3()
            if height > 114.2:result.height4()
        if month == 53:
            if weight <= 11.7:result.weight1()
            if 11.7 < weight <= 13.3:result.weight2()
            if 13.3 < weight <= 22.4:result.weight3()
            if 22.4 < weight <= 25.7:result.weight4()
            if weight > 25.7:result.weight5()
            if height <= 93:result.height1()
            if 93 < height <= 97.4:result.height2()
            if 97.4 < height <= 114.9:result.height3()
            if height > 114.9:result.height4()
        if month == 54:
            if weight <= 11.8:result.weight1()
            if 11.8 < weight <= 13.4:result.weight2()
            if 13.4 < weight <= 22.7:result.weight3()
            if 22.7 < weight <= 26:result.weight4()
            if weight > 26:result.weight5()
            if height <= 93.4:result.height1()
            if 93.4 < height <= 97.8:result.height2()
            if 97.8 < height <= 115.5:result.height3()
            if height > 115.5:result.height4()
        if month == 55:
            if weight <= 11.9:result.weight1()
            if 11.9 < weight <= 13.5:result.weight2()
            if 13.5 < weight <= 22.9:result.weight3()
            if 22.9 < weight <= 26.3:result.weight4()
            if weight > 26.3:result.weight5()
            if height <= 93.9:result.height1()
            if 93.9 < height <= 98.3:result.height2()
            if 98.3 < height <= 116.1:result.height3()
            if height > 116.1:result.height4()
        if month == 56:
            if weight <= 12:result.weight1()
            if 12 < weight <= 13.6:result.weight2()
            if 13.6 < weight <= 23.2:result.weight3()
            if 23.2 < weight <= 26.6:result.weight4()
            if weight > 26.6:result.weight5()
            if height <= 94.3:result.height1()
            if 94.3 < height <= 98.8:result.height2()
            if 98.8 < height <= 116.7:result.height3()
            if height > 116.7:result.height4()
        if month == 57:
            if weight <= 12.1:result.weight1()
            if 12.1 < weight <= 13.7:result.weight2()
            if 13.7 < weight <= 23.4:result.weight3()
            if 23.4 < weight <= 26.9:result.weight4()
            if weight > 26.9:result.weight5()
            if height <= 94.7:result.height1()
            if 94.7 < height <= 99.3:result.height2()
            if 99.3 < height <= 117.4:result.height3()
            if height > 117.4:result.height4()
        if month == 58:
            if weight <= 12.2:result.weight1()
            if 12.2 < weight <= 13.8:result.weight2()
            if 13.8 < weight <= 23.7:result.weight3()
            if 23.7 < weight <= 27.2:result.weight4()
            if weight > 27.2:result.weight5()
            if height <= 95.2:result.height1()
            if 95.2 < height <= 99.7:result.height2()
            if 99.7 < height <= 118:result.height3()
            if height > 118:result.height4()
        if month == 59:
            if weight <= 12.3:result.weight1()
            if 12.3 < weight <= 14:result.weight2()
            if 14 < weight <= 23.9:result.weight3()
            if 23.9 < weight <= 27.6:result.weight4()
            if weight > 27.6:result.weight5()
            if height <= 95.6:result.height1()
            if 95.6 < height <= 100.2:result.height2()
            if 100.2 < height <= 118.6:result.height3()
            if height > 118.6:result.height4()
        if month == 60:
            if weight <= 12.4:result.weight1()
            if 12.4 < weight <= 14.1:result.weight2()
            if 14.1 < weight <= 60.2:result.weight3()
            if 60.2 < weight <= 27.9:result.weight4()
            if weight > 27.9:result.weight5()
            if height <= 96.1:result.height1()
            if 96.1 < height <= 100.7:result.height2()
            if 100.7 < height <= 119.2:result.height3()
            if height > 119.2:result.height4()
        if month > 60: messagebox.showinfo("Lỗi tháng tuổi","Tháng tuổi không có hoặc chưa hỗ trợ")
    
def Xls_get():
    root.filename = filedialog.askopenfilename(initialdir='/Data', title='Chọn một tệp Excel để lưu', filetype=[("Tệp Excel", "*.xlsx")])
    if root.filename == '':
        pass
    if root.filename not in  '':
        global link1
        link1 = Label(root, text=root.filename + '   Hủy')
        link1.grid(row=0,column=3,pady=2,padx=2,sticky=W)
        link1.bind("<Button-1>", lambda e: callback())
        XlsLocation['state'] = 'disabled'
def confirm():
    if a == False:
        try:
            int(Month.get())
            float(Weight.get().replace(',','.'))
            float(Height.get().replace(',','.'))
        except: messagebox.showwarning("Không thể chuyển đổi","Không thể chuyển đổi, có thể là vì một số lí do sau:\n1. Tháng tuổi bắt buộc phải là số nguyên.\n2. Chiều cao, cân nặng bắt buộc phải là số.\n3. Tháng tuổi, chiều cao, cân nặng là 3 thông tin bắt buộc, không thể bỏ trống.")
        else: main()
    if a == True:
        try:
            float(Weight.get().replace(',','.'))
            float(Height.get().replace(',','.'))
            now = datetime.datetime.now()
            x = str(Birth.get())
            date = x.split("/")
            month = int(date[1])
            year = int(date[2])
            month = (12 - month) + (2021-year)*12
        except: messagebox.showwarning("Không thể chuyển đổi","Không thể chuyển đổi, có thể là vì một số lí do sau:\n1. Nhập ngày tháng năm sinh không quá 2021.\n2. Chiều cao, cân nặng bắt buộc phải là số.\n3. Ngày sinh, chiều cao, cân nặng là 3 thông tin bắt buộc, không thể bỏ trống.")
        else: main()
def delete():
    try:
        Info.grid_forget()
        Underline.grid_forget()
        HLabel.grid_forget()
        WLabel.grid_forget()
        Delete.grid_forget()
        Confirm.grid(row=9,column=1,pady=2,padx=2)
    except:
        pass
    if a == False:
        try:
            int(Month.get())
            float(Weight.get().replace(',','.'))
            float(Height.get().replace(',','.'))
        except: messagebox.showwarning("Không thể chuyển đổi","Không thể chuyển đổi, có thể là vì một số lí do sau:\n1. Tháng tuổi bắt buộc phải là số nguyên.\n2. Chiều cao, cân nặng bắt buộc phải là số.\n3. Tháng tuổi, chiều cao, cân nặng là 3 thông tin bắt buộc, không thể bỏ trống.")
        else: main()
    if a == True:
        try:
            float(Weight.get().replace(',','.'))
            float(Height.get().replace(',','.'))
            now = datetime.datetime.now()
            x = str(Birth.get())
            date = x.split("/")
            month = int(date[1])
            year = int(date[2])
            month = (12 - month) + (2021-year)*12
        except: messagebox.showwarning("Không thể chuyển đổi","Không thể chuyển đổi, có thể là vì một số lí do sau:\n1. Nhập ngày tháng năm sinh không quá 2021.\n2. Chiều cao, cân nặng bắt buộc phải là số.\n3. Ngày sinh, chiều cao, cân nặng là 3 thông tin bắt buộc, không thể bỏ trống.")
        else: main()
def xlsoption():
    global Confirm, Delete, Name, PName, Ad, Birth, XlsOption, XlsOption2, AdLabel, PNameLabel, BirthL, a, ClassNamel, ClassName
    a = True
    XlsOption.grid_forget()
    AdLabel.grid_forget()
    Ad.grid_forget()
    PNameLabel.grid_forget()
    PName.grid_forget()
    BirthL.grid_forget()
    Birth.grid_forget()
    InfoLabel.grid_forget()
    Month.grid_forget()
    MonthOp.grid(row=6,column=1,pady=2,padx=2)
    ClassNamel.grid(row=1,pady=2,padx=2)
    ClassName.grid(row=1,column=1,pady=2,padx=2)
    BirthL.grid(row=3,pady=2,padx=2)
    Birth.grid(row=3,column=1,pady=2,padx=2)
    XlsOption2.grid(row=0,column=2,pady=2,padx=2)
def xlsoption2():
    global Confirm, Delete, Name, PName, Ad, Birth, XlsOption, XlsOption2, AdLabel, PNameLabel, BirthL, a, ClassNamel, ClassName
    a = False
    XlsOption2.grid_forget()
    BirthL.grid_forget()
    Birth.grid_forget()
    ClassNamel.grid_forget()
    ClassName.grid_forget()
    MonthOp.grid_forget()
    MonthLabel.grid(row=6,pady=2,padx=2)
    Month.grid(row=6,column=1,pady=2,padx=2)
    InfoLabel.grid(row=1,pady=2,padx=2)
    PNameLabel.grid(row=3,pady=2,padx=2)
    PName.grid(row=3,pady=2,column=1,padx=2)
    AdLabel.grid(row=2,column=2,pady=2,padx=2)
    Ad.grid(row=2,column=3,pady=2,padx=2,sticky=W)
    BirthL.grid(row=3,pady=2,column=2,padx=2)
    Birth.grid(row=3,pady=2,column=3,padx=2,sticky=W)
    XlsOption.grid(row=0,column=2,pady=2,padx=2)

#---------------------------------------- TKINTER ---------------------------------------#
#-------------------- Tkinter Windows Setup --------------------#
root=Tk(); root.resizable(0,0)
global Confirm, Delete, Name, PName, Ad, Birth, XlsOption, XlsOption2, AdLabel, PNameLabel, BirthL, a, ClassNamel, ClassName
fonts = tkFont.Font(family='Arial', size=11)
root.geometry('850x320')
root.title('Phần mềm theo dõi sức khỏe của trẻ mầm non. v1.0')
XlsLabel = Label(root, text="Lưu dưới dạng file Excel:", font=('Arial',11))
XlsOption = Button(root, text="1 Lớp/file", command=xlsoption)
XlsOption2 = Button(root, text="Nhiều Lớp/file", command=xlsoption2)

XlsLocation = Button(root, text='Chọn tệp', command=Xls_get)
XlsRead = Button(root, text='Đọc tệp (Phần mềm bổ trợ)')

InfoLabel = Label(root, text="THÔNG TIN CỦA TRẺ:", font=('Arial',11))

ClassNamel = Label(root, text="Tên lớp:", font=('Arial',11))
ClassName = Entry(width=30)

NameLabel = Label(root, text="Họ và Tên của trẻ:", font=('Arial',11))
Name = Entry(width=30)

PNameLabel = Label(root, text="Họ và Tên của người bảo hộ:", font=('Arial',11))
PName = Entry(width=30)

AdLabel = Label(root, text="Địa chỉ:", font=('Arial',11))
Ad = Entry(width=30)

BirthL = Label(root, text="Ngày sinh:", font=('Arial',11))
Birth = Entry(width=30)

GenderLabel = Label(root, text="Giới tính:", font=('Arial',11))
variable = StringVar()
variable.set('Nam')
Gender = OptionMenu(root, variable, 'Nam', 'Nữ','Nam')

MonthLabel = Label(root, text="Tháng tuổi:", font=('Arial',11))
Month = Entry(width=30)
MonthOp = Label(root, text="(Tự động tính)", font=('Arial',11))
WeightLabel = Label(root, text="Cân nặng:", font=('Arial',11))
Weight = Entry(width=30)

HeightLabel = Label(root, text="Chiều cao:", font=('Arial',11))
Height = Entry(width=30)

Confirm = Button(root, text="Xác nhận", command=confirm)
Delete = Button(root, text="Xác nhận", command=delete)

AddInfo = Label(root, text='Thêm thông tin', font=('Arial',11))
AddInfo.bind("<Button-1>", lambda e: call())

#-------------------- Tkinter Windows Launch --------------------#
XlsLabel.grid(row=0,pady=2,padx=2)
XlsLocation.grid(row=0,column=1,pady=2,padx=2)
XlsOption.grid(row=0,column=2,pady=2,padx=2)

InfoLabel.grid(row=1,column=0,pady=2,padx=2)

NameLabel.grid(row=2,pady=2,padx=2)
Name.grid(row=2,column=1,pady=2,padx=2)

PNameLabel.grid(row=3,pady=2,padx=2)
PName.grid(row=3,pady=2,column=1,padx=2)

AdLabel.grid(row=2,column=2,pady=2,padx=2)
Ad.grid(row=2,column=3,pady=2,padx=2,sticky=W)

BirthL.grid(row=3,pady=2,column=2,padx=2)
Birth.grid(row=3,pady=2,column=3,padx=2,sticky=W)

Label(root, text=" ").grid(row=4)

GenderLabel.grid(row=5,pady=2,padx=2)
Gender.grid(row=5,column=1,pady=2,padx=2)

MonthLabel.grid(row=6,pady=2,padx=2)
Month.grid(row=6,column=1,pady=2,padx=2)

WeightLabel.grid(row=7,pady=2,padx=2)
Weight.grid(row=7,column=1,pady=2,padx=2)

HeightLabel.grid(row=8,pady=2,padx=2)
Height.grid(row=8,column=1,pady=2,padx=2)

Confirm.grid(row=9,column=1,pady=2,padx=2)

a = False

root.mainloop()
#---------------------------------------- TKINTER ----------------------------------------#
#---------------------------------------- PYTHON ----------------------------------------#

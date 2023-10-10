# _*_ coding:UTF-8 _*_
import shutil
import sys, os
import datetime
import time
import re
from tkinter.filedialog import *

def oldcode():
    addr_boot = 0x00000000
    addr_firmware = 0x00002000
    addr_calil_code = 0x00066000
    addr_cali_data1 = 0x000F0000
    addr_cali_data2 = 0x000DB000
    p_file_size = 0x0100000
    # p_file_size = 0x0100
    f_rd_note = 'product_note_sta.txt'
    note_r = open(f_rd_note, 'r')
    f_ver = ''
    f_prj = ''
    f_rf = ''
    line = note_r.readline()
    while line:
        # print(line)

        part = line.partition('=')
        # print(part)
        if part[0] == 'type':
            f_type = part[-1]
            f_type = f_type.replace('\n', '')
            print(f_type)
            line_type = line
        if part[0] == 'bootloader' and f_type == 'eth':
            f_boot = part[-1]
            f_boot = f_boot.replace('\n', '')
            print(f_boot)
            line_boot = line
        if part[0] == 'prj':
            f_prj = part[-1]
            f_prj = f_prj.replace('\n', '')
            print(f_prj)
            line_prj = line
        if part[0] == 'rf':
            f_rf = part[-1]
            f_rf = f_rf.replace('\n', '')
            print(f_rf)
            line_rf = line
        if part[0] == 'firm_version' and f_type == 'eth':
            f_ver = part[-1]
            f_ver = f_ver.replace('\n', '')
            print(f_ver)
        if part[0] == 'firmware' and f_type == 'eth':
            f_firmware = part[-1]
            f_firmware = f_firmware.replace('\n', '')
            print(f_firmware)
        if part[0] == 'calibware' and f_type == 'eth':
            f_calib_code = part[-1]
            f_calib_code = f_calib_code.replace('\n', '')
            print(f_calib_code)
        if part[0] == 'calibdata1':
            f_calib_data1 = part[-1]
            f_calib_data1 = f_calib_data1.replace('\n', '')
            print(f_calib_data1)
            line_calib_data1 = line
        if part[0] == 'calibdata2':
            f_calib_data2 = part[-1]
            f_calib_data2 = f_calib_data2.replace('\n', '')
            print(f_calib_data2)
            line_calib_data2 = line
        line = note_r.readline()

    f_prfix = 'rom'
    # f_prj = '13r'
    # f_rf = '5p8'
    # f_ver = 'v5.4.67'
    # f_firmware = 'nft_13r_5p8_20220817_151724.bin'
    # f_calib_code = 'NPES13R-01-V01-crc.bin'
    # f_calib_data = '6683_40m_crc.bin'
    f_date = datetime.datetime.now()
    date_p = datetime.datetime.now().date()
    f_date_p = str(f_date)

    timeStr = time.strftime('%Y%m%d_%H%M%S', time.localtime())
    # print(timeStr)
    if f_type == 'eth':
        f_name = f_type + '_' + f_ver + '_' + f_prj + '_' + f_rf + '_' + timeStr
    else:
        f_name = f_type + '_' + f_prj + '_' + f_rf + '_' + timeStr
    f_name_bin = f_prfix + '_' + f_name + '.bin'
    f_note = 'note' + '_' + f_name + '.txt'
    path = 'pdt_' + f_name
    print(f_name)
    print(f_name_bin)
    print(f_note)
    path_output = './/out/'
    if os.path.exists(path_output) == False:
        os.makedirs(path_output)
    path = path_output + path
    source_path = path + '/' + 'source'
    os.makedirs(path)
    os.makedirs(source_path)
    if f_type == 'eth':
        shutil.copyfile(f_boot, source_path + '/' + f_boot)
        shutil.copyfile(f_firmware, source_path + '/' + f_firmware)
        shutil.copyfile(f_calib_code, source_path + '/' + f_calib_code)
    shutil.copyfile(f_calib_data1, source_path + '/' + f_calib_data1)
    shutil.copyfile(f_calib_data2, source_path + '/' + f_calib_data2)
    # f_name = 'product_13r_file'
    if f_type == 'eth':
        shutil.copyfile(f_rd_note, path + './' + f_note)
    else:
        notefile = open(path + './' + f_note, 'w+')
        notefile.write(line_type)
        notefile.write(line_rf)
        notefile.write(line_prj)
        notefile.write(line_calib_data1)
        notefile.write(line_calib_data2)
        notefile.close()

    product_file = open(path + './' + f_name_bin, 'wb')
    i = 0
    byte_val = b'\xff'
    # a = b'\xff'
    # b = a.to_bytes(1, 'big')
    # dummy_data=byte()
    # dummy_byte = dummy_data.to_bytes(1, byteorder='little', signed=True)
    while i < p_file_size:
        product_file.write(byte_val)
        i = i + 1
    # write dummy data for all file end
    # begin write bootloader
    if f_type == 'eth':
        product_file.seek(addr_boot, 0)
        bootloader = open('NL6683_bootloader_v1.03.bin', 'rb')
        for bt in bootloader:
            product_file.write(bt)
        bootloader.close()
        # wrtie bootlaoder end
        # begin write fireware
        product_file.seek(addr_firmware, 0)
        firmware = open(f_firmware, 'rb')
        for bt in firmware:
            product_file.write(bt)
        firmware.close()
        # write cali_code
        product_file.seek(addr_calil_code, 0)
        calib_code = open(f_calib_code, 'rb')
        for bt in calib_code:
            product_file.write(bt)
        calib_code.close()

    product_file.seek(addr_cali_data1, 0)
    calib_data = open(f_calib_data1, 'rb')
    for bt in calib_data:
        product_file.write(bt)
    calib_data.close()
    product_file.seek(addr_cali_data2, 0)
    calib_data = open(f_calib_data2, 'rb')
    for bt in calib_data:
        product_file.write(bt)
    calib_data.close()

    product_file.close()

    print('execute here')
    pass

from tkinter import *
from tkinter.messagebox import *
dir_out = '.\out\\'
file_boot = None
file_mtd1 = None
file_mtd2 = None
file_40m = None
file_20m = None
log_file = None

import time  # 引入time模块

# 格式化成2023-01-02 17:43:11形式

def wr_log(str):
    global  log_file
    f_time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_file.write(f_time1 + '   '+ str +'\n')
def op_boot(o_entry_addr_btld):
    global  dir_out
    global file_boot
    o_entry_addr_btld.delete(0, END)
    file_boot = askopenfilename(title='选择文件',filetypes=[('bootloader文件',"*.bin")])
    if file_boot == '':
        print('do not select bootloader file')
        pass
    else:
        filename = os.path.basename(file_boot)
        out_name = dir_out + filename
        shutil.copyfile(file_boot, out_name)
        o_entry_addr_btld.insert(0,file_boot)

def op_mtd1(o_entry_addr_mtd1):
    global  dir_out
    global file_mtd1
    o_entry_addr_mtd1.delete(0, END)
    file_mtd1 = askopenfilename(title='选择文件',filetypes=[('生产固件',"*.bin")])
    if file_mtd1 == '':
        print('do not select mtd1 file')
        pass
    else:
        filename = os.path.basename(file_mtd1)
        out_name = dir_out + filename
        shutil.copyfile(file_mtd1, out_name)
        o_entry_addr_mtd1.insert(0,file_mtd1)
def op_mtd2(o_entry_addr_mtd2):
    global  dir_out
    global file_mtd2
    o_entry_addr_mtd2.delete(0, END)
    file_mtd2 = askopenfilename(title='选择文件',filetypes=[('校准固件',"*.bin")])
    filename = os.path.basename(file_mtd2)
    out_name = dir_out + filename
    shutil.copyfile(file_mtd2, out_name)
    o_entry_addr_mtd2.insert(0,file_mtd2)
def op_40m(o_entry_addr_40m):
    global  dir_out
    global file_40m
    o_entry_addr_40m.delete(0, END)
    file_40m = askopenfilename(title='选择文件',filetypes=[('40m校准数据',"*.bin")])
    filename = os.path.basename(file_40m)
    out_name = dir_out + filename
    shutil.copyfile(file_40m, out_name)
    o_entry_addr_40m.insert(0,file_40m)
def op_20m(o_entry_addr_20m):
    global  dir_out
    global file_20m
    o_entry_addr_20m.delete(0, END)
    file_20m = askopenfilename(title='选择文件',filetypes=[('20m校准数据',"*.bin")])
    filename = os.path.basename(file_20m)
    out_name = dir_out + filename
    shutil.copyfile(file_20m, out_name)
    o_entry_addr_20m.insert(0,file_20m)
def eth_check(file_boot, file_mtd1, file_mtd2,file_40m,file_20m):
    if file_boot == '' or file_boot == None:
        showinfo('错误', '请选择BootLoader文件')
    else:
        print('bootload:' + file_boot)
        if file_mtd1 == '' or file_mtd1 == None:
            showinfo('错误', '请选择生产固件')
        else:
            print('生产固件:' + file_mtd1)
            if file_mtd2 == '' or file_mtd2 == None:
                showinfo('错误', '请选择校准固件')
            else:
                print('校准固件:' + file_mtd2)
                if file_40m == '' or file_40m == None:
                    showinfo('错误', '请选择40m校准数据')
                else:
                    print('40m校准数据:' + file_40m)
                    if file_20m == '' or file_20m == None:
                        showinfo('错误', '请选择20m校准数据')
                    else:
                        print('20m校准数据:' + file_20m)
def usb_check(file_40m,file_20m):
    wr_log('usb-检查输入文件')
    if file_40m == '' or file_40m == None:
        showinfo('错误', '请选择40m校准数据')
    else:
        print('40m校准数据:' + file_40m)
        if file_20m == '' or file_20m == None:
            showinfo('错误', '请选择20m校准数据')
        else:
            print('20m校准数据:' + file_20m)
    wr_log('usb-检查输入文件结束')
def etu_check(file_boot, file_mtd1):
    if file_boot == '' or file_boot == None:
        showinfo('错误', '请选择BootLoader文件')
    else:
        print('bootload:' + file_boot)
        if file_mtd1 == '' or file_mtd1 == None:
            showinfo('错误', '请选择生产固件')
        else:
            print('生产固件:' + file_mtd1)
            '''
            if file_mtd2 == '' or file_mtd2 == None:
                showinfo('错误', '请选择校准固件')
            else:
                print('校准固件:' + file_mtd2)
            '''
def file_check(sel_type, file_boot, file_mtd1, file_mtd2,file_40m,file_20m):
    choose = sel_type.get()
    if choose == 'sta_eth':
        eth_check(file_boot, file_mtd1, file_mtd2,file_40m,file_20m)
    if choose == 'sta_usb':
        usb_check(file_40m, file_20m)
    if choose == 'etu':
        etu_check(file_boot, file_mtd1)
def eth_gen(file_boot, file_mtd1, file_mtd2,file_40m,file_20m):
    timestr = time.strftime('%Y%m%d_%H%M%S', time.localtime())
    p_file_size = 0x0100000
    f_name_bin = 'pdt_eth_' + timestr + '.bin'

    path_output = './pdt_eth_' + timestr
    os.makedirs(path_output)
    product_file = open(path_output + './' + f_name_bin, 'wb')
    i = 0
    byte_val = b'\xff'
    while i < p_file_size:
        product_file.write(byte_val)
        i = i + 1
    addr_boot = 0x00000000
    addr_firmware = 0x00002000
    addr_calil_code = 0x00066000
    product_file.seek(addr_boot, 0)

    bootloader = open(file_boot, 'rb')
    for bt in bootloader:
        product_file.write(bt)
    bootloader.close()
    product_file.seek(addr_firmware, 0)
    f_firmware = file_mtd1
    firmware = open(f_firmware, 'rb')
    for bt in firmware:
        product_file.write(bt)
    firmware.close()
    # write cali_code
    f_calib_code = file_mtd2
    product_file.seek(addr_calil_code, 0)
    calib_code = open(f_calib_code, 'rb')
    for bt in calib_code:
        product_file.write(bt)
    calib_code.close()

    addr_cali_data1 = 0x000F0000
    addr_cali_data2 = 0x000DB000
    product_file.seek(addr_cali_data1, 0)
    f_calib_data1 = file_40m
    f_calib_data2 = file_20m
    calib_data = open(f_calib_data1, 'rb')
    for bt in calib_data:
        product_file.write(bt)
    calib_data.close()

    product_file.seek(addr_cali_data2, 0)
    calib_data = open(f_calib_data2, 'rb')
    for bt in calib_data:
        product_file.write(bt)
    calib_data.close()

    product_file.close()
    showinfo('成功', '制作rom结束')
    pass
def usb_gen(file_40m,file_20m):
    timestr = time.strftime('%Y%m%d_%H%M%S', time.localtime())
    p_file_size = 0x0100000
    f_name_bin = 'pdt_usb_' + timestr + '.bin'

    path_output = './pdt_usb_' + timestr
    os.makedirs(path_output)
    product_file = open(path_output + './' + f_name_bin, 'wb')
    i = 0
    byte_val = b'\xff'
    while i < p_file_size:
        product_file.write(byte_val)
        i = i + 1
    addr_cali_data1 = 0x000F0000
    addr_cali_data2 = 0x000DB000
    product_file.seek(addr_cali_data1, 0)
    f_calib_data1 = file_40m
    f_calib_data2 = file_20m
    calib_data = open(f_calib_data1, 'rb')
    for bt in calib_data:
        product_file.write(bt)
    calib_data.close()
    product_file.seek(addr_cali_data2, 0)
    calib_data = open(f_calib_data2, 'rb')
    for bt in calib_data:
        product_file.write(bt)
    calib_data.close()
    product_file.close()
    showinfo('成功', '制作rom结束')
    pass
def etu_gen(file_boot, file_mtd1):

    timestr = time.strftime('%Y%m%d_%H%M%S', time.localtime())
    p_file_size = 0x0100000
    addr_boot = 0x00000000
    addr_firmware = 0x00002000
    addr_calil_code = 0x00066000
    f_name_bin = 'pdt_etu_' + timestr + '.bin'

    path_output = './pdt_etu_' + timestr
    os.makedirs(path_output)
    product_file = open(path_output + './' + f_name_bin, 'wb')
    i = 0
    byte_val = b'\xff'
    while i < p_file_size:
        product_file.write(byte_val)
        i = i + 1
    product_file.seek(addr_boot, 0)
    bootloader = open(file_boot, 'rb')
    for bt in bootloader:
        product_file.write(bt)
    bootloader.close()
    product_file.seek(addr_firmware, 0)
    f_calib_code = f_firmware = file_mtd1
    firmware = open(f_firmware, 'rb')
    for bt in firmware:
        product_file.write(bt)
    firmware.close()
    # write cali_code
    product_file.seek(addr_calil_code, 0)
    calib_code = open(f_calib_code, 'rb')
    for bt in calib_code:
        product_file.write(bt)
    calib_code.close()
    product_file.close()
    showinfo('成功', '制作rom结束')
    pass
def make_rom(sel_type, file_boot, file_mtd1, file_mtd2,file_40m,file_20m):
    addr_boot = 0x00000000
    addr_firmware = 0x00002000
    addr_calil_code = 0x00066000
    addr_cali_data1 = 0x000F0000
    addr_cali_data2 = 0x000DB000
    p_file_size = 0x0100000
    choose = sel_type.get()

    if choose == 'sta_eth':
        eth_gen(file_boot, file_mtd1, file_mtd2, file_40m, file_20m)
    if choose == 'sta_usb':
        usb_gen(file_40m, file_20m)
    if choose == 'etu':
        etu_gen(file_boot, file_mtd1)

def rom_gen(win, sel_type, file_boot, file_mtd1, file_mtd2,file_40m,file_20m):
    file_check(sel_type, file_boot, file_mtd1, file_mtd2,file_40m,file_20m)
    make_rom(sel_type, file_boot, file_mtd1, file_mtd2,file_40m,file_20m)

def newgui():
    global file_boot
    global dir_out
    global file_mtd1
    global file_mtd2
    global file_40m
    global file_20m
    global  log_file
    win = Tk()
    win.title('6683-ROM-制作工具')
    win.geometry('800x250')
    sel_type = StringVar()
    sel_type.set('sta_eth')
    log_name = '.\log.txt'
    out_name = log_name
    log_file = open(out_name, 'w+')

    wr_log('write to log file')
    rd_tp1 = Radiobutton(win, variable=sel_type,value='sta_eth',text='sta-以太网')
    rd_tp2 = Radiobutton(win, variable=sel_type, value='sta_usb', text='sta-模组')
    rd_tp3 = Radiobutton(win, variable=sel_type, value='etu', text='etu')
    rd_tp1.grid(row = 60,column=0)
    rd_tp2.grid(row=60, column=1)
    rd_tp3.grid(row=60, column=2)
    txt_btld = 'Bootloader'
    txt_mtd1 = '分区1(生产固件)'
    txt_mtd2 = '分区2(校准固件)'
    #----------bootload label,entry,button
    o_lebel_btld = Label(win, text=txt_btld)
    o_lebel_btld.grid(row=1, column=0)
    addr_btld = 0x00000000
    o_entry_addr_btld = Entry(win,width=80)
    o_entry_addr_btld.grid(row=1, column=1)
    btn_boot = Button(win, text='浏览', command=lambda: op_boot(o_entry_addr_btld))
    btn_boot.grid(row=1, column=20)

    # ----------mtd1 label,entry,button
    o_lebel_mtd1 = Label(win, text=txt_mtd1)
    o_lebel_mtd1.grid(row=10,column=0)
    o_entry_addr_mtd1 = Entry(win, width=80)
    o_entry_addr_mtd1.grid(row=10, column=1)
    btn_mtd1 = Button(win, text='浏览', command=lambda: op_mtd1(o_entry_addr_mtd1))
    btn_mtd1.grid(row=10, column=20)


    o_lebel_mtd2 = Label(win, text=txt_mtd2)
    o_lebel_mtd2.grid(row=20,column=0)
    o_entry_addr_mtd2 = Entry(win, width=80)
    o_entry_addr_mtd2.grid(row=20, column=1)
    btn_mtd2 = Button(win, text='浏览', command=lambda: op_mtd2(o_entry_addr_mtd2))
    btn_mtd2.grid(row=20, column=20)


    txt_40m = '40m校准数据'
    txt_20m = '20m校准数据'

    o_lebel_40m = Label(win, text=txt_40m)
    o_lebel_40m.grid(row=30, column=0)
    o_entry_addr_40m = Entry(win, width=80)
    o_entry_addr_40m.grid(row=30, column=1)
    btn_40m = Button(win, text='浏览', command=lambda: op_40m(o_entry_addr_40m))
    btn_40m.grid(row=30, column=20)


    o_lebel_20m = Label(win, text=txt_20m)
    o_lebel_20m.grid(row=40, column=0)
    o_entry_addr_20m = Entry(win, width=80)
    o_entry_addr_20m.grid(row=40, column=1)
    btn_20m = Button(win, text='浏览', command=lambda: op_20m(o_entry_addr_20m))
    btn_20m.grid(row=40, column=20)


    bt_gen = Button(win,text='制作ROM',width=30,command=lambda:rom_gen(win,sel_type,file_boot, file_mtd1, file_mtd2,file_40m,file_20m))
    bt_gen.grid(row=90,column=1)


    win.mainloop()
if __name__ == '__main__':
    use_method = 2
    if use_method == 1:
        oldcode()
    else:
        newgui()





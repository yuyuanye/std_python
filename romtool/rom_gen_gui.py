# _*_ coding:UTF-8 _*_
import shutil
import sys, os
import datetime
import time
import re

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
def rom_gen():
    print('='*10 + 'genrom' + '='*10)
    pass

def newgui():
    win = Tk()
    win.geometry('800x600')

    txt_btld = 'Bootloader基地址:'
    txt_mtd1 = '分区1基地址:'
    txt_mtd2 = '分区2(校准固件)基地址:'
    o_lebel_btld = Label(win, text = txt_btld)
    o_lebel_btld.grid(row=0,column=0)
    addr_btld = 0x00000000
    o_entry_addr_btld = Entry(win)
    o_entry_addr_btld.grid(row=0,column=1)
    o_entry_addr_btld.insert(0,str(addr_btld))

    o_lebel_mtd1 = Label(win, text=txt_mtd1)
    o_lebel_mtd1.grid(row=1,column=0)
    o_lebel_mtd2 = Label(win, text=txt_mtd2)
    o_lebel_mtd2.grid(row=2,column=0)

    txt_40m = '40m校准数据基地址:'
    txt_20m = '20m校准数据基地址:'

    o_lebel_40m = Label(win, text=txt_40m)
    o_lebel_40m.grid(row=3, column=0)

    o_lebel_20m = Label(win, text=txt_20m)
    o_lebel_20m.grid(row=4, column=0)

    bt_gen = Button(win,text='制作ROM',command=rom_gen)
    bt_gen.grid(row=10,column=20)
    win.mainloop()
if __name__ == '__main__':
    use_method = 2
    if use_method == 1:
        oldcode()
    else:
        newgui()





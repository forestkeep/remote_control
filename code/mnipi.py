import serial

PUSH_MENU = 1
PUSH_RIGHT = b''
PUSH_Z = b''
PUSH_R = b''
PUSH_DOWN = b''
PUSH_ENTER = b''
PUSH_UP = b''
PUSH_L = b''
PUSH_CALL = b''
PUSH_LEFT = b''
PUSH_I = b''
PUSH_C = b''
CHANGE_SHIFT=b''
CHANGE_FREQ=  ''
CHANGE_LEVEL=b''
CHANGE_RANGE = b''  # = 
client = serial.Serial("COM16", 9600, timeout=1)

client.write(CHANGE_RANGE)
'''
Прибор принимает однобайтные команды соответствующие нажатию клавиш управления:
0х0 – Меню;
0х1 – Вправо;
0х2 – Z/;
0х3 – режим R;
0х4 – Вниз;
0х5 – Ввод;
0х6 – Вверх;
0х7 – режим L;
0х8 – калибровка;
0х9 – Влево;
0хА – режим I;
0хВ – режим С;
0хС – изменение смещения;
0хD – изменение частоты;
0xE – изменение уровня сигнала;
0xF – изменение поддиапазона.

'''

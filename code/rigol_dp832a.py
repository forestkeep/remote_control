from pymodbus.client import ModbusSerialClient
from interface.set_power_supply_window import Ui_Set_power_supply
from PyQt5.QtCore import QTimer, QDateTime
from Classes import ch_response_to_step, base_device, ch_response_to_step, base_ch
from power_supply_class import power_supply


class ch_power_supply_class(base_ch):
    def __init__(self, number, device_class) -> None:
        super().__init__(number)
        self.base_duration_step = 0.1#у каждого канала каждого прибора есть свое время. необходимое для выполнения шага
        self.steps_current = []
        self.steps_voltage = []
        self.max_current = 5
        self.max_voltage = 30
        self.max_power = 300
        self.min_step_V = 0.001
        self.min_step_A = 0.001
        self.min_step_W = 1
        self.dict_buf_parameters["type_of_work"] = "Стабилизация напряжения"
        self.dict_buf_parameters["type_step"] = "Заданный шаг"
        self.dict_buf_parameters["high_limit"] = str(10)
        self.dict_buf_parameters["low_limit"] = str(self.min_step_V)
        self.dict_buf_parameters["step"] = "2"
        self.dict_buf_parameters["second_value"] = str(self.max_current)
        self.dict_buf_parameters["repeat_reverse"] = False


class rigol_dp832a_class(power_supply):
    def __init__(self, name,installation_class) -> None:
        super().__init__(name, "serial", installation_class)
        self.ch1 = ch_power_supply_class(1, self)
        self.ch2 = ch_power_supply_class(2, self)
        self.ch3 = ch_power_supply_class(3, self)
        self.channels = [self.ch1, self.ch2, self.ch3]
        self.ch1.is_active = True#по умолчанию для каждого прибора включен первый канал
        self.active_channel = self.ch1 #поле необходимо для записи параметров при настройке в нужный канал

    def _set_voltage(self,ch_num, voltage) -> bool:
        '''установить значение напряжения канала'''
        self.open_port()
        self.select_channel(ch_num)
        self.client.write(f'VOLT {voltage}\n'.encode())
        self.client.write(f'VOLT?\n'.encode())
        response = self.client.readline().decode().strip()
        try:
            response = float(response)
        except:
            response = False
        self.client.close()
        return  response == voltage

    def _set_current(self,ch_num, current) -> bool: 
        '''установить значение тока канала'''
        self.open_port()
        self.select_channel(ch_num)
        self.client.write(f'CURR {current}\n'.encode())
        self.client.write(f'CURR?\n'.encode())
        response = self.client.readline().decode().strip()
        try:
            response = float(response)
        except:
            response = False
        self.client.close()
        return  response == current

    def _output_switching_on(self,ch_num) -> bool:
        '''включить канал'''
        self.open_port()
        self.client.write(f'OUTP CH{ch_num},ON\n'.encode())
        self.client.close()

    def _output_switching_off(self, ch_num) -> bool:
        '''выключить канал'''
        self.open_port()
        self.client.write(f'OUTP CH{ch_num},OFF\n'.encode())
        self.client.close()

    def _get_current_voltage(self, ch_num) -> float:
        '''возвращает значение установленного напряжения канала'''
        self.open_port()
        self.select_channel(ch_num)
        self.client.write(f'MEAS:VOLT?\n'.encode())
        response = self.client.readline().decode().strip()
        try:
            response = float(response)
        except:
            response = False
        self.client.close()
        return  response

    def _get_current_current(self, ch_num) -> float:
        '''возвращает значение измеренного тока канала'''
        self.open_port()
        self.select_channel(ch_num)
        self.client.write(f'MEAS:CURR?\n'.encode())
        response = self.client.readline().decode().strip()
        try:
            response = float(response)
        except:
            response = False
        self.client.close()
        return  response

    def _get_setting_voltage(self, ch_num) -> float:
        '''возвращает значение установленного напряжения канала'''
        self.open_port()
        self.select_channel(ch_num)
        self.client.write(f'VOLT?\n'.encode())
        response = self.client.readline().decode().strip()
        try:
            response = float(response)
        except:
            response = False
        self.client.close()
        return  response

    def _get_setting_current(self, ch_num) -> float:
        '''возвращает значение установленного тока канала'''
        self.open_port()
        self.select_channel(ch_num)
        self.client.write(f'CURR?\n'.encode())
        response = self.client.readline().decode().strip()
        try:
            response = float(response)
        except:
            response = False
        self.client.close()
        return   response

    def _get_setting_state(self, ch_num) -> bool:
        '''возвращает состояние канала вкл(true) или выкл(false)'''
        pass

    def open_port(self):
        if self.client.is_open == False:
            self.client.open()

    def select_channel(self, channel):
        self.open_port()
        self.client.write(f'INST CH{channel}\n'.encode())
        


if __name__ == "__main__":
    print("тестирование ригола")
    rt = 0

    rigol = rigol_dp832a_class("rigol", rt)
    rigol.show_setting_window(rt)

 
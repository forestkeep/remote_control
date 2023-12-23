from maisheng_power_class import maisheng_power_class


# сюда добавляются классы всех устройств в системе вместе с ключами
dict_device_class = {"Maisheng": maisheng_power_class}


class device:
    """device parameters"""

    def __init__(self, model, type_of_connection, protocol) -> None:
        self.model = model
        self.type_of_connection = type_of_connection
        self.protocol = protocol

    def get_model(self) -> str:
        return self.model


class powersupply(device):
    def __init__(self, model, type_of_connection, protocol, number_of_channel):
        super().__init__(model, type_of_connection, protocol)
        self.number_of_channel = number_of_channel


if __name__ == "__main__":
    lst = powersupply("maisheng", "COM", "modbus", 1)

    print(lst.get_model())

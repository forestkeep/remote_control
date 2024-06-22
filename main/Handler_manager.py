import enum


#разработка управляющего событиями.
#задачи: сбор информации о составе установки и анализ на возможные события
#выдача по запросу списка событий
#анализ состояния во время эксперимента и выдача наступивших событий
#события срабатывания таймера включать или нет?

'''
события:
	общие:
		прибор произвел действие
		прибор закончил измерения
	

'''
class expEvents(enum.Enum):
	action_done = 1#сделано действие прибора
	end_meas = 2#прибор закончил работу
	half_meas_done = 3#половина измерений прибора произведена
	action_after_half_meas_done = 4#сделано действие прибора при условии, что половина действий уже совершена
	timer_expired = 5#истекло время таймера



class eventsManager():
	def __init__(self) -> None:
		pass
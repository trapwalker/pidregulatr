import tinytuya

DEVICE_ID = 'id_вашего_устройства'
LOCAL_KEY = 'ваш_local_key'
IP_ADDRESS = 'ip_адрес_устройства'

# Создание экземпляра устройства
device = tinytuya.OutletDevice(DEVICE_ID, IP_ADDRESS, LOCAL_KEY)

# Установка версии протокола (по умолчанию 3.3)
device.set_version(3.3)

# Включение устройства
device.turn_on()

# Выключение устройства
device.turn_off()

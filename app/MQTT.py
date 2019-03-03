import logging

from paho.mqtt.client import Client


class MQTT:
    client = None

    def __init__(self, client_id: str = 'raspberry005', clean_session: bool = True,
                 auto_connect: bool = True, **kwargs):
        self.client = Client(client_id=client_id, clean_session=clean_session, **kwargs)
        self.client.on_message = self._on_message
        if auto_connect:
            self.connect(host='iot.eclipse.org')

    def connect(self, host: str, port: int = 1883, keepalive: int = 60, **kwargs):
        is_connected = self.client.connect(host=host, port=port, keepalive=keepalive, **kwargs)
        if is_connected in range(3):
            logging.info('Successful connect')
            return True
        raise ConnectionError(f'MQTT connection error id {is_connected}')

    def _on_message(self, client, userdata, msg):
        logging.info(f'{msg.topic} {msg.payload!s}')

    def pulish(self, topic: str, payload: str = None, retain: bool = False, **kwargs):
        message_info = self.client.publish(topic=topic, payload=payload, retain=retain, **kwargs)
        message_info.wait_for_publish()
        if message_info.is_published():
            logging.info(f'Successful published message "{msg}" to topic {topic}')
            return True
        logging.info(f'Publishing error for message "{msg}" to topic {topic}')
        return False

    def __del__(self):
        self.client.disconnect()

from time import sleep


def fake_db():
    try:
        print('Conectando no banco de dados')
        sleep(2)
    finally:
        print('Desconectando do banco de dados')
        sleep(1)
        
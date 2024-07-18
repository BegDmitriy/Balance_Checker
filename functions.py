import web3
from config import *
from web3 import Web3


def get_wallets(file_path: str = "data/wallets.txt") -> list[str]:
    """
    Читает файл с адресами кошельков и возвращает список адресов.

    Args:
        file_path (str): Путь к файлу с кошельками. По умолчанию "data/wallets.txt".

    Returns:
        list[str]: Список адресов кошельков.
    """
    with open(file_path) as f:
        wallets = f.read().split('\n')
    return [wallet.strip() for wallet in wallets if wallet.strip()]


def checker_balance(chain_id, wallets):
    """
    Проверяет балансы кошельков в указанной блокчейн-сети и сохраняет результаты в файл.

    Args:
        chain_id (str): Идентификатор сети.
        wallets (list[str]): Список адресов кошельков.

    Returns:
        None
    """
    # Получаем конфигурацию сети из словаря NETWORKS
    network = NETWORKS[chain_id]

    # Создаем объект Web3 для взаимодействия с блокчейном через публичный RPC
    w3 = Web3(web3.HTTPProvider(network['rpc']))

    # Проверяем подключение к сети
    if not w3.is_connected():
        print(f"Не удалось подключиться к сети {network['name']}")
        return

    total_balance = 0  # Инициализируем общую сумму балансов
    balances = []  # Список для хранения балансов кошельков

    # Проходим по каждому кошельку в списке
    for index_of_wallet, wallet in enumerate(wallets):
        # Преобразуем адрес кошелька в формат checksum
        check_sum = w3.to_checksum_address(wallet)

        # Получаем баланс кошелька в минимальных единицах (Wei)
        balance = w3.eth.get_balance(check_sum)

        # Преобразуем баланс в удобочитаемый формат (Ether)
        readable_balance = round(balance / (10 ** 18), 4)

        # Добавляем адрес кошелька и его баланс в список
        balances.append((check_sum, readable_balance))

        # Увеличиваем общую сумму балансов
        total_balance += readable_balance

        # Выводим информацию о текущем кошельке и его балансе
        print(f'{index_of_wallet}. {check_sum} - {readable_balance} - {network['symbol']}')

    # Убедимся, что директория "data" существует
    os.makedirs("data", exist_ok=True)

    # Записываем балансы кошельков в файл
    with open(f'data/{network['name']}.txt', 'w') as f:
        for check_sum, balance in balances:
            f.write(f'{check_sum} - {balance} {network['symbol']} \n')

    # Выводим итоговую информацию
    print(f'Кошельков проверено: {len(wallets)}')
    print(f'Суммарный баланс в сети {network['name']}: {round(total_balance, 4)} {network['symbol']}')
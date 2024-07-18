# Конфигурация для различных сетей с публичными RPC
# Этот словарь содержит параметры для каждой поддерживаемой сети:
# - 'name': Название сети
# - 'rpc': URL публичного RPC-сервера для взаимодействия с сетью
# - 'symbol': Символ основной криптовалюты этой сети (например, ETH для Ethereum)
NETWORKS = {
    '1': {'name': 'Ethereum', 'rpc': 'https://rpc.ankr.com/eth', 'symbol': 'ETH'},
    '2': {'name': 'Arbitrum', 'rpc': 'https://arb1.arbitrum.io/rpc', 'symbol': 'ETH'},
    '3': {'name': 'Optimism', 'rpc': 'https://mainnet.optimism.io', 'symbol': 'ETH'},
    '4': {'name': 'zkSync', 'rpc': 'https://mainnet.era.zksync.io', 'symbol': 'ETH'},
    '5': {'name': 'BSC', 'rpc': 'https://bsc-dataseed.binance.org/', 'symbol': 'BNB'},
    '6': {'name': 'Polygon', 'rpc': 'https://polygon-rpc.com', 'symbol': 'MATIC'},
    '7': {'name': 'Avalanche', 'rpc': 'https://avalanche-c-chain-rpc.publicnode.com', 'symbol': 'AVAX'},
    '8': {'name': 'Linea', 'rpc': 'https://1rpc.io/linea', 'symbol': 'ETH'},
    '9': {'name': 'Scroll', 'rpc': 'https://scroll.drpc.org', 'symbol': 'ETH'},
    '10': {'name': 'Base', 'rpc': 'https://mainnet.base.org', 'symbol': 'ETH'}
}
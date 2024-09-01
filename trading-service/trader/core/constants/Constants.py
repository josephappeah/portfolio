import logging


class Constants:
    ConfigFilePath = "configs/config.dev.cfg"
    LoggingFormat = '%(asctime)s.%(msecs)06dZ | %(levelname)s | %(name)s | %(message)s'
    LoggingLevel = logging.DEBUG
    LoggingDateFormat = '%Y-%m-d%T%H:%M:%S'


class ConfigConstants:
    WebSocketServerSection = "WebSocketServer"
    ConnectionSection = "Connection"
    WebSocketsSection = "WebSocket"
    GatewayServerSection = "GatewayServer"
    PricingSection = "Pricing"
    TradeServerSection = "TradeServer"

    # Server
    ServerHostKey = "host"
    ServerPortKey = "port"

    # Connection
    ConnectionNamePrefixKey = "connectionnameprefix"
    MaxAllowedConnections = "maxallowedconnections"

    # Web Sockets
    WebSocketConnectionNamePrefix = "websocketconnectionnameprefix"
    WebSocketConnectionTimeout = "websocketconnectiontimeout"

    # Gateway Server
    GatewayServerHost = "gatewayserverhost"
    GatewayServerPort = "gatewayserverport"
    GatewayServerLinux = "gatewayserverlinux"
    GatewayServerWindows = "gatewayserverwindows"

    # Pricing
    PricingConfigDelimiter = "pricingconfigdelimiter"
    PricingAssetConfigDelimiter = "pricingassetconfigdelimiter"
    PricingFxConfig = "pricingfxconfig"
    PriceFrequency = "pricefrequency"

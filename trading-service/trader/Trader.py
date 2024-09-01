import logging
import nest_asyncio
from trader.TraderModule import TraderModule
from trader.core.constants.Constants import Constants

logging.basicConfig(format=Constants.LoggingFormat, level=Constants.LoggingLevel, datefmt=Constants.LoggingDateFormat)
logger = logging.getLogger(__name__)
nest_asyncio.apply()

tsm = TraderModule()
tsm.start()

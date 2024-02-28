from enum import Enum
from typing import Optional, List

from espn_api_orm.consts import ESPNSportTypes
from espn_api_orm.generic.api import ESPNBaseAPI
from espn_api_orm.generic.schema import BaseType
from espn_api_orm.sport.schema import Sport


class ESPNSportAPI(ESPNBaseAPI):
    """
    ESPN Sport API for retrieving sport information.

    Attributes:

    Methods:
    """

    def __init__(self, sport: ESPNSportTypes):
        """
        Initialize ESPNSportAPI.
        """
        super().__init__()
        self.sport: ESPNSportTypes = sport

    def get_sport(self):
        return Sport(**self.api_request(f"{self._core_url}/{self.sport.value}"))

    def get_leagues(self,return_values = True):
        res = BaseType(**self.api_request(f"{self._core_url}/{self.sport.value}/leagues?limit=200"))
        if not return_values:
            return res
        return self._get_values(f"{self._core_url}/{self.sport.value}/leagues", res.items)
import requests
import pandas as pd
import geopandas as gpd


class InvalidInputError(Exception):
    def __init__(self, message) -> None:
    """Executes when there is an invalid input

    :param message: Message to be displayed
    :type message: str

    """
        super().__init__(message)


class ambee:
    """Base class to initialize credentials"""

    def __init__(self, x_api_key) -> None:
        """Initializes parameters required for API to function

        Args:
            x_api_key (str): Ambee api key
        """
        self.x_api_key = x_api_key

    def multiple_calls(
        self,
        func,
        by,
        lat_lngs=None,
        postalCodes=None,
        countryCodes=None,
        cities=None,
        places=None,
        **func_kwargs,
    ):
        """Function to make multiple api calls for a list of inputs.

        :param func: Function to make multiple calls on.
        :type func: function
        :param by: by value to be passed to the function
        :type by: str
        :param lat_lngs: list of pairs of latitudes and longitudes. Defaults to None.
        :type lat_lngs: list
        :param postalCodes: list of postal codes and corresponding country codes. Defaults to None.
        :type postalCodes: list
        :param countryCodes: list of country codes for by country-code api call. Defaults to None.
        :type countryCodes: list
        :param cities: list of cities. Defaults to None.
        :type cities: list
        :param places: list of places. Defaults to None.
        :type places: list
        :param parallel: Makes requests in parallel if True. Defaults to False.
        :type parallel: bool
        :param **func_kwargs: 
        :returns: list of api responses in dictionary or pandas DataFrame format
        :rtype: outputs
        :raises InvalidInputError: Executes when there is an invalid input

        """
        if by == "latlng":
            if lat_lngs == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                outputs = []
                for lat, lng in lat_lngs:
                    output = func(by=by, lat=lat, lng=lng, **func_kwargs)
                    outputs.append(output)
                return outputs

        if by == "postcode":
            if postalCodes == None:
                raise InvalidInputError(
                    "The call is missing either postalCode or countryCode value"
                )
            else:
                outputs = []
                for postalCode, countryCode in postalCodes:
                    output = func(
                        by=by,
                        postalCode=postalCode,
                        countryCode=countryCode,
                        **func_kwargs,
                    )
                    outputs.append(output)
                return outputs
        if by == "city":
            if cities == None:
                raise InvalidInputError("The call is missing city value")
            else:
                outputs = []
                for city in cities:
                    output = func(by=by, city=city, **func_kwargs)
                    outputs.append(output)
                return outputs
        if by == "countrycode":
            if countryCodes == None:
                raise InvalidInputError("The call is missing countryCode value")
            else:
                outputs = []
                for countryCode in countryCodes:
                    output = func(by=by, countryCode=countryCode, **func_kwargs)
                    outputs.append(output)
                return outputs
        if by == "place":
            if places == None:
                raise InvalidInputError("The call is missing place value")
            else:
                outputs = []
                for place in places:
                    output = func(by=by, place=place, **func_kwargs)
                    outputs.append(output)
                return outputs

    def to_geodataframe(self, df, x="lng", y="lat"):
        """_summary_

        :param df: Pandas DataFrame
        :type df: DataFrame
        :param x: Name of longitude column. Defaults to 'lng'.
        :type x: str
        :param y: Name of latitude column. Defaults to 'lat'.
        :type y: str
        :returns: geopandas GeoDataFrame
        :rtype: GeoDataFrame

        """
        return gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(x=df[x], y=df[y]))


class air_quality(ambee):
    """Contains methods to fetch data from Air Quality API"""

    def get_latest(
        self,
        by,
        lat=None,
        lng=None,
        postalCode=None,
        countryCode=None,
        city=None,
        limit=None,
        return_df=False,
    ):
        """Retrives latest Air Quality data for a given location

        :param by: str
        :param lat: float (Default value = None)
        :param lng: float (Default value = None)
        :param postalCode: int (Default value = None)
        :param countryCode: str (Default value = None)
        :param city: str (Default value = None)
        :param limit: int (Default value = None)
        :param return_df: bool (Default value = False)
        :returns: dict: API response in dictionary format
        :raises InvalidInputError: Raised when the input to query is invalid
        :raises e: Any exception that occurs during api call and data parsing

        """
        base_url = "https://api.ambeedata.com/latest/"
        if by == "latlng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-lat-lng?lat={}&lng={}".format(lat, lng)
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json(), record_path=["stations"], errors="ignore"
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e

        if by == "postcode":
            if postalCode == None or countryCode == None:
                raise InvalidInputError(
                    "The call is missing either postalCode or countryCode value"
                )
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = (
                        base_url
                        + "by-postal-code?postalCode={}&countryCode={}".format(
                            postalCode, countryCode
                        )
                    )
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json(), record_path=["stations"], errors="ignore"
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e

        if by == "city":
            if city == None:
                raise InvalidInputError("The call is missing city value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-city?city={}".format(city)
                    if limit is not None:
                        url = url + "&limit={}".format(limit)
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json(), record_path=["stations"], errors="ignore"
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e

        if by == "countrycode":
            if countryCode == None:
                raise InvalidInputError("The call is missing countryCode value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-country-code?countryCode={}".format(
                        countryCode
                    )
                    if limit is not None:
                        url = url + "&limit={}".format(limit)
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json(), record_path=["stations"], errors="ignore"
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e

    def get_historical(
        self,
        by,
        from_val,
        to_val,
        lat=None,
        lng=None,
        postalCode=None,
        countryCode=None,
        return_df=False,
    ):
        """Retrives historical Air Quality data for a given location

        :param by: str
        :param from_val: str
        :param to_val: _type_
        :param lat: float (Default value = None)
        :param lng: float (Default value = None)
        :param postalCode: int (Default value = None)
        :param countryCode: str (Default value = None)
        :param return_df: bool (Default value = False)
        :returns: dict: API response in dictionary format
        :raises InvalidInputError: Raised when the input to query is invalid
        :raises e: Any exception that occurs during api call and data parsing

        """
        base_url = "https://api.ambeedata.com/history/"
        if by == "latlng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-lat-lng?lat={}&lng={}&from={}&to={}".format(
                        lat, lng, from_val, to_val
                    )
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json(), record_path=["data"], errors="ignore"
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)
        if by == "postcode":
            if postalCode == None or countryCode == None:
                raise InvalidInputError(
                    "The call is missing either postalCode or countryCode value"
                )
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = (
                        base_url
                        + "by-postal-code?postalCode={}&countryCode={}&from={}&to={}".format(
                            postalCode, countryCode, from_val, to_val
                        )
                    )
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json(), record_path=["data"], errors="ignore"
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e

    def get_analytics(self, by="order", order="worst", return_df=False):
        """Get Air Quality Analytics

        :param by: str (Default value = "order")
        :param order: str (Default value = "worst")
        :param return_df: bool (Default value = False)
        :returns: dict: API response in dictionary format
        :raises InvalidInputError: Raised when the input to query is invalid
        :raises e: Any exception that occurs during api call and data parsing

        """
        base_url = "https://api.ambeedata.com/latest/"
        if by == "order":
            if order == None:
                raise InvalidInputError("The call is missing order value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-order/{}".format(order)
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json(), record_path=["stations"], errors="ignore"
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e


class pollen(ambee):
    """Contains methods to fetch data from Pollen API"""

    def get_latest(
        self, by, lat=None, lng=None, place=None, speciesRisk=False, return_df=False
    ):
        """Retrives latest pollen data for a given location

        :param by: str
        :param lat: float (Default value = None)
        :param lng: float (Default value = None)
        :param place: str (Default value = None)
        :param speciesRisk: bool (Default value = False)
        :param return_df: bool (Default value = False)
        :returns: dict: API response in dictionary format
        :raises InvalidInputError: Raised when the input to query is invalid
        :raises e: Any exception that occurs during api call and data parsing

        """
        base_url = "https://api.ambeedata.com/latest/pollen/"
        if by == "latlng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-lat-lng?lat={}&lng={}&speciesRisk={}".format(
                        lat, lng, speciesRisk
                    )
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json(),
                            record_path=["data"],
                            meta=["lat", "lng"],
                            errors="ignore",
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e
        if by == "place":
            if place == None:
                raise InvalidInputError("The call is missing place value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-place?place={}&speciesRisk={}".format(
                        place, speciesRisk
                    )
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json(),
                            record_path=["data"],
                            meta=["lat", "lng"],
                            errors="ignore",
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e

    def get_historical(
        self,
        by,
        from_val,
        to_val,
        lat=None,
        lng=None,
        place=None,
        speciesRisk=False,
        return_df=False,
    ):
        """Retrives historical pollen data for a given location

        :param by: str
        :param from_val: str
        :param to_val: _type_
        :param lat: float (Default value = None)
        :param lng: float (Default value = None)
        :param place: str (Default value = None)
        :param return_df: bool (Default value = False)
        :param speciesRisk:  (Default value = False)
        :returns: dict: API response in dictionary format
        :raises InvalidInputError: Raised when the input to query is invalid
        :raises e: Any exception that occurs during api call and data parsing

        """
        base_url = "https://api.ambeedata.com/history/pollen/"
        if by == "latlng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = (
                        base_url
                        + "by-lat-lng?lat={}&lng={}&from={}&to={}&speciesRisk={}".format(
                            lat, lng, from_val, to_val, speciesRisk
                        )
                    )
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json(),
                            record_path=["data"],
                            meta=["lat", "lng"],
                            errors="ignore",
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e
        if by == "place":
            if place == None:
                raise InvalidInputError("The call is missing place value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = (
                        base_url
                        + "by-place?place={}&from={}&to={}&speciesRisk={}".format(
                            place, from_val, to_val, speciesRisk
                        )
                    )
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json(),
                            record_path=["data"],
                            meta=["lat", "lng"],
                            errors="ignore",
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e

    def get_forecast(
        self, by, lat=None, lng=None, place=None, speciesRisk=False, return_df=False
    ):
        """Retrives forecasted pollen data for a given location

        :param by: str
        :param lat: float (Default value = None)
        :param lng: float (Default value = None)
        :param place: str (Default value = None)
        :param return_df: bool (Default value = False)
        :param speciesRisk:  (Default value = False)
        :returns: dict: API response in dictionary format
        :raises InvalidInputError: Raised when the input to query is invalid
        :raises e: Any exception that occurs during api call and data parsing

        """
        base_url = "https://api.ambeedata.com/forecast/pollen/"
        if by == "latlng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-lat-lng?lat={}&lng={}&speciesRisk={}".format(
                        lat, lng, speciesRisk
                    )
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json(),
                            record_path=["data"],
                            meta=["lat", "lng"],
                            errors="ignore",
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e
        if by == "place":
            if place == None:
                raise InvalidInputError("The call is missing place value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-place?place={}&speciesRisk={}".format(
                        place, speciesRisk
                    )
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json(),
                            record_path=["data"],
                            meta=["lat", "lng"],
                            errors="ignore",
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e


class weather(ambee):
    """Contains methods to fetch data from Weather API"""

    def get_latest(self, by, lat=None, lng=None, units=None, return_df=False):
        """Retrives latest weather data for a given location

        :param by: str
        :param lat: float (Default value = None)
        :param lng: float (Default value = None)
        :param units: str (Default value = None)
        :param return_df: bool (Default value = False)
        :returns: dict: API response in dictionary format
        :raises InvalidInputError: Raised when the input to query is invalid
        :raises e: Any exception that occurs during api call and data parsing

        """
        base_url = "https://api.ambeedata.com/weather/latest/"
        if by == "latlng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-lat-lng?lat={}&lng={}".format(lat, lng)
                    if units is not None:
                        url = url + "&units={}".format(units)
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json()["data"], errors="ignore"
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e

    def get_historical(
        self,
        by,
        from_val,
        to_val,
        lat=None,
        lng=None,
        daily=False,
        units=None,
        return_df=False,
    ):
        """Retrives historical weather data for a given location

        :param by: str
        :param from_val: str
        :param to_val: _type_
        :param lat: float (Default value = None)
        :param lng: float (Default value = None)
        :param daily: bool (Default value = False)
        :param units: str (Default value = None)
        :param return_df: bool (Default value = False)
        :returns: dict: API response in dictionary format
        :raises InvalidInputError: Raised when the input to query is invalid
        :raises e: Any exception that occurs during api call and data parsing

        """
        base_url = "https://api.ambeedata.com/weather/history/"
        if by == "latlng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    if daily == True:
                        base_url = base_url + "daily/"
                    url = base_url + "by-lat-lng?lat={}&lng={}&from={}&to={}".format(
                        lat, lng, from_val, to_val
                    )
                    if units is not None:
                        url = url + "&units={}".format(units)
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json()["data"],
                            record_path=["history"],
                            meta=["lat", "lng"],
                            errors="ignore",
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e

    def get_forecast(
        self, by, lat=None, lng=None, daily=False, units=None, return_df=False
    ):
        """Retrives forecasted weather data for a given location

        :param by: str
        :param lat: float (Default value = None)
        :param lng: float (Default value = None)
        :param daily: bool (Default value = False)
        :param units: str (Default value = None)
        :param return_df: bool (Default value = False)
        :returns: dict: API response in dictionary format
        :raises InvalidInputError: Raised when the input to query is invalid
        :raises e: Any exception that occurs during api call and data parsing

        """
        base_url = "https://api.ambeedata.com/weather/forecast/"
        if by == "latlng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    if daily == True:
                        base_url = base_url + "daily/"
                    url = base_url + "by-lat-lng?lat={}&lng={}".format(lat, lng)
                    if units is not None:
                        url = url + "&units={}".format(units)
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json()["data"],
                            record_path=["forecast"],
                            meta=["lat", "lng"],
                            errors="ignore",
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e

    def get_severe_weather(
        self, by, lat=None, lng=None, place=None, units=None, return_df=False
    ):
        """Gets severe weather data for a given location

        :param by: str
        :param lat: float (Default value = None)
        :param lng: float (Default value = None)
        :param place: str (Default value = None)
        :param units: str (Default value = None)
        :param return_df: bool (Default value = False)
        :returns: dict: API response in dictionary format
        :raises InvalidInputError: Raised when the input to query is invalid
        :raises e: Any exception that occurs during api call and data parsing

        """
        base_url = "https://api.ambeedata.com/weather/alerts/latest/"
        if by == "latlng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-lat-lng?lat={}&lng={}".format(lat, lng)
                    if units is not None:
                        url = url + "&units={}".format(units)
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json(), record_path=["data"], errors="ignore"
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e

        if by == "place":
            if place == None:
                raise InvalidInputError("The call is missing place value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-place?place={}".format(place)
                    if units is not None:
                        url = url + "&units={}".format(units)
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json(), record_path=["data"], errors="ignore"
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e


class fire(ambee):
    """Contains methods to fetch data from Fire API"""

    def get_latest(
        self,
        by,
        lat=None,
        lng=None,
        place=None,
        coordinates=None,
        burnedAreaLoc=False,
        type=None,
        return_df=False,
    ):
        """Retrives latest fire data for a given location

        :param by: str
        :param lat: float (Default value = None)
        :param lng: float (Default value = None)
        :param place: str (Default value = None)
        :param coordinates: list (Default value = None)
        :param burnedAreaLoc: bool (Default value = False)
        :param type: str (Default value = None)
        :param return_df: bool (Default value = False)
        :returns: dict: API response in dictionary format
        :raises InvalidInputError: Raised when the input to query is invalid
        :raises e: Any exception that occurs during api call and data parsing

        """
        base_url = "https://api.ambeedata.com/fire/v2/latest/"
        if by == "latlng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-lat-lng?lat={}&lng={}&burnedAreaLoc={}".format(
                        lat, lng, burnedAreaLoc
                    )
                    if type is not None:
                        url = url + "type={}".format(type)
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        try:
                            return pd.json_normalize(
                                response.json(), record_path=["result"], errors="ignore"
                            )
                        except:
                            print("Cannot convert to df")
                            return response.json()
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e

        if by == "polygon":
            if coordinates == None:
                raise InvalidInputError("The call is missing coordinates")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    body = {"coordinates": coordinates}
                    url = base_url + "by-polygon?burnedAreaLoc={}".format(burnedAreaLoc)
                    if type is not None:
                        url = url + "type={}".format(type)
                    response = requests.post(
                        url,
                        headers=headers,
                        json=body,
                    )
                    if return_df == True:
                        try:
                            return pd.json_normalize(
                                response.json(), record_path=["result"], errors="ignore"
                            )
                        except:
                            print("Cannot convert to df")
                            return response.json()
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e

        if by == "place":
            if place == None:
                raise InvalidInputError("The call is missing place value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-place?place={}&burnedAreaLoc={}".format(
                        place, burnedAreaLoc
                    )
                    if type is not None:
                        url = url + "type={}".format(type)
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        try:
                            return pd.json_normalize(
                                response.json(), record_path=["result"], errors="ignore"
                            )
                        except:
                            print("Cannot convert to df")
                            return response.json()
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e

    def get_forcast(
        self,
        by,
        lat=None,
        lng=None,
        return_df=False,
    ):
        """Retrives fire danger forecasr for a given location

        :param by: _type_
        :param lat: _type_ (Default value = None)
        :param lng: _type_ (Default value = None)
        :param return_df: bool (Default value = False)
        :returns: dict: API response in dictionary format
        :raises InvalidInputError: Raised when the input to query is invalid
        :raises e: Any exception that occurs during api call and data parsing

        """
        base_url = "https://api.ambeedata.com/fire/v2/forecast/"
        if by == "latlng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-lat-lng?lat={}&lng={}".format(lat, lng)
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        try:
                            return pd.json_normalize(
                                response.json(), record_path=["result"], errors="ignore"
                            )
                        except:
                            print("Cannot convert to df")
                            return response.json()
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e


class ndvi(ambee):
    """Contains methods to fetch data from NDVI API"""

    def get_latest(self, by, lat=None, lng=None, return_df=False):
        """Retrives latest ndvi data for a given location

        :param by: str
        :param lat: float (Default value = None)
        :param lng: float (Default value = None)
        :param return_df: bool (Default value = False)
        :returns: dict: API response in dictionary format
        :raises InvalidInputError: Raised when the input to query is invalid
        :raises e: Any exception that occurs during api call and data parsing

        """
        base_url = "https://api.ambeedata.com/ndvi/latest/"
        if by == "latlng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-lat-lng?lat={}&lng={}".format(lat, lng)
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        return pd.json_normalize(
                            response.json(), record_path=["data"], errors="ignore"
                        )
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e


class natural_disaster(ambee):
    """Contains methods to fetch data from NDVI API"""

    def get_latest(
        self,
        by,
        lat=None,
        lng=None,
        alertLevel=None,
        continent=None,
        eventType=None,
        return_df=False,
    ):
        """Retrives latest disasters data for a given location

        :param by: str
        :param lat: float (Default value = None)
        :param lng: float (Default value = None)
        :param alertLevel: str (Default value = None)
        :param continent: str (Default value = None)
        :param eventType: str (Default value = None)
        :param return_df: bool (Default value = False)
        :returns: dict: API response in dictionary format
        :raises InvalidInputError: Raised when the input to query is invalid
        :raises e: Any exception that occurs during api call and data parsing

        """
        base_url = "https://api.ambeedata.com/disasters/latest/"
        if by == "latlng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-lat-lng?lat={}&lng={}".format(lat, lng)
                    if alertLevel is not None:
                        url = url + "&alertLevel={}".format(alertLevel)
                    if continent is not None:
                        url = url + "&continent={}".format(continent)
                    if eventType is not None:
                        url = url + "&eventType={}".format(eventType)
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        try:
                            return pd.json_normalize(
                                response.json(), record_path=["result"], errors="ignore"
                            )
                        except:
                            print("Cannot convert to df")
                            return response.json()
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e

    def get_historical(
        self,
        by,
        from_val,
        to_val,
        lat=None,
        lng=None,
        alertLevel=None,
        continent=None,
        eventType=None,
        return_df=False,
    ):
        """Retrives historical disasters data for a given location

        :param by: str
        :param from_val: str
        :param to_val: _type_
        :param lat: float (Default value = None)
        :param lng: float (Default value = None)
        :param alertLevel: str (Default value = None)
        :param continent: str (Default value = None)
        :param eventType: str (Default value = None)
        :param return_df: bool (Default value = False)
        :returns: dict: API response in dictionary format
        :raises InvalidInputError: Raised when the input to query is invalid
        :raises e: Any exception that occurs during api call and data parsing

        """
        base_url = "https://api.ambeedata.com/disasters/history/"
        if by == "latlng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    url = base_url + "by-lat-lng?lat={}&lng={}&from={}&to={}".format(
                        lat,
                        lng,
                        from_val,
                        to_val,
                    )
                    if alertLevel is not None:
                        url = url + "&alertLevel={}".format(alertLevel)
                    if continent is not None:
                        url = url + "&continent={}".format(continent)
                    if eventType is not None:
                        url = url + "&eventType={}".format(eventType)
                    response = requests.get(url, headers=headers)
                    if return_df == True:
                        try:
                            return pd.json_normalize(
                                response.json(), record_path=["result"], errors="ignore"
                            )
                        except:
                            print("Cannot convert to df")
                            return response.json()
                    else:
                        return response.json()
                except Exception as e:
                    print(response.status_code)
                    raise e

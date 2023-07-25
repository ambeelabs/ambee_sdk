import requests
import pandas as pd
import geopandas as gpd


class InvalidInputError(Exception):
    def __init__(self, message) -> None:
        """Executes when there is an invalid input

        Args:
            message (str): Message to be displayed
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

        Args:
            func (function): Function to make multiple calls on.
            by (str): by value to be passed to the function
            lat_lngs (list, optional): list of pairs of latitudes and longitudes. Defaults to None.
            postalCodes (list, optional): list of postal codes and corresponding country codes. Defaults to None.
            countryCodes (list, optional): list of country codes for by country-code api call. Defaults to None.
            cities (list, optional): list of cities. Defaults to None.
            places (list, optional): list of places. Defaults to None.
            parallel (bool, optional): Makes requests in parallel if True. Defaults to False.

        Raises:
            InvalidInputError: Executes when there is an invalid input

        Returns:
            outputs: list of api responses in dictionary or pandas DataFrame format
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

        Args:
            df (DataFrame): Pandas DataFrame
            x (str, optional): Name of longitude column. Defaults to 'lng'.
            y (str, optional): Name of latitude column. Defaults to 'lat'.

        Returns:
            GeoDataFrame: geopandas GeoDataFrame
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

        Args:
            by (str): signifies the type of input supported by Ambee API. Refer to API Documentation.
            lat (float/int/str, optional): Latitude. Defaults to None.
            lng (float/int/str, optional): Longitude. Defaults to None.
            postalCode (int/str, optional): Post Code. Defaults to None.
            countryCode (str, optional): Two letter ISO Code for the country. Defaults to None.
            city (str, optional): Name of the city. Defaults to None.
            limit (int, optional): Parameter to limit query results. Defaults to None.
            return_df (bool, optional): Converts results to pandas dataframe if True. Defaults to False.

        Raises:
            InvalidInputError: Raised when the input to query is invalid
            e: Any exception that occurs during api call and data parsing

        Returns:
            dict: API response in dictionary format
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

        Args:
            by (str): signifies the type of input supported by Ambee API. Refer to API Documentation.
            from_val (str): Start timestamp for historical query
            to_val (_type_): End timestamp for historical query
            lat (float/int/str, optional): Latitude. Defaults to None.
            lng (float/int/str, optional): Longitude. Defaults to None.
            postalCode (int/str, optional): Post Code. Defaults to None.
            countryCode (str, optional): Two letter ISO Code for the country. Defaults to None.
            return_df (bool, optional): Converts results to pandas dataframe if True. Defaults to False.

        Raises:
            InvalidInputError: Raised when the input to query is invalid
            e: Any exception that occurs during api call and data parsing

        Returns:
            dict: API response in dictionary format
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

        Args:
            by (str, optional): signifies the type of input supported by Ambee API. Refer to API Documentation. Defaults to "order".
            order (str, optional): Order by worst or best. Defaults to "worst".
            return_df (bool, optional): Converts results to pandas dataframe if True. Defaults to False.

        Raises:
            InvalidInputError: Raised when the input to query is invalid
            e: Any exception that occurs during api call and data parsing

        Returns:
            dict: API response in dictionary format
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

        Args:
            by (str): signifies the type of input supported by Ambee API. Refer to API Documentation.
            lat (float/int/str, optional): Latitude. Defaults to None.
            lng (float/int/str, optional): Longitude. Defaults to None.
            place (str, optional): Placename. Defaults to None.
            speciesRisk (bool, optional): Gives risk for species if True
            return_df (bool, optional): Converts results to pandas dataframe if True. Defaults to False.

        Raises:
            InvalidInputError: Raised when the input to query is invalid
            e: Any exception that occurs during api call and data parsing

        Returns:
            dict: API response in dictionary format
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

        Args:
            by (str): signifies the type of input supported by Ambee API. Refer to API Documentation.
            from_val (str): Start timestamp for historical query
            to_val (_type_): End timestamp for historical query
            lat (float/int/str, optional): Latitude. Defaults to None.
            lng (float/int/str, optional): Longitude. Defaults to None.
            place (str, optional): Placename. Defaults to None.
            return_df (bool, optional): Converts results to pandas dataframe if True. Defaults to False.

        Raises:
            InvalidInputError: Raised when the input to query is invalid
            e: Any exception that occurs during api call and data parsing

        Returns:
            dict: API response in dictionary format
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

        Args:
            by (str): signifies the type of input supported by Ambee API. Refer to API Documentation.
            lat (float/int/str, optional): Latitude. Defaults to None.
            lng (float/int/str, optional): Longitude. Defaults to None.
            place (str, optional): Placename. Defaults to None.
            return_df (bool, optional): Converts results to pandas dataframe if True. Defaults to False.

        Raises:
            InvalidInputError: Raised when the input to query is invalid
            e: Any exception that occurs during api call and data parsing

        Returns:
            dict: API response in dictionary format
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

        Args:
            by (str): signifies the type of input supported by Ambee API. Refer to API Documentation.
            lat (float/int/str, optional): Latitude. Defaults to None.
            lng (float/int/str, optional): Longitude. Defaults to None.
            units (str, optional): Gives data in metric units if 'si' is passed. Defaults to None.
            return_df (bool, optional): Converts results to pandas dataframe if True. Defaults to False.

        Raises:
            InvalidInputError: Raised when the input to query is invalid
            e: Any exception that occurs during api call and data parsing

        Returns:
            dict: API response in dictionary format
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

        Args:
            by (str): signifies the type of input supported by Ambee API. Refer to API Documentation.
            from_val (str): Start timestamp for historical query
            to_val (_type_): End timestamp for historical query
            lat (float/int/str, optional): Latitude. Defaults to None.
            lng (float/int/str, optional): Longitude. Defaults to None.
            daily (bool, optional): Gives daily aggregate if True. Defaults to False.
            units (str, optional): Gives data in metric units if 'si' is passed. Defaults to None.
            return_df (bool, optional): Converts results to pandas dataframe if True. Defaults to False.

        Raises:
            InvalidInputError: Raised when the input to query is invalid
            e: Any exception that occurs during api call and data parsing

        Returns:
            dict: API response in dictionary format
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

        Args:
            by (str): signifies the type of input supported by Ambee API. Refer to API Documentation.
            lat (float/int/str, optional): Latitude. Defaults to None.
            lng (float/int/str, optional): Longitude. Defaults to None.
            daily (bool, optional): Gives daily aggregate if True. Defaults to False.
            units (str, optional): Gives data in metric units if 'si' is passed. Defaults to None.
            return_df (bool, optional): Converts results to pandas dataframe if True. Defaults to False.

        Raises:
            InvalidInputError: Raised when the input to query is invalid
            e: Any exception that occurs during api call and data parsing

        Returns:
            dict: API response in dictionary format
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

        Args:
            by (str): signifies the type of input supported by Ambee API. Refer to API Documentation.
            lat (float/int/str, optional): Latitude. Defaults to None.
            lng (float/int/str, optional): Longitude. Defaults to None.
            place (str, optional): Placename. Defaults to None.
            units (str, optional): Gives data in metric units if 'si' is passed. Defaults to None.
            return_df (bool, optional): Converts results to pandas dataframe if True. Defaults to False.

        Raises:
            InvalidInputError: Raised when the input to query is invalid
            e: Any exception that occurs during api call and data parsing

        Returns:
            dict: API response in dictionary format
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

        Args:
            by (str): signifies the type of input supported by Ambee API. Refer to API Documentation.
            lat (float/int/str, optional): Latitude. Defaults to None.
            lng (float/int/str, optional): Longitude. Defaults to None.
            burnedAreaLoc (bool, optional): Burned area polygon locations
            type (str,optional): The type of fire (Reported Fire/ Detected Fire)
            return_df (bool, optional): Converts results to pandas dataframe if True. Defaults to False.

        Raises:
            InvalidInputError: Raised when the input to query is invalid
            e: Any exception that occurs during api call and data parsing

        Returns:
            dict: API response in dictionary format
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
                                response.json(), record_path=["data"], errors="ignore"
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
                                response.json(), record_path=["data"], errors="ignore"
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
                                response.json(), record_path=["data"], errors="ignore"
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
                                response.json(), record_path=["data"], errors="ignore"
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

        Args:
            by (str): signifies the type of input supported by Ambee API. Refer to API Documentation.
            lat (float/int/str, optional): Latitude. Defaults to None.
            lng (float/int/str, optional): Longitude. Defaults to None.
            return_df (bool, optional): Converts results to pandas dataframe if True. Defaults to False.

        Raises:
            InvalidInputError: Raised when the input to query is invalid
            e: Any exception that occurs during api call and data parsing

        Returns:
            dict: API response in dictionary format
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

        Args:
            by (str): signifies the type of input supported by Ambee API. Refer to API Documentation.
            lat (float/int/str, optional): Latitude. Defaults to None.
            lng (float/int/str, optional): Longitude. Defaults to None.
            return_df (bool, optional): Converts results to pandas dataframe if True. Defaults to False.

        Raises:
            InvalidInputError: Raised when the input to query is invalid
            e: Any exception that occurs during api call and data parsing

        Returns:
            dict: API response in dictionary format
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
                        return pd.json_normalize(
                            response.json(), record_path=["data"], errors="ignore"
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
        alertLevel=None,
        continent=None,
        eventType=None,
        return_df=False,
    ):
        """Retrives historical disasters data for a given location

        Args:
            by (str): signifies the type of input supported by Ambee API. Refer to API Documentation.
            from_val (str): Start timestamp for historical query
            to_val (_type_): End timestamp for historical query
            lat (float/int/str, optional): Latitude. Defaults to None.
            lng (float/int/str, optional): Longitude. Defaults to None.
            place (str, optional): Placename. Defaults to None.
            return_df (bool, optional): Converts results to pandas dataframe if True. Defaults to False.

        Raises:
            InvalidInputError: Raised when the input to query is invalid
            e: Any exception that occurs during api call and data parsing

        Returns:
            dict: API response in dictionary format
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

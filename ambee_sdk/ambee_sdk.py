import requests


class InvalidInputError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class ambee:
    def __init__(self, x_api_key) -> None:
        self.x_api_key = x_api_key


class air_quality(ambee):
    def get_latest(
        self,
        by,
        lat=None,
        lng=None,
        postalCode=None,
        countryCode=None,
        city=None,
        limit=None,
    ):
        if by == "lat-lng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    response = requests.get(
                        "https://api.ambeedata.com/latest/by-lat-lng?lat={}&lng={}".format(
                            lat, lng
                        ),
                        headers=headers,
                    )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)

        if by == "postal-code":
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
                    response = requests.get(
                        "https://api.ambeedata.com/latest/by-postal-code?postalCode={}&countryCode={}".format(
                            postalCode, countryCode
                        ),
                        headers=headers,
                    )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)

        if by == "city":
            if city == None:
                raise InvalidInputError("The call is missing city value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    if limit == None:
                        response = requests.get(
                            "https://api.ambeedata.com/latest/by-city?city={}".format(
                                city
                            ),
                            headers=headers,
                        )
                    else:
                        response = requests.get(
                            "https://api.ambeedata.com/latest/by-city?city={}&limit={}".format(
                                city, limit
                            ),
                            headers=headers,
                        )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)

        if by == "country-code":
            if countryCode == None:
                raise InvalidInputError("The call is missing countryCode value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    if limit == None:
                        response = requests.get(
                            "https://api.ambeedata.com/latest/by-country-code?countryCode={}".format(
                                countryCode
                            ),
                            headers=headers,
                        )
                    else:
                        response = requests.get(
                            "https://api.ambeedata.com/latest/by-country-code?countryCode={}&limit={}".format(
                                countryCode, limit
                            ),
                            headers=headers,
                        )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)

    def get_historical(
        self,
        by,
        from_val,
        to_val,
        lat=None,
        lng=None,
        postalCode=None,
        countryCode=None,
    ):
        if by == "lat-lng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    response = requests.get(
                        "https://api.ambeedata.com/history/by-lat-lng?lat={}&lng={}&from={}&to={}".format(
                            lat, lng, from_val, to_val
                        ),
                        headers=headers,
                    )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)
        if by == "postal-code":
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
                    response = requests.get(
                        "https://api.ambeedata.com/history/by-postal-code?postalCode={}&countryCode={}&from={}&to={}".format(
                            postalCode, countryCode, from_val, to_val
                        ),
                        headers=headers,
                    )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)

    def get_analytics(self, by="order", order="worst"):
        if by == "order":
            if order == None:
                raise InvalidInputError("The call is missing order value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    response = requests.get(
                        "https://api.ambeedata.com/latest/by-order/{}".format(order),
                        headers=headers,
                    )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)


class pollen(ambee):
    def get_latest(self, by, lat=None, lng=None, place=None):
        if by == "lat-lng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    response = requests.get(
                        "https://api.ambeedata.com/latest/pollen/by-lat-lng?lat={}&lng={}".format(
                            lat, lng
                        ),
                        headers=headers,
                    )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)
        if by == "place":
            if place == None:
                raise InvalidInputError("The call is missing place value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    response = requests.get(
                        "https://api.ambeedata.com/latest/pollen/by-place?place={}".format(
                            place
                        ),
                        headers=headers,
                    )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)

    def get_historical(self, by, from_val, to_val, lat=None, lng=None, place=None):
        if by == "lat-lng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    response = requests.get(
                        "https://api.ambeedata.com/history/pollen/by-lat-lng?lat={}&lng={}&from={}&to={}".format(
                            lat, lng, from_val, to_val
                        ),
                        headers=headers,
                    )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)
        if by == "place":
            if place == None:
                raise InvalidInputError("The call is missing place value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    response = requests.get(
                        "https://api.ambeedata.com/history/pollen/by-place?place={}&from={}&to={}".format(
                            place, from_val, to_val
                        ),
                        headers=headers,
                    )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)

    def get_forecast(self, by, lat=None, lng=None, place=None):
        if by == "lat-lng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    response = requests.get(
                        "https://api.ambeedata.com/forecast/pollen/by-lat-lng?lat={}&lng={}".format(
                            lat, lng
                        ),
                        headers=headers,
                    )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)
        if by == "place":
            if place == None:
                raise InvalidInputError("The call is missing place value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    response = requests.get(
                        "https://api.ambeedata.com/forecast/pollen/by-place?place={}".format(
                            place
                        ),
                        headers=headers,
                    )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)


class weather(ambee):
    def get_latest(self, by, lat=None, lng=None, units=None):
        if by == "lat-lng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    if units != None:
                        response = requests.get(
                            "https://api.ambeedata.com/weather/latest/by-lat-lng?lat={}&lng={}&units={}".format(
                                lat, lng, units
                            ),
                            headers=headers,
                        )
                    else:
                        response = requests.get(
                            "https://api.ambeedata.com/weather/latest/by-lat-lng?lat={}&lng={}".format(
                                lat, lng
                            ),
                            headers=headers,
                        )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)

    def get_historical(
        self, by, from_val, to_val, lat=None, lng=None, daily=False, units=None
    ):
        if by == "lat-lng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    if daily == True:
                        if units != None:
                            response = requests.get(
                                "https://api.ambeedata.com/weather/history/daily/by-lat-lng?lat={}&lng={}&from={}&to={}&units={}".format(
                                    lat, lng, from_val, to_val, units
                                ),
                                headers=headers,
                            )
                        else:
                            response = requests.get(
                                "https://api.ambeedata.com/weather/history/daily/by-lat-lng?lat={}&lng={}&from={}&to={}".format(
                                    lat, lng, from_val, to_val
                                ),
                                headers=headers,
                            )
                    else:
                        if units != None:
                            response = requests.get(
                                "https://api.ambeedata.com/weather/history/by-lat-lng?lat={}&lng={}&from={}&to={}&units={}".format(
                                    lat, lng, from_val, to_val, units
                                ),
                                headers=headers,
                            )
                        else:
                            response = requests.get(
                                "https://api.ambeedata.com/weather/history/by-lat-lng?lat={}&lng={}&from={}&to={}".format(
                                    lat, lng, from_val, to_val
                                ),
                                headers=headers,
                            )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)

    def get_forecast(self, by, lat=None, lng=None, daily=False, units=None):
        if by == "lat-lng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    if daily == True:
                        if units != None:
                            response = requests.get(
                                "https://api.ambeedata.com/weather/forecast/daily/by-lat-lng?lat={}&lng={}&units={}".format(
                                    lat, lng, units
                                ),
                                headers=headers,
                            )
                        else:
                            response = requests.get(
                                "https://api.ambeedata.com/weather/forecast/daily/by-lat-lng?lat={}&lng={}".format(
                                    lat, lng
                                ),
                                headers=headers,
                            )
                    else:
                        if units != None:
                            response = requests.get(
                                "https://api.ambeedata.com/weather/forecast/by-lat-lng?lat={}&lng={}&units={}".format(
                                    lat, lng, units
                                ),
                                headers=headers,
                            )
                        else:
                            response = requests.get(
                                "https://api.ambeedata.com/weather/forecast/by-lat-lng?lat={}&lng={}".format(
                                    lat, lng
                                ),
                                headers=headers,
                            )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)

    def get_severe_weather(self, by, lat=None, lng=None, place=None, units=None):
        if by == "lat-lng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    if units != None:
                        response = requests.get(
                            "https://api.ambeedata.com/weather/alerts/latest/by-lat-lng?lat={}&lng={}&units={}".format(
                                lat, lng, units
                            ),
                            headers=headers,
                        )
                    else:
                        response = requests.get(
                            "https://api.ambeedata.com/weather/alerts/latest/by-lat-lng?lat={}&lng={}".format(
                                lat, lng
                            ),
                            headers=headers,
                        )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)

        if by == "place":
            if place == None:
                raise InvalidInputError("The call is missing place value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    if units != None:
                        response = requests.get(
                            "https://api.ambeedata.com/weather/alerts/latest/by-place?place={}&units={}".format(
                                place, units
                            ),
                            headers=headers,
                        )
                    else:
                        response = requests.get(
                            "https://api.ambeedata.com/weather/alerts/latest/by-place?place={}".format(
                                place
                            ),
                            headers=headers,
                        )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)


class fire(ambee):
    def get_latest(self, by, lat=None, lng=None, place=None):
        if by == "lat-lng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    response = requests.get(
                        "https://api.ambeedata.com/latest/fire?lat={}&lng={}".format(
                            lat, lng
                        ),
                        headers=headers,
                    )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)

        if by == "place":
            if place == None:
                raise InvalidInputError("The call is missing place value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    response = requests.get(
                        "https://api.ambeedata.com/latest/fire/by-place?place={}".format(
                            place
                        ),
                        headers=headers,
                    )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)


class ndvi(ambee):
    def get_latest(self, by, lat=None, lng=None, place=None):
        if by == "lat-lng":
            if lat == None or lng == None:
                raise InvalidInputError("The call is missing either lat or lng value")
            else:
                try:
                    headers = {
                        "x-api-key": self.x_api_key,
                        "Content-type": "application/json",
                    }
                    response = requests.get(
                        "https://api.ambeedata.com/ndvi/latest/by-lat-lng?lat={}&lng={}".format(
                            lat, lng
                        ),
                        headers=headers,
                    )
                    return response.json()
                except Exception as e:
                    print(e)
                    print(response.status_code)

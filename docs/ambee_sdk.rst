
ambee_sdk package
*****************

The examples mentioned in the documentation is also part of examples
jupyter notebook present in the github repo, So feel free to download
it and play with it.


Submodules
==========


ambee_sdk.ambee_sdk module
==========================

.. py:class:: ambee_sdk.ambee_sdk.InvalidInputError(message)

   Bases: ``Exception``
   Executes when there is an invalid input

   :param message: Message to be displayed
   :type message: str
   

.. py:class:: ambee_sdk.ambee_sdk.ambee(x_api_key)**

   Bases: ``object``

   Base class to initialize credentials

   .. py:function:: multiple_calls(func, by, lat_lngs=None, postalCodes=None,countryCodes=None, cities=None, places=None, **func_kwargs)

      Function to make multiple api calls for a list of inputs.

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

   .. py:function:: to_geodataframe(df, x='lng', y='lat')

      Utility function to convert to GeoDataFrame

      :param df: Pandas DataFrame
      :type df: DataFrame
      :param x: Name of longitude column. Defaults to 'lng'.
      :type x: str
      :param y: Name of latitude column. Defaults to 'lat'.
      :type y: str
      :returns: geopandas GeoDataFrame
      :rtype: GeoDataFrame


.. py:class:: ambee_sdk.ambee_sdk.air_quality(x_api_key)**

   Bases: `ambee <#ambee_sdk.ambee_sdk.ambee>`_

   Contains methods to fetch data from Air Quality API

   .. py:function:: get_analytics(by='order', order='worst', return_df=False)

      Get Air Quality Analytics

      :param by: str (Default value = "order")
      :param order: str (Default value = "worst")
      :param return_df: bool (Default value = False)
      :returns: dict: API response in dictionary format
      :raises InvalidInputError: Raised when the input to query is invalid
      :raises e: Any exception that occurs during api call and data parsing

   .. py:function:: get_historical(by, from_val, to_val, lat=None, lng=None,postalCode=None, countryCode=None, return_df=False)

      Retrives historical Air Quality data for a given location

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

   .. py:function:: get_latest(by, lat=None, lng=None, postalCode=None,countryCode=None, city=None, limit=None, return_df=False)

      Retrives latest Air Quality data for a given location

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

.. py:class:: ambee_sdk.ambee_sdk.fire(x_api_key)

   Bases: `ambee <#ambee_sdk.ambee_sdk.ambee>`_

   Contains methods to fetch data from Fire API

   .. py:function:: get_latest(self,by,lat=None,lng=None,place=None,coordinates=None,burnedAreaLoc=False,type=None,return_df=False)

      Retrives latest fire data for a given location

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

   .. py:function:: get_forcast(self,by,lat=None,lng=None,return_df=False)

      Retrives latest fire data for a given location

      :param by: _type_
      :param lat: _type_ (Default value = None)
      :param lng: _type_ (Default value = None)
      :param return_df: bool (Default value = False)
      :returns: dict: API response in dictionary format
      :raises InvalidInputError: Raised when the input to query is invalid
      :raises e: Any exception that occurs during api call and data parsing

.. py:class:: ambee_sdk.ambee_sdk.ndvi(x_api_key)

   Bases: `ambee <#ambee_sdk.ambee_sdk.ambee>`_

   Contains methods to fetch data from NDVI API

   .. py:function:: get_latest(by, lat=None, lng=None, return_df=False)

      Retrives latest ndvi data for a given location

      :param by: str
      :param lat: float (Default value = None)
      :param lng: float (Default value = None)
      :param return_df: bool (Default value = False)
      :returns: dict: API response in dictionary format
      :raises InvalidInputError: Raised when the input to query is invalid
      :raises e: Any exception that occurs during api call and data parsing


.. py:class:: ambee_sdk.ambee_sdk.pollen(x_api_key)

   Bases: `ambee <#ambee_sdk.ambee_sdk.ambee>`_

   Contains methods to fetch data from Pollen API

   .. py:function:: get_forecast(by, lat=None, lng=None, place=None,return_df=False)

      Retrives forecasted pollen data for a given location

      :param by: str
      :param lat: float (Default value = None)
      :param lng: float (Default value = None)
      :param place: str (Default value = None)
      :param return_df: bool (Default value = False)
      :param speciesRisk:  (Default value = False)
      :returns: dict: API response in dictionary format
      :raises InvalidInputError: Raised when the input to query is invalid
      :raises e: Any exception that occurs during api call and data parsing

   .. py:function:: get_historical(by, from_val, to_val, lat=None, lng=None,place=None, return_df=False)

      Retrives historical pollen data for a given location

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

   .. py:function:: get_latest(by, lat=None, lng=None, place=None, return_df=False)

      Retrives latest pollen data for a given location

      :param by: str
      :param lat: float (Default value = None)
      :param lng: float (Default value = None)
      :param place: str (Default value = None)
      :param speciesRisk: bool (Default value = False)
      :param return_df: bool (Default value = False)
      :returns: dict: API response in dictionary format
      :raises InvalidInputError: Raised when the input to query is invalid
      :raises e: Any exception that occurs during api call and data parsing

.. py:class:: ambee_sdk.ambee_sdk.weather(x_api_key)**

   Bases: `ambee <#ambee_sdk.ambee_sdk.ambee>`_

   Contains methods to fetch data from Weather API

   .. py:function:: get_forecast(by, lat=None, lng=None, daily=False, units=None,return_df=False)

      Retrives forecasted weather data for a given location

      :param by: str
      :param lat: float (Default value = None)
      :param lng: float (Default value = None)
      :param daily: bool (Default value = False)
      :param units: str (Default value = None)
      :param return_df: bool (Default value = False)
      :returns: dict: API response in dictionary format
      :raises InvalidInputError: Raised when the input to query is invalid
      :raises e: Any exception that occurs during api call and data parsing

   .. py:function:: get_historical(by, from_val, to_val, lat=None, lng=None,daily=False, units=None, return_df=False)

      Retrives historical weather data for a given location

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


   .. py:function:: get_latest(by, lat=None, lng=None, units=None, return_df=False)

      Retrives latest weather data for a given location

      :param by: str
      :param lat: float (Default value = None)
      :param lng: float (Default value = None)
      :param units: str (Default value = None)
      :param return_df: bool (Default value = False)
      :returns: dict: API response in dictionary format
      :raises InvalidInputError: Raised when the input to query is invalid
      :raises e: Any exception that occurs during api call and data parsing


   .. py:function:: get_severe_weather(by, lat=None, lng=None, place=None,units=None, return_df=False)

      Gets severe weather data for a given location

      :param by: str
      :param lat: float (Default value = None)
      :param lng: float (Default value = None)
      :param place: str (Default value = None)
      :param units: str (Default value = None)
      :param return_df: bool (Default value = False)
      :returns: dict: API response in dictionary format
      :raises InvalidInputError: Raised when the input to query is invalid
      :raises e: Any exception that occurs during api call and data parsing


.. py:class:: ambee_sdk.ambee_sdk.natural_disaster(x_api_key)

   Bases: `ambee <#ambee_sdk.ambee_sdk.ambee>`_

   Contains methods to fetch data from Disasters API

   .. py:function:: get_latest(self,by,lat=None,lng=None,alertLevel=None,continent=None,eventType=None,return_df=False)

      Retrives latest disasters data for a given location

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
   

   .. py:function:: get_historical(self,by,from_val,to_val,lat=None,lng=None,alertLevel=None,continent=None,eventType=None,return_df=False)

      Retrives historical disasters data for a given location

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


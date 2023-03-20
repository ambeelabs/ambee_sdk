
ambee_sdk package
*****************

The examples mentioned in the documentation is also part of examples
jupyter notebook present in the github repo, So feel free to download
it and play with it.


Submodules
==========


ambee_sdk.ambee_sdk module
==========================

.. py:class:: ambee_sdk.ambee_sdk.InvalidInputError(message)**

   Bases: ``Exception``

.. py:class:: ambee_sdk.ambee_sdk.air_quality(x_api_key)**

   Bases: `ambee <#ambee_sdk.ambee_sdk.ambee>`_

   Contains methods to fetch data from Air Quality API

   .. py:function:: get_analytics(by='order', order='worst', return_df=False)**

      Get Air Quality Analytics

      :Parameters:
         *  **by** (*str**, **optional*) – signifies the type of input
            supported by Ambee API. Refer to API Documentation.
            Defaults to “order”.

         *  **order** (*str**, **optional*) – Order by worst or best.
            Defaults to “worst”.

         *  **return_df** (*bool**, **optional*) – Converts results to
            pandas dataframe if True. Defaults to False.

      :Raises:
         *  `InvalidInputError
            <#ambee_sdk.ambee_sdk.InvalidInputError>`_ – Raised when
            the input to query is invalid

         *  **e** – Any exception that occurs during api call and data
            parsing

      :Returns:
         API response in dictionary format

      :Return type:
         dict

   .. py:function:: get_historical(by, from_val, to_val, lat=None, lng=None,
   postalCode=None, countryCode=None, return_df=False)**

      Retrives historical Air Quality data for a given location

      :Parameters:
         *  **by** (*str*) – signifies the type of input supported by
            Ambee API. Refer to API Documentation.

         *  **from_val** (*str*) – Start timestamp for historical
            query

         *  **to_val** (*_type_*) – End timestamp for historical query

         *  **lat** (*float/int/str**, **optional*) – Latitude.
            Defaults to None.

         *  **lng** (*float/int/str**, **optional*) – Longitude.
            Defaults to None.

         *  **postalCode** (*int/str**, **optional*) – Post Code.
            Defaults to None.

         *  **countryCode** (*str**, **optional*) – Two letter ISO
            Code for the country. Defaults to None.

         *  **return_df** (*bool**, **optional*) – Converts results to
            pandas dataframe if True. Defaults to False.

      :Raises:
         *  `InvalidInputError
            <#ambee_sdk.ambee_sdk.InvalidInputError>`_ – Raised when
            the input to query is invalid

         *  **e** – Any exception that occurs during api call and data
            parsing

      :Returns:
         API response in dictionary format

      :Return type:
         dict

   .. py:function:: get_latest(by, lat=None, lng=None, postalCode=None,
   countryCode=None, city=None, limit=None, return_df=False)**

      Retrives latest Air Quality data for a given location

      :Parameters:
         *  **by** (*str*) – signifies the type of input supported by
            Ambee API. Refer to API Documentation.

         *  **lat** (*float/int/str**, **optional*) – Latitude.
            Defaults to None.

         *  **lng** (*float/int/str**, **optional*) – Longitude.
            Defaults to None.

         *  **postalCode** (*int/str**, **optional*) – Post Code.
            Defaults to None.

         *  **countryCode** (*str**, **optional*) – Two letter ISO
            Code for the country. Defaults to None.

         *  **city** (*str**, **optional*) – Name of the city.
            Defaults to None.

         *  **limit** (*int**, **optional*) – Parameter to limit query
            results. Defaults to None.

         *  **return_df** (*bool**, **optional*) – Converts results to
            pandas dataframe if True. Defaults to False.

      :Raises:
         *  `InvalidInputError
            <#ambee_sdk.ambee_sdk.InvalidInputError>`_ – Raised when
            the input to query is invalid

         *  **e** – Any exception that occurs during api call and data
            parsing

      :Returns:
         API response in dictionary format

      :Return type:
         dict

.. py:class:: ambee_sdk.ambee_sdk.ambee(x_api_key)**

   Bases: ``object``

   Base class to initialize credentials

   .. py:function:: multiple_calls(func, by, lat_lngs=None, postalCodes=None,
   countryCodes=None, cities=None, places=None, **func_kwargs)**

      Function to make multiple api calls for a list of inputs.

      :Parameters:
         *  **func** (*function*) – Function to make multiple calls
            on.

         *  **by** (*str*) – by value to be passed to the function

         *  **lat_lngs** (*list**, **optional*) – list of pairs of
            latitudes and longitudes. Defaults to None.

         *  **postalCodes** (*list**, **optional*) – list of postal
            codes and corresponding country codes. Defaults to None.

         *  **countryCodes** (*list**, **optional*) – list of country
            codes for by country-code api call. Defaults to None.

         *  **cities** (*list**, **optional*) – list of cities.
            Defaults to None.

         *  **places** (*list**, **optional*) – list of places.
            Defaults to None.

         *  **parallel** (*bool**, **optional*) – Makes requests in
            parallel if True. Defaults to False.

      :Raises:
         `InvalidInputError <#ambee_sdk.ambee_sdk.InvalidInputError>`_
         – Executes when there is an invalid input

      :Returns:
         list of api responses in dictionary or pandas DataFrame
         format

      :Return type:
         outputs

   .. py:function:: to_geodataframe(df, x='lng', y='lat')**

      _summary_

      :Parameters:
         *  **df** (*DataFrame*) – Pandas DataFrame

         *  **x** (*str**, **optional*) – Name of longitude column.
            Defaults to ‘lng’.

         *  **y** (*str**, **optional*) – Name of latitude column.
            Defaults to ‘lat’.

      :Returns:
         geopandas GeoDataFrame

      :Return type:
         GeoDataFrame

.. py:class:: ambee_sdk.ambee_sdk.fire(x_api_key)**

   Bases: `ambee <#ambee_sdk.ambee_sdk.ambee>`_

   Contains methods to fetch data from Fire API

   .. py:function:: get_latest(by, lat=None, lng=None, place=None, return_df=False)**

      Retrives latest fire data for a given location

      :Parameters:
         *  **by** (*str*) – signifies the type of input supported by
            Ambee API. Refer to API Documentation.

         *  **lat** (*float/int/str**, **optional*) – Latitude.
            Defaults to None.

         *  **lng** (*float/int/str**, **optional*) – Longitude.
            Defaults to None.

         *  **place** (*str**, **optional*) – Placename. Defaults to
            None.

         *  **return_df** (*bool**, **optional*) – Converts results to
            pandas dataframe if True. Defaults to False.

      :Raises:
         *  `InvalidInputError
            <#ambee_sdk.ambee_sdk.InvalidInputError>`_ – Raised when
            the input to query is invalid

         *  **e** – Any exception that occurs during api call and data
            parsing

      :Returns:
         API response in dictionary format

      :Return type:
         dict

.. py:class:: ambee_sdk.ambee_sdk.ndvi(x_api_key)**

   Bases: `ambee <#ambee_sdk.ambee_sdk.ambee>`_

   Contains methods to fetch data from NDVI API

   .. py:function:: get_latest(by, lat=None, lng=None, return_df=False)**

      Retrives latest ndvi data for a given location

      :Parameters:
         *  **by** (*str*) – signifies the type of input supported by
            Ambee API. Refer to API Documentation.

         *  **lat** (*float/int/str**, **optional*) – Latitude.
            Defaults to None.

         *  **lng** (*float/int/str**, **optional*) – Longitude.
            Defaults to None.

         *  **return_df** (*bool**, **optional*) – Converts results to
            pandas dataframe if True. Defaults to False.

      :Raises:
         *  `InvalidInputError
            <#ambee_sdk.ambee_sdk.InvalidInputError>`_ – Raised when
            the input to query is invalid

         *  **e** – Any exception that occurs during api call and data
            parsing

      :Returns:
         API response in dictionary format

      :Return type:
         dict

.. py:class:: ambee_sdk.ambee_sdk.pollen(x_api_key)**

   Bases: `ambee <#ambee_sdk.ambee_sdk.ambee>`_

   Contains methods to fetch data from Pollen API

   .. py:function:: get_forecast(by, lat=None, lng=None, place=None,
   return_df=False)**

      Retrives forecasted pollen data for a given location

      :Parameters:
         *  **by** (*str*) – signifies the type of input supported by
            Ambee API. Refer to API Documentation.

         *  **lat** (*float/int/str**, **optional*) – Latitude.
            Defaults to None.

         *  **lng** (*float/int/str**, **optional*) – Longitude.
            Defaults to None.

         *  **place** (*str**, **optional*) – Placename. Defaults to
            None.

         *  **return_df** (*bool**, **optional*) – Converts results to
            pandas dataframe if True. Defaults to False.

      :Raises:
         *  `InvalidInputError
            <#ambee_sdk.ambee_sdk.InvalidInputError>`_ – Raised when
            the input to query is invalid

         *  **e** – Any exception that occurs during api call and data
            parsing

      :Returns:
         API response in dictionary format

      :Return type:
         dict

   .. py:function:: get_historical(by, from_val, to_val, lat=None, lng=None,
   place=None, return_df=False)**

      Retrives historical pollen data for a given location

      :Parameters:
         *  **by** (*str*) – signifies the type of input supported by
            Ambee API. Refer to API Documentation.

         *  **from_val** (*str*) – Start timestamp for historical
            query

         *  **to_val** (*_type_*) – End timestamp for historical query

         *  **lat** (*float/int/str**, **optional*) – Latitude.
            Defaults to None.

         *  **lng** (*float/int/str**, **optional*) – Longitude.
            Defaults to None.

         *  **place** (*str**, **optional*) – Placename. Defaults to
            None.

         *  **return_df** (*bool**, **optional*) – Converts results to
            pandas dataframe if True. Defaults to False.

      :Raises:
         *  `InvalidInputError
            <#ambee_sdk.ambee_sdk.InvalidInputError>`_ – Raised when
            the input to query is invalid

         *  **e** – Any exception that occurs during api call and data
            parsing

      :Returns:
         API response in dictionary format

      :Return type:
         dict

   .. py:function:: get_latest(by, lat=None, lng=None, place=None, return_df=False)**

      Retrives latest pollen data for a given location

      :Parameters:
         *  **by** (*str*) – signifies the type of input supported by
            Ambee API. Refer to API Documentation.

         *  **lat** (*float/int/str**, **optional*) – Latitude.
            Defaults to None.

         *  **lng** (*float/int/str**, **optional*) – Longitude.
            Defaults to None.

         *  **place** (*str**, **optional*) – Placename. Defaults to
            None.

         *  **return_df** (*bool**, **optional*) – Converts results to
            pandas dataframe if True. Defaults to False.

      :Raises:
         *  `InvalidInputError
            <#ambee_sdk.ambee_sdk.InvalidInputError>`_ – Raised when
            the input to query is invalid

         *  **e** – Any exception that occurs during api call and data
            parsing

      :Returns:
         API response in dictionary format

      :Return type:
         dict

.. py:class:: ambee_sdk.ambee_sdk.weather(x_api_key)**

   Bases: `ambee <#ambee_sdk.ambee_sdk.ambee>`_

   Contains methods to fetch data from Weather API

   .. py:function:: get_forecast(by, lat=None, lng=None, daily=False, units=None,
   return_df=False)**

      Retrives forecasted weather data for a given location

      :Parameters:
         *  **by** (*str*) – signifies the type of input supported by
            Ambee API. Refer to API Documentation.

         *  **lat** (*float/int/str**, **optional*) – Latitude.
            Defaults to None.

         *  **lng** (*float/int/str**, **optional*) – Longitude.
            Defaults to None.

         *  **daily** (*bool**, **optional*) – Gives daily aggregate
            if True. Defaults to False.

         *  **units** (*str**, **optional*) – Gives data in metric
            units if ‘si’ is passed. Defaults to None.

         *  **return_df** (*bool**, **optional*) – Converts results to
            pandas dataframe if True. Defaults to False.

      :Raises:
         *  `InvalidInputError
            <#ambee_sdk.ambee_sdk.InvalidInputError>`_ – Raised when
            the input to query is invalid

         *  **e** – Any exception that occurs during api call and data
            parsing

      :Returns:
         API response in dictionary format

      :Return type:
         dict

   .. py:function:: get_historical(by, from_val, to_val, lat=None, lng=None,
   daily=False, units=None, return_df=False)**

      Retrives historical weather data for a given location

      :Parameters:
         *  **by** (*str*) – signifies the type of input supported by
            Ambee API. Refer to API Documentation.

         *  **from_val** (*str*) – Start timestamp for historical
            query

         *  **to_val** (*_type_*) – End timestamp for historical query

         *  **lat** (*float/int/str**, **optional*) – Latitude.
            Defaults to None.

         *  **lng** (*float/int/str**, **optional*) – Longitude.
            Defaults to None.

         *  **daily** (*bool**, **optional*) – Gives daily aggregate
            if True. Defaults to False.

         *  **units** (*str**, **optional*) – Gives data in metric
            units if ‘si’ is passed. Defaults to None.

         *  **return_df** (*bool**, **optional*) – Converts results to
            pandas dataframe if True. Defaults to False.

      :Raises:
         *  `InvalidInputError
            <#ambee_sdk.ambee_sdk.InvalidInputError>`_ – Raised when
            the input to query is invalid

         *  **e** – Any exception that occurs during api call and data
            parsing

      :Returns:
         API response in dictionary format

      :Return type:
         dict

   .. py:function:: get_latest(by, lat=None, lng=None, units=None, return_df=False)**

      Retrives latest weather data for a given location

      :Parameters:
         *  **by** (*str*) – signifies the type of input supported by
            Ambee API. Refer to API Documentation.

         *  **lat** (*float/int/str**, **optional*) – Latitude.
            Defaults to None.

         *  **lng** (*float/int/str**, **optional*) – Longitude.
            Defaults to None.

         *  **units** (*str**, **optional*) – Gives data in metric
            units if ‘si’ is passed. Defaults to None.

         *  **return_df** (*bool**, **optional*) – Converts results to
            pandas dataframe if True. Defaults to False.

      :Raises:
         *  `InvalidInputError
            <#ambee_sdk.ambee_sdk.InvalidInputError>`_ – Raised when
            the input to query is invalid

         *  **e** – Any exception that occurs during api call and data
            parsing

      :Returns:
         API response in dictionary format

      :Return type:
         dict

   .. py:function:: get_severe_weather(by, lat=None, lng=None, place=None,
   units=None, return_df=False)**

      Gets severe weather data for a given location

      :Parameters:
         *  **by** (*str*) – signifies the type of input supported by
            Ambee API. Refer to API Documentation.

         *  **lat** (*float/int/str**, **optional*) – Latitude.
            Defaults to None.

         *  **lng** (*float/int/str**, **optional*) – Longitude.
            Defaults to None.

         *  **place** (*str**, **optional*) – Placename. Defaults to
            None.

         *  **units** (*str**, **optional*) – Gives data in metric
            units if ‘si’ is passed. Defaults to None.

         *  **return_df** (*bool**, **optional*) – Converts results to
            pandas dataframe if True. Defaults to False.

      :Raises:
         *  `InvalidInputError
            <#ambee_sdk.ambee_sdk.InvalidInputError>`_ – Raised when
            the input to query is invalid

         *  **e** – Any exception that occurs during api call and data
            parsing

      :Returns:
         API response in dictionary format

      :Return type:
         dict

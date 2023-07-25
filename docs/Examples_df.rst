examples with dataframe output
*****************

.. code:: ipython3

    import ambee_sdk as ambee
    import datetime

.. code:: ipython3

    x_api_key = "Your Key Here"

.. code:: ipython3

    aq = ambee.air_quality(x_api_key=x_api_key)

.. code:: ipython3

    aq.x_api_key

.. code:: ipython3

    aq.get_latest(by='latlng', lat=12, lng=77, return_df=True)

.. code:: ipython3

    aq.get_latest(by='postcode', postalCode=560020, countryCode="IN",return_df=True)

.. code:: ipython3

    aq.get_latest(by='city', city="Mysore", return_df=True)

.. code:: ipython3

    aq.get_latest(by='countrycode', countryCode="IN", return_df=True)

.. code:: ipython3

    to_val = datetime.datetime.utcnow()
    from_val = to_val - datetime.timedelta(days=1)

.. code:: ipython3

    to_val = to_val.strftime("%Y-%m-%d %H:%M:%S")
    to_val

.. code:: ipython3

    from_val = from_val.strftime("%Y-%m-%d %H:%M:%S")
    from_val

.. code:: ipython3

    aq.get_historical(by='latlng', lat=12, lng=77, from_val=from_val, to_val=to_val, return_df=True)

.. code:: ipython3

    aq.get_historical(by='postcode', postalCode=560020, countryCode="IN", from_val=from_val, to_val=to_val, return_df=True)

.. code:: ipython3

    pollen = ambee.pollen(x_api_key=x_api_key)

.. code:: ipython3

    pollen.get_latest(by='latlng', lat=12, lng=77, return_df=True)

.. code:: ipython3

    pollen.get_latest(by='place', place='London', return_df=True)

.. code:: ipython3

    pollen.get_historical(by='latlng', lat=12, lng=77, from_val=from_val, to_val=to_val, return_df=True)

.. code:: ipython3

    pollen.get_historical(by='place', place='London', from_val=from_val, to_val=to_val, return_df=True)

.. code:: ipython3

    pollen.get_forecast(by='latlng', lat=12, lng=77, return_df=True)

.. code:: ipython3

    pollen.get_forecast(by='place', place='London', return_df=True)

.. code:: ipython3

    weather = ambee.weather(x_api_key=x_api_key)

.. code:: ipython3

    weather.get_latest(by='latlng', lat=12, lng=77, return_df=True)

.. code:: ipython3

    weather.get_historical(by='latlng', lat=12, lng=77, from_val=from_val, to_val=to_val, return_df=True)

.. code:: ipython3

    weather.get_historical(by='latlng', lat=12, lng=77, from_val=from_val, to_val=to_val, daily=True, return_df=True)

.. code:: ipython3

    weather.get_forecast(by='latlng', lat=12, lng=77, return_df=True)

.. code:: ipython3

    weather.get_forecast(by='latlng', lat=12, lng=77, daily=True, return_df=True)

.. code:: ipython3

    weather.get_severe_weather(by='latlng', lat=12, lng=77, return_df=True)

.. code:: ipython3

    weather.get_severe_weather(by='place', place='London', return_df=True)

.. code:: ipython3

    weather.get_latest(by='latlng', lat=12, lng=77, units='si', return_df=True)

.. code:: ipython3

    weather.get_historical(by='latlng', lat=12, lng=77, from_val=from_val, to_val=to_val, units='si', return_df=True)

.. code:: ipython3

    weather.get_historical(by='latlng', lat=12, lng=77, from_val=from_val, to_val=to_val, daily=True, units='si', return_df=True)

.. code:: ipython3

    weather.get_forecast(by='latlng', lat=12, lng=77, units='si', return_df=True)

.. code:: ipython3

    weather.get_forecast(by='latlng', lat=12, lng=77, daily=True, units='si', return_df=True)

.. code:: ipython3

    weather.get_severe_weather(by='latlng', lat=12, lng=77, units='si', return_df=True)

.. code:: ipython3

    weather.get_severe_weather(by='place', place='London', units='si', return_df=True)

.. code:: ipython3

    fire = ambee.fire(x_api_key=x_api_key)

.. code:: ipython3

    fire.get_latest(by='latlng', lat=12, lng=77, return_df=True)

.. code:: ipython3

    fire.get_latest(by='place', place='London', return_df=True)

.. code:: ipython3

    fire.get_latest(by="polygon", burnedAreaLoc=True,coordinates=[[-147.6153523, 64.8027699],[-147.6097851, 64.8030029],[-147.6097314, 64.8010606]],return_df=True)

.. code:: ipython3

    fire.get_forcast(by="latlng", lat=-28.25, lng=142.5, return_df=True)

.. code:: ipython3

    ndvi = ambee.ndvi(x_api_key=x_api_key)

.. code:: ipython3

    ndvi.get_latest(by='latlng', lat=12, lng=77, return_df=True)

.. code:: ipython3

    disaster = ambee.natural_disaster(x_api_key=x_api_key)

.. code:: ipython3

    disaster.get_latest(by="latlng",lat=-15.76166996,lng=-72.48771045489497, return_df=True)

.. code:: ipython3

    disaster.get_historical(by="latlng",lat=-15.76166996,lng=-72.48771045489497, from_val=from_val, to_val=to_val, return_df=True)

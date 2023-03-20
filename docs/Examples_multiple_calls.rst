examples for multiple calls
*****************

.. code:: ipython3

    %load_ext nb_black
    import ambee_sdk as ambee
    import pandas as pd
    import datetime

.. code:: ipython3

    postcodes = [(560016, "IN"), (560017, "IN"), (560018, "IN")]
    lat_lngs = [(12, 77), (12.05, 77.05), (12.1, 77.1)]
    cities = ["Bangalore", "Mysore", "Delhi"]
    countrycodes = ["IN", "US", "FR"]
    places = ["London,UK", "Paris,FR", "Boston,US"]

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

    x_api_key = "Your API Key"

.. code:: ipython3

    aq = ambee.air_quality(x_api_key=x_api_key)

.. code:: ipython3

    aq.multiple_calls(
        by="postcode",
        func=aq.get_latest,
        postalCodes=postcodes,
    )

.. code:: ipython3

    dfs = aq.multiple_calls(
        by="postcode",
        func=aq.get_latest,
        postalCodes=postcodes,
        return_df=True,
    )
    pd.concat(dfs)

.. code:: ipython3

    aq.multiple_calls(by="latlng", func=aq.get_latest, lat_lngs=lat_lngs)

.. code:: ipython3

    dfs = aq.multiple_calls(
        by="latlng", func=aq.get_latest, lat_lngs=lat_lngs, return_df=True
    )
    pd.concat(dfs)

.. code:: ipython3

    aq.multiple_calls(
        by="city",
        func=aq.get_latest,
        cities=cities,
    )

.. code:: ipython3

    dfs = aq.multiple_calls(by="city", func=aq.get_latest, cities=cities, return_df=True)
    pd.concat(dfs)

.. code:: ipython3

    aq.multiple_calls(
        by="countrycode",
        func=aq.get_latest,
        countryCodes=countrycodes,
    )

.. code:: ipython3

    dfs = aq.multiple_calls(
        by="countrycode", func=aq.get_latest, countryCodes=countrycodes, return_df=True
    )
    pd.concat(dfs)

.. code:: ipython3

    dfs = aq.multiple_calls(
        by="latlng",
        func=aq.get_historical,
        lat_lngs=lat_lngs,
        from_val=from_val,
        to_val=to_val,
        return_df=True,
    )
    pd.concat(dfs)

.. code:: ipython3

    pollen = ambee.pollen(x_api_key=x_api_key)

.. code:: ipython3

    dfs = pollen.multiple_calls(
        by="latlng", func=pollen.get_latest, lat_lngs=lat_lngs, return_df=True
    )
    pd.concat(dfs)

.. code:: ipython3

    dfs = pollen.multiple_calls(
        by="place", func=pollen.get_latest, places=places, return_df=True
    )
    pd.concat(dfs)

.. code:: ipython3

    dfs = pollen.multiple_calls(
        by="latlng",
        func=pollen.get_historical,
        lat_lngs=lat_lngs,
        from_val=from_val,
        to_val=to_val,
        return_df=True,
    )
    pd.concat(dfs)

.. code:: ipython3

    dfs = pollen.multiple_calls(
        by="place",
        func=pollen.get_historical,
        places=places,
        from_val=from_val,
        to_val=to_val,
        return_df=True,
    )
    pd.concat(dfs)

.. code:: ipython3

    dfs = pollen.multiple_calls(
        by="latlng", func=pollen.get_forecast, lat_lngs=lat_lngs, return_df=True
    )
    pd.concat(dfs)

.. code:: ipython3

    dfs = pollen.multiple_calls(
        by="place", func=pollen.get_forecast, places=places, return_df=True
    )
    pd.concat(dfs)

.. code:: ipython3

    df = pd.concat(dfs)

.. code:: ipython3

    gdf = pollen.to_geodataframe(df)


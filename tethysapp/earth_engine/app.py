from tethys_sdk.base import TethysAppBase, url_map_maker


class EarthEngine(TethysAppBase):
    """
    Tethys app class for Earth Engine.
    """

    name = 'Time Series of VI & ET in the Southwestern Amazon'
    index = 'earth_engine:home'
    icon = 'earth_engine/images/earth-engine-logo.png'
    package = 'earth_engine'
    root_url = 'earth-engine'
    color = '#524745'
    description = 'This app creates time series of vegetation indices and evapotranspiration in the context of watersheds and indigenous territories'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='earth-engine',
                controller='earth_engine.controllers.home'
            ),
            UrlMap(
                name='get_image_collection',
                url='earth-engine/get-image-collection',
                controller='earth_engine.controllers.get_image_collection'
            ),
            UrlMap(
                name='get_time_series_plot',
                url='earth-engine/get-time-series-plot',
                controller='earth_engine.controllers.get_time_series_plot'
            ),
            UrlMap(
                name='getFeatureCollectionTileUrl',
                url='earth-engine/get-feature-collection-TileUrl',
                controller='earth_engine.gee.methods.getFeatureCollectionTileUrl'
            ),
        )

        return url_maps
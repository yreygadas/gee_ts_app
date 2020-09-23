EE_PRODUCTS = {
    'modis': {
        'terra': {
            'evapotranspiration': {
                'display': 'Net Evapotranspiration 8-Day 500m',
                'collection': 'MODIS/006/MOD16A2',
                'index': 'ET',
                'vis_params': {
                    'min': -32767,
                    'max': 32700,
                    'palette':[
                        'ffffff', 'fcd163', '99b718', '66a000', '3e8601', '207401',
                        '056201','004c00', '011301'
                    ],
                },
                'start_date': '2001-01-01',
                'end_date': None  # to present
            },
            'NDVI': {
                'display': 'NDVI 16-Day 500m',
                'collection': 'MODIS/006/MOD13A1',
                'index': 'NDVI',
                'vis_params': {
                    'min': -2000,
                    'max': 10000,
                    'palette': [
                        'ffffff', 'ce7e45', 'df923d', 'f1b555', 'fcd163', '99b718', '74a901',
                        '66a000', '529400', '3e8601', '207401', '056201', '004c00', '023b01',
                        '012e01', '011d01', '011301'
                    ],
                },
                'start_date': '2000-02-18',
                'end_date': None  # to present
            }
        },
    },
    'landsat': {
        '8': {
            'ndvi': {
                'display': '8-day NDVI',
                'collection': 'LANDSAT/LC08/C01/T1_8DAY_NDVI',
                'index': 'NDVI',
                'vis_params': {
                    'min': 0.0,
                    'max': 1.0,
                    'palette': [
                        'FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718', '74A901',
                        '66A000', '529400', '3E8601', '207401', '056201', '004C00', '023B01',
                        '012E01', '011D01', '011301'
                    ],
                },
                'start_date': '2013-04-01',
                'end_date': None  # to present
            },
            'evi': {
                'display': '8-day EVI',
                'collection': 'LANDSAT/LC08/C01/T1_8DAY_EVI',
                'index': 'EVI',
                'vis_params': {
                    'min': 0.0,
                    'max': 1.0,
                    'palette': [
                        'FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718', '74A901',
                        '66A000', '529400', '3E8601', '207401', '056201', '004C00', '023B01',
                        '012E01', '011D01', '011301'
                    ],
                },
                'start_date': '2013-04-01',
                'end_date': None  # to present
            },
        }
    }
}


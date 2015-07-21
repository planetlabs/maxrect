
import os
import json

import maxrect

EPS = 1e-8


def test_get_maximal_rectangle():

    srcpath = os.path.join(os.path.dirname(__file__), 'fixtures/polygon.geojson')

    with open(srcpath) as src:
        data = src.read()
    geojson = json.loads(data)

    feature = geojson.get('features')[0]
    coordinates = feature.get('geometry').get('coordinates')[0]
    ll, ur =  maxrect.get_maximal_rectangle(coordinates)

    expected_ll = [-101.645507812426, 39.222888638556988]
    expected_ur = [-92.877169942000137, 42.293564192171694]

    assert abs(expected_ll[0] - ll[0] < EPS)
    assert abs(expected_ll[1] - ll[1] < EPS)
    assert abs(expected_ur[0] - ur[0] < EPS)
    assert abs(expected_ur[1] - ur[1] < EPS)


import copy
import json
import click
from maxrect import get_maximal_rectangle, rect2poly, get_intersection


@click.command('max-rect')
@click.argument('polygon', default='-', required=False, nargs=1)
@click.option('--compare', is_flag=True, help='Leaves the original polygon in the feature collection')
@click.pass_context
def maxrect(ctx, polygon, compare):
    """
    Get an approximately maximal area, axis-aligned rectangle
    for a polygon represented by GeoJSON.
    """

    if polygon == '-':
        src = click.open_file('-')

        if not src.isatty():
            data = src.read()
        else:
            click.echo(ctx.get_usage())
            ctx.exit(1)
    else:
        with open(polygon, 'r') as src:
            data = src.read()

    geojson = json.loads(data)

    if geojson.get('type') == 'Feature':

        geojson = {
            'type': 'FeatureCollection',
            'features': [geojson]
        }

    features = geojson.get('features')
    n_features = len(features)

    if compare:
        features = features + copy.deepcopy(features)

    for feature in features[:n_features]:
        coordinates = get_maximal_rectangle(feature['geometry']['coordinates'][0])
        feature['geometry']['coordinates'] = [rect2poly(*coordinates)]

    geojson['features'] = features
    click.echo(json.dumps(geojson))


@click.command('poly-intersect')
@click.argument('input_geoms', required=True, nargs=-1)
@click.pass_context
def polyinter(ctx, input_geoms):
    """Find an intersection polygon given multiple geometry inputs"""
    coords = []
    for ig in input_geoms:
        with open(ig, 'r') as src:
            data = src.read()
            geojson = json.loads(data)

            if geojson.get('type') == 'Feature':
                geojson = {
                    'type': 'FeatureCollection',
                    'features': [geojson]
                }

            features = geojson.get('features')
            n_features = len(features)

            for feature in features[:n_features]:
                c = feature['geometry']['coordinates'][0]
                coords.append(c)

    inter_geojson, _ = get_intersection(coords)

    geojson = {
        'type': 'FeatureCollection',
        'features': [inter_geojson]
    }

    click.echo(json.dumps(geojson))

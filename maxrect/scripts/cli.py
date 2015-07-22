
import copy
import json
import click
from maxrect import get_maximal_rectangle, rect2poly


@click.command('maxrect')
@click.argument('polygon', default='-', required=False)
@click.option('--compare', is_flag=True, help='Leaves the original polygon in the feature collection')
@click.pass_context
def cli(ctx, polygon, compare):
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
        feature['geometry']['coordinates'] = [ rect2poly(*coordinates) ]

    geojson['features'] = features
    click.echo(json.dumps(geojson))

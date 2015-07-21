
import json
import click
from maxrect import get_maximal_rectangle, rect2poly


@click.command('maxrect')
@click.argument('polygon', default='-', required=False)
def cli(polygon):
    """
    Get an approximately maximal area, axis-aligned rectangle
    for a polygon represented by GeoJSON.
    """

    if polygon == '-':
        src = click.open_file('-')
        if not src.isatty():
            data = src.read()
    else:
        with open(polygon, 'r') as src:
            data = src.read()

    geojson = json.loads(data)

    features = geojson.get('features')

    for feature in features:
        coordinates = get_maximal_rectangle(feature['geometry']['coordinates'][0])
        feature['geometry']['coordinates'] = [ rect2poly(*coordinates) ]

    geojson['features'] = features
    click.echo(json.dumps(geojson))

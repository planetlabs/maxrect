
import os
from click.testing import CliRunner
from maxrect.scripts.cli import maxrect, polyinter


def test_maxrect():

    srcpath = os.path.join(os.path.dirname(__file__), 'fixtures/polygon.geojson')

    runner = CliRunner()
    result = runner.invoke(maxrect, [srcpath])
    assert result.exit_code == 0


def test_poly_intersect():
    srcpath1 = os.path.join(os.path.dirname(__file__), 'fixtures/polygon.geojson')
    srcpath2 = os.path.join(os.path.dirname(__file__), 'fixtures/polygon2.geojson')

    runner = CliRunner()
    result = runner.invoke(polyinter, [srcpath1, srcpath2])

    print result
    assert result.exit_code == 0

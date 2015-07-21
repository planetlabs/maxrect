
import os
from click.testing import CliRunner
from maxrect.scripts.cli import cli


def test_cli():

    srcpath = os.path.join(os.path.dirname(__file__), 'fixtures/polygon.geojson')

    runner = CliRunner()
    result = runner.invoke(cli, [srcpath])
    assert result.exit_code == 0

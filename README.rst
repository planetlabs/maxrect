maxrect
=======

Find the maximally inscribed, axis-aligned rectangle for a given polygon.

.. image:: https://pl-amit.s3.amazonaws.com/demo/maxrect/maximal-rectangle.png


Installation
------------

.. code-block:: bash

    pip install git+https://github.com/planetlabs/maxrect.git


CLI
---

.. code-block:: bash


    # For a given GeoJSON file
    $ maxrect [path/to/file]

    # Piping
    $ cat path/to/file.geojson | maxrect

    # For a quick visualization
    $ cat path/to/file.geojson | maxrect | geojsonio

    # For comparison between the original polygon and the inscribed rectangle
    $ cat path/to/file.geojson | maxrect --compare | geojsonio


Python
------

.. code-block:: python

    from maxrect import get_maximal_rectangle, rect2poly

    # For a given convex polygon
    coordinates = [ [x0, y0], [x1, y1], ... [xn, yn] ]

    # get the maximally inscribed rectangle
    ll, ur = get_maximal_rectangle(coordinates)

    # casting the rectangle to a GeoJSON-friendly closed polygon
    rect2poly(ll, ur)

maxrect
=======

Find the maximally inscribed, axis-aligned rectangle for a given polygon.
Find the intersection of multiple polygons.

.. image:: https://pl-amit.s3.amazonaws.com/demo/maxrect/maximal-rectangle.png


Installation
------------

.. code-block:: bash

    pip install git+https://${GITHUB_TOKEN}@github.com/planetlabs/maxrect.git


CLI
---

.. code-block:: bash


    # For a given GeoJSON file
    $ max-rect [path/to/file]

    # Piping
    $ cat path/to/file.geojson | max-rect

    # For a quick visualization
    $ cat path/to/file.geojson | max-rect | geojsonio

    # For comparison between the original polygon and the inscribed rectangle
    $ cat path/to/file.geojson | max-rect --compare | geojsonio

    # Find the intersection of two geojson files
    poly-intersect path/to/file1.geojson path/to/file2.geojson | geojsonio

    # Find the largest inscribed rectangle that sits within multiple shapes
    poly-intersect path/to/file1.geojson path/to/file2.geojson | max-rect | geojsonio

    # Find the intersection of two geojson files
    poly-intersect path/to/file1.geojson path/to/file2.geojson | geojsonio

    # Find the largest inscribed rectangle that sits within multiple shapes
    poly-intersect path/to/file1.geojson path/to/file2.geojson | max-rect | geojsonio


Python
------

.. code-block:: python

    from maxrect import get_intersection, get_maximal_rectangle, rect2poly

    # For a given convex polygon
    coordinates1 = [ [x0, y0], [x1, y1], ... [xn, yn] ]
    coordinates2 = [ [x0, y0], [x1, y1], ... [xn, yn] ]

    # find the intersection of the polygons
    _, coordinates = get_intersection([coordinates1, coordinates2])

    # get the maximally inscribed rectangle
    ll, ur = get_maximal_rectangle(coordinates)

    # casting the rectangle to a GeoJSON-friendly closed polygon
    rect2poly(ll, ur)

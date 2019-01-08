"""utils module."""
import json
import gpxpy
import gpxpy.gpx


# Create MapPoint class
class MapPoint(object):
    """MapPoint class."""

    def __init__(self, name, latitude, longitude, elevation, comment):
        super(MapPoint, self).__init__()
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation
        self.comment = comment


def open_gpx_file(filepath):
    """Open a gpx file and parse it with gpxpy."""
    gpx_file = open(filepath, 'r')
    gpx = gpxpy.parse(gpx_file)

    return gpx


def gpx_to_json(gpx):
    """Turn a parsed gpx file to json."""
    map_point_list = []

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                map_point = MapPoint(
                    None,
                    point.latitude,
                    point.longitude,
                    point.elevation,
                    None,
                )

                map_point_list.append(map_point)

    for waypoint in gpx.waypoints:
        map_point = MapPoint(
            waypoint.name,
            waypoint.latitude,
            waypoint.longitude,
            waypoint.elevation,
            waypoint.comment,
        )

        map_point_list.append(map_point)

    for route in gpx.routes:
        print('Route:')
        for point in route.points:
            map_point = MapPoint(
                None,
                point.latitude,
                point.longitude,
                point.elevation,
                None,
            )

            map_point_list.append(map_point)

    return json.dumps(map_point_list, default=lambda x: x.__dict__)

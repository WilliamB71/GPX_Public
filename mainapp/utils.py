import googlemaps
import gpxpy.gpx

api_key = "EXAMPLE_API_KEY"
gmaps = googlemaps.Client(api_key)


def get_coordinates(origin, destination, mode):
    directions_result = gmaps.directions(origin, destination, mode=mode)
    steps = directions_result[0]["legs"][0]["steps"]
    coordinates = []

    for step in steps:
        start_location = step["start_location"]
        coordinates.append((start_location["lat"], start_location["lng"]))

    return coordinates


def write_gpx_file(coordinates):
    gpx = gpxpy.gpx.GPX()

    gpx_track = gpxpy.gpx.GPXTrack()
    gpx.tracks.append(gpx_track)

    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)

    for lat, lon in coordinates:
        gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(latitude=lat, longitude=lon))

    return gpx.to_xml()

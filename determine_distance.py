import googlemaps
import geopy.distance

gmaps = googlemaps.Client(key='')
address1 = '2002 W 12500 S Riverton, Utah 84065'
address2 = '8210 Euclid Ave, Cleveland, OH 44103'

def main():
    address1_coordinates = retrieve_coordinates(address1)
    address2_coordinates = retrieve_coordinates(address2)
    distance = find_distance(address1_coordinates, address2_coordinates)
    print(f'Total Distance: {int(round(distance, 0))} miles')


def find_distance(address1_coordinates, address2_coordinates):
    distance = geopy.distance.geodesic(address1_coordinates, address2_coordinates).miles
    return distance


def retrieve_coordinates(address):
    geocode_result = gmaps.geocode(address)
    coordinates = geocode_result[0].get('geometry', {}).get('location', {})
    latitude = coordinates.get('lat', {})
    longitude = coordinates.get('lng', {})
    loc_tuple = (latitude, longitude)
    return loc_tuple


if __name__ == "__main__":
    main()
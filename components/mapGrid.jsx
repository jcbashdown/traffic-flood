import { GoogleMap, LoadScript, TrafficLayer } from '@react-google-maps/api'
import getCentralLatLongsForGridOfFour from '../lib/get-central-lat-longs-for-grid-of-four'

const MapGrid = () => {
    //get api key from the env
    const API_KEY = process.env.NEXT_PUBLIC_GOOGLE_MAPS_API_KEY
    const mapCenters = getCentralLatLongsForGridOfFour({ lat: -1.292105389694844, lng: 36.82089822660569 })
    //[
    //{ lat: -1.240786409142414, lng: 36.76733656834888 },
    //{ lat: -1.240786409142414, lng: 36.87550979598019 },
    //{ lat: -1.342304603945234, lng: 36.76733656834888 },
    //{ lat: -1.342304603945234, lng: 36.87550979598019 },
    //]
    //const mapStyles = [
    //{
    //featureType: 'all',
    //elementType: 'labels',
    //stylers: [{ visibility: 'off' }],
    //},
    //{
    //featureType: 'administrative',
    //elementType: 'geometry',
    //stylers: [{ visibility: 'off' }],
    //},
    //{
    //featureType: 'landscape',
    //elementType: 'all',
    //stylers: [{ color: '#f2f2f2' }],
    //},
    //{
    //featureType: 'poi',
    //elementType: 'all',
    //stylers: [{ visibility: 'off' }],
    //},
    //{
    //featureType: 'road',
    //elementType: 'geometry',
    //stylers: [{ color: '#ffffff' }],
    //},
    //{
    //featureType: 'transit',
    //elementType: 'all',
    //stylers: [{ visibility: 'off' }],
    //},
    //{
    //featureType: 'water',
    //elementType: 'all',
    //stylers: [{ color: '#d9d9d9' }],
    //},
    //]
    const mapStyles = [
        // Custom map styles here
        // Example:
        //{
        //featureType: 'all',
        //elementType: 'all',
        //stylers: [{ saturation: -100 }, { lightness: 0 }, { visibility: 'on' }],
        //},
        {
            featureType: 'all',
            elementType: 'all',
            stylers: [{ visibility: 'off' }], // Hide all map features
        },
    ]

    //const trafficOptions = {
    //opacity: 0.9,
    //zIndex: 1000,
    //styles: [
    //{ elementType: 'labels', stylers: [{ visibility: 'off' }] },
    //{ elementType: 'geometry', stylers: [{ weight: 10 }] },
    //{
    //featureType: 'road.highway',
    //elementType: 'geometry',
    //stylers: [{ color: '#ff0000', strokeOpacity: 1.0, strokeWeight: 10 }],
    //},
    //{
    //featureType: 'road.arterial',
    //elementType: 'geometry',
    //stylers: [{ color: '#ff8800', strokeOpacity: 1.0, strokeWeight: 8 }],
    //},
    //{ featureType: 'road.local', elementType: 'geometry.fill', stylers: [{ color: '#ff0000' }] },
    //],
    //}
    const mapContainerStyle = [
        {
            width: '5000px',
            height: '5000px',
            right: '-9px',
            bottom: '-9px',
        },
        {
            width: '5000px',
            height: '5000px',
            left: '-9px',
            bottom: '-9px',
        },
        {
            width: '5000px',
            height: '5000px',
            right: '-9px',
            top: '-9px',
        },
        {
            width: '5000px',
            height: '5000px',
            left: '-9px',
            top: '-9px',
        },
    ]

    return (
        <>
            <LoadScript googleMapsApiKey={API_KEY}>
                <div className="map-grid">
                    {mapCenters.map((mapCenter, index) => (
                        <GoogleMap
                            key={index}
                            mapContainerStyle={mapContainerStyle[index]}
                            center={mapCenter}
                            zoom={16}
                            options={{ styles: mapStyles, disableDefaultUI: true }}
                        >
                            <TrafficLayer />
                        </GoogleMap>
                    ))}
                </div>
            </LoadScript>
            <style jsx>{`
                .map-grid {
                    display: grid;
                    grid-template-columns: repeat(2, 1fr);
                    grid-gap: 20px;
                }
            `}</style>
        </>
    )
}

export default MapGrid

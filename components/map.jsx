import { useEffect, useState } from 'react'
import { GoogleMap, LoadScript, TrafficLayer } from '@react-google-maps/api'

const Map = () => {
    const [mapCenter, setMapCenter] = useState({ lat: 0, lng: 0 })

    useEffect(() => {
        setMapCenter({
            lat: -1.2924348955452392,
            lng: 36.820800560383645,
        })
    }, [])
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
    const trafficOptions = {
        styles: [
            {
                featureType: 'traffic',
                elementType: 'geometry',
                stylers: [
                    { visibility: 'off' }, // Hide traffic lines for levels other than 2 and 3
                ],
            },
            {
                featureType: 'traffic',
                elementType: 'geometry',
                stylers: [
                    { color: '#ff0000' }, // Bright red color for level 2 and 3 traffic
                    { weight: 7 }, // Increase the weight for better visibility
                    { visibility: 'on' }, // Show traffic lines for level 2 and 3
                ],
                conditions: ['level2', 'level3'], // Apply this style for traffic levels 2 and 3
            },
        ],
    }
    const mapContainerStyle = {
        width: '6000px',
        height: '6000px',
    }

    return (
        <LoadScript googleMapsApiKey="">
            <GoogleMap mapContainerStyle={mapContainerStyle} center={mapCenter} zoom={16}>
                <TrafficLayer options={options} />
            </GoogleMap>
        </LoadScript>
    )
}

export default Map

import { useEffect, useState } from 'react';
import { GoogleMap, LoadScript, TrafficLayer } from '@react-google-maps/api';

const Map = () => {
  const [mapCenter, setMapCenter] = useState({ lat: 0, lng: 0 });

  useEffect(() => {
          setMapCenter({
            lat: -1.2924348955452392,
            lng: 36.820800560383645
          })
  }, []);

  const options = {
    opacity: 0.9, // Adjust opacity for a more prominent display
    styles: [
      { elementType: 'labels', stylers: [{ visibility: 'off' }] }, // Turn off road labels for a cleaner look
      { elementType: 'geometry', stylers: [{ weight: 100 }] }, // Increase the thickness of the traffic lines
      { featureType: 'road.local', elementType: 'geometry.fill', stylers: [{ color: '#ff0000' }] }, // Highlight congested areas with a different color
    ],
  };
  const mapContainerStyle = {
    width: '6000px',
    height: '6000px',
  };

  return (
    <LoadScript googleMapsApiKey="">
      <GoogleMap
        mapContainerStyle={mapContainerStyle}
        center={mapCenter}
        zoom={16}
      >
        <TrafficLayer options={options} />
      </GoogleMap>
    </LoadScript>
  );
};

export default Map;

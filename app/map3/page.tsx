'use client'
import Map from '../../components/map'
const Map2 = () => {
    const centre = { lat: -1.342304603945234, lng: 36.76733656834888 }
    return (
        <div>
            <Map centre={centre} />
        </div>
    )
}

export default Map2

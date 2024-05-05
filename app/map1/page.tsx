'use client'
import Map from '../../components/map'
const Map1 = () => {
    const centre = { lat: -1.240786409142414, lng: 36.76733656834888 }
    return (
        <div>
            <Map centre={centre} />
        </div>
    )
}

export default Map1

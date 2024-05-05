'use client'
import Map from '../../components/map'
const Map2 = () => {
    const centre = { lat: -1.240786409142414, lng: 36.87550979598019 }
    return (
        <div>
            <Map centre={centre} />
        </div>
    )
}

export default Map2

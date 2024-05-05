'use client'
import Map from '../../components/map'
import getCentralLatLongsForGridOfFour from '../../lib/get-central-lat-longs-for-grid-of-four'
const Map1 = () => {
    const centre = getCentralLatLongsForGridOfFour({ lat: -1.292105389694844, lng: 36.82089822660569 })[0]
    return (
        <div>
            <Map centre={centre} />
        </div>
    )
}

export default Map1

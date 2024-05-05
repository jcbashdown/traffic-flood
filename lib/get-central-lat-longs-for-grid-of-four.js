function degreesPerPixel(zoomLevel, latitude) {
    const earthCircumferenceKm = 40075 // in kilometers at the equator
    const pixelsAtZoomLevel0 = 256 // Google Maps tile size at zoom level 0
    const totalPixels = pixelsAtZoomLevel0 * Math.pow(2, zoomLevel)

    const degreesPerPxLongitude = 360 / totalPixels
    const degreesPerPxLatitude = degreesPerPxLongitude * Math.cos((latitude * Math.PI) / 180)

    return { degreesPerPxLongitude, degreesPerPxLatitude }
}

export default function getCentralLatLongsForGridOfFour(center) {
    const { degreesPerPxLongitude, degreesPerPxLatitude } = degreesPerPixel(16, center.lat)

    const halfLat = degreesPerPxLatitude * 2500
    const halfLong = degreesPerPxLongitude * 2500

    return [
        { lat: center.lat + halfLat, lng: center.lng - halfLong },
        { lat: center.lat + halfLat, lng: center.lng + halfLong },
        { lat: center.lat - halfLat, lng: center.lng - halfLong },
        { lat: center.lat - halfLat, lng: center.lng + halfLong },
    ]
}
// Example usage for zoom level 10 at 40 degrees latitude
//const { degreesPerPxLongitude, degreesPerPxLatitude } = degreesPerPixel(10, 40)
//console.log(`Degrees per pixel (Longitude): ${degreesPerPxLongitude}`)
//console.log(`Degrees per pixel (Latitude): ${degreesPerPxLatitude}`)

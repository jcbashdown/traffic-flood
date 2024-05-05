const { chromium } = require('playwright')

async function captureScreenshot(url, outputPath) {
    const browser = await chromium.launch()
    const page = await browser.newPage()

    await page.goto(url, { waitUntil: 'networkidle' })

    await page.screenshot({ path: `output_images/${outputPath}`, fullPage: true })

    await browser.close()
}

const maps = ['map1', 'map2', 'map3', 'map4']

const outputTimestamp = new Date().toISOString().replace(/:/g, '-')
for (const map of maps) {
    const url = `http://localhost:3001/${map}`
    //output image to date-stamped file
    const outputPath = `${outputTimestamp}/${map}.png`

    captureScreenshot(url, outputPath)
        .then(() => {
            console.log(`Screenshot captured successfully: ${outputPath}`)
        })
        .catch((error) => {
            console.error('Error capturing screenshot:', error)
        })
}

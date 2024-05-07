const { chromium } = require('playwright')

async function captureScreenshot(url, outputPath) {
    const browser = await chromium.launch()
    const page = await browser.newPage()

    await page.goto(url, { waitUntil: 'networkidle' })

    let screenshotBuffer = await page.screenshot({ path: `output_images/${outputPath}`, fullPage: true })
    if (screenshotBuffer.length < 500000) {
        console.log(`Retrying ${outputPath}`)
        screenshotBuffer = await page.screenshot({ path: `output_images/${outputPath}`, fullPage: true })
    }
    if (screenshotBuffer.length < 500000) {
        console.log(`Retrying ${outputPath}`)
        screenshotBuffer = await page.screenshot({ path: `output_images/${outputPath}`, fullPage: true })
    }
    if (screenshotBuffer.length < 500000) {
        console.log(`Retrying ${outputPath}`)
        screenshotBuffer = await page.screenshot({ path: `output_images/${outputPath}`, fullPage: true })
    }
    if (screenshotBuffer.length < 500000) {
        console.log(`Retrying ${outputPath}`)
        screenshotBuffer = await page.screenshot({ path: `output_images/${outputPath}`, fullPage: true })
    }
	console.log("image size: "+screenshotBuffer.length)


    await browser.close()
}

async function captureScreenshots() {
const maps = ['map1', 'map2', 'map3', 'map4']

const outputTimestamp = new Date().toISOString().replace(/:/g, '-')
for (const map of maps) {
    const url = `http://localhost:3000/${map}`
    //output image to date-stamped file
    const outputPath = `${outputTimestamp}/${map}.png`

    await captureScreenshot(url, outputPath)
        .then(() => {
            console.log(`Screenshot captured successfully: ${outputPath}`)
        })
        .catch((error) => {
            console.error('Error capturing screenshot:', error)
        })
}
}
captureScreenshots()

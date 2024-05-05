const { chromium } = require('playwright')

async function captureScreenshot(url, outputPath) {
    const browser = await chromium.launch()
    const page = await browser.newPage()

    await page.goto(url, { waitUntil: 'networkidle' })

    await page.screenshot({ path: outputPath, fullPage: true })

    await browser.close()
}

const maps = ['map1', 'map2', 'map3', 'map4']
for (const map of maps) {
    const url = `http://localhost:3001/${map}`
    const outputPath = `${map}.png`

    captureScreenshot(url, outputPath)
        .then(() => {
            console.log(`Screenshot captured successfully: ${outputPath}`)
        })
        .catch((error) => {
            console.error('Error capturing screenshot:', error)
        })
}

const { chromium } = require('playwright')

async function captureScreenshot(url, outputPath) {
    const browser = await chromium.launch()
    const page = await browser.newPage()

    await page.goto(url, { waitUntil: 'networkidle' })

    await page.screenshot({ path: outputPath, fullPage: true })

    await browser.close()
}

// Usage example
const url = 'http://localhost:3001' // Replace with the URL of your locally served web page
const outputPath = 'screenshot.png'

captureScreenshot(url, outputPath)
    .then(() => {
        console.log(`Screenshot captured successfully: ${outputPath}`)
    })
    .catch((error) => {
        console.error('Error capturing screenshot:', error)
    })

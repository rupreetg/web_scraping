const puppeteer = require('puppeteer');

(async() => {
    const browser = await puppeteer.launch({headless: false});

    const page = await browser.newPage();

    //Navigate to a URL in the newly opened page in the bowser
    await page.goto("https://www.wikipedia.com");

    await page.setViewport({width: 1080, height: 1024});

    await page.waitForNavigation({waitUntil: 'networkidle0'})

    await browser.close();

})();

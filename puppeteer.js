const puppeteer = require('puppeteer');

(async() => {
    const browser = await puppeteer.launch({headless: false});

    const page = await browser.newPage();
    
    await page.setViewport({width: 1080, height: 1024});

    console.log(process.argv[2]);
    //Navigate to a URL in the newly opened page in the bowser
    await page.goto(process.argv[2], {waitUntil: 'networkidle0', timeout: 0});

    //await page.waitForNavigation({waitUntil: 'networkidle0', timeout: 0});
    //console.log("Navigation completed");
    await page.screenshot({path: "screenshot.jpg"});
    browser.close();

})();

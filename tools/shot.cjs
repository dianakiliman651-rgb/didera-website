#!/usr/bin/env node
// Скриншот сторінки з емуляцією пристрою (через Chromium, який є в хмарному образі).
// Використання: node tools/shot.cjs <url|файл.html> [out.png] [пристрій="iPhone 15"] [--full]
const { chromium, devices } = require('playwright');
const path = require('path');

(async () => {
  const args = process.argv.slice(2).filter((a) => a !== '--full');
  const full = process.argv.includes('--full');
  const [target, out = 'screenshot.png', deviceName = 'iPhone 15'] = args;
  if (!target) { console.error('Usage: node tools/shot.cjs <url|file> [out.png] [device] [--full]'); process.exit(1); }
  const device = devices[deviceName];
  if (!device) { console.error(`Unknown device: ${deviceName}`); process.exit(1); }
  const { defaultBrowserType, ...ctxOpts } = device; // завжди Chromium
  const url = /^[a-z]+:\/\//i.test(target) ? target : 'file://' + path.resolve(target);

  const browser = await chromium.launch();
  const page = await browser.newPage(ctxOpts);
  const errors = [];
  page.on('pageerror', (e) => errors.push(e.message));
  page.on('console', (m) => m.type() === 'error' && errors.push(m.text()));
  await page.goto(url, { waitUntil: 'networkidle' });
  const info = await page.evaluate(() => ({
    title: document.title,
    viewport: `${innerWidth}x${innerHeight}`,
    horizontalOverflow: document.documentElement.scrollWidth > innerWidth,
  }));
  await page.screenshot({ path: out, fullPage: full });
  await browser.close();
  console.log(JSON.stringify({ device: deviceName, out, ...info, errors }, null, 2));
})().catch((e) => { console.error(e); process.exit(1); });

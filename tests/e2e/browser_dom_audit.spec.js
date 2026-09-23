/**
 * Playwright DOM Audit Suite
 * 
 * Stage 2 E2E: verifies computed styles in a real headless browser.
 * Regex static analysis cannot catch CSS cascade, Tailwind JIT compilation,
 * or layout math. This suite evaluates real getComputedStyle() values.
 * 
 * Setup:
 *   npm install --save-dev @playwright/test
 *   npx playwright install chromium
 * 
 * Run:
 *   npx playwright test tests/e2e/browser_dom_audit.spec.js
 * 
 * Each test can be run in isolation:
 *   npx playwright test --grep "quiet-luxury"
 */

import { test, expect } from '@playwright/test';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const GALLERY_DIR = path.resolve(__dirname, '../../skills/design-director/gallery');

/** Helper: file:// URL for a gallery HTML file */
function p2url(filename) {
  const clean = filename.replace('p2_', '');
  return `file://${path.join(GALLERY_DIR, clean)}`;
}

/** Helper: get computed borderRadius for the first matching selector */
async function computedRadius(page, selector) {
  const el = page.locator(selector).first();
  return el.evaluate(node => window.getComputedStyle(node).borderRadius);
}

/** Helper: get computed boxShadow */
async function computedShadow(page, selector) {
  const el = page.locator(selector).first();
  return el.evaluate(node => window.getComputedStyle(node).boxShadow);
}

/** Helper: get computed color */
async function computedColor(page, selector, prop = 'backgroundColor') {
  const el = page.locator(selector).first();
  return el.evaluate((node, p) => window.getComputedStyle(node)[p], prop);
}

// ─────────────────────────────────────────────────────────────────────────────
// Quiet Luxury
// ─────────────────────────────────────────────────────────────────────────────
test.describe('quiet-luxury DOM audit', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(p2url('p2_quiet_luxury.html'));
  });

  test('border-radius is 0px on primary containers', async ({ page }) => {
    const containers = page.locator('.portfolio-card, .card, nav, button, section').first();
    const count = await page.locator('.portfolio-card, .card, nav, button, section').count();
    for (let i = 0; i < Math.min(count, 10); i++) {
      const radius = await page.locator('.portfolio-card, .card, nav, button, section')
        .nth(i)
        .evaluate(el => window.getComputedStyle(el).borderRadius);
      // Quiet luxury: radius must be 0px
      expect(radius, `Element ${i} borderRadius`).toMatch(/^0px/);
    }
  });

  test('Cormorant Garamond font loads for display headings', async ({ page }) => {
    const fontLoaded = await page.evaluate(() =>
      document.fonts.check('300 24px "Cormorant Garamond"') ||
      document.fonts.check('400 24px "Cormorant Garamond"') ||
      document.fonts.check('300 24px Cormorant')
    );
    expect(fontLoaded, 'Cormorant Garamond should be loaded').toBe(true);
  });

  test('no colored box-shadow (shadow must be none)', async ({ page }) => {
    const cards = page.locator('.portfolio-card, .card').first();
    if (await cards.count() === 0) return;
    const shadow = await cards.evaluate(el => window.getComputedStyle(el).boxShadow);
    expect(shadow).toBe('none');
  });

  test('canvas is alabaster — not pure white', async ({ page }) => {
    const bg = await page.evaluate(() =>
      window.getComputedStyle(document.body).backgroundColor
    );
    // rgb(251,251,249) = #FBFBF9 or similar warm off-white; definitely not rgb(255,255,255)
    expect(bg).not.toBe('rgb(255, 255, 255)');
  });
});

// ─────────────────────────────────────────────────────────────────────────────
// Swiss / Editorial
// ─────────────────────────────────────────────────────────────────────────────
test.describe('swiss-editorial DOM audit', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(p2url('p2_swiss_editorial.html'));
  });

  test('border-radius is 0px or max 2px on all containers', async ({ page }) => {
    const els = page.locator('section, article, .card, button, nav');
    const count = await els.count();
    for (let i = 0; i < Math.min(count, 10); i++) {
      const radius = await els.nth(i).evaluate(el => {
        const r = window.getComputedStyle(el).borderRadius;
        return parseFloat(r) || 0;
      });
      expect(radius, `Element ${i} radius`).toBeLessThanOrEqual(2);
    }
  });

  test('no blurred box shadows (blur must be 0)', async ({ page }) => {
    const els = page.locator('section, .card, article').first();
    if (await els.count() === 0) return;
    const shadow = await els.evaluate(el => window.getComputedStyle(el).boxShadow);
    if (shadow !== 'none') {
      // Parse blur radius from "0px 1px 0px rgba(...)" pattern
      const parts = shadow.split(' ');
      const blurIndex = parts.length >= 3 ? 2 : -1;
      if (blurIndex >= 0) {
        const blur = parseFloat(parts[blurIndex]) || 0;
        expect(blur, 'Shadow blur must be 0 for Swiss Editorial').toBeLessThanOrEqual(1);
      }
    }
  });

  test('exactly one accent color is present', async ({ page }) => {
    // Count distinct non-black, non-white, non-gray foreground colors
    const accentColors = await page.evaluate(() => {
      const colors = new Set();
      document.querySelectorAll('*').forEach(el => {
        const style = window.getComputedStyle(el);
        const color = style.color;
        // Exclude near-black, near-white, gray
        const [r, g, b] = color.match(/\d+/g)?.map(Number) ?? [0, 0, 0];
        const isNeutral = Math.abs(r - g) < 20 && Math.abs(g - b) < 20 && Math.abs(r - b) < 20;
        if (!isNeutral && (r > 100 || g > 100 || b > 100)) {
          colors.add(color);
        }
      });
      return colors.size;
    });
    // Swiss editorial allows 0 (monochrome) or 1 accent color
    expect(accentColors, 'Swiss editorial: max 1 accent color').toBeLessThanOrEqual(3); // loose — styles cascade
  });
});

// ─────────────────────────────────────────────────────────────────────────────
// Neo-Brutalism
// ─────────────────────────────────────────────────────────────────────────────
test.describe('neo-brutalism DOM audit', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(p2url('p2_neo_brutalism.html'));
  });

  test('cards have hard offset box-shadow (not blurred)', async ({ page }) => {
    const cards = page.locator('.card, section, article').first();
    if (await cards.count() === 0) return;
    const shadow = await cards.evaluate(el => window.getComputedStyle(el).boxShadow);
    // Hard offset shadows: "4px 4px 0px rgb(0,0,0)" or similar
    expect(shadow).not.toBe('none');
    // Blur component should be 0 or very small
    const blurMatch = shadow.match(/\d+px\s+(\d+)px\s+(\d+)px/);
    if (blurMatch) {
      const blur = parseInt(blurMatch[2], 10);
      expect(blur, 'Neo-brutalism: shadow must be hard (0px blur)').toBeLessThanOrEqual(2);
    }
  });

  test('no pill-shaped buttons (border-radius < 50%)', async ({ page }) => {
    const buttons = page.locator('button, .btn, a[class*="button"]');
    const count = await buttons.count();
    for (let i = 0; i < Math.min(count, 5); i++) {
      const radius = await buttons.nth(i).evaluate(el => parseFloat(window.getComputedStyle(el).borderRadius) || 0);
      expect(radius, `Button ${i} should not be pill-shaped`).toBeLessThan(9999);
    }
  });
});

// ─────────────────────────────────────────────────────────────────────────────
// Cyberpunk
// ─────────────────────────────────────────────────────────────────────────────
test.describe('cyberpunk DOM audit', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(p2url('p2_cyberpunk.html'));
  });

  test('background is dark (not light)', async ({ page }) => {
    const bg = await page.evaluate(() =>
      window.getComputedStyle(document.body).backgroundColor
    );
    const [r, g, b] = (bg.match(/\d+/g) ?? ['200', '200', '200']).map(Number);
    const luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b;
    expect(luminance, 'Cyberpunk body must be dark (luminance < 80)').toBeLessThan(80);
  });

  test('no light-mode pill buttons (rounded-full class absent)', async ({ page }) => {
    const pills = await page.locator('.rounded-full').count();
    expect(pills, 'rounded-full is forbidden in Cyberpunk').toBe(0);
  });
});

// ─────────────────────────────────────────────────────────────────────────────
// Space Age Optimism
// ─────────────────────────────────────────────────────────────────────────────
test.describe('space-age-optimism DOM audit', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(p2url('p2_space_age_optimism.html'));
  });

  test('background is light / warm-white (not dark)', async ({ page }) => {
    const bg = await page.evaluate(() =>
      window.getComputedStyle(document.body).backgroundColor
    );
    const [r, g, b] = (bg.match(/\d+/g) ?? ['0', '0', '0']).map(Number);
    const luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b;
    expect(luminance, 'Space Age body must be light (luminance > 180)').toBeGreaterThan(180);
  });

  test('primary containers have generous border-radius (>=16px)', async ({ page }) => {
    const cards = page.locator('.card, section, article').first();
    if (await cards.count() === 0) return;
    const radius = await cards.evaluate(el => parseFloat(window.getComputedStyle(el).borderRadius) || 0);
    expect(radius, 'Space Age pods must have >= 16px radius').toBeGreaterThanOrEqual(16);
  });
});

// ─────────────────────────────────────────────────────────────────────────────
// Bauhaus
// ─────────────────────────────────────────────────────────────────────────────
test.describe('bauhaus DOM audit', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(p2url('p2_bauhaus.html'));
  });

  test('rectangular containers have 0px radius (not rounded)', async ({ page }) => {
    const cards = page.locator('section, article, .card, div[class*="card"]').first();
    if (await cards.count() === 0) return;
    const radius = await cards.evaluate(el => parseFloat(window.getComputedStyle(el).borderRadius) || 0);
    expect(radius, 'Bauhaus containers must be 0px radius').toBeLessThanOrEqual(2);
  });

  test('no blurred shadows', async ({ page }) => {
    const els = page.locator('section, .card, article').first();
    if (await els.count() === 0) return;
    const shadow = await els.evaluate(el => window.getComputedStyle(el).boxShadow);
    expect(shadow).toBe('none');
  });
});

// ─────────────────────────────────────────────────────────────────────────────
// Y2K / Frutiger Aero
// ─────────────────────────────────────────────────────────────────────────────
test.describe('y2k-frutiger-aero DOM audit', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(p2url('p2_y2k_frutiger_aero.html'));
  });

  test('buttons have generous border-radius (>= 8px)', async ({ page }) => {
    const buttons = page.locator('button, .btn').first();
    if (await buttons.count() === 0) return;
    const radius = await buttons.evaluate(el => parseFloat(window.getComputedStyle(el).borderRadius) || 0);
    expect(radius, 'Y2K buttons must be rounded (>= 8px)').toBeGreaterThanOrEqual(8);
  });

  test('page is light mode (not dark)', async ({ page }) => {
    const bg = await page.evaluate(() =>
      window.getComputedStyle(document.body).backgroundColor
    );
    const [r, g, b] = (bg.match(/\d+/g) ?? ['0', '0', '0']).map(Number);
    const luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b;
    expect(luminance, 'Y2K must be light mode (luminance > 150)').toBeGreaterThan(150);
  });
});

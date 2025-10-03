import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Capture console messages
        page.on('console', lambda msg: print(f"CONSOLE: {msg.text}"))

        # Get absolute paths for the HTML files
        original_html_path = os.path.abspath('services.html')
        optimized_html_path = os.path.abspath('services_optimized.html')

        # Navigate to the optimized HTML file and take a screenshot
        await page.goto(f'file://{optimized_html_path}', timeout=60000)
        await page.screenshot(path='jules-scratch/verification/optimized.png')
        print("Took screenshot of optimized.png")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
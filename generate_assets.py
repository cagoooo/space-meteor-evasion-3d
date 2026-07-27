import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

def generate_og_image():
    width, height = 1200, 630
    img = Image.new('RGBA', (width, height), (3, 7, 18, 255))
    draw = ImageDraw.Draw(img)

    for y in range(height):
        r = int(3 + (y / height) * 15)
        g = int(7 + (y / height) * 20)
        b = int(18 + (y / height) * 45)
        draw.line([(0, y), (width, y)], fill=(r, g, b, 255))

    draw.ellipse([400, -100, 1100, 600], fill=(0, 240, 255, 25))
    draw.ellipse([-200, 200, 500, 900], fill=(168, 85, 247, 30))

    font_path = "C:\\Windows\\Fonts\\msjhbd.ttc"
    font_sub_path = "C:\\Windows\\Fonts\\msjh.ttc"
    
    title_font = ImageFont.truetype(font_path, 52)
    subtitle_font = ImageFont.truetype(font_sub_path, 26)
    badge_font = ImageFont.truetype(font_path, 22)
    footer_font = ImageFont.truetype(font_sub_path, 24)

    draw.rounded_rectangle([60, 60, 1140, 570], radius=24, outline=(0, 240, 255, 120), width=3)
    draw.rounded_rectangle([70, 70, 1130, 560], radius=20, fill=(10, 22, 40, 180), outline=(0, 240, 255, 60), width=1)

    draw.rounded_rectangle([100, 110, 480, 155], radius=20, fill=(168, 85, 247, 60), outline=(168, 85, 247, 200), width=2)
    draw.text((120, 118), "🌌 國小國中星際科普解題遊戲", font=badge_font, fill=(216, 180, 254))

    draw.text((100, 185), "🚀 3D 星際雷霆大冒險", font=title_font, fill=(0, 240, 255))
    draw.text((100, 255), "隕石防禦打擊 · 全屏觸控滑動 · 太空科學解題策略", font=title_font, fill=(255, 255, 255))
    
    draw.text((100, 365), "✨ 支援電腦 WASD 鍵盤與手機/平板雙端全屏滑動操控", font=subtitle_font, fill=(148, 163, 184))
    draw.text((100, 410), "⚡ 酷炫 Three.js 第一人稱座艙、雷射連擊與 Web Audio 聲效", font=subtitle_font, fill=(148, 163, 184))

    draw.line([(100, 480), (1100, 480)], fill=(0, 240, 255, 80), width=1)
    draw.text((100, 505), "Made with ❤️ by 阿凱老師", font=footer_font, fill=(0, 240, 255))
    draw.text((680, 505), "https://cagoooo.github.io/space-meteor-evasion-3d/", font=subtitle_font, fill=(100, 116, 139))

    img.save("og-preview.png", "PNG")
    print("og-preview.png generated successfully.")

def generate_icons():
    sizes = [(512, "icon-512.png"), (192, "icon-192.png"), (180, "apple-touch-icon.png"), (32, "favicon-32.png")]
    font_path = "C:\\Windows\\Fonts\\msjhbd.ttc"

    for size, filename in sizes:
        img = Image.new('RGBA', (size, size), (3, 7, 18, 255))
        draw = ImageDraw.Draw(img)

        margin = int(size * 0.05)
        draw.ellipse([margin, margin, size - margin, size - margin], fill=(10, 22, 40, 255), outline=(0, 240, 255, 200), width=max(2, int(size * 0.03)))
        
        fsize = int(size * 0.45)
        try:
            font = ImageFont.truetype(font_path, fsize)
        except:
            font = ImageFont.load_default()
        
        draw.text((size // 2, size // 2), "🚀", font=font, anchor="mm", fill=(0, 240, 255))
        img.save(filename, "PNG")
        print(f"{filename} ({size}x{size}) generated.")

    img32 = Image.open("favicon-32.png")
    img32.save("favicon.ico", format="ICO", sizes=[(32, 32)])
    print("favicon.ico generated.")

if __name__ == "__main__":
    generate_og_image()
    generate_icons()

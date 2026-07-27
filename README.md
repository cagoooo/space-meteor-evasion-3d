# 🚀 3D 星際雷霆解題大冒險 (3D Space Meteor Evasion & Education Quiz Engine)

> **第一人稱飛船駕駛 · 電腦鍵盤/滑鼠/手機觸控全響應 · 3D 隕石爆破碎塊物理 · 班級排行榜與 36 題跨學科學霸問答大冒險**

[![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F%20by%20%E9%98%BF%E5%87%B1%E8%80%81%E5%B8%AB-ff4081.svg)](https://www.smes.tyc.edu.tw/modules/tadnews/page.php?ncsn=11&nsn=16#a5)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Deployed-00f0ff.svg)](https://cagoooo.github.io/space-meteor-evasion-3d/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌐 線上即時體驗 (Live Demo)

- **👉 網站線上體驗連線網址**：[https://cagoooo.github.io/space-meteor-evasion-3d/](https://cagoooo.github.io/space-meteor-evasion-3d/)
- **📦 GitHub 專案儲存庫**：[https://github.com/cagoooo/space-meteor-evasion-3d](https://github.com/cagoooo/space-meteor-evasion-3d)

---

## ✨ 核心特色與遊戲亮點

### 💥 1. 3D 隕石爆破碎塊物理 (Mesh Shatter Physics)
- 採用 Three.js 實體網格處理解構，當雷射擊中隕石時，不只有火光粒子，還會瞬間**爆破散落 5 個實體 3D 隕石碎片 (`DodecahedronGeometry`)**，隨機彈射旋轉飛散！

### 🏆 2. 班級星際英雄排行榜與稱號存檔 (Leaderboard System)
- **名字與座號登錄**：支援學生在結算畫面輸入姓名/座號（如：`501阿凱`）存檔。
- **Top 5 尊榮勳章**：自動排序全校前 5 名紀錄，頒發 `🥇 🥈 🥉 4️⃣ 5️⃣` 徽章與最高稱號（如 `👑 星際銀河大師學霸`），大幅提升課堂學習動機。

### 📚 3. 4 大主題 36 題跨學科題庫 (Expanded Question Bank)
- 內建 4 大領域解題目錄，點擊首頁即可自由切換挑戰：
  1. ☀️ **太陽系與天文科學** (10 題)
  2. 🌱 **國小自然與生態環境** (10 題)
  3. 💻 **資訊科技與 AI 常識** (9 題)
  4. 🧠 **星際邏輯與密碼推理** (6 題 - 全新加開！)

### 🖥️ 4. 電腦端 1040px 大氣美學 UI ＋ 動態答對/答錯回饋
- 桌面端彈窗寬度大幅擴展至 `1040px`，配合 `clamp(20px, 2.6vw, 30px)` 超大清晰標題與 `2x2` 雙欄大按鈕。
- 答對時高亮顯示 **【領取能量獎勵 · 繼續飛行 🚀】**，答錯時溫馨提示 **【吸收觀念知識 · 繼續飛行 🚀】**。

### 🔊 5. 零延遲雙軌音效系統 ＋ Pixabay CC0 原創 BGM
- **高音質 BGM**：引入 Pixabay CC0 "Space Arcade Synthwave" 原創樂曲，帶有 2 秒平滑淡入效果。
- **雙軌音效 (Zero-Latency Dual SFX)**：使用 FFmpeg 壓製標準 128k CBR MP3 檔，並結合 Web Audio 零時差發聲層 (`<1ms` 超低延遲)，100% 確保雷射、爆破、寶箱、衝刺、答對、答錯與 GameOver 音效清楚震撼！

---

## 📱 操作指南與控制方式 (Controls & RWD)

全站具備 **RWD 響應式設計**，不論是在電腦大螢幕、iPad 觸控板或手機都能暢快遊玩：

| 裝置 / 平台 | 操作方式 | 遊戲功能說明 |
|---|---|---|
| 💻 **電腦端** | `WASD` 或 滑鼠游標移動 | 傾斜控制飛船飛行方向 |
| 💻 **電腦鍵盤** | `J` 鍵 / `Space` 鍵 | 發射雷射砲 / 按住曲速衝刺 |
| 📱 **手機/平板** | 螢幕隨意按住滑動 | 手指引導飛船飛行 |
| 📱 **觸控按鈕** | 畫面右下角 `💥發射` / `🚀衝刺` | 雙手靈敏操作戰鬥 |

---

## 🛠️ 技術架構與工具鏈 (Tech Stack)

- **3D 繪圖引擎**：Three.js (`WebGLRenderer`, `PerspectiveCamera`, `Group`, `MeshDodecahedron`)
- **聲音音訊系統**：Pixabay CC0 Audio + Web Audio API (`AudioContext`, `GainNode`) 雙軌發聲層
- **數據快取存檔**：HTML5 `LocalStorage` 學生班級榜單 JSON 序列化
- **PWA 與自動更新**：Service Worker 快取管理 ＋ 網路版本主動比對彈窗 (`reg.update()`)
- **樣式與美學**：Vanilla CSS Modern Dark Mode, Glassmorphism, Google Fonts (`Orbitron`, `Noto Sans TC`)

---

## 🚀 本地開發與啟動 (Local Setup)

本專案為純靜態 HTML5 + Three.js 獨立單頁應用程式，無需複雜的 `node_modules` 安裝：

```bash
# 1. 克隆 GitHub 專案儲存庫
git clone https://github.com/cagoooo/space-meteor-evasion-3d.git

# 2. 進入專案目錄
cd space-meteor-evasion-3d

# 3. 啟動本地 HTTP 伺服器 (可使用 Python 或 Live Server)
python -m http.server 8000

# 4. 開啟瀏覽器造訪
http://localhost:8000
```

---

## 👤 版權與作者資訊 (Author & Credit)

Made with ❤️ by [阿凱老師](https://www.smes.tyc.edu.tw/modules/tadnews/page.php?ncsn=11&nsn=16#a5)

- **作者**：石門國小 阿凱老師 (Akai)
- **聯絡資訊 / 教師專頁**：[石門國小教師資訊頁](https://www.smes.tyc.edu.tw/modules/tadnews/page.php?ncsn=11&nsn=16#a5)

---

## 📄 授權條款 (License)

本專案採用 [MIT License](LICENSE) 授權發布，歡迎全國國中小教師、教育工作者與程式愛好者自由教學使用與二次創作！

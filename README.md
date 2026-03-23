<<<<<<< HEAD
# booking-app-demo-2025
=======
# 🐋 Booking App Demo 2025 — Lab Series

> **Full Stack Web Development with Docker & Docker Compose**
> Repository: [surachai-p/booking-app-demo-2025](https://github.com/surachai-p/booking-app-demo-2025)

---

## 📋 ข้อมูลรายวิชา

| รายการ | รายละเอียด |
|--------|-----------|
| **วิชา** | การพัฒนา Web Application แบบ Full Stack |
| **ระดับ** | ปริญญาตรี / บัณฑิตศึกษา |
| **เครื่องมือหลัก** | Docker, Docker Compose, Node.js, SQLite, Nginx |
| **Repository** | [booking-app-demo-2025](https://github.com/surachai-p/booking-app-demo-2025) |

---

## 🗂️ สารบัญใบงานการทดลอง

```
booking-app-demo-2025/
├── 📄 README.md                        ← คุณอยู่ที่นี่
│
├── 🐋 LAB_DOCKER_COMPOSE.md            ← ใบงาน Docker & Docker Compose
│
├── backend/                            ← Node.js Express API
├── frontend/                           ← Static HTML/CSS/JS
├── newman/                             ← API Test Collection
└── tests/robot/                        ← Robot Framework Tests
```

---

## 📚 รายการใบงานการทดลอง

| Lab | หัวข้อ | เวลา | ระดับ | ไฟล์ |
|-----|--------|------|-------|------|
| **Lab 1** | 🐋 Docker Foundation & Docker Compose | 3 ชั่วโมง | 🟢 เริ่มต้น | [LAB_DOCKER_COMPOSE.md](LAB_DOCKER_COMPOSE.md) |
| **Lab 2** | 🐍 Flask Application with PythonSQL | 2 ชั่วโมง | 🟢 เริ่มต้น | _Coming Soon_ |
| **Lab 3** | 🔐 User Authentication & Authorization | 2 ชั่วโมง | 🟡 กลาง | _Coming Soon_ |
| **Lab 4** | 🎫 Ticket Management System | 3 ชั่วโมง | 🟡 กลาง | _Coming Soon_ |
| **Lab 5** | 🧪 Testing & Quality Assurance | 2 ชั่วโมง | 🟡 กลาง | _Coming Soon_ |
| **Lab 6** | ⚙️ CI/CD with GitHub Actions | 3 ชั่วโมง | 🔴 สูง | _Coming Soon_ |
| **Lab 7** | 🚀 Docker Production Deployment | 3 ชั่วโมง | 🔴 สูง | _Coming Soon_ |

---

## 🏗️ สถาปัตยกรรมของ Application

```
┌──────────────────────────────────────────────────────────┐
│                    Docker Network                         │
│                                                           │
│   ┌─────────────┐    ┌──────────────────────────────┐    │
│   │  Frontend   │───▶│          Backend             │    │
│   │  (Nginx)    │    │        (Node.js)             │    │
│   │  Port: 3000 │    │  ┌────────────────────────┐  │    │
│   └─────────────┘    │  │  booking.db (SQLite)   │  │    │
│          ▲           │  │  /app/data/ (Volume)   │  │    │
└──────────┼───────────│  └────────────────────────┘  │────┘
           │           │         Port: 5000            │
     Browser (User)    └──────────────────────────────┘
```

### Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| **Frontend** | HTML5, CSS3, JavaScript | Static |
| **Web Server** | Nginx | Alpine |
| **Backend** | Node.js + Express.js | 20 LTS |
| **Database** | SQLite (better-sqlite3) | ไฟล์เดียว — ไม่ต้อง Server |
| **Container** | Docker + Docker Compose | v2.x |

---

## 🚀 Quick Start

### สำหรับนักศึกษาที่ต้องการรัน Application ทันที

**1. Clone Repository**
```bash
git clone https://github.com/surachai-p/booking-app-demo-2025.git
cd booking-app-demo-2025
```

**2. รัน Application ด้วย Docker Compose**
```bash
docker compose up -d --build
```

**3. เปิด Browser**
```
Frontend  →  http://localhost:3000
Backend   →  http://localhost:5000/api/health
```

**4. หยุด Application**
```bash
docker compose down
```

> 💡 สำหรับขั้นตอนการทดลองแบบละเอียด ดูได้ที่ [LAB_DOCKER_COMPOSE.md](LAB_DOCKER_COMPOSE.md)

---

## ✅ ข้อกำหนดก่อนเริ่มทดลอง

### Software ที่ต้องติดตั้ง

- [ ] **Docker Desktop** v26.x+ → [Download](https://www.docker.com/products/docker-desktop)
- [ ] **Git** v2.x+ → [Download](https://git-scm.com)
- [ ] **VS Code** (แนะนำ) → [Download](https://code.visualstudio.com)
- [ ] **VS Code Extension**: Docker, REST Client (แนะนำ)

### ตรวจสอบการติดตั้ง
```bash
docker --version          # Docker version 26.x.x ขึ้นไป
docker compose version    # Docker Compose version v2.x.x (ไม่ใส่ version: ใน yaml)
git --version             # git version 2.x.x
```

---

## 📖 แหล่งข้อมูลอ้างอิง

| แหล่ง | ลิงก์ |
|-------|-------|
| Docker Official Docs | https://docs.docker.com |
| Docker Compose Docs | https://docs.docker.com/compose |
| Node.js Docs | https://nodejs.org/docs |
| SQLite Official | https://www.sqlite.org/docs.html |
| better-sqlite3 | https://github.com/WiseLibs/better-sqlite3 |
| Nginx Docs | https://nginx.org/en/docs |

---

## 👨‍🏫 ผู้จัดทำ

| รายการ | ข้อมูล |
|--------|-------|
| **Repository** | surachai-p/booking-app-demo-2025 |
| **License** | MIT |
| **อัปเดตล่าสุด** | 2025 |

---

<div align="center">

**[🐋 เริ่มต้นทดลอง Lab 1 →](LAB_DOCKER_COMPOSE.md)**

</div>
>>>>>>> d5e83a35562b371c68ac38acfd80486ab5f0aa19

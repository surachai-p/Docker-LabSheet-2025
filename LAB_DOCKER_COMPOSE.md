# 🐋 Lab 1: Docker & Docker Compose

[← กลับหน้าหลัก](README.md)

---

## 🎯 วัตถุประสงค์การเรียนรู้

หลังจากทำการทดลองนี้แล้ว นักศึกษาจะสามารถ:

- [ ] อธิบายแนวคิดพื้นฐานของ Docker และ Container Technology ได้
- [ ] เขียน `Dockerfile` สำหรับ Node.js Backend และ Nginx Frontend ได้
- [ ] เขียน `docker-compose.yml` เพื่อรัน Multi-Service Application ได้
- [ ] ใช้คำสั่ง Docker พื้นฐานในการ Build, Run, Debug Container ได้
- [ ] อธิบาย Docker Network และ Volume ได้
- [ ] ตรวจสอบและแก้ปัญหา Container ด้วย `docker logs` และ `docker exec` ได้
### การเรียนรู้เพื่อฝึกฝนตนเองให้มีความรู้ ความชำนาญ สามารถวิเคราะห์ปัญหาได้ อย่าพึ่งพาแค่ AI โดยที่ไม่มีความรู้พื้นฐาน
### ใช้ AI อย่างชาญฉลาด เพื่อเป็นผู้ช่วยในการเรียนรู้ของตนเอง ทุกคนสามารถใช้ AI ได้ แต่คนที่ มีความรู้พื้นฐาน + AI จะกลายเป็นคนที่อยู่รอดในอนาคต
---

## 📖 สารบัญ

- [ภาคทฤษฎี](#-ภาคทฤษฎี)
  - [1.1 Docker คืออะไร](#11-docker-คืออะไร)
  - [1.2 แนวคิดสำคัญ](#12-แนวคิดสำคัญ)
  - [1.3 โครงสร้าง Dockerfile](#13-โครงสร้าง-dockerfile)
  - [1.4 Docker Compose](#14-docker-compose)
  - [1.5 Docker Volume](#15-docker-volume)
  - [1.6 สถาปัตยกรรมของ Booking App](#16-สถาปัตยกรรมของ-booking-app)
  - [1.7 คำสั่งพื้นฐาน](#17-คำสั่ง-docker-พื้นฐาน)
- [ภาคปฏิบัติ](#-ภาคปฏิบัติ)
  - [ขั้นตอนที่ 1: เตรียมสภาพแวดล้อม](#-ขั้นตอนที่-1-เตรียมสภาพแวดล้อม)
  - [ขั้นตอนที่ 2: Docker พื้นฐาน](#-ขั้นตอนที่-2-ทดลองใช้คำสั่ง-docker-พื้นฐาน)
  - [ขั้นตอนที่ 3: Dockerfile Backend](#-ขั้นตอนที่-3-เขียน-dockerfile-สำหรับ-backend)
  - [ขั้นตอนที่ 4: Dockerfile Frontend](#-ขั้นตอนที่-4-เขียน-dockerfile-สำหรับ-frontend)
  - [ขั้นตอนที่ 5: Docker Compose](#-ขั้นตอนที่-5-สร้าง-docker-compose)
  - [ขั้นตอนที่ 6: รันและทดสอบระบบ](#-ขั้นตอนที่-6-รันและทดสอบระบบ)

- [สรุปและการประเมิน](#-สรุปและการประเมิน)
- [งานเพิ่มเติม](#-งานเพิ่มเติม-challenge)

---

## 📚 ภาคทฤษฎี

### 1.1 Docker คืออะไร

**Docker** คือแพลตฟอร์ม Open-source สำหรับสร้าง ส่ง และรัน Application ใน **Container**

> **Container** = หน่วยซอฟต์แวร์ที่รวมโค้ด + Dependencies + Configuration ทั้งหมดเข้าด้วยกัน ทำให้ Application ทำงานได้เหมือนกันในทุกสภาพแวดล้อม

#### Container vs Virtual Machine

![docker-architecture](images/docker-architecture.png)

| คุณสมบัติ | Container | Virtual Machine |
|----------|-----------|----------------|
| **ขนาด** | เบา (MBs) | หนัก (GBs) |
| **เวลาเริ่มต้น** | วินาที | นาที |
| **การใช้ OS** | Share Host Kernel | OS แยกของตัวเอง |
| **Isolation** | Process Level | Hardware Level |
| **Portability** | สูงมาก | ปานกลาง |
| **Performance** | ใกล้เคียง Native | Overhead มากกว่า |

---

### 1.2 แนวคิดสำคัญ

```
Docker Ecosystem
├── 📦 Image      → Blueprint / Template สำหรับสร้าง Container
├── 🏃 Container  → Instance ที่รันจาก Image
├── 📄 Dockerfile → ไฟล์คำสั่งสำหรับสร้าง Image
├── 🌐 Docker Hub → Registry กลางสำหรับเก็บ/แชร์ Image
├── 💾 Volume     → พื้นที่เก็บข้อมูลถาวรนอก Container
└── 🔗 Network    → Virtual Network สำหรับการสื่อสารระหว่าง Container
```

#### Image Layer System
![docker-architecture](images/image-layer.png)

---

### 1.3 โครงสร้าง Dockerfile

| Instruction | ความหมาย | ตัวอย่าง |
|-------------|---------|---------|
| `FROM` | กำหนด Base Image | `FROM node:20-alpine` |
| `WORKDIR` | กำหนด Working Directory | `WORKDIR /app` |
| `COPY` | คัดลอกไฟล์จาก Host | `COPY package*.json ./` |
| `RUN` | รันคำสั่งระหว่าง Build | `RUN npm install` |
| `ENV` | กำหนด Environment Variable | `ENV PORT=5000` |
| `EXPOSE` | ระบุ Port ที่ Container ใช้ | `EXPOSE 5000` |
| `CMD` | คำสั่งเริ่มต้นเมื่อ Container รัน | `CMD ["node", "server.js"]` |
| `ENTRYPOINT` | Executable หลักของ Container | `ENTRYPOINT ["nginx"]` |
| `ARG` | Build-time Variable | `ARG NODE_ENV=production` |
| `VOLUME` | กำหนด Mount Point | `VOLUME ["/data"]` |

---

### 1.4 Docker Compose

**Docker Compose** คือเครื่องมือสำหรับนิยามและรัน **Multi-Container Application** โดยใช้ไฟล์ `docker-compose.yml`

#### โครงสร้างหลักของ docker-compose.yml

```yaml

services:          # กำหนดแต่ละ Container
  web:
    build: .       # Build จาก Dockerfile
    ports:
      - "3000:80"  # Host:Container Port Mapping
    environment:   # Environment Variables
      - NODE_ENV=production
    volumes:       # Mount Volumes
      - ./data:/app/data
    depends_on:    # ลำดับการเริ่มต้น
      - db
    networks:      # เชื่อมต่อ Network
      - app-net

  db:
    image: postgres:17-alpine   # ตัวอย่าง Image จาก Registry (ใบงานนี้ใช้ SQLite แทน)
    volumes:
      - db_data:/data/db

networks:          # กำหนด Virtual Networks
  app-net:
    driver: bridge

volumes:           # กำหนด Named Volumes
  db_data:
```

#### คำสั่ง Docker Compose ที่สำคัญ

```
docker compose up -d        → เริ่ม Service ทั้งหมด (Background)
docker compose down         → หยุดและลบ Container ทั้งหมด
docker compose down -v      → หยุด + ลบ Volume ด้วย
docker compose build        → Build Images ทั้งหมด
docker compose ps           → ดูสถานะ Service
docker compose logs -f      → ดู Log แบบ Real-time
docker compose exec <svc> sh → เข้าไปใน Container
docker compose restart <svc> → Restart Service เฉพาะ
docker compose config       → ตรวจสอบ Syntax ของ YAML
```

---

### 1.5 Docker Volume

**Docker Volume** คือกลไกที่ Docker ใช้ในการจัดการพื้นที่เก็บข้อมูลแบบ **Persistent** ซึ่งมีอายุยืนยาวกว่า Container และอยู่นอกขอบเขตของ Container Filesystem

> ⚠️ **ปัญหาหลักของ Container**: ข้อมูลที่เขียนใน Container Layer จะ **หายทันที** เมื่อ Container ถูกลบ  
> ✅ **แก้ด้วย Volume**: เก็บข้อมูลไว้นอก Container — ลบ Container กี่ครั้งก็ยังมีข้อมูล

---

#### ประเภทของ Docker Storage

```
Docker Storage Options
│
├── 📦 Volumes          ← Docker จัดการให้ (แนะนำ)
│   ├── Named Volume    ← มีชื่อ, ใช้ร่วมกันได้ระหว่าง Container
│   └── Anonymous Volume← ไม่มีชื่อ, ผูกกับ Container เดียว
│
├── 🗂️  Bind Mounts      ← Mount โฟลเดอร์จาก Host โดยตรง
│   └── /host/path:/container/path
│
└── 🧠 tmpfs Mounts     ← เก็บใน RAM (ข้อมูลหายเมื่อหยุด)
    └── ใช้สำหรับข้อมูลชั่วคราวที่ sensitive
```

---

#### เปรียบเทียบ 3 ประเภท

| คุณสมบัติ | Named Volume | Bind Mount | tmpfs |
|----------|-------------|-----------|-------|
| **ตำแหน่งเก็บข้อมูล** | Docker Area (`/var/lib/docker/volumes/`) | ใดก็ได้บน Host | RAM |
| **ข้อมูลคงอยู่หลัง rm** | ✅ ใช่ | ✅ ใช่ | ❌ ไม่ |
| **แชร์ระหว่าง Container** | ✅ ง่าย | ✅ ได้ | ❌ ไม่ |
| **Performance** | ดีมาก | ดี (Linux) | ดีที่สุด |
| **ใช้สำหรับ** | Database, ข้อมูล App | Source Code (Dev), Config | Session, Cache |
| **Backup ง่าย** | ✅ ใช่ | ✅ ใช่ | ❌ ไม่ |
| **ทำงานข้าม OS** | ✅ ทุก OS | ⚠️ path ต่างกัน | ✅ ทุก OS |

---

#### Volume Lifecycle
![docker-architecture](images/volume-life-cycle.png)

---

#### Named Volume: ทำงานอย่างไร
![docker-architecture](images/name-valume.png)

---

#### Bind Mount: ทำงานอย่างไร
![docker-architecture](images/bind-mount-2.png)

---

#### คำสั่ง Volume ที่สำคัญ

```bash
# ── Create ─────────────────────────────────────────────────
docker volume create my-volume           # สร้าง Named Volume

# ── List & Inspect ─────────────────────────────────────────
docker volume ls                         # แสดง Volume ทั้งหมด
docker volume ls --filter dangling=true  # Volume ที่ไม่มี Container ใช้
docker volume inspect my-volume          # ดูรายละเอียด (path, driver, etc.)

# ── Use in docker run ──────────────────────────────────────
docker run -v my-volume:/app/data image           # Named Volume
docker run -v $(pwd)/data:/app/data image         # Bind Mount
docker run -v /app/data image                     # Anonymous Volume
docker run --mount type=volume,src=my-volume,dst=/app/data image  # --mount syntax

# ── Remove ─────────────────────────────────────────────────
docker volume rm my-volume               # ลบ Volume (ต้อง rm container ก่อน)
docker volume prune                      # ลบ Volume ที่ไม่ได้ใช้ทั้งหมด
docker compose down -v                   # หยุด + ลบ Container + Named Volumes
```

---

#### Volume ใน Docker Compose

```yaml
services:
  backend:
    volumes:
      # รูปแบบที่ 1: Named Volume (แนะนำสำหรับ Database)
      - sqlite_data:/app/data

      # รูปแบบที่ 2: Bind Mount (สำหรับ Development)
      - ./backend:/app

      # รูปแบบที่ 3: Anonymous Volume (ไม่แนะนำ)
      - /app/node_modules

      # รูปแบบที่ 4: Read-only Bind Mount
      - ./config:/app/config:ro

volumes:
  sqlite_data:            # กำหนด Named Volume ระดับ top-level
    driver: local         # ใช้ local storage (default)
    name: booking-sqlite-data   # ชื่อที่แสดงใน docker volume ls
```

---

#### Volume กับ SQLite ใน Booking App
![docker-architecture](images/volume-sqlite.png)

---

#### Volume Backup & Restore

```bash
# ── Backup: Copy จาก Volume ไปยัง tar file ─────────────────
docker run --rm   -v booking-sqlite-data:/source:ro   -v $(pwd):/backup   alpine   tar czf /backup/booking-backup-$(date +%Y%m%d).tar.gz -C /source .

# ── Restore: Copy จาก tar file กลับเข้า Volume ────────────
docker run --rm   -v booking-sqlite-data:/target   -v $(pwd):/backup   alpine   tar xzf /backup/booking-backup-20250801.tar.gz -C /target
```

---

### 1.6 สถาปัตยกรรมของ Booking App

```
booking-app-demo-2025/
├── frontend/               ← Static HTML/CSS/JS (Nginx)
│   ├── index.html
│   ├── css/
│   └── js/
├── backend/                ← REST API (Node.js + Express)
│   ├── server.js
│   ├── models/
│   ├── routes/
│   └── package.json
├── newman/                 ← API Test Collection (Postman)
└── tests/robot/            ← E2E Tests (Robot Framework)
```

#### Data Flow
![docker-architecture](images/booking-app-architecture.png)

> 💡 **SQLite ต่างจาก MongoDB/PostgreSQL** ตรงที่ไม่ต้องรัน Database Server แยก
> ข้อมูลเก็บอยู่ใน **ไฟล์เดียว** (`booking.db`) ภายใน Backend Container

| Service | Image | Port | หน้าที่ |
|---------|-------|------|--------|
| `frontend` | `nginx:alpine` (Custom) | `3000→80` | Serve HTML + Proxy /api/ |
| `backend` | `node:20-alpine` (Custom) | `5000→5000` | REST API + SQLite Database |

---

### 1.7 คำสั่ง Docker พื้นฐาน

```
── Image Management ───────────────────────────────────
docker pull <image>              ดึง Image จาก Registry
docker images                    แสดง Image ทั้งหมด
docker build -t <name> <path>    Build Image จาก Dockerfile
docker rmi <image>               ลบ Image
docker image prune               ลบ Dangling Images

── Container Lifecycle ────────────────────────────────
docker run [flags] <image>       สร้างและรัน Container
docker start <id/name>           เริ่ม Container ที่หยุดอยู่
docker stop <id/name>            หยุด Container
docker restart <id/name>         Restart Container
docker rm <id/name>              ลบ Container (ต้อง Stop ก่อน)
docker rm -f <id/name>           Force ลบ Container

── Inspection & Debugging ─────────────────────────────
docker ps                        แสดง Container ที่รันอยู่
docker ps -a                     แสดงทุก Container
docker logs <id/name>            ดู Log
docker logs -f <id/name>         ดู Log แบบ Real-time
docker exec -it <id> bash/sh     เข้าไปใน Shell ของ Container
docker inspect <id>              ดูรายละเอียดทั้งหมด
docker stats                     ดูการใช้ Resource

── System ─────────────────────────────────────────────
docker system df                 ดูพื้นที่ที่ Docker ใช้
docker system prune              ลบสิ่งที่ไม่ใช้ทั้งหมด
docker network ls                แสดง Network ทั้งหมด
docker volume ls                 แสดง Volume ทั้งหมด
```

---

## 🔬 ภาคปฏิบัติ

> ⚠️ **สำคัญ**: ทำตามลำดับขั้นตอนโดยไม่ข้ามขั้น และบันทึกผลลัพธ์ในช่องที่กำหนดทุกขั้น

---

### 🔵 ขั้นตอนที่ 1: เตรียมสภาพแวดล้อม

**วัตถุประสงค์**: ตรวจสอบ Docker, Git และ Clone Repository

#### 1.0 Terminal ที่ใช้ในใบงาน

ใบงานนี้ใช้คำสั่ง Shell สำหรับ **macOS Terminal** และ **Windows Git Bash** ซึ่งมี syntax เหมือนกันทุกคำสั่ง

> 🪟 **Windows**: ติดตั้ง **Git for Windows** แล้วใช้ **Git Bash** ได้เลย  
> ดาวน์โหลดที่ https://git-scm.com — ทุกคำสั่งในใบงานนี้ทำงานได้ทันทีโดยไม่ต้องแก้ไข

---

#### 1.1 ตรวจสอบการติดตั้ง
**พิมพ์ และรันครั้งละ 1 คำสั่งด้วยตนเอง**
```bash
docker --version
docker compose version
git --version
docker info | head -20
```

<details>
<summary>✅ ผลลัพธ์ที่ควรได้รับ</summary>

```
Docker version 27.x.x, build xxxxxxx    ← v24.0+ ขึ้นไปทั้งหมดใช้ได้
Docker Compose version v2.29.x          ← v2.25+ จะแสดง warning ถ้ามี version:
git version 2.43.0
```
</details>

> **📝 บันทึกผล**:
![alt text](image.png) 
```

```

#### 1.2 Clone Repository

```bash
# Clone project จาก GitHub
# กรณีมี Folder นี้ที่สามารถรันได้อยู่แล้ว สามารถใช้ Folder เดิมได้ โดยไม่ต้อง Clone ใหม่
git clone https://github.com/surachai-p/booking-app-demo-2025.git

# เข้าไปยัง Directory
cd booking-app-demo-2025

# ดูโครงสร้างไฟล์
ls -la
```

<details>
<summary>✅ โครงสร้างที่ถูกต้อง</summary>

```
drwxr-xr-x  backend/
drwxr-xr-x  frontend/
drwxr-xr-x  newman/
drwxr-xr-x  node_modules/
drwxr-xr-x  reports/
drwxr-xr-x  tests/
-rw-r--r--  package.json
-rw-r--r--  README.md
```
</details>



#### 1.3 สร้าง .env File

สร้างไฟล์ `.env` ที่ Root Directory พร้อมเนื้อหาดังนี้:

```bash
# ── Database (SQLite) ─────────────────────────────────────────
# Path ภายใน Container ที่เก็บ database file
DB_PATH=/app/data/booking.db

# ── Backend ───────────────────────────────────────────────────
NODE_ENV=production
BACKEND_PORT=5000
HOST_BACKEND_PORT=5000

# ── Frontend ──────────────────────────────────────────────────
FRONTEND_PORT=3000
HOST_FRONTEND_PORT=3000
```

```bash
# เพิ่มใน .gitignore (ทุก OS)
echo ".env" >> .gitignore

# ตรวจสอบ
cat .env
```

> ⚠️ **ห้าม Commit `.env` ขึ้น GitHub** เพราะมีข้อมูลที่เป็นความลับ

**แก้ไขไฟล์​ server.js ในส่วนการกำหนด port ถ้าข้อมูลมีการแก้ไขแล้ว ให้ข้ามขั้นตอนนี้**

```bash
const PORT=process.env.BACKEND_PORT || 5000;
//const PORT       = 5000;
```
**หมายเลข Port ที่มีในตำแหน่งอื่น ๆ ให้แทนด้วย ${PORT}**
---


### 🔵 ขั้นตอนที่ 2: ทดลองใช้คำสั่ง Docker พื้นฐาน

**วัตถุประสงค์**: ฝึกใช้คำสั่ง Docker สำหรับการจัดการ Container และ Image

---

#### 2.1 Pull และรัน Nginx Container


```bash
# ดึง nginx:alpine image จาก Docker Hub
docker pull nginx:alpine

# ดู Image ที่ดาวน์โหลดมา
docker images

# รัน Container
# -d = Detached (Background)
# --name = กำหนดชื่อ Container
# -p = Map Port (Host:Container)
# กรณีที่ port 8080 ถูกใช้งานอยู่ สามารถเปลี่ยนเป็น port อื่นได้ เช่น 8081
# กรณีที่ต้องการยกเลิกหรือ kill process ที่ใช้งาน port สามารถใช้คำสั่ง npx kill-port 8080
docker run -d --name my-nginx -p 8080:80 nginx:alpine

# ตรวจสอบ Container ที่กำลังรัน
docker ps
```
![docker maping port](images/docker-map-port.png)

<details>
<summary>✅ ผลลัพธ์ที่คาดหวัง</summary>

```
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS        PORTS
a1b2c3d4e5f6   nginx:alpine   "/docker-entrypoint.…"   2 seconds ago  Up 2 seconds  0.0.0.0:8080->80/tcp
```
</details>

**บันทึกผลการทดลอง**
```
![alt text](image-1.png)
```

เปิด Browser ไปที่ **http://localhost:8080** ควรเห็นหน้า `Welcome to nginx!`

**อธิบาย แต่ละส่วนของคำสั่ง docker run -d --name my-nginx -p 8080:80 nginx:alpine**
```text
docker run คำสั่งให้ Docker สร้างและเริ่มการทำงานของ container ใหม่
-d คือ Detached Mode คือการสั่งให้ Container ทำงานในพื้นหลัง เราสามารถใช้ Terminal ต่อได้โดยที่ Container ไม่ปิดตัวลง
--name my-nginx เป็นการตั้งชื่อให้ Container ว่า my-nginx
-p 8080:80 การทำ Port mapping เพื่อเชื่อมโลกภายนอกกับ Container 8080 คือพอร์ตบนเครื่อง 80 คือพอร์ต Service ใน Container
nginx:alpine คือชื่อของ image ที่จะนำมาใช้ nginx คือ Software Web Server ,alpine คือ Tag ของ Images ที่เน้นขนาดเล็กพิเศษ
```



---

#### 2.2 ตรวจสอบ Container

```bash
# ดู Log ของ Nginx
docker logs my-nginx

# ดู Log แบบ Follow เพื่อติดตามดู log(กด Ctrl+C เพื่อออก)
docker logs -f my-nginx

# เข้าไปใน Shell ของ Container
docker exec -it my-nginx sh

# คำสั่งภายใน Container (หลัง exec):
ls /usr/share/nginx/html      # ดูไฟล์ที่ Nginx Serve
cat /usr/share/nginx/html/index.html   # ดูเนื้อหา HTML
nginx -v                       # ดู Nginx version
exit                           # ออกจาก Container Shell
```

<details>
<summary>💡 อธิบายคำสั่ง exec</summary>

```
docker exec -it my-nginx sh
            │  │
            │  └── -t: Allocate a pseudo-TTY (terminal)
            └───── -i: Keep STDIN open (Interactive)

เทียบเท่ากับการ SSH เข้าไปใน Container
ทุกอย่างที่ทำใน Shell นี้อยู่ภายใน Container เท่านั้น
```
![docker exec](images/docker-exec-it.png)

**บันทึกผลการรันคำสั่ง docker exec -it และ ls /usr/share/nginx/html**

   ```bash
   ![alt text](image-2.png)
   ```
</details>

---

#### 2.3 ดูรายละเอียดและ Inspect

```bash
# ดูรายละเอียดทั้งหมดของ Container (JSON format)
docker inspect my-nginx

# ดูเฉพาะ IP Address
docker inspect my-nginx --format='{{.NetworkSettings.IPAddress}}'

# ดูการใช้ Resource (CPU, Memory, Network)
docker stats my-nginx
# กด Ctrl+C เพื่อออก
```

> **📝 บันทึกผล**: Container ID คือ: `0438f77f4ec7e12e9c73377701c040d5b06328d72d4d47ef094d79fa974a098a` และ IP Address คือ: `172.17.0.2`

---

#### 2.4 Lifecycle: Stop, Start, Remove

```bash
# หยุด Container
docker stop my-nginx

# ดูสถานะ (ควรแสดง Exited)
docker ps -a

# เริ่ม Container ใหม่
docker start my-nginx

# ดูสถานะอีกครั้ง (ควรแสดง Up)
docker ps

# หยุดและลบ Container
docker stop my-nginx
docker rm my-nginx

# ตรวจสอบ (ไม่ควรมี my-nginx แล้ว)
docker ps -a
```

---

#### 2.5 ทดลอง Node.js Container

```bash
# รัน Node.js Container แบบ Interactive
# --rm = ลบ Container อัตโนมัติเมื่อออกจาก container ด้วยคำสั่ง exit
docker run -it --rm node:20-alpine sh

# ภายใน Container:
node --version
npm --version
node -e "console.log('Hello from Docker! Running in:', process.env.HOSTNAME)"
exit
```
<details>
<summary>💡 ความหมายของ flags ใน docker run</summary>

| Flag | ความหมาย |
|------|---------|
| `-d` | Detached — รันใน Background |
| `-it` | Interactive + TTY — รันแบบ Interactive |
| `--rm` | ลบ Container อัตโนมัติเมื่อหยุด |
| `--name` | กำหนดชื่อ Container |
| `-p host port:container port` | Map Port จาก Host ไปยัง Container |
| `-e KEY=VALUE` | กำหนด Environment Variable |
| `-v host path:container path` | Mount Volume |
| `--network` | กำหนด Network |
</details>

**บันทึกรูปผลการทดลอง**
```text
บันทึกรูปผลการทดลองที่นี่
```
---

### ❓ คำถามท้ายขั้นตอนที่ 2

1. `docker ps` กับ `docker ps -a` ต่างกันอย่างไร?

   > _คำตอบ_: docker ps ใช้ดู containers ที่ Running อยู่ , docker ps -a ใช้ดู container ทั้งหมดในเครื่องเรา

2. ขนาดของ `nginx:alpine` image คือเท่าไร?

   > _คำตอบ_: ตัวเลขขนาดโดยประมาณ ขนาดตอนดาวน์โหลด (Compressed Size): ประมาณ 10 - 15 MB, ขนาดบน Disk (Uncompressed/Image Size): ประมาณ 40 - 45 MB

3. flag `--rm` ใน `docker run` มีประโยชน์ในกรณีใด?

   > _คำตอบ_: มีประโยชน์ในกรณี: ป้องกันขยะค้างเครื่อง: ไม่ต้องตามลบ Container (สถานะ Exited) เองภายหลัง, งานชั่วคราว (One-off tasks): เช่น การสั่งรันสคริปต์, การ Build งาน หรือการทดสอบคำสั่งสั้นๆ, การ Debug: ใช้มุดเข้าไปเช็คไฟล์ใน Image แล้วจบงาน, CI/CD: ใช้รันขั้นตอนทดสอบในระบบอัตโนมัติเพื่อประหยัดพื้นที่ Disk

4. `docker exec -it` ต่างจาก `docker run -it` อย่างไร?

   > _คำตอบ_: docker run -it ใช้สร้างและเริ่ม container ใหม่จาก image, docker exec -it ใช้สั่งงาน container ที่กำลัง run อยู่แล้ว

5. ต้องการดูว่าในเครื่องมี image อะไรอยู่บ้าง จะเขียนคำสั่งอย่างไร
   ```bash
   docker images
   ```
6. ต้องการลบ image ชื่อ nginx:alpine จะต้องเขียนคำสั่งอย่างไร หากมีหลายขั้นตอนที่ต้องเขียน ให้เขียนลำดับคำสั่งให้ถูกต้อง
   ```bash
   1. docker stop <container_id_>
   2. docker rm <container_id>
   3. docker rmi mginx:alpine
   ```
7. เมื่อลบ image แล้วให้ทำการ pull image กลับมาเหมือนเดิม พร้อมทำการรัน container
   ```bash
   docker run -d --name my-nignx -p 80:80 nginx:alpine
   ```
---

### 🔵 ขั้นตอนที่ 3: เขียน Dockerfile สำหรับ Backend

**วัตถุประสงค์**: สร้าง Docker Image สำหรับ Node.js Express API

---

#### 3.1 ศึกษา Backend Code

```bash
# ดู Entry Point ของ Application
cat backend/server.js

# ดู Dependencies ทั้งหมด
cat backend/package.json

# ดู API Routes
ls backend
```

<details>
<summary>💡 สิ่งที่ต้องรู้ก่อนเขียน Dockerfile</summary>

จาก `package.json` สังเกตว่า:
- **start script** คืออะไร → ใช้ใน `CMD` จากตัวอย่างคือ `node server.js`
- **node version** ที่ต้องการ → ใช้ใน `FROM` จากตัวอย่างคือ `1.0.0`
- **port** ที่ใช้ → ใช้ใน `EXPOSE`
- **better-sqlite3** ต้องการ compile native module → ต้องเพิ่ม build tools ใน Alpine
</details>

---

#### 3.2 สร้าง `.dockerignore`

สร้างไฟล์ `backend/.dockerignore` พร้อมเนื้อหาดังนี้:

```bash
cat > backend/.dockerignore << 'EOF'
node_modules
npm-debug.log
.env
.env.local
.env.*.local
.git
.gitignore
*.md
coverage/
*.test.js
*.spec.js
EOF
```

```bash
# ตรวจสอบ
cat backend/.dockerignore
```

> **หมายเหตุ**: `.dockerignore` ทำงานเหมือน `.gitignore` แต่สำหรับ Docker Build Context

---

#### 3.3 เขียน Dockerfile สำหรับ Backend

สร้างไฟล์ `backend/Dockerfile` ที่มีเนื้อหาดังนี้:

```bash
# ─────────────────────────────────────────────────────────────
# Stage: Production Environment
# Base Image: node:20-alpine (Active LTS — node:18 EOL เม.ย. 2025)
# ─────────────────────────────────────────────────────────────
FROM node:20-alpine

# ─── Build Tools สำหรับ better-sqlite3 ────────────────────
# better-sqlite3 เป็น Native Module ต้องการ C++ compiler
# python3 + make + g++ ใช้ตอน Build เท่านั้น
RUN apk add --no-cache python3 make g++

# กำหนด Working Directory ภายใน Container
WORKDIR /app

# ─── Install Dependencies ──────────────────────────────────
# คัดลอก package files ก่อน (เพื่อใช้ Layer Cache)
# ถ้า package.json ไม่เปลี่ยน → npm install จะใช้ Cache
COPY package*.json ./

# ติดตั้ง Production Dependencies เท่านั้น
RUN npm install --omit=dev

# ─── Copy Source Code ─────────────────────────────────────
# คัดลอก Source Code (ทำทีหลังเพื่อ Cache Optimization)
COPY . .

# ─── Database Directory ───────────────────────────────────
# สร้างโฟลเดอร์สำหรับเก็บ SQLite database file
RUN mkdir -p /app/data

# ─── Configuration ────────────────────────────────────────
# รวม ENV ไว้บรรทัดเดียว = ลด Layer 1 ชั้น (Best Practice)
ENV NODE_ENV=production PORT=5000 DB_PATH=/app/data/booking.db

# ระบุ Port ที่ Application ฟัง
EXPOSE 5000

# ─── Start Application ────────────────────────────────────
# CMD จะถูกแทนที่ได้เมื่อรัน Container
CMD ["node", "server.js"]
```

```bash
# ตรวจสอบเนื้อหาไฟล์
cat backend/Dockerfile
```

<details>
<summary>💡 ทำไมต้อง COPY package*.json ./ ก่อน?</summary>

```
# แบบไม่ดี (ทุกครั้งที่แก้โค้ด จะ npm install ใหม่)
COPY . .
RUN npm install

# แบบดี (ใช้ Cache ได้)
COPY package*.json ./    ← Layer นี้ Cache ได้ (เปลี่ยนเฉพาะเมื่อ package.json เปลี่ยน)
RUN npm install          ← ใช้ Cache ถ้า Layer ก่อนหน้าไม่เปลี่ยน
COPY . .                 ← Layer นี้เปลี่ยนบ่อย แต่ npm install ไม่ต้องรันใหม่
```

> **📌 หมายเหตุ SQLite**: `better-sqlite3` ต้องการ `python3 make g++` ใน Alpine
> ใน Production ควรใช้ Multi-stage Build เพื่อไม่ให้ build tools ติดไปใน Image สุดท้าย
</details>

**Multi-stage Build คืออะไร?**
```
Multi-stage Build คือเทคนิคการเขียน Dockerfile แบบ "แบ่งขั้นตอน" เพื่อแยกส่วนที่ใช้ Build ออกจากส่วนที่ใช้ Run

Stage 1 (Build): ใช้ Image ตัวใหญ่ที่มีเครื่องมือครบ (Compiler, SDK) เพื่อสร้างไฟล์งานออกมา

Stage 2 (Final): สร้าง Image ใหม่ตัวเล็กจิ๋ว แล้ว Copy เฉพาะไฟล์ที่ Build เสร็จ มาใส่
```
---

#### 3.4 Build Backend Image

```bash
# Build Image จาก Dockerfile ใน ./backend
# -t คือ Tag ในรูปแบบ name:version
docker build -t booking-backend:1.0 ./backend

# ดูกระบวนการ Build แบบ Detail
docker build -t booking-backend:1.0 ./backend --progress=plain 2>&1 | head -50

# ตรวจสอบ Image ที่สร้างได้
docker images | grep booking

# ดูรายละเอียด Image (Layer History)
docker history booking-backend:1.0
```

<details>
<summary>✅ ผลลัพธ์ที่คาดหวัง</summary>

```
REPOSITORY         TAG    IMAGE ID       CREATED         SIZE
booking-backend    1.0    abc123def456   5 seconds ago   ~200MB
```
</details>

> **📝 บันทึกผล**: ขนาดของ booking-backend:1.0 คือ: `484` MB 

---

#### 3.5 ทดสอบรัน Backend Container

```bash
# สร้าง Network เพื่อใช้งานร่วมกันระหว่าง backend และ frontend โดยตั้งชื่อ network ว่า booking-network
docker network create booking-network

# การระบุ port  -p 5000:5000 หาก server.js ระบุ port ในการรันคือ 3000 คำสั่งต้องแก้ไขเป็น -p 5000:3000 เพื่อ map จาก port 5000 ของ host ไปยัง port 3000 ของ container backend

docker run -d --name backend --network booking-network -p 5000:5000 -e DB_PATH=/app/data/booking.db -v $(pwd)/test-data:/app/data booking-backend:1.0
```
**คำถามการทดลอง**
**อธิบายคำสั่งในส่วน -e DB_PATH=/app/data/booking.db -v $(pwd)/test-data:/app/data**
```
1. -e DB_PATH=/app/data/booking.db (Environment Variable)
-e ย่อมาจาก --env: ใช้สำหรับกำหนด "ตัวแปรสภาพแวดล้อม" ให้กับแอปพลิเคชันที่รันอยู่ข้างใน

ความหมาย: บอกให้ Code (Node.js) รู้ว่าไฟล์ Database อยู่ที่ไหน โดยใน Code ของคุณจะดึงค่านี้ไปใช้ผ่าน process.env.DB_PATH

ประโยชน์: ทำให้เราเปลี่ยนที่อยู่ไฟล์หรือตั้งค่าต่างๆ ได้โดย ไม่ต้องแก้ Code แค่เปลี่ยนตอนสั่ง docker run ก็พอ

2. -v $(pwd)/test-data:/app/data (Bind Mount Volume)
-v ย่อมาจาก --volume: ใช้สำหรับ "เชื่อมโยงโฟลเดอร์" ระหว่างเครื่องเรา (Host) กับ Container

โครงสร้าง: -v [เครื่องเรา]:[ใน Container]

$(pwd)/test-data: คือโฟลเดอร์ในเครื่องเรา ($(pwd) คือตำแหน่งปัจจุบันที่คุณอยู่)

:/app/data: คือตำแหน่งโฟลเดอร์ข้างใน Container

ประโยชน์หลัก:

Data Persistence: ปกติถ้า Container ถูกลบ ข้อมูลข้างในจะหายหมด แต่การใช้ -v จะทำให้ไฟล์ฐานข้อมูลถูกเก็บไว้ในเครื่องเราจริงๆ ข้อมูลจึง ไม่หาย

Easy Access: คุณสามารถเอาไฟล์จากเครื่องเราใส่เข้าไปใน Container ได้ง่ายๆ แค่ลากไฟล์ลงโฟลเดอร์ test-data

สรุปการทำงานร่วมกัน
เมื่อรันคำสั่งนี้:

Docker จะเอาโฟลเดอร์ test-data ในเครื่องคุณไปแปะทับไว้ที่ /app/data ใน Container

ตัวแปร DB_PATH จะชี้ไปที่ไฟล์ภายในโฟลเดอร์นั้น

ผลลัพธ์: แอปจะอ่าน/เขียนไฟล์ Database ลงในเครื่องคุณโดยตรงผ่านทางช่องเชื่อมต่อนี้ครับ
```

```bash
# ดู Log เพื่อตรวจสอบการเริ่มต้น
docker logs backend

# ทดสอบ API (SQLite สร้างไฟล์ .db อัตโนมัติ ไม่ต้องติดตั้ง Server)
curl http://localhost:5000

# ลบ Container ทดสอบ
docker stop backend
docker rm backend
```
#### เปิด web browser แล้วทดสอบเข้าที่ http://localhost:5000/api-docs

**บันทึกผลการทดลอง**
```
บันทึกรูปผลการรัน curl http://localhost:5000
![alt text](image-3.png)
ก่อนจะลบ Container ทดสอบสามารถเข้าใช้งานได้ตามปกติแต่หลังจากที่ลบจึงไม่สามารถเข้าใช้งานได้
```
---

### ❓ คำถามท้ายขั้นตอนที่ 3

1. `booking-backend:1.0` คืออะไร?

   > _คำตอบ_: ชื่อและเวอร์ชันของ Docker Image ที่คุณสร้างขึ้นครับ โดยสามารถแยกส่วนประกอบออกเป็น 2 ส่วนหลักที่เรียกว่า Repository และ Tag ดังนี้:

1. booking-backend (Repository Name)
คือ ชื่อของ Image เพื่อให้เราจำได้ว่า Image นี้คือโปรแกรมอะไร

เปรียบเสมือน "ชื่อโปรแกรม" เช่น Line, Chrome หรือในกรณีของคุณคือระบบ Backend ของโปรเจกต์ Booking

2. 1.0 (Tag)
คือ ป้ายระบุเวอร์ชัน (Version) หรือสถานะของ Image นั้น

เปรียบเสมือน "เลขเวอร์ชัน" ของซอฟต์แวร์

ประโยชน์: ช่วยให้เราบริหารจัดการได้ว่าอันไหนคือตัวเก่า อันไหนคือตัวใหม่ (เช่น 1.0, 2.0, testing, production)

ข้อควรระวัง: ถ้าคุณไม่ใส่ Tag (เช่น พิมพ์แค่ booking-backend) Docker จะใส่ Tag ให้เองอัตโนมัติเป็น :latest

2. ถ้าต้องการให้ ทดสอบ API ด้วย `curl http://localhost` ต้องทำอย่างไร?

   > _คำตอบ_: 1. การตั้งค่าตอนรัน Container (Port Mapping)
หัวใจสำคัญคือคุณต้องเชื่อมต่อ Port 80 ของเครื่องเรา เข้ากับ Port ที่แอปข้างใน Container ใช้งาน (จาก Dockerfile ของคุณคือ Port 5000)

ใช้คำสั่ง docker run พร้อมกับ Flag -p ดังนี้:

Bash
docker run -d \
  -p 80:5000 \
  --name my-api \
  booking-backend:1.0
80:5000: หมายถึงเมื่อเราเรียก http://localhost (ซึ่งปกติคือ Port 80) Docker จะส่งข้อมูลไปที่ Port 5000 ใน Container ให้โดยอัตโนมัติ

2. การใช้คำสั่ง curl เพื่อทดสอบ
เมื่อ Container รันแล้ว ให้เปิด Terminal ใหม่แล้วพิมพ์:

ทดสอบแบบปกติ:

Bash
curl http://localhost
ทดสอบแบบดูรายละเอียด Header (ดูว่าต่อติดไหม/ได้สถานะ 200 หรือเปล่า):

Bash
curl -i http://localhost
ถ้า API ของคุณมี Path เพิ่มเติม (เช่น /api/bookings):

Bash
curl http://localhost/api/bookings

---

### 🔵 ขั้นตอนที่ 4: เขียน Dockerfile สำหรับ Frontend

**วัตถุประสงค์**: สร้าง Docker Image สำหรับ Static Website ด้วย Nginx

---

#### 4.1 ศึกษา Frontend Structure

```bash
# ดูโครงสร้าง Frontend
ls -la frontend/
cat frontend/index.html | head -30
```

> Frontend เป็น Static Website (HTML + CSS + JS) ไม่ต้อง Build → ใช้ Nginx Serve โดยตรง

---

#### 4.2 สร้าง Nginx Configuration

สร้างไฟล์ `frontend/nginx.conf` พร้อมเนื้อหาดังนี้:
**เลข Port 5000 คือ Host port ที่จะ map ไปยัง Port ของ backend container กรณีที่ Container run ที่ port อื่นให้เปลี่ยนเลข 5000 เป็นเลข Port ของ backend**
```bash
server {
    listen 80;
    server_name localhost;

    # Root Directory สำหรับ Static Files
    root /usr/share/nginx/html;
    index index.html;

    # Handle Client-side Routing (SPA)
    location / {
        try_files $uri $uri/ /index.html;
    }

    # Proxy API requests ไปยัง Backend Container
    # "backend" คือชื่อ Service ใน docker-compose.yml
    # เลข Port 5000 คือ Host port ที่จะ map ไปยัง Port ของ backend container กรณีที่ Container run ที่ port อื่นให้เปลี่ยนเลข 5000 เป็นเลข Port ของ backend container
    location /api/ {
        proxy_pass         http://backend:5000;
        proxy_http_version 1.1;
        proxy_set_header   Upgrade $http_upgrade;
        proxy_set_header   Connection 'upgrade';
        proxy_set_header   Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header   X-Real-IP $remote_addr;
    }

    # Cache Static Assets (1 ปี)
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # Gzip Compression
    gzip on;
    gzip_types text/plain text/css application/json application/javascript;
}
```

```bash
# ตรวจสอบ
cat frontend/nginx.conf
```

<details>
<summary>💡 ทำไม proxy_pass ในส่วนของการระบุ proxy_pass   http://backend:5000/api/; ใช้ชื่อ backend แทนการใช้ localhost?</summary>

ใน Docker Network, Container สามารถค้นหากันได้ด้วย **Service Name** (ในกรณีนี้ ไฟล์ docker-compose.yml ต้องกำหนดชื่อ service ของส่วน API Server ว่า **backend**) 

```
frontend container → DNS lookup "backend" → backend container IP
```

เหมือนกับการใช้ Hostname ชื่อ backend แทน IP Address ซึ่งเปลี่ยนแปลงได้
</details>

---

#### 4.3 เขียน Dockerfile สำหรับ Frontend

สร้างไฟล์ `frontend/Dockerfile` พร้อมเนื้อหาดังนี้:

```bash
# Stage 1: Build (ขั้นตอนปรุงอาหาร)
FROM node:20-alpine AS build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Production (ขั้นตอนเสิร์ฟ)
FROM nginx:stable-alpine
# ก๊อปปี้เฉพาะไฟล์ที่ Build เสร็จแล้ว (อยู่ในโฟลเดอร์ dist) ไปที่ Nginx
COPY --from=build-stage /app/dist /usr/share/nginx/html

# (อย่าลืมก๊อปปี้ nginx.conf ของคุณไปด้วย)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

```bash
# ตรวจสอบ
cat frontend/Dockerfile
```

<details>
<summary>💡 ทำไม CMD ต้องมี daemon off?</summary>

Docker Container จะหยุดทำงานเมื่อ Process หลัก (PID 1) สิ้นสุด

```
# Nginx ปกติ (Background daemon) → Process หลักจบทันที → Container หยุด ❌
CMD ["nginx"]

# Nginx Foreground → Process หลักทำงานต่อเนื่อง → Container ยังรัน ✅
CMD ["nginx", "-g", "daemon off;"]
```
</details>

---

#### 4.4 Build Frontend Image
**ก่อนรันคำสั่ง ให้อยู่ที่ไดเรคทอรี่ booking-app-demo-2025**
```bash
# Build Frontend Image
docker build -t booking-frontend:1.0 ./frontend

# เปรียบเทียบขนาด
docker images | grep booking

# ทดสอบรัน Frontend 
# ก่อนการรันให้ตรวจสอบว่า Port 3000 บนเครื่องไม่มีแอปพลิเคชั่นอื่นใช้งานอยู่
docker run -d --name booking-frontend-test -p 3000:80 --network booking-network booking-frontend:1.0

# เปิด Browser ไปที่ http://localhost:3000
curl -I http://localhost:3000

# ดู Configuration ของ Nginx
docker exec booking-frontend-test cat /etc/nginx/conf.d/nginx.conf

# ลบ Container ทดสอบ
docker stop booking-frontend-test && docker rm booking-frontend-test
```

> **📝 บันทึกผล**: booking-frontend:1.0 ขนาด `31` MB | booking-backend:1.0 ขนาด `178` MB

---

### ❓ คำถามท้ายขั้นตอนที่ 4

1. ขนาดของ `booking-frontend:1.0` เทียบกับ `booking-backend:1.0` ต่างกันอย่างไร? เพราะเหตุใด?

   > _คำตอบ_: โดยปกติแล้ว booking-frontend:1.0 จะมีขนาดใหญ่กว่า booking-backend:1.0 อย่างมาก (มักจะต่างกันหลายเท่าตัว) แม้ว่าทั้งคู่จะเป็นแอปพลิเคชัน Node.js เหมือนกันก็ตามครับ

เหตุผลหลักที่ทำให้ขนาดต่างกัน:
1. ความซับซ้อนของ Dependencies (node_modules)
Frontend: มักใช้ Framework เช่น React, Vue หรือ Next.js ซึ่งมี "ของแถม" เยอะมาก ทั้งตัวช่วยสร้าง UI, ตัวจัดการ State, ระบบ Routing และเครื่องมือสำหรับ Compile โค้ด (เช่น Webpack, Vite, Babel) ทำให้โฟลเดอร์ node_modules บวมขึ้นอย่างรวดเร็ว

Backend: หากเป็น API ขนาดเล็กที่ใช้ Express และ SQLite ตามที่คุณทำ จะมี Library ที่จำเป็นต้องใช้เพียงไม่กี่ตัว ขนาดจึงเบากว่ามาก

2. สภาพแวดล้อมในการทำงาน (Runtime vs. Build Tooling)
Frontend: ในขั้นตอนการสร้าง (Build) จำเป็นต้องใช้เครื่องมือหนักๆ ในการแปลงโค้ด Modern JS ให้กลายเป็นไฟล์ Static (HTML/CSS/JS) ซึ่งถ้าเราไม่ได้ใช้เทคนิค Multi-stage Build เครื่องมือเหล่านี้จะถูกขังอยู่ใน Image สุดท้ายด้วย

Backend: มักจะรันโค้ดตรงๆ ผ่าน Node.js Runtime ได้เลย ไม่ต้องผ่านกระบวนการแปลงไฟล์ที่ซับซ้อนเท่าฝั่งหน้าบ้าน

3. Base Image ที่ใช้
หากฝั่ง Backend ใช้ Base Image แบบ Alpine (เช่น node:20-alpine) จะมีขนาดเริ่มต้นเพียงประมาณ 50MB

แต่ถ้าฝั่ง Frontend ไม่ได้ระบุว่าเป็น Alpine หรือใช้ Image มาตรฐานตัวเต็ม ขนาดเริ่มต้นอาจพุ่งไปถึง 300MB - 900MB ตั้งแต่ยังไม่ได้เริ่มลงโปรแกรมเลยครับ

2. `location /api/` ใน nginx.conf ทำหน้าที่อะไร?

   > _คำตอบ_: ใน nginx.conf ส่วนของ location /api/ ทำหน้าที่เป็น "พนักงานแยกเส้นทาง" (Reverse Proxy) เพื่อส่งต่อคำขอ (Request) ไปยังเครื่องต้นทางที่ถูกต้องครับ

หน้าที่หลักของมันมี 3 อย่าง:
1. การทำ Reverse Proxy (ส่งต่อคำขอ)
เมื่อมี User เรียกใช้งานผ่าน Browser มาที่ http://localhost/api/users ตัว Nginx จะดูที่ Path ว่าขึ้นต้นด้วย /api/ หรือไม่? ถ้าใช่ มันจะส่งต่อนิ้วไปที่ Backend Service (เช่น http://backend:5000) ทันที

ประโยชน์: User ไม่ต้องรู้ว่า Backend จริงๆ อยู่ที่ไหน หรือรัน Port อะไร รู้แค่ว่าเรียกผ่าน Nginx (Port 80) ที่เดียวจบ

2. การจัดการเรื่อง CORS (Cross-Origin Resource Sharing)
เนื่องจาก Frontend และ Backend รันอยู่คนละที่ (คนละ Port/Service) ปกติ Browser จะสั่งบล็อกการดึงข้อมูล แต่เมื่อเราใช้ Nginx มาบังหน้า (Proxy) ทั้งคู่จะเสมือนรันอยู่บน Domain และ Port เดียวกัน ทำให้ปัญหาเรื่อง CORS หมดไปโดยไม่ต้องแก้ Code ใน Backend เลยครับ

3. การตัดหรือจัดการ Path (Rewriting)
บางครั้งเราตั้งค่าให้ Nginx ตัดคำว่า /api ออกก่อนส่งไปหา Backend (ถ้า Backend ไม่ได้เขียนรอรับ Path /api) หรือเติม Path บางอย่างเข้าไปโดยอัตโนมัติ

3. ทำไม Frontend Container ถึงใช้ชื่อ `backend` ในการ Proxy ได้?

   > _คำตอบ_: สาเหตุที่ Frontend (หรือ Nginx) สามารถเรียกใช้ชื่อ backend ได้โดยตรง เป็นเพราะคุณสมบัติที่เรียกว่า Docker Embedded DNS ครับ

1. ระบบ DNS ภายในของ Docker
เมื่อเราใช้งาน Docker Compose หรือสร้าง User-defined Network ขึ้นมา Docker จะสร้างระบบจัดการชื่อโดเมน (DNS) ให้โดยอัตโนมัติ

ชื่อ Service = ชื่อ Domain: ทุกตัวที่อยู่ใน Network เดียวกัน จะสามารถ "คุย" กันได้ด้วยชื่อ Service ที่เราตั้งไว้ในไฟล์ docker-compose.yml

ตัวอย่าง: หากคุณตั้งชื่อ Service ว่า backend ในไฟล์ Compose ตัว Docker Engine จะทำหน้าที่เหมือนสมุดโทรศัพท์ เมื่อ Nginx ถามหา http://backend ตัว Docker DNS จะตอบกลับเป็น IP Address จริง ของ Container นั้นให้ทันที

2. ประโยชน์ของการใช้ชื่อแทน IP
IP ไม่คงที่: ทุกครั้งที่ Restart หรือลบ Container แล้วสร้างใหม่ IP Address มักจะเปลี่ยนไปเรื่อยๆ (เช่น จาก 172.18.0.3 เป็น 172.18.0.5)

ชื่อคงที่เสมอ: ไม่ว่า IP จะเปลี่ยนไปกี่ครั้ง แต่ชื่อ backend จะยังคงชี้ไปยัง Container ที่ถูกต้องเสมอ ทำให้เราไม่ต้องตามไปแก้ไฟล์ nginx.conf บ่อยๆ

---

### 🔵 ขั้นตอนที่ 5: สร้าง Docker Compose

**วัตถุประสงค์**: เชื่อม Frontend กับ Backend และกำหนด SQLite Volume ให้ถูกต้อง 

---

#### 5.1 สร้าง docker-compose.yml

สร้างไฟล์ `docker-compose.yml` ที่ Root Directory พร้อมเนื้อหาดังนี้:

```bash
# ══════════════════════════════════════════════════════
#  Compose Specification (ไม่ต้องระบุ version แล้ว)
#  https://docs.docker.com/compose/compose-file/
# ══════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════
#  Services (SQLite ไม่ต้อง Database Container แยก!)
# ══════════════════════════════════════════════════════
services:

  # ─── Backend API + SQLite ─────────────────────────────
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: booking-backend
    restart: unless-stopped
    environment:
      NODE_ENV: ${NODE_ENV}
      BACKEND_PORT: ${BACKEND_PORT}
      DB_PATH: ${DB_PATH}          # Path ของ SQLite file ใน Container
    ports:
      - "${HOST_BACKEND_PORT}:${BACKEND_PORT}"
    volumes:
      # Mount Volume เพื่อให้ booking.db อยู่รอดเมื่อ Container ถูก restart
      - sqlite_data:/app/data
    networks:
      - booking-net
    # หมายเหตุ: ไม่มี depends_on เพราะ SQLite ไม่มี Database Server
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:${BACKEND_PORT}/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s

  # ─── Frontend Web ─────────────────────────────────────
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: booking-frontend
    restart: unless-stopped
    ports:
      - "${HOST_FRONTEND_PORT}:${FRONTEND_PORT}"
    depends_on:
      backend:
        condition: service_healthy
    networks:
      - booking-net

# ══════════════════════════════════════════════════════
#  Networks
# ══════════════════════════════════════════════════════
networks:
  booking-net:
    driver: bridge
    name: booking-network

# ══════════════════════════════════════════════════════
#  Volumes — เก็บ SQLite .db file ให้อยู่รอดข้าม restart
# ══════════════════════════════════════════════════════
volumes:
  sqlite_data:
    driver: local
    name: booking-sqlite-data
```

```bash
# ตรวจสอบ
cat docker-compose.yml
```

---

#### 5.2 ตรวจสอบ Configuration

```bash
# Validate docker-compose.yml syntax
docker compose config

# ดูรายการ Service ทั้งหมด
docker compose config --services
```

<details>
<summary>✅ ผลลัพธ์ที่ถูกต้อง</summary>

```
# docker compose config --services ควรแสดง:
backend
frontend
```

</details>

---

### ❓ คำถามท้ายขั้นตอนที่ 5

1. docker-compose.yml คืออะไร มีประโยชน์อย่างไร?

   > _คำตอบ_: docker-compose.yml คือไฟล์ที่ใช้สำหรับ "นิยาม (Define) และรัน" แอปพลิเคชันที่ประกอบด้วยหลายๆ Container พร้อมกัน โดยเขียนอยู่ในรูปแบบภาษา YAML ซึ่งอ่านง่ายและเป็นระเบียบครับ

ประโยชน์ของ docker-compose.yml
จัดการหลาย Container ในคำสั่งเดียว: แทนที่คุณจะต้องพิมพ์ docker run ยาวๆ ทีละตัวสำหรับ Database, Backend และ Frontend คุณแค่พิมพ์ docker compose up คำสั่งเดียว ระบบจะรันทุกอย่างให้ตามที่เขียนไว้ในไฟล์

บันทึกการตั้งค่าไว้เป็นลายลักษณ์อักษร: ทุกการตั้งค่า เช่น การ Map Port (-p), การทำ Volume (-v), และการตั้งค่า Environment (-e) จะถูกบันทึกไว้ในไฟล์นี้ ไม่ต้องกลัวลืมคำสั่งรัน

สร้าง Network ให้อัตโนมัติ: Docker Compose จะสร้าง Network วงเดียวกันให้ทุก Service ในไฟล์ ทำให้พวกมันคุยกันได้ผ่าน "ชื่อ Service" (เช่น Backend ต่อไปที่ DB โดยใช้ชื่อ db ได้เลย ไม่ต้องใช้ IP)

Environment Isolation: สามารถจำลองสภาพแวดล้อมที่เหมือนกันเป๊ะๆ ให้กับทีมพัฒนาคนอื่นๆ หรือรันบน Server จริงได้เพียงแค่ส่งไฟล์นี้ไป

2. `restart: unless-stopped` หมายความว่าอย่างไร?

   > _คำตอบ_: restart: unless-stopped คือ นโยบายการเริ่มใหม่ (Restart Policy) ของ Container ที่ออกแบบมาให้สมดุลที่สุดสำหรับการใช้งานทั่วไป มีความหมายตรงตัวคือ:"ให้ Docker สั่ง Restart Container นี้โดยอัตโนมัติเสมอ ยกเว้นแต่ว่าเจ้าของเครื่อง (เรา) จะเป็นคนสั่ง Stop มันเองด้วยมือ"รายละเอียดการทำงานถ้า Container ล่ม (Crash): Docker จะสั่ง Restart ให้ใหม่ทันทีถ้า Restart เครื่อง Server: เมื่อเครื่องเปิดกลับมาใหม่ Docker Daemon จะสั่งให้ Container นี้รันขึ้นมาเองโดยอัตโนมัติถ้าเราสั่ง docker stop: Docker จะ ไม่ สั่งรันใหม่จนกว่าเราจะสั่ง docker start อีกครั้ง (นี่คือจุดที่ต่างจาก always)เปรียบเทียบกับนโยบายอื่นๆนโยบายการทำงานno (Default)ไม่สั่ง Restart ใหม่ในทุกกรณีon-failureRestart เฉพาะตอนที่แอปพัง (Exit code ไม่ใช่ 0)alwaysRestart ตลอดเวลา แม้เราจะสั่ง Stop ไปแล้ว เมื่อเปิดเครื่องใหม่มันก็จะโผล่มาอีกunless-stoppedRestart ตลอดเวลา "ยกเว้น" เราจะสั่งหยุดมันเองก่อนปิดเครื่อง/ปิด Service

3. Named Volume `sqlite_data` ต่างจาก Bind Mount อย่างไร? และทำไมต้องใช้กับ SQLite?

   > _คำตอบ_: ในการจัดการข้อมูลใน Docker ทั้ง Named Volume และ Bind Mount ต่างก็มีหน้าที่เก็บรักษาข้อมูลไม่ให้หายไปเมื่อ Container ถูกลบ แต่มีวิธีจัดการและจุดประสงค์ที่ต่างกันชัดเจนครับ1. ความแตกต่างที่สำคัญคุณสมบัติNamed Volume (sqlite_data)Bind Mount (./data:/app/data)การจัดเก็บDocker เป็นคนจัดการ (อยู่ใน /var/lib/docker/volumes/)เราเป็นคนกำหนด Path เองในเครื่อง (Host Machine)ความสะดวกไม่ต้องกังวลเรื่อง Path ในเครื่อง ย้ายเครื่องง่ายกว่าเข้าถึงไฟล์ได้ง่ายจาก File Explorer/Finder ในเครื่องเราสิทธิ์การเข้าถึงDocker จัดการ Permission ให้เสร็จสรรพมักมีปัญหาเรื่อง Permission ระหว่าง OS เครื่องเรากับ Linux ใน Dockerความสะอาดแยกขาดจากไฟล์โปรเจกต์ ไม่ปนกับ Source Codeปนอยู่กับโฟลเดอร์งานของเรา

---

### 🔵 ขั้นตอนที่ 6: รันและทดสอบระบบ

**วัตถุประสงค์**: เริ่มต้น Monitor และ Debug Application ทั้งหมด

---
**ก่อนการรันทดสอบ ให้ลบ container backend และ frontend ที่สร้างในการทดลองก่อนหน้าออกก่อน**
```
docker rm -f backend frontend
docker network rm booking-network
```

#### 6.1 Build และเริ่ม Services

```bash
# Build Images ทุก Service พร้อมกัน
docker compose build

# Build + เริ่มทุก Service (Detached)
docker compose up -d --build

# ดูสถานะ Service
docker compose ps
```

<details>
<summary>✅ ผลลัพธ์ที่คาดหวัง</summary>

```
NAME                STATUS          PORTS
booking-backend     Up (healthy)    0.0.0.0:5000->5000/tcp
booking-frontend    Up              0.0.0.0:3000->80/tcp
```
</details>

> ⚠️ ครั้งแรกจะใช้เวลานานเพราะต้อง Build `booking-backend` (compile `better-sqlite3`)


---

#### 6.2 Monitor Log

```bash
# ดู Log ทุก Service พร้อมกัน (Ctrl+C เพื่อออก)
docker compose logs -f

# ดู Log เฉพาะ Service
docker compose logs -f backend
docker compose logs -f frontend

# ดู Log 50 บรรทัดล่าสุด
docker compose logs --tail=50 backend
```

<details>
<summary>💡 สิ่งที่ควรเห็นใน Log</summary>

**Backend Log** ที่สำเร็จ:
```
booking-backend  | Server running on port 5000
booking-backend  | SQLite database initialized: /app/data/booking.db
booking-backend  | Database tables created successfully
```

**Frontend Log** ที่สำเร็จ:
```
booking-frontend  | /docker-entrypoint.sh: Configuration complete; ready for start up
booking-frontend  | ... nginx: worker process
```
</details>

---

#### 6.3 ทดสอบ Application

```bash
# ── Test 1: Frontend ─────────────────────────────────────────
curl -I http://localhost:3000
# ควรได้ HTTP/1.1 200 OK

# ── Test 2: Backend Health Check ─────────────────────────────
curl http://localhost:5000/api/health

# ── Test 3: GET All Bookings ──────────────────────────────────
curl http://localhost:5000/api/bookings

# ── Test 6: เปิด Browser ─────────────────────────────────────
# http://localhost:3000
```

```bash
# ── Test 4: POST สร้าง Booking ใหม่ ──────────────────────────
curl -X POST http://localhost:5000/api/bookings -H "Content-Type: application/json" -d '{
    "fullname": "นายทดสอบ ระบบ",
    "email":"test@gmail.com",
    "phone":"0123456789",
    "room": "101",
    "roomtype":"delux",
    "guests":2,
    "checkin": "2025-08-01",
    "checkout": "2025-08-03"
  }'
```

**บันทึกรูปผลการทดลอง**
```
บันทึกรูปที่นี่
```

---

#### 6.4 Debug: ตรวจสอบ Container Network

```bash
# เข้าไปใน Backend Container
docker compose exec backend sh

# ภายใน Backend Container:
# ดู Environment Variables (ทำงานภายใน Alpine Container ไม่ใช่ Windows Shell)
env | grep -E "DB_PATH|PORT|NODE"

# ตรวจสอบว่า SQLite file ถูกสร้างแล้ว
ls -lh /app/data/

# ดูขนาดของ Database file (คำสั่งเหล่านี้รันภายใน Alpine Container)
du -sh /app/data/booking.db

exit
```
---

#### 6.5 ดู Resource Usage

```bash
# ดูการใช้ CPU/Memory ของทุก Container
docker stats

# ดู Network ที่สร้างขึ้น
docker network ls | grep booking

# ดูรายละเอียด Network
docker network inspect booking-network

# ดู IP Address ของแต่ละ Container
docker network inspect booking-network \
  --format='{{range .Containers}}{{.Name}}: {{.IPv4Address}}{{"\n"}}{{end}}'
```

> **📝 บันทึกผลการทดลอง**:
> - IP ของ frontend: `............`
> - IP ของ backend: `............`


---

#### 6.6 Restart และ Scale

```bash
# Restart เฉพาะ Backend
docker compose restart backend

# หยุดเฉพาะ Frontend ชั่วคราว
docker compose stop frontend

# เริ่ม Frontend ใหม่
docker compose start frontend

# ดู Events ทั้งหมด
docker compose events --json 2>/dev/null | head -20
```

---

### ❓ คำถามท้ายขั้นตอนที่ 6

1. `docker compose ps` แสดงสถานะ Service อย่างไร?

   > _คำตอบ_: ข้อมูลที่ docker compose ps แสดง NAME	ชื่อของ Container (มักจะตามด้วยชื่อโปรเจกต์และลำดับตัวเลข)
IMAGE	ชื่อ Image ที่ Service นั้นใช้งานอยู่
COMMAND	คำสั่งหรือสคริปต์ที่รันอยู่ภายใน Container
SERVICE	ชื่อ Service ที่เราตั้งไว้ในไฟล์ docker-compose.yml
STATUS	สถานะปัจจุบัน เช่น running, exited, restarting
PORTS	การเชื่อมต่อ Port ระหว่างเครื่อง Host กับ Container

2. IP Address ของแต่ละ Container ในผลจาก `docker network inspect` คืออะไร?

   > _คำตอบ_: ในผลลัพธ์ของคำสั่ง docker network inspect [network_name] ตัว IP Address ของแต่ละ Container คือที่อยู่เครือข่ายจำลอง (Virtual IP) ที่ Docker ออกให้เพื่อให้ Container สามารถคุยกันเองได้ภายในวง Network นั้นครับ

คุณสามารถหาดูได้ในส่วนของ JSON ที่ระบุว่า "Containers": { ... } ซึ่งจะมีรายละเอียดดังนี้:

ส่วนประกอบสำคัญใน Inspect
ภายใต้หัวข้อ Containers คุณจะเห็นข้อมูลรายตัวดังนี้:

IPv4Address: นี่คือ IP จริงที่ Container ใช้สื่อสาร (เช่น 172.18.0.2/16)

Name: ชื่อของ Container นั้นๆ

EndpointID: รหัสประจำจุดเชื่อมต่อของ Container กับ Network นี้

MacAddress: ที่อยู่ทางกายภาพจำลอง (MAC Address) ของ Interface นั้น

ลักษณะเฉพาะของ IP ใน Docker Network
เป็น Private IP: โดยปกติจะขึ้นต้นด้วย 172.x.x.x ซึ่งเป็นวงภายในเครื่อง Host เท่านั้น โลกภายนอกจะมองไม่เห็น IP นี้โดยตรง (ต้องผ่านการทำ Port Mapping -p)

เปลี่ยนแปลงได้ (Dynamic): หากคุณลบ Container แล้วสร้างใหม่ หรือ Restart เครื่อง IP นี้อาจจะเปลี่ยนไปได้ (ยกเว้นจะกำหนดแบบ Static)

ใช้สื่อสารระหว่างกัน: ถ้า Container A และ B อยู่ใน Network เดียวกัน พวกมันสามารถใช้ IP เหล่านี้คุยกันได้โดยตรง (หรือใช้ชื่อ Container แทนก็ได้ถ้าเป็น User-defined network)

3. SQLite database file (`booking.db`) ถูกสร้างใน Path ใดภายใน Container?

   > _คำตอบ_: เหตุผลและที่มาของ Path นี้:
การกำหนด Working Directory (WORKDIR /app):
คำสั่งนี้ระบุว่าโฟลเดอร์หลักที่แอปทำงานคือ /app

การสร้างโฟลเดอร์ (RUN mkdir -p /app/data):
มีการเตรียมโฟลเดอร์ชื่อ data ไว้ภายใต้ /app เพื่อรอรับไฟล์ Database

การประกาศ Environment Variable (ENV DB_PATH=/app/data/booking.db):
บรรทัดนี้ใน Dockerfile เป็นตัวกำหนด Path เต็ม ที่แอป Node.js ของคุณจะใช้ในการเขียนไฟล์ SQLite ลงไปครับ

---

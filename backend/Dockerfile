FROM node:20-alpine

# ติดตั้ง build tools สำหรับ native module
RUN apk add --no-cache make g++ python3

WORKDIR /app

# Copy package.json ก่อนเพื่อลดเวลา rebuild
COPY package*.json ./
# ตั้ง locale เป็น UTF-8
RUN apk add --no-cache bash tzdata && \
    export LANG=C.UTF-8

# ติดตั้ง dependencies
RUN npm install

# Copy code ที่เหลือ
COPY . .

# Expose port ของ app
EXPOSE 5000

# Run server
CMD ["npm", "start"]
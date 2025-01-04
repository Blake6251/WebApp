const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// 기본 라우트
app.get('/', (req, res) => {
    res.send('Node.js 서버 실행 중!');
});

// Django API 호출
app.get('/django-api', async (req, res) => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/hello/');
        res.json(response.data);
    } catch (error) {
        console.error('Django API 호출 오류:', error);
        res.status(500).send('Django 서버와 연결 실패');
    }
});

const PORT = 3000;
app.listen(PORT, () => console.log(`Node.js 서버가 http://localhost:${PORT}에서 실행 중입니다.`));

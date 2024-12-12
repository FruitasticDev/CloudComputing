const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const authRoutes = require('./routes/auth-routes');

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.use('/auth', authRoutes); 

const port = 8080;
const host = process.env.NODE_ENV !== "production" ? "localhost" : "0.0.0.0"
app.listen(port, () => {
  console.log(`Server is running on http://${host}:${port}`);
});

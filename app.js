const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const authRoutes = require('./routes/auth-routes');

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.use('/auth', authRoutes);  // Menambahkan rute registrasi dan login di /auth

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

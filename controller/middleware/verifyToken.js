const jwt = require('jsonwebtoken');

const verifyToken = (req, res, next) => {
  const token = req.header('Authorization');

  if (!token) {
    return res.status(401).send('Akses ditolak, token tidak ada');
  }

  try {
    const decoded = jwt.verify(token, 'your_secret_key'); 
    req.user = decoded; 
    next();
  } catch (err) {
    res.status(400).send('Token tidak valid');
  }
};

module.exports = verifyToken;

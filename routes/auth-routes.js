const express = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const db = require('../db');
const admin = require('firebase-admin');
const router = express.Router();
const verifyToken = require('../controller/middleware/verifyToken');

const firestore = db.firestore();

router.post('/register', async (req, res) => {
  const { name, email, password, address } = req.body;

 
  const userSnapshot = await firestore.collection('users').where('email', '==', email).get();
  if (!userSnapshot.empty) {
    return res.status(400).send('Email sudah digunakan');
  }


  const hashedPassword = await bcrypt.hash(password, 10);

  // Simpan data pengguna ke Firestore
  const userRef = firestore.collection('users').doc();
  await userRef.set({
    name: name,
    email: email,
    password: hashedPassword,
    address: address,
  });

  res.status(201).json({
    message: 'User successfully registered',
    user: {
      name: name,
      email: email,
      address: address
    }
  });
  
});

router.post('/login', async (req, res) => {
  const { email, password } = req.body;

  try {
      const userSnapshot = await firestore.collection('users').where('email', '==', email).get();
      if (userSnapshot.empty) {
          return res.status(404).send('Email tidak ditemukan');
      }

      const userDoc = userSnapshot.docs[0];
      const user = userDoc.data();

      const isPasswordValid = await bcrypt.compare(password, user.password);
      if (!isPasswordValid) {
          return res.status(401).send('Password salah');
      }

      const token = jwt.sign(
          { userId: userDoc.id },
          'your_secret_key',
          { expiresIn: '1h' }
      );

      res.status(200).json({
          message: 'Login berhasil',
          token: token,
          user: {
              name: user.name,
              email: user.email,
              address: user.address
          }
      });
  } catch (error) {
      console.error('Error during login:', error);
      res.status(500).send('Terjadi kesalahan pada server');
  }
});
  
router.post('/feedback', async (req, res) => {
  const { feedback } = req.body;

  if (!feedback || feedback.trim() === '') {
    return res.status(400).send('Feedback tidak boleh kosong');
  }

  

    res.status(201).json({
      message: 'Feedback berhasil disimpan',
      feedback: feedback
    });
 
});
 
  router.get('/protected', verifyToken, (req, res) => {
    res.status(200).send('Akses berhasil ke endpoint yang dilindungi');
  });
  
module.exports = router;

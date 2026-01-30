const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
require('dotenv').config();

const MONGOURI = process.env.MONGODB_URI;
const User = mongoose.model('User', new mongoose.Schema({
  username: String,
  passwordHash: String
}));

async function addUser() {
  await mongoose.connect(MONGOURI, { useNewUrlParser: true, useUnifiedTopology: true });

  const username = 'palak';
  const password = '12345';
  const passwordHash = await bcrypt.hash(password, 10);

  const existing = await User.findOne({ username });
  if (existing) {
    console.log('⚠️ User already exists');
    process.exit(0);
  }

  await User.create({ username, passwordHash });
  console.log('✅ User added:', username);
  mongoose.disconnect();
}
addUser();

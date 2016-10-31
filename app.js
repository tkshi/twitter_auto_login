var express = require('express');
var app = express();
var cors = require('cors')
import loginTwitter from './webdriver';

app.use(cors());
app.get('/', function (req, res) {
  loginTwitter()
  res.send('処理中');
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});

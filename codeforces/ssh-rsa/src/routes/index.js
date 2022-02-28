var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index');
});

router.get('/submit', function(req, res, next) {
  res.render('submit');
});

router.get('/get', function(req, res, next) {
  res.render('get');
});

router.get('/delete', function(req, res, next) {
  res.render('delete');
});

router.get('/ping', function(req, res, next) {
  res.send("pong");
});

module.exports = router;

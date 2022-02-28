var express = require('express');
var storage = require('../storage/storage')
var Iconv = require('iconv').Iconv;
var router = express.Router();
var repo = new storage('/tmp/repo')



function get_encoded_filename(req) {
  if (!req.query.encoding || !req.query.filename) {
    throw new Error("Missing required query params!") 
  } else {
    iconv = new Iconv('utf8', req.query.encoding);
    filename = iconv.convert(req.query.filename);
    return filename
  }
}

router.get('/', function(req, res, next) {
    try {
      filename = get_encoded_filename(req);
      res.set("Content-Type", "application/octet-stream").send(repo.get(filename));
    } catch (e) {
      res.status(400).send(e.message);
    }    
});

router.put('/', express.raw({type: () => true}), function(req, res, next) {
  try {
    filename = get_encoded_filename(req);
    repo.save(filename, req.body);
    res.send('ok');
  } catch (e) {
    res.status(400).send(e.message);
  }    
});

router.delete('/', function(req, res, next) {
  try {
    filename = get_encoded_filename(req)
    repo.delete(filename)
    res.send('ok');
  } catch (e) {
    res.status(400).send(e.message);
  }
});

module.exports = router;

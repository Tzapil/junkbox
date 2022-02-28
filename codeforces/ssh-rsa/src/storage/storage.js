const fs = require('fs');
const path = require('path');


class Storage {
    constructor(storage_dir) {
        if (!fs.existsSync(storage_dir)) {
            fs.mkdirSync(storage_dir);
        }
        this.dir = storage_dir;
    }

    safePath(filename) {
        return path.resolve(this.dir, Buffer.from(filename).toString('base64'))
    }

    save(filename, content) {
        let p = this.safePath(filename)
        if (fs.existsSync(p)) {
            throw new Error('File ' + filename + ' exists!');
        }
        fs.writeFileSync(p, content)
    }

    get(filename) {
        let p = this.safePath(filename)
        if (!fs.existsSync(p)) {
            throw new Error('File ' + filename + ' does not exist!');
        }
        return fs.readFileSync(p, "binary")
    }

    delete(filename) {
        let p = this.safePath(filename)
        if (!fs.existsSync(p)) {
            throw new Error('File ' + filename + ' does not exist!');
        }
        fs.unlinkSync(p)
    }
  }

module.exports = Storage;
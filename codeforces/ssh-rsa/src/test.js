const fs = require('fs');
const path = require('path');
var Iconv = require('iconv').Iconv;

// Iconv(FROM, TO)

// MAYBE GB18030
const encodings = [
    'EUC-CN', 'HZ', 'GBK', 'CP936', 'GB18030', 'EUC-TW', 'BIG5', 'CP950', 'BIG5-HKSCS',
    'BIG5-HKSCS:2004', 'BIG5-HKSCS:2001', 'BIG5-HKSCS:1999', 'ISO-2022-CN',
    'ISO-2022-CN-EXT', 'BIG5-2003'
];

let name = '../loludied.log';

const original = Buffer.from('flag', 'base64').toString();
console.log(original)

for (let i = 0; i < encodings.length; i++) {
    const CHIN = encodings[i];
    try {
        const iconv11 = new Iconv(CHIN, 'UTF-8');
        name = iconv11.convert(original).toString();
        console.log('=====BAM====', CHIN, name);
    } catch (e) {
        console.log(CHIN, 'ERROR')
    }
}

console.log('HERE')

const TRY_ENC = 'GB18030';

const iconv = new Iconv('utf8', TRY_ENC);
const filename = iconv.convert(name);

console.log('HERE 2')

const path1 = Buffer.from(filename).toString('base64');
const resolve = path.resolve('/tmp/repo', path1);

console.log('name', name);
console.log('filename', filename);
console.log('path', path1);
console.log('resolve', resolve);
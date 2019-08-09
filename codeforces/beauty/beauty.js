var n = +readline();

function calc() {
    if (n < 4) {
        return [];
    }

    var result = [];
    var second = [];
    var first = [];
    var words = {};

    var vowels = /[aoiue]/g;
    function count(str) {
        var r = str.match(vowels);

        return r;
    }


    for (var i = 0; i < n; i++) {
        var input = readline();
        var r = input.match(vowels);
        var count = r.length;
        var last = r[count - 1];

        if (!words[count]) {
            words[count] = {
                array: []
            };
        }

        var hm = words[count];

        if (!hm[last]) {
            hm[last] = [input];
            hm.array.push(input);
        } else {
            var uniq = true;
            for (var j = 0; j < hm[last].length; j++) {
                var v = hm[last][j];
                second.push([input, v]);
                hm[last].splice(j, 1);
                hm.array.splice(hm.array.indexOf(v), 1);
                uniq = false;
                break;
            }

            if (uniq) {
                hm[last].push(input);
                hm.array.push(input);
            }
        }
    }

    for (var vow in words) {
        var arr = words[vow].array;

        for (var j = 0; j < arr.length - 1; j = j + 2) {
            first.push([arr[j], arr[j + 1]]);
        }
    }

    while (second.length >= 1 && (second.length + first.length) > 1) {
        var fp = null;
        if (first.length) {
            fp = first.pop();
        } else {
            fp = second.pop();
        }

        var sp = second.pop();

        result.push(fp[0] + ' ' + sp[0] + '\n' + fp[1] + ' ' + sp[1]);
    }

    return result;
}

var r = calc();
write(r.length);
if (r.length) {
    write('\n');
    write(r.join('\n'));
}
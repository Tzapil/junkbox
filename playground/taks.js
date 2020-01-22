var tree = {
    left: {
        left: {
            v: 'd'
        },
        right: {
            v: 'e'
        },
        v: 'b'
    },
    right: {
        left: {
            v: 'b'
        },
        right: {
            v: 'd'
        },
        v: 'e'
    },
    v: 'a'
};

var aCode = 'a'.charCodeAt(0);

function getCode(char) {
    var shift = char.charCodeAt(0) - aCode
    return 0b1 << shift;
}

function getWeight(descriptor) {
    var result = 0;
    while (descriptor !== 0) {
        result += descriptor & 0b1;
        descriptor = descriptor >> 1;
    }

    return result;
}

function findPair(tree) {
    var max = 0;
    var answer = [];
    var map = {};

    function recursive(node) {
        var dL = 0;
        var dR = 0;
        if (node.left) {
            dL = recursive(node.left);
        }

        if (node.right) {
            dR = recursive(node.right);
        }

        var descriptor = dL | dR | getCode(node.v);

        if (!map[descriptor]) {
            map[descriptor] = [node];
        } else {
            map[descriptor].push(node);
            var w = getWeight(descriptor);
            if (w > max) {
                max = w;
                answer = map[descriptor];
            }
        }

        return descriptor;
    }

    recursive(tree);

    return answer;
}

// console.log(findPair(tree));
// alphabet = a-z

var tree = {
    v: 5,
    left: {
        v: 3,
        left: {
            v: 1,
            right: {
                v: 7
            }
        },
        right: {
            v: 2
        }
    },
    right: {
        v: 7,
        left: {
            v: 4
        },
        right: {
            v: 30,
            right: {
                v: 1
            }
        }
    }
}

function collectAnswer(tree) {
    function normalize(n) {
        return n || 0;
    }

    function recursive(tree) {
        if (!tree) {
            return [];
        }

        var result = [tree.v];
    
        var lA = recursive(tree.left);
        var rA = recursive(tree.right);

        lA.unshift(0);
        rA.unshift(0);

        var len = Math.max(lA.length, rA.length);

        for (var i = 0; i < len; i++) {
            result[i] = normalize(result[i]) + normalize(lA[i]) + normalize(rA[i]);
        }
    
        return result;
    }

    return recursive(tree);
}

function collectAnswer2(tree) {
    function recursive(tree, arr, lvl) {
        if (!tree) {
            return;
        }

        for (var i = 0; i < arr.length; i++) {
            arr[i] += tree.v;
        }

        if (arr.length < lvl) {
            arr.push(tree.v);
        }

        recursive(tree.left, array, lvl + 1);
        recursive(tree.right, array, lvl + 1);
    }

    var array = [];
    recursive(tree, array, 1);

    return array;
}

// [60, 55, 52, 51]
// tree.prepared = collectAnswer2(tree);

// function findAnswer(tree, lvl) {
//     return tree.prepared[lvl - 1] || 0;
// }
// console.log(tree.prepared);
// console.log(findAnswer(tree, 1));
// console.log(findAnswer(tree, 2));
// console.log(findAnswer(tree, 3));
// console.log(findAnswer(tree, 4));

var array = [1,2,3,4,5,6,7,8,9,10];

function findSum(arr, sum) {
    var i = 0;
    var j = 0;

    var s = 0;
    while (j !== arr.length) {
        if (sum === s) {
            return [i, j];
        }

        if (s > sum) {
            s -= arr[i];
            i++;
            continue;
        }

        s += arr[j];

        j++;
    }

    return false;
}

findSum(array, 12);
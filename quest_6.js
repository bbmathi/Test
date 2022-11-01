// Write a JavaScript program to compute the union of two arrays. [5 marks]

// Sample Data : console.log(union([1, 2, 3], [100, 2, 1, 10]));
// Output: [1, 2, 3, 10, 100]

function union(array1,array2)
{
    result = [];
    var obj = {};

    for (var i=0;i<array1.length;i++){
        obj[array1[i]] = true;

    }

    for (var j=0;j<array2.length;j++){
        obj[array2[j]] = true;
    }

    for (const x in obj){
        result.push(Number(x));
    }
    return result;
}

console.log(union([1, 2, 3], [100, 2, 1, 10]))

// [1, 2, 3, 10, 100]
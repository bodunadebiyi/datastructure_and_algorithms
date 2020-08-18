function quickSort(arr) {
    if (arr.length <= 1) return arr;

    const [left, right, pivot] = partition(arr)
    return [...quickSort(left), pivot, ...quickSort(right)]
}

function partition(arr) {
    let size = arr.length
    let pivot = arr[0]
    let left = []
    let right = []
    let counter = 1

    while (counter < size) {
        if (arr[counter] < pivot) {
            left.push(arr[counter])
        } else {
            right.push(arr[counter])
        }
        counter += 1
    }

    return [left, right, pivot]
}


const a = [120, 11, 30, 210, 10002, 1201, 80, 91, 22, 544]
const sorted = quickSort(a)
console.log(sorted, sorted.length)

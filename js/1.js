let name = document.getElementById('id_name')
let btn = document.getElementById('myBtn')


function my_change(e) {
    console.log(e)
}


function my_click(e) {
    name.value = 'Hi world'
    console.log(e)
}

btn.addEventListener('click', my_click)


let divElm = document.getElementById('marka-select');
console.log(divElm);
// let age = 44;
//
// function fun(age) {
//     console.log(age)
//
//     let a = [1, 2, 3, 4]
//
//     for (let i, i < a.length, i++) {
//         console.log(i)
//     }
//     if (age === 55) {
//         let s;
//     }
// }


// fun()
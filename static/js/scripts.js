
//созадние pdf документа из формы клиент
console.log('Yahooo!!!')
    let btn_doc = document.getElementById('btn-doc')
    let form = document.getElementById('doc-form')

function send_print_pdf(e) {
    console.log('Print!!!')
    let data = {
        'name': form.name.value,
        'last_name': form.surname.value
    }
    let csrftoken = form.csrfmiddlewaretoken.value
    let a = window.location.href
    a = a.split('/')
    //console.log(a.last())
    fetch('http://127.0.0.1:8000/client/pdf/39/', {
        method: 'POST',
        headers: {"X-CSRFToken": csrftoken},
        body: JSON.stringify(data)
    })
        .then(res => res.json())
        .then(res => console.log(res))
}



btn_doc.addEventListener('click', send_print_pdf)


//поиск по символам в строке


var arr = ['a','add','audio','remove','adds','classlist','lol','sap','sanek','left','width']
    document.getElementById('search').onkeyup = function(){
        document.getElementById('result').innerHTML = '';
        var l = this.value.length;
        if(l>0){
            for(var i=0;i<arr.length;i++){
                var _ = arr[i].split('').slice(0,l).join('');
                if(_==this.value){
                    document.getElementById('result').innerHTML+='<div class="list">'+arr[i]+'</div>';
                }
            }
        }
    };

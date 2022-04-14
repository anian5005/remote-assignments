function ajax(src, callback) {

    console.log("STEP 1")

    var xhr = new XMLHttpRequest(); // XMLHttpRequest �ΨӻP���A�����s�u�� obj

    console.log("STEP 2") 
    xhr.open('GET', src, true); // �]�w�s�u ���P�B true
    xhr.send(); //�e�X�s�u
    console.log("STEP 3")
    xhr.onload = function () { //onload �� load �ƥ� �Өƥ󬰡u���ƥ����]���H��A�~�|Ĳ�o���ƥ�v
    //console.log(xhr.responseText);
    }
    console.log("STEP 4") //���\�s�u�N callback
    xhr.onreadystatechange = function () {

        if (this.readyState == 4 && this.status == 200) {
            console.log('status 200');
            callback(xhr.response);
        }
        
    }
}

function render(data) {
    const obj = JSON.parse(data);
    var obj_num = obj.length; 

    //console.log(obj[0]) //{name: 'Pixel 3', price: 27700, description: '�̷s�� Google ����C'}
    //console.log(obj[0]['name'])
    //const keys = Object.keys(obj[0]); // �ӫ~���y�z����

    var step;
    var item
    for (step = 0; step < obj_num; step++) { //�M�C�Ҧ��ӫ~ step �ӫ~�ؼ�
        item = obj[step]
        name = 'name: '+ item['name']
        price = 'price: ' + item['price']
        DESC = 'description: ' + item['description']

        var tag_num = 1
        for (const tag of [name, price, DESC,]) {
              
            var newli = document.createElement("li"); // �s�W<li>
            newli.id = 'li_' + step + tag_num // �]�w <li> id = li + 0 +1
            var newContent = document.createTextNode(tag); //�s�W���e
            newli.appendChild(newContent); //�⤺�e�[�J  <li>���e��r</li>

             var currentli = document.getElementById('li_' + step + tag_num - 1) //���e�@�� li
             document.body.insertBefore(newli, currentli); //�[�J html

            var tag_num = tag_num + 1
        }
            
    }
}


ajax("https://appworks-school.github.io/Remote-Aassigiment-Data/products",
    function (response) {
        console.log('callback begin');
        console.log(response);
        render(response);
    }
);
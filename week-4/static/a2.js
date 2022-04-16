function ajax(src, callback) {

    //console.log("STEP 1")

    var xhr = new XMLHttpRequest(); // XMLHttpRequest 用來與伺服器做連線的 obj

    //console.log("STEP 2") 
    xhr.open('GET', src, true); // 設定連線 不同步 true
    xhr.send(); //送出連線

    //console.log("STEP 3")
    xhr.onload = function () { //onload 表 load 事件 該事件為「當資料全部跑完以後，才會觸發此事件」
    //console.log(xhr.responseText);
    }

    //console.log("STEP 4") //成功連線就 callback
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

    //console.log(obj[0]) //{name: 'Pixel 3', price: 27700, description: '最新的 Google 手機。'}
    //console.log(obj[0]['name'])
    //const keys = Object.keys(obj[0]); // 商品之描述項目

    var step;
    var item
    for (step = 0; step < obj_num; step++) { //遍列所有商品 step 商品總數
        item = obj[step]
        name = 'Name :  '+ item['name'] //tag_num =1
        price = 'Price : $  ' + item['price'] //tag_num =2
        DESC = 'Description :  ' + item['description'] //tag_num =3

        var tag_num = 1
        for (const tag of [name, price, DESC,]) {
            console.log("tag_num", tag_num)
            var newli = document.createElement("li"); // 新增<li>
            newli.id = 'li_' + step + tag_num // 設定 <li> id = li + 0 +1
            
            var newContent = document.createTextNode(tag); //新增內容
            newli.appendChild(newContent); //把內容加入  <li>內容文字</li>
            console.log(newli)
            var currentli = document.getElementById('li_' + step + tag_num - 1) //找到前一個 li
            console.log(currentli)
            document.body.insertBefore(newli, currentli); //加入 html
            var tag_num = tag_num + 1
            console.log("---------------------")
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
function makeNumber() {
    word = document.getElementById("num_save").value;
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            alert('計算結果：' + this.responseText);
            document.getElementById("result").innerHTML = xhr.response;
        }
    }
    var url = "http://192.168.50.117:3000/data?number=" + word;
    xhr.open('GET', url, true);
    xhr.send();
}




var xhr = new XMLHttpRequest();
xhr.open('GET', "http://192.168.50.117:3000/data?number=10", true);
xhr.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
        console.log(xhr.response);
    }
}
xhr.send();
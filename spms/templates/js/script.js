Cookie = {
    get: function(name) {
        let cookies = document.cookie.replace(' ','').split(';');        
        for (let index = 0; index < cookies.length; index++) {
            const cookie = cookies[index].split("=");
            if (name == cookie[0]) {
                return cookie[1];
            }
        }
        return null;
    },
    getAll : function(){
        var cookies = new Map();
        for (const value in document.cookie.split(';')) {
            let cookie = document.cookie.split('=');
            cookies.set(cookies[0],cookies[1]);
        }
        return cookies;
    },
    set:function(name, value) {
        document.cookie = name + "=" + value;
    },
    delete: function (name) {
        var exp = new Date();
        exp.setTime(exp.getTime() - 1);
        var value = Cookie.get(name);
        console.log(value)
        if (value != null)
            document.cookie = name + "=" + value + ";expires=" + exp.toGMTString();
    }
}

// Ajax({
//     method:"POST",
//     url:"/login/",
//     async:true,
//     timeout:1000,
//     data:{
        
//     },
//     callback:function(success){

//     },
// })

function Ajax(dictionary){
    var xmlhttp = new XMLHttpRequest();
    
    xmlhttp.timeout = dictionary.async == true ? (dictionary.timeout || 1000) : null;

    xmlhttp.onreadystatechange = function(){
        if (xmlhttp.readyState == 4) {
            if (xmlhttp.status == 200) {
                dictionary.callback(true,xmlhttp.response);
            }else{
                dictionary.callback(false,xmlhttp.status);
            }
        }
    }
    xmlhttp.open(dictionary.method,dictionary.url,dictionary.async);
    var data = new FormData();
    for (const key in dictionary.data || {}) {
        data.append(key,dictionary.data[key])
    }
    xmlhttp.send(data);
}


function show(...list){
    for (const i of list) {
        document.getElementById(i).style.display = "inline";
    }
}

function hide(...list){
    for (const i of list) {
        document.getElementById(i).style.display = "none";
    }
}
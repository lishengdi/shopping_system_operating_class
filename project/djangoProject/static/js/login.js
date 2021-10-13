    var pwd =document.getElementById("password");
    var flag =0;
    var uname=document.getElementById("username");
    var result=document.getElementById("result");


    function check(){
       if(uname.value==="" || pwd.value===""){
            result.innerText="用户名或密码为空"
           return false
        }
       else{
           return true
       }

    }
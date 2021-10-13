
var pwd =document.getElementById("password");
var flag =0;
var uname=document.getElementById("username");
var result=document.getElementById("result");
var btn=document.getElementById("submit");

btn.onclick= function(){
    if(uname.value==="" || pwd.value===""){
        alert("用户名或密码为空");
    }
}
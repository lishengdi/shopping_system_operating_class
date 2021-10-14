var username =document.getElementById("username");
var phone =document.getElementById("phone");
var password =document.getElementById("password");
var password_2nd=document.getElementById("password_2nd");
var add=document.getElementById("address");
var result=document.getElementById("result");


function check(){
    console.log("tel",typeof (phone.value))
    if(username.value.length>20|| username.value.length<4 ){

        alert("用户名格式错误：请输入4-20位用户名")
        return false
    }
    if((phone.value.length<11 || phone.value.length>15)){
            alert("手机号码格式错误：请输入有效手机号码")
            return false
        }

    var myreg = /^(((13[0-9]{1})|159|153)+\d{8})$/;
        if(!myreg.test(phone.value)){
             alert("手机号码格式错误：请输入有效手机号码")
            return false
        }

    if( password.value.length>20||password.value.length<6 ){
        alert("密码格式错误：请输入6-20位密码")
        return false
    }


    if(password.value!==password_2nd.value){
            alert("两次输入密码不一致，请更正后重新输入")
            return false
        }
        return true
}
function loginUser(){
    $.ajax({
            type:"POST",
            url :"/login-user/",
            data:"title=ajax call",
            datatype:"json",
            error:function(data){alert('Error:'+data);}
            success:function(data){alert('OK!'+data.message+','+data.code);}
          });
        }
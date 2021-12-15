import { authApi } from './api/auth.js';

document.getElementById("login_button").onclick = () => auth.login();

class auth {
    static login() {
        const email    = document.getElementById("email").value;
        const password = document.getElementById("password").value;
        
        const data = {  email, password  };
        authApi.login(data, auth.login_success, auth.login_faild);    
    }

    static login_success(res) {
        console.log(res.data.token);
        document.cookie = `service_token= ${ res.data.token };`;
        location.href = '/';
    }

    static login_faild(err) {
        alert("Login Faild, Plase Try Again.")
        document.getElementById("email").value    = '';
        document.getElementById("password").value = '';
    }
}



const data = {
    'name'    : '阿麵',
    'email'   : 'amian@gmail.com',
    'phone'   : '123456789',
    'birthday': '1999/06/07',
    'password': '12345'
};


import { authApi } from './api/auth.js';

document.getElementById("signup_button").onclick = () => auth.signup();

class auth {
    static signup() {
        const email    = document.getElementById("email").value;
        const password = document.getElementById("password").value;
        const name     = document.getElementById("name").value;
        const phone    = document.getElementById("phone").value;
        const birthday = document.getElementById("birthday").value;
        
        const data = {  email, password, name, phone, birthday  };
        authApi.signup(data, auth.signup_success, auth.signup_faild);    
    }

    static signup_success(res) {
        location.href = '/login';
    }

    static signup_faild(err) {
        alert("signup Faild, Plase Try Again.")
        document.getElementById("email").value          = '';
        document.getElementById("password").value       = '';
        document.getElementById("name").value           = '';
        document.getElementById("phone").value          = '';
        document.getElementById("birthday").value       = '';
        document.getElementById("password_again").value = '';
    }
}



const data = {
    'name'    : '阿麵',
    'email'   : 'amian@gmail.com',
    'phone'   : '123456789',
    'birthday': '1999/06/07',
    'password': '12345'
};


import { getJwtToken } from './utils.js';
import { userApi }     from './api/user.js';
import { index }       from './index.js';

window.onload = () => {
    member.checkLogined();
};

export class member {
    static checkLogined() {
        const jwtToken = getJwtToken('service_token');
        userApi.info(jwtToken, member.checkLoginedSuccess, member.checkLoginedFaild);
    }

    static checkLoginedSuccess(res) {
        console.log(res);
        index.checkLoginedSuccess(res);
        document.getElementById("email").value      = res.data.email;
        document.getElementById("name").value       = res.data.name;
        document.getElementById("phone").value      = res.data.phone;
        document.getElementById("birthday").value   = res.data.birthday;
        document.getElementById("subscribed").value = 'True';
        document.getElementById("admin").value      = res.data.admin;
    }

    static checkLoginedFaild(err) {
        index.checkLoginedFaild(err);
        location.href = '/login';
    }
}
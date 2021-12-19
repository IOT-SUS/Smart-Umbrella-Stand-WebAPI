import { getJwtToken } from './utils.js';
import { userApi }     from './api/user.js';

window.onload = () => {
    member.checkLogined();
};

class member {
    static checkLogined() {
        const jwtToken = getJwtToken('service_token');
        userApi.info(jwtToken, member.checkLoginedSuccess, member.checkLoginedFaild);
    }

    static checkLoginedSuccess(res) {
        console.log(res);
        document.getElementById("email").value      = res.data.email;
        document.getElementById("name").value       = res.data.name;
        document.getElementById("phone").value      = res.data.phone;
        document.getElementById("birthday").value   = res.data.birthday;
        document.getElementById("subscribed").value = 'True';
        document.getElementById("admin").value      = res.data.admin;
    }

    static checkLoginedFaild(err) {
        location.href = '/login';
    } 
}

/* ============================================================================ */
/* "                           TRYING TO LOG OUT                              " */
/* ============================================================================ */ 

document.getElementById("logout_button").onclick = () => logout.deleteAllCookies();

class logout {
    static deleteAllCookies() {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i];
            var eqPos = cookie.indexOf("=");
            var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
            document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
        }
        window.location.href='/';
    }
}


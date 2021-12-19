import { getJwtToken } from './utils.js';
import { userApi }     from './api/user.js';

window.onload = () => {
    index.checkLogined();
};

export class index {
    static checkLogined() {
        const jwtToken = getJwtToken('service_token');
        userApi.info(jwtToken, index.checkLoginedSuccess, index.checkLoginedFaild);
    }

    static checkLoginedSuccess(res) {
        document.getElementById("rent_item").style.display   = "block"
        document.getElementById("member_item").style.display = "block"
        document.getElementById("member_item").childNodes[0].innerHTML = res.data.email;
    }

    static checkLoginedFaild(err) {
        document.getElementById("rent_item").style.display   = "none"
        document.getElementById("member_item").style.display = "none"
    }
}
import { getJwtToken } from './utils.js';
import { userApi }     from './api/user.js';
import { deviceApi }   from './api/device.js';

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

/* ============================================================================ */
/* "                      TRYING TO DRAW A GOOGLE MAP                         " */
/* ============================================================================ */ 

export class device {
    static checkInfos() {
        // testing...
        deviceApi.infos(device.checkInfosSuccess, device.checkInfosFaild);
        console.log(map);
    
    }

    static checkInfosSuccess(res) {
        res.data.forEach(data => {
            let latLng = new google.maps.LatLng(parseFloat(data.embedded_code[0]), parseFloat(data.embedded_code[1])); 
            let marker = new google.maps.Marker({
                position: latLng,
                icon: 'https://images.plurk.com/1JbrGWSGZlyNYFcMykIdRS.png',
                animation: google.maps.Animation.DROP,
                draggable: false,
                map: map
            });
        });
        
    }

    static checkInfosFaild(err) {
        // location.href = '/login';
        console.log(err);
    }
}

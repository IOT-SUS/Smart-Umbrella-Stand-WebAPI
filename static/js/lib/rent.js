import { getJwtToken } from './utils.js';
import { deviceApi }   from './api/device.js';
import { index }       from './index.js';

// window.onload = () => {
//     index.checkLogined();
//     rent.checkInfos();
// };

var nextButton = document.getElementById("btn_next");
nextButton.onclick = () => {
    document.getElementById("formDevice").style.display = "none";
    document.getElementById("formRent").style.display = "block";  
    index.checkLogined();
    rent.checkInfos();
}

export class rent {
    static checkInfos() {
        // testing...
        const device_id = document.getElementById("input_device_id").value;
        console.log(device_id);
        //deviceApi.infos(rent.checkInfosSuccess, rent.checkInfosFailed);
        deviceApi.info(device_id, rent.checkInfosSuccess, rent.checkInfosFailed);

        // const data = {
        //     'location'      : ':D',
        //     'embedded_code' : ['123', '456']
        // };

        // deviceApi.add(data, rent.checkInfosSuccess, rent.checkInfosFaild);
        // deviceApi.delete('e6fe9df5', rent.checkInfosSuccess, rent.checkInfosFaild);
    }

    static checkInfosSuccess(res) {
        console.log(res);
        index.checkLoginedSuccess(res);
        document.getElementById("device_id").value  = res.data.public_id;
        document.getElementById("location").value   = res.data.location;
        document.getElementById("amount").value     = res.data.amount;
        if (res.data.amount == 0) {
            alert("Oops! There is no umbrella available here now. Click the confirm button and go back to our Home Page.")
            location.href = '/';
        }
    }

    static checkInfosFailed(err) {
        // location.href = '/login';
        console.log(err);
    }
}

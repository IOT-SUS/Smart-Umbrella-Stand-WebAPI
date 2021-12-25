import { getJwtToken } from './utils.js';
import { deviceApi }   from './api/device.js';
import { rentApi }     from './api/rent.js';

var nextButton = document.getElementById("btn_next");
nextButton.onclick = () => {
    const device_id = document.getElementById("input_device_id").value;
    rentAvailableCheck.checkInfos(device_id);
}

var rentButton = document.getElementById("btn_rent");
rentButton.onclick = () => {
    const device_id = document.getElementById("input_device_id").value;
    rent.rentStart(device_id);
}

export class rentAvailableCheck {
    static checkInfos(device_id) {
        console.log(device_id);
        //deviceApi.infos(rent.checkInfosSuccess, rent.checkInfosFailed);
        deviceApi.info(device_id, rentAvailableCheck.checkInfosSuccess, rentAvailableCheck.checkInfosFailed);
    }

    static checkInfosSuccess(res) {
        console.log(res);
        if (res.data.amount == 0) {
            alert("Oops! There is no umbrella available here now. Click the confirm button and go back to our Home Page.")
            location.href = '/';
        }
        document.getElementById("formDevice").style.display = "none";
        document.getElementById("formRent").style.display   = "block";
        document.getElementById("device_id").value  = res.data.public_id;
        document.getElementById("location").value   = res.data.location;
        document.getElementById("amount").value     = res.data.amount;
    }

    static checkInfosFailed(err) {
        alert("Oops! Wrong device id. Click the confirm button and go back to our Rent Page.")
        location.href = '/rent';
        console.log(err);
    }
}

var checkRentTimer = null;

export class rent {
    // Rent
    static rentStart(device_id) {
        rentApi.rent(device_id, rent.rentStartSuccess, rent.rentStartFaild);
    }

    static rentStartSuccess(res) {
        console.log(res);
        document.getElementById("divBuffer").style.display = "block";
        document.getElementById("divLoading").style.display = "block";
        document.getElementById("btn_rent").style.display = "none";
        
        const rrs_id = res.data.public_id;
        
        checkRentTimer = setInterval(() => rent.checkRentFinish(rrs_id), 500);
        // clearInterval(checkRentTimer);
    }

    static rentStartFaild(err) {
        console.log(err);
    }

    // RRS
    static checkRentFinish(rrs_id) {
        rentApi.getRRS(rrs_id, rent.checkRentFinishSuccess, rent.checkRentFinishFaild);
    }

    static checkRentFinishSuccess(res) {
        const expire_date = new Date(res.data.expire_time);
        const now_date    = Date.now()
        const status = res.data.status;
        console.log(status);
        if(status == 'S1') {
            // rent success
            document.getElementById("formRent").style.display   = "none";
            document.getElementById("formSuccess").style.display = "block";
            clearInterval(checkRentTimer);
        }
        if(now_date > expire_date) {
            // rent faild
            document.getElementById("formRent").style.display   = "none";
            document.getElementById("formFail").style.display = "block";
            clearInterval(checkRentTimer);
        }
    }

    static checkRentFinishFaild(err) {
        console.log(err);
        clearInterval(checkRentTimer);
    }
    
    // Polling
    static polling() {
        const jwtToken = getJwtToken('service_token');
        rentApi.polling(jwtToken, rent.pollingSuccess, rent.pollingFaild);
    }

    static pollingSuccess(res) {
        console.log(res)
        const device_id = res.data.device_id;
        rentAvailableCheck.checkInfos(device_id);
        rent.rentStartSuccess(res);
    }

    static pollingFaild(err) {
        console.log(err)
    }
}
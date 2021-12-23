import { deviceApi }   from './api/device.js';

var nextButton = document.getElementById("btn_next");
nextButton.onclick = () => {
    document.getElementById("formDevice").style.display = "none";
    document.getElementById("formRent").style.display   = "block";
    rent.checkInfos();
}

var rentButton = document.getElementById("btn_rent");
rentButton.onclick = () => {
    document.getElementById("divBuffer").style.display = "block";
    document.getElementById("divLoading").style.display = "block";
    document.getElementById("btn_rent").style.display = "none";
}

// 這裡的觸發我暫時都用緩衝按鈕，緩衝圖會切到租借失敗，緩衝文字會切到租借成功

var tmpButton = document.getElementById("divBuffer");
tmpButton.onclick = () => {
    document.getElementById("formRent").style.display   = "none";
    document.getElementById("formFail").style.display = "block";
}

var tmpButton = document.getElementById("divLoading");
tmpButton.onclick = () => {
    document.getElementById("formRent").style.display   = "none";
    document.getElementById("formSuccess").style.display = "block";
}

export class rent {
    static checkInfos() {
        const device_id = document.getElementById("input_device_id").value;
        console.log(device_id);
        //deviceApi.infos(rent.checkInfosSuccess, rent.checkInfosFailed);
        deviceApi.info(device_id, rent.checkInfosSuccess, rent.checkInfosFailed);
    }

    static checkInfosSuccess(res) {
        console.log(res);
        document.getElementById("device_id").value  = res.data.public_id;
        document.getElementById("location").value   = res.data.location;
        document.getElementById("amount").value     = res.data.amount;
        if (res.data.amount == 0) {
            alert("Oops! There is no umbrella available here now. Click the confirm button and go back to our Home Page.")
            location.href = '/';
        }
    }

    static checkInfosFailed(err) {
        alert("Oops! Wrong device id. Click the confirm button and go back to our Rent Page.")
        location.href = '/rent';
        console.log(err);
    }
}

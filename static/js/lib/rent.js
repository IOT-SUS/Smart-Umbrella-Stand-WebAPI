import { getJwtToken } from './utils.js';
import { deviceApi }   from './api/device.js';
import { index }       from './index.js';

window.onload = () => {
    index.checkLogined();
    rent.checkInfos();
};

export class rent {
    static checkInfos() {
        //testing...
        deviceApi.infos(rent.checkInfosSuccess, rent.checkInfosFaild);
        deviceApi.info('1742a5c2', rent.checkInfosSuccess, rent.checkInfosFaild);
        
    }

    static checkInfosSuccess(res) {
        console.log(res);
    }

    static checkInfosFaild(err) {
        // location.href = '/login';
        console.log(err);
    }
}
const BASE_URL = '/api'

export class deviceApi {
    static infos(func, efunc) {
        axios({
            method : 'get',
            url    : BASE_URL + '/devices',
        }).then(res => func(res.data)).catch(err => efunc(err));
    }

    static info(device_id, func, efunc) {
        axios({
            method : 'get',
            url    : BASE_URL + `/device/${ device_id }`,
        }).then(res => func(res.data)).catch(err => efunc(err));
    }
};
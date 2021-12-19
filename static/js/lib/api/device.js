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

    static add(data, func, efunc) {
        axios({
            method : 'post',
            url    : BASE_URL + '/device/add',
            data,
        }).then(res => func(res.data)).catch(err => efunc(err));
    }

    static update(device_id, data, func, efunc) {
        axios({
            method : 'post',
            url    : BASE_URL + `/device/update/${ device_id }`,
            data,
        }).then(res => func(res.data)).catch(err => efunc(err));
    }

    static delete(device_id, func, efunc) {
        axios({
            method : 'post',
            url    : BASE_URL + `/device/delete/${ device_id }`,
        }).then(res => func(res.data)).catch(err => efunc(err));
    }
};
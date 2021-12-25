const BASE_URL = '/api'

export class rentApi {
    static getRecords(token, func, efunc) {
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        axios.defaults.headers.post['Authorization']   = `Bearer ${token}`;
        axios({
            method : 'get',
            url    : BASE_URL + '/rent/records',
        }).then(res => func(res.data)).catch(err => efunc(err));
    }

    static getRRS(rrs_id, func, efunc) {
        axios({
            method : 'get',
            url    : BASE_URL + `/rrs/${ rrs_id }`,
        }).then(res => func(res.data)).catch(err => efunc(err));
    }

    static rent(device_id, func, efunc) {
        axios({
            method : 'post',
            url    : BASE_URL + `/rent/${ device_id }`,
        }).then(res => func(res.data)).catch(err => efunc(err));
    }

    static polling(token, func, efunc) {
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        axios.defaults.headers.post['Authorization']   = `Bearer ${token}`;
        axios({
            method : 'get',
            url    : BASE_URL + `/rrs/polling/action/0/user`,
        }).then(res => func(res.data)).catch(err => efunc(err));
    }
};
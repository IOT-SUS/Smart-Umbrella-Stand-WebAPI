const BASE_URL = 'http://127.0.0.1:5000/api'

export class authApi {
    static login(data, func, efunc) {
        axios({
            method : 'post',
            url    : BASE_URL + '/auth/login',
            data,
        }).then(res => func(res.data)).catch(err => efunc(err));
    }

    static signup(data, func, efunc) {
        axios({
            method : 'post',
            url    : BASE_URL + '/auth/signup',
            data,
        }).then(res => func(res.data)).catch(err => efunc(err));
    }
};
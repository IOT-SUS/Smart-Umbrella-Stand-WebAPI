const BASE_URL = '/api'

export class userApi {
    static info(token, func, efunc) {
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        axios.defaults.headers.post['Authorization']   = `Bearer ${token}`;
        axios({
            method : 'get',
            url    : BASE_URL + '/user',
        }).then(res => func(res.data)).catch(err => efunc(err));
    }
};
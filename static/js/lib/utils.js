export function getJwtToken(cname) {
    const cookies = document.cookie.split(';');
    let bearer = '';
    cookies.forEach((cookie) => {
        var data = cookie.split('=');
        if (data.length > 1) {
            var k = data[0];
            var v = data[1];
            if (k.trim() === cname) bearer = v.trim();
        }
    });
    return bearer;
}

// const jwtToken = getCookie('service_token');

// axios.defaults.headers.common['Authorization'] = `Bearer ${jwtToken}`;
// axios.defaults.headers.post['Authorization']   = `Bearer ${jwtToken}`;
// axios.interceptors.response.use(
//     response => response,
//     error => {
//         const { status } = error.response;
//         console.log(status);
//         if (status === 401) {
//             alert('驗證失敗，請重新登入');
//             logout();
//         }
//         return Promise.reject(error);
//     }
// );

// async function logout() {
//     window.location = "/login";
// }
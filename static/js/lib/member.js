import { getJwtToken } from './utils.js';
import { userApi }     from './api/user.js';
import { rentApi }     from './api/rent.js';
import { index }       from './index.js';

export class member {
    static checkLogined() {
        const jwtToken = getJwtToken('service_token');
        userApi.info(jwtToken, member.checkLoginedSuccess, member.checkLoginedFaild);
        rentApi.getRecords(jwtToken, member.checkTableSuccess, member.checkTableFaild);
    }

    static checkLoginedSuccess(res) {
        console.log(res);
        index.checkLoginedSuccess(res);
        document.getElementById("email").value      = res.data.email;
        document.getElementById("name").value       = res.data.name;
        document.getElementById("phone").value      = res.data.phone;
        document.getElementById("birthday").value   = res.data.birthday;
        document.getElementById("subscribed").value = 'True';
        document.getElementById("admin").value      = res.data.admin;
        
    }

    static checkLoginedFaild(err) {
        index.checkLoginedFaild(err);
        location.href = '/login';
    }

    static checkTableSuccess(res) {
        console.log(res);
        document.getElementById("number").value      = res.data.records.length;
            $('#myRecordTable').bootstrapTable({
                columns:[ 
                    {field:'checkbox', title:'checkbox', align:'center', width:40, visible:true, checkbox:true},
                    {field:'rent_device_id', title:'Rent Device', align:'center', width:120, visible:true},
                    {field:'rent_time', title:'Rent Time', align:'center', width:120, visible:true},
                    {field:'return_device_id', title:'Return Device', align:'center', width:120, visible:true},
                    {field:'return_time', title:'Return Time', align:'center', width:120, visible:true}
                  ],
                  data : getMyData(),
                  search : true //查詢

            })

            function getMyData() {
                var mydata = [];
                for (var i = 0; i < res.data.records.length; i++) {
                  mydata.push({
                    rent_device_id: res.data.records[i].rent_device_id,
                    rent_time: res.data.records[i].rent_time,
                    return_device_id:res.data.records[i].return_device_id,
                    return_time: res.data.records[i].return_time
                  });
                }
                return mydata;
              }


    }

    static checkTableFaild(err) {
        console.log("FAIL")
    }
}
/* ============================================================================ */
/* "                           TRYING TO LOG OUT                              " */
/* ============================================================================ */ 

document.getElementById("logout_button").onclick = () => logout.deleteAllCookies();

class logout {
    static deleteAllCookies() {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i];
            var eqPos = cookie.indexOf("=");
            var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
            document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
        }
        window.location.href='/';
    }
}



var recordButton = document.getElementById("btn_record");
recordButton.onclick = () => {
    document.getElementById("memberFirstPage").style.display = "none";
    document.getElementById("formMember").style.display = "none";
    document.getElementById("recordTable").style.display = "block";
}




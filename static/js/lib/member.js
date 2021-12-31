import { getJwtToken }   from './utils.js';
import { userApi }       from './api/user.js';
import { index }         from './index.js';
import { umbrellaTable } from './umbrella.js';
import { deviceApi }     from './api/device.js';

export class member {
    static checkLogined() {
        const jwtToken = getJwtToken('service_token');
        userApi.info(jwtToken, member.checkLoginedSuccess, member.checkLoginedFaild);
        umbrellaTable.get();
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

var recordButton = document.getElementById("btn_device");
recordButton.onclick = () => {
    document.getElementById("memberFirstPage").style.display = "none";
    document.getElementById("formMember").style.display = "none";
    document.getElementById("recordTable").style.display = "none";
    document.getElementById("deviceTable").style.display = "block";
    deviceDetailTable.get()
}


// device details

export class deviceDetailTable{
    static get() {
        deviceApi.infos(deviceDetailTable.checkTableSuccess, deviceDetailTable.checkTableFaild);
    }

    static update() {
        deviceApi.infos(deviceDetailTable.updateTable, deviceDetailTable.checkTableFaild);
    }

    static updateTable(res) {
        $('#deviceDetailTable').bootstrapTable('load',  getMyData())
        function getMyData() {
            var mydata = [];
            
            for (var i = 0; i < res.data.length; i++) {
                var status_updated = new Date(res.data[i].status_updated_at);
                var now_date       = Date.now()
                var time_diff      = diff_minutes(now_date, status_updated)
                
                mydata.push({
                    device_id : res.data[i].public_id,
                    ip        : res.data[i].status[0],
                    wifi      : res.data[i].status[1],
                    running   : (time_diff < 0.1) ? '● Running'  : 'Stop'
                });
            }
            return mydata;
        }
    }
    
    static checkTableSuccess(res) {
        console.log(res);
        $('#deviceDetailTable').bootstrapTable({
            columns:[ 
                {field:'checkbox'   , title:'checkbox'   , align:'center', width:40, visible:true, checkbox:true},
                {field:'running'    , title:'Status'     , align:'center', width:120, visible:true, cellStyle:(value, row, index)=>deviceDetailTable.cellStyle(value, row, index)},
                {field:'device_id'  , title:'Device ID'  , align:'center', width:80, visible:true},
                {field:'ip'         , title:'IP Adress'  , align:'center', width:120, visible:true},
                {field:'wifi'       , title:'Wifi'       , align:'center', width:80, visible:true},
                ],
                data : getMyData(),
                search : true //查詢
        });
        function getMyData() {
            var mydata = [];
            
            for (var i = 0; i < res.data.length; i++) {
                var status_updated = new Date(res.data[i].status_updated_at);
                var now_date       = Date.now()
                var time_diff      = diff_minutes(now_date, status_updated)
                
                mydata.push({
                    device_id : res.data[i].public_id,
                    ip        : res.data[i].status[0],
                    wifi      : res.data[i].status[1],
                    running   : (time_diff < 0.1) ? '● Running'  : 'Stop'
                });
            }
            return mydata;
        }
        checkDeviceTimer = setInterval(() => deviceDetailTable.update(), 500);
    }

    static checkTableFaild(err) {
        console.log(err);
        console.log("FAIL")
    }

    static cellStyle(value, row, index) {

        if (value == "● Running") {
            return {
                css: {
                    color: 'rgb(57, 230, 0)'
                  }
            }
        }
        return {
          css: {
            color: 'gray'
          }
        }
          
    }
}

function diff_minutes(dt2, dt1) 
{

  var diff =(dt2 - dt1) / 1000;
  diff /= 60;
  return Math.abs(diff);
  
}
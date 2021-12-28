import { getJwtToken } from './utils.js';
import { rentApi }     from './api/rent.js';

export class umbrellaTable{
    static get(){
        const jwtToken = getJwtToken('service_token');
        rentApi.getRecords(jwtToken, umbrellaTable.checkTableSuccess, umbrellaTable.checkTableFaild);
    }
    static checkTableSuccess(res) {
        console.log(res);
        var length = res.data.records.length;
        var laststatus = res.data.records[length-1].return_time;
        console.log(laststatus);
        if (laststatus == null){
            // document.getElementById("status").style.display = "block";
            document.getElementById("renting_item").style.display = "block";
            document.getElementById("renting_icon").style.display = "block";
            document.getElementById("brand_item").style.display = "none";
        }
        document.getElementById("number").value = length;
            $('#myRecordTable').bootstrapTable({
                columns:[ 
                    {field:'checkbox', title:'checkbox', align:'center', width:40, visible:true, checkbox:true},
                    {field:'rent_device_id', title:'Rent Device', align:'center', width:80, visible:true},
                    {field:'rent_time', title:'Rent Time', align:'center', width:120, visible:true},
                    {field:'return_device_id', title:'Return Device', align:'center', width:80, visible:true},
                    {field:'return_time', title:'Return Time', align:'center', width:120, visible:true}
                  ],
                  data : getMyData(),
                  search : true //查詢

            })

            function getMyData() {
                var mydata = [];
                
                for (var i = 0; i < res.data.records.length; i++) {
                    var rent_date = new Date(res.data.records[i].rent_time);
                    var return_date = new Date(res.data.records[i].return_time);
                    
                    if (res.data.records[i].return_time==null){
                        mydata.push({
                            rent_device_id: res.data.records[i].rent_device_id,
                            // rent_time: res.data.records[i].rent_time,
                            rent_time: rent_date.toLocaleString('zh-TW'),
                            return_device_id:res.data.records[i].return_device_id,
                            return_time: '-'
                            // return_time: res.data.records[i].return_time
                          });
                    }

                    else mydata.push({
                    rent_device_id: res.data.records[i].rent_device_id,
                    // rent_time: res.data.records[i].rent_time,
                    rent_time: rent_date.toLocaleString('zh-TW'),
                    return_device_id:res.data.records[i].return_device_id,
                    return_time: return_date.toLocaleString('zh-TW')
                    // return_time: res.data.records[i].return_time
                  });
                }
                return mydata;
              }


    }

    static checkTableFaild(err) {
        console.log(err);
        console.log("FAIL")
    }
}

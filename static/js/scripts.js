/*!
* Start Bootstrap - Full Width Pics v5.0.4 (https://startbootstrap.com/template/full-width-pics)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-full-width-pics/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


// function functionNext() {
//     document.getElementById("formDevice").style.display = "none";
//     document.getElementById("formRent").style.display = "block";  
// }


/* ============================================================================ */
/* "                      TRYING TO DRAW A GOOGLE MAP                         " */
/* ============================================================================ */ 


var map;
function initMap() {

  let location = {
      lat: 25.018597, // 經度
      lng: 121.534225 // 緯度
  };
  map = new google.maps.Map(document.getElementById('map'), {
    center: location,// 我設在本部跟分部的中間 [25.018597,121.534225]
    zoom: 15,
  });

  // 本部分部分別的經緯度去查看 map.geojson 檔案

    fetch('http://127.0.0.1:5000/static/js/map.geojson')
    .then(results => results.json())
    .then(result => {
      let res = result.features;
      Array.prototype.forEach.call(res, r => {
        let latLng = new google.maps.LatLng(r.geometry.coordinates[0], r.geometry.coordinates[1]);
        let marker = new google.maps.Marker({
          position: latLng,
          icon: 'https://images.plurk.com/1JbrGWSGZlyNYFcMykIdRS.png',
          animation: google.maps.Animation.DROP,
          draggable: false,
          map: this.map
        });
      });
  });

/* ============================================================================ */
/* "                         POINT OUT SINGLE MARKER                          " */
/* ============================================================================ */     
  
  // let marker = new google.maps.Marker({
  //     position: location,
  //     icon: 'https://images.plurk.com/1JbrGWSGZlyNYFcMykIdRS.png',
  //     animation: google.maps.Animation.DROP,
  //     draggable: false,
  //     map: this.map 
  //   });

}
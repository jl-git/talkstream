function initMap() {
  $.getJSON( "_data/alltalks.json", function( json ) {
    // read all data into universities
    var universities = load_target(json);

    // init a new map with init coord center and zoom level
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 4,
      center: {lat: 35.477371, lng: -96.523195}
    });

    // put markers on the map
    setMarkers(map, universities);
  });
}

// load information read from the json
function load_target(json) {
    // hard coded universities lat and long...
    var u_location = {
    'University of Arizona' : [32.231899, -110.950921],
    'Cornell University' : [42.446834, -76.480093],
    'Columbia University' : [40.807544, -73.962562],
    'Harvard University': [42.376971, -71.116660],
    'Stanford University': [37.427500, -122.169601],
    'Brown University': [41.826852, -71.402591],
    'University of California, Berkeley': [37.871642, -122.258638],
    'Carnegie Mellon University': [40.444285, -79.944287],
    'University of Washington': [47.654902, -122.303498],
    'UIUC': [40.102666, -88.227215],
  };

    var universities = {};

    // loop through all seminar records in the json file
    for (i = 0; i < json['records'].length; i++) {
      // if the university's coord is in the u_location
      if (u_location.hasOwnProperty(json['records'][i]['University'])) {

        // append the seminar information to the univeristies's entry after its other seminars
        if (universities.hasOwnProperty(json['records'][i]['University'])) {
          universities[json['records'][i]['University']][3] = universities[json['records'][i]['University']][3].concat("<br>" + json['records'][i]['Time'] + " " + json['records'][i]['Topic']);
          universities[json['records'][i]['University']][4] = universities[json['records'][i]['University']][4]  + 1;

        // if the university appears first time, then create a new entry and put lat, long and
        // other information need to be put into infowindow
        } else {
          universities[json['records'][i]['University']] = [ u_location[json['records'][i]['University']][0], u_location[json['records'][i]['University']][1], 1, json['records'][i]['Time'] + " " + json['records'][i]['Topic'], 1];
        }
      }
    }
  return universities;
}

function setMarkers(map, universities) {
  // load the marker pic
  var image = {
    url: 'images/cap.png',
    // This marker is 20 pixels wide by 32 pixels high.
    size: new google.maps.Size(48, 48),
    // The origin for this image is (0, 0).
    origin: new google.maps.Point(0, 0),
    // The anchor for this image is the base of the flagpole at (0, 32).
    anchor: new google.maps.Point(24, 24)
  };

  // def the clickable area of the marker
  var shape = {
    coords: [10,0,30],
    type: 'circle'
  };

  // loop through the universities
  for (var university in universities) {
    // init the infowindow
    infowindow = new google.maps.InfoWindow();
    // init the marker
    marker = new google.maps.Marker({
      position: {lat: universities[university][0], lng: universities[university][1]},
      map: map,
      icon: image,
      shape: shape,
      title: university,
      zIndex: universities[university][2],
    });

    // generate the content need to be put into the infowindow
    var content = university + ' (' + universities[university][4] + ')<hr>' + universities[university][3];
    
    // add a click listener to the marker that will open the infowindow
    google.maps.event.addListener(marker,'click', (function(marker,content,infowindow){ 
        return function() {
            infowindow.setContent(content);
            infowindow.open(map,marker);
        };
    })(marker,content,infowindow));  
  }
}

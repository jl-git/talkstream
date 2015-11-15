var app = angular.module('myVis', []);

app.controller('wordcloudCtrl', function($scope, $http) {
  $http.get("_data/alltalks.json")
  .success(
    function(response) {
      $scope.speakers = response.speakers;
      $scope.talks = response.records;
      $scope.init();
    });


    $scope.initAllSpeakers = function(entri) {
      if ($scope.allspeakers.indexOf(entri) < 0) {
        $scope.allspeakers.push(entri); 
      }
    };

    $scope.updateWC = function() {
      $scope.drawWC($scope.getWordlist($scope.wcSpeaker));
    };


    $scope.drawWC = function(wordlist) {
      var fill = d3.scale.category20();

      d3.layout.cloud().size([800, 400])
        .words(wordlist.map(function(d) {
          return {text: d, size: 10 + Math.random() * 50};
        }))
        .rotate(function() { return 0; })
        .font("Impact")
        .fontSize(function(d) { return d.size; })
        .on("end", draw)
        .start();

      function draw(words) {
      // delete last word cloud
      d3.select("#wordcloud svg").html("")  
      d3.select("#wordcloud svg")

        .append("g")
          .attr("transform", "translate(400,200)")
        .selectAll("text")
          .data(words)
        .enter().append("text")
          .style("font-size", function(d) { return d.size + "px"; })
          .style("font-family", "Impact")
          .style("fill", function(d, i) { return fill(i); })
          .attr("text-anchor", "middle")
          .attr("transform", function(d) {
            return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
          })
          .text(function(d) { return d.text; });
      }
    }

    $scope.getWordlist = function(speaker) {
      $scope.corpus = "";

      angular.forEach($scope.talks, function(value, key) {
        if (value.Speaker == speaker) {
          $scope.corpus += (value.Description);

        }
      });

      var result = $scope.corpus.split(" ");
      var filter_result = [];

      angular.forEach(result, function(value, key) {
        console.log(key);
        if (value.length >= 3) {
           filter_result.push(value);
        }
      });

      return filter_result;
    }

    $scope.init = function() {
      $scope.wcSpeaker = $scope.speakers[0].Name;
      $scope.updateWC($scope.wcSpeaker);
    }
});

app.controller('pieCtrl', function($scope, $http) {
  $http.get("_data/topic_counts.json")
  .success(
    function(response) {
      $scope.topic_counts = response.records;
      $scope.topic_labels = response.labels;
      $scope.cur_month = "1900-01"
      $scope.pie_index = 0;
      $scope.init();

    });

    $scope.init = function() {
      var svg = d3.select(".piegraph")
        .append("svg")
        .append("g")

      svg.append("g")
        .attr("class", "slices");
      svg.append("g")
        .attr("class", "labels");
      svg.append("g")
        .attr("class", "lines");

      var width = 800,
          height = 500,
        radius = Math.min(width, height) / 2;

      var pie = d3.layout.pie()
        .sort(null)
        .value(function(d) {
          return d.value;
        });

      var arc = d3.svg.arc()
        .outerRadius(radius * 0.8)
        .innerRadius(radius * 0.4);

      var outerArc = d3.svg.arc()
        .innerRadius(radius * 0.9)
        .outerRadius(radius * 0.9);

      svg.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

      var key = function(d){ return d.data.label; };
      var color = d3.scale.category20()
        .domain($scope.topic_labels)

      function refreshData (){
        if ($scope.pie_index >= $scope.topic_counts.length) {
          $scope.pie_index = 0;
        } else if ($scope.pie_index < 0) {
          $scope.pie_index = $scope.topic_counts.length - 1;
        }

        $scope.cur_month = $scope.topic_counts[$scope.pie_index]['Date'];
        $scope.$apply();

        var labels = color.domain();
        return labels.map(function(label){

          return { label: label, value: $scope.topic_counts[$scope.pie_index][label] }
        });
      }

      change(refreshData());

      d3.select(".next")
        .on("click", function(){
          $scope.pie_index=$scope.pie_index-1;
          change(refreshData());
        });

      d3.select(".prev")
        .on("click", function(){
          $scope.pie_index=$scope.pie_index+1;
          change(refreshData());
        });

      function mergeWithFirstEqualZero(first, second){
        var secondSet = d3.set(); second.forEach(function(d) { secondSet.add(d.label); });

        var onlyFirst = first
          .filter(function(d){ return !secondSet.has(d.label) })
          .map(function(d) { return {label: d.label, value: 0}; });
        return d3.merge([ second, onlyFirst ])
          .sort(function(a,b) {
            return d3.ascending(a.label, b.label);
          });
      }

      function change(data) {
        var duration = 150;
        var data0 = svg.select(".slices").selectAll("path.slice")
          .data().map(function(d) { return d.data });
        if (data0.length == 0) data0 = data;
        var was = mergeWithFirstEqualZero(data, data0);
        var is = mergeWithFirstEqualZero(data0, data);

        /* ------- SLICE ARCS -------*/

        var slice = svg.select(".slices").selectAll("path.slice")
          .data(pie(was), key);

        slice.enter()
          .insert("path")
          .attr("class", "slice")
          .style("fill", function(d) { return color(d.data.label); })
          .each(function(d) {
            this._current = d;
          });

        slice = svg.select(".slices").selectAll("path.slice")
          .data(pie(is), key);

        slice   
          .transition().duration(duration)
          .attrTween("d", function(d) {
            var interpolate = d3.interpolate(this._current, d);
            var _this = this;
            return function(t) {
              _this._current = interpolate(t);
              return arc(_this._current);
            };
          });

        slice = svg.select(".slices").selectAll("path.slice")
          .data(pie(data), key);

        slice
          .exit().transition().delay(duration).duration(0)
          .remove();

        /* ------- TEXT LABELS -------*/

        var text = svg.select(".labels").selectAll("text")
          .data(pie(was), key);

        text.enter()
          .append("text")
          .attr("dy", ".35em")
          .style("opacity", 0)
          .text(function(d) {
            return d.data.label;
          })
          .each(function(d) {
            this._current = d;
          });
        
        function midAngle(d){
          return d.startAngle + (d.endAngle - d.startAngle)/2;
        }

        text = svg.select(".labels").selectAll("text")
          .data(pie(is), key);

        text.transition().duration(duration)
          .style("opacity", function(d) {
            return d.data.value == 0 ? 0 : 1;
          })
          .attrTween("transform", function(d) {
            var interpolate = d3.interpolate(this._current, d);
            var _this = this;
            return function(t) {
              var d2 = interpolate(t);
              _this._current = d2;
              var pos = outerArc.centroid(d2);
              pos[0] = radius * (midAngle(d2) < Math.PI ? 1 : -1);
              return "translate("+ pos +")";
            };
          })
          .styleTween("text-anchor", function(d){
            var interpolate = d3.interpolate(this._current, d);
            return function(t) {
              var d2 = interpolate(t);
              return midAngle(d2) < Math.PI ? "start":"end";
            };
          });
        
        text = svg.select(".labels").selectAll("text")
          .data(pie(data), key);

        text
          .exit().transition().delay(duration)
          .remove();

        /* ------- SLICE TO TEXT POLYLINES -------*/

        var polyline = svg.select(".lines").selectAll("polyline")
          .data(pie(was), key);
        
        polyline.enter()
          .append("polyline")
          .style("opacity", 0)
          .each(function(d) {
            this._current = d;
          });

        polyline = svg.select(".lines").selectAll("polyline")
          .data(pie(is), key);
        
        polyline.transition().duration(duration)
          .style("opacity", function(d) {
            return d.data.value == 0 ? 0 : .5;
          })
          .attrTween("points", function(d){
            this._current = this._current;
            var interpolate = d3.interpolate(this._current, d);
            var _this = this;
            return function(t) {
              var d2 = interpolate(t);
              _this._current = d2;
              var pos = outerArc.centroid(d2);
              pos[0] = radius * 0.95 * (midAngle(d2) < Math.PI ? 1 : -1);
              return [arc.centroid(d2), outerArc.centroid(d2), pos];
            };      
          });
        
        polyline = svg.select(".lines").selectAll("polyline")
          .data(pie(data), key);
        
        polyline
          .exit().transition().delay(duration)
          .remove();
      };
    }
});


var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 750 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .ticks(12);

var svg = d3.select(".barchart").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.tsv("_data/month_total.tsv", type, function(error, data) {
  if (error) throw error;

  x.domain(data.map(function(d) { return d.month; }));
  y.domain([0, d3.max(data, function(d) { return d.count; })]);

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Count");

  svg.selectAll(".bar")
      .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.month); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.count); })
      .attr("height", function(d) { return height - y(d.count); });
});

function type(d) {
  d.count = +d.count;
  return d;
}

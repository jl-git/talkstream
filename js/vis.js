var app = angular.module('myVis', []);

//
// Word Cloud
//
app.controller('wordcloudCtrl', function($scope, $http) {
  $http.get("_data/alltalks.json")
  .success(
    function(response) {
      // read data from alltalks.json
      $scope.speakers = response.speakers;
      $scope.talks = response.records;
      $scope.init();
    });

    // add all unique speakers
    $scope.initAllSpeakers = function(entri) {
      if ($scope.allspeakers.indexOf(entri) < 0) {
        $scope.allspeakers.push(entri); 
      }
    };

    // this function will first call getWordlist by the speaker user selected
    // (from the dropdown menu), then pass the wordlist to drawWC to
    // update/redraw the word cloud
    $scope.updateWC = function() {
      $scope.drawWC($scope.getWordlist($scope.wcSpeaker));
    };

    // draw the word cloud with the wordlist
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

    // construct wordlist for the speaker
    $scope.getWordlist = function(speaker) {
      $scope.corpus = "";

      // concat the speaker's all seminar description/abstract to a
      // corpus
      angular.forEach($scope.talks, function(value, key) {
        if (value.Speaker == speaker) {
          $scope.corpus += (value.Description);

        }
      });

      // a stop word list contains common meaningless English words
      var stopwords = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "want", "wants","when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "wanted", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"];

      var result = $scope.corpus.split(" ");
      var filter_result = [];

      angular.forEach(result, function(value, key) {
        value = value.toLowerCase().trim();

        // remove non-alphabet char at the front
        while ((value.length > 0) && (value[0] < 'a' || value[0] > 'z')) {
          value = value.substring(1, value.length);
        }

        // remove non-alphabet char at the tail
        while ((value.length > 0) && (value[value.length - 1] < 'a' || value[value.length - 1] > 'z')) {
          value = value.substring(0, value.length - 1);
        }

        if (value.length >= 3) {
          // remove stop words
          if (stopwords.indexOf(value.trim()) < 0) {
            filter_result.push(value.toUpperCase());
          }
        }

      });

      return filter_result;
    }

    $scope.init = function() {
      $scope.wcSpeaker = $scope.speakers[0].Name;
      $scope.updateWC();
    }
});

//
// Pie/Donut Graph
//
app.controller('pieCtrl', function($scope, $http) {
  $http.get("_data/topic_counts.json")
  .success(
    function(response) {
      $scope.topic_counts = response.records;
      $scope.topic_labels = response.labels;
      // the month displayed in the title
      $scope.cur_month = "1900-01"
      // index indicate the current position of records
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

      // read labels as key
      var key = function(d){ return d.data.label; };
      var color = d3.scale.category20()
        .domain($scope.topic_labels)

      // return the new data need to be draw
      function refreshData (){
        // check if pie_index out of bound
        if ($scope.pie_index >= $scope.topic_counts.length) {
          $scope.pie_index = 0;
        } else if ($scope.pie_index < 0) {
          $scope.pie_index = $scope.topic_counts.length - 1;
        }

        // read the current month from the first position of an entry ('Date')
        $scope.cur_month = $scope.topic_counts[$scope.pie_index]['Date'];
        // force angular.js to change the month displayed in the title
        $scope.$apply();

        // return the new data of the new pie_index
        var labels = color.domain();
        return labels.map(function(label){
          return { label: label, value: $scope.topic_counts[$scope.pie_index][label] }
        });
      }

      // repaint the graph with animation in change
      change(refreshData());

      // when click the two buttons
      d3.select(".next")
        .on("click", function(){
          // decrement the index
          $scope.pie_index=$scope.pie_index-1;
          // repaint with the data of new pie_index
          change(refreshData());
        });

      d3.select(".prev")
        .on("click", function(){
          // increment
          $scope.pie_index=$scope.pie_index+1;
          // repaint
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

      // repaint and animate with new data
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

//
// Bar Chart Generation
//
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

// read the tsv file
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

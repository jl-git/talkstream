var app = angular.module('sscApp', []);

app.controller('homepageCtrl', function($scope, $http) {
	$http.get("_data/alltalks.json")
	.success(
		function(response) {
			// after get the alltalks.json
			$scope.talks = response.records;
			$scope.printIndex = 0;
		}
		);

		// init function
		$scope.init = function() {
			$scope.showallentries = true;
			$scope.filterstring = [];
			$scope.alltags = [];
			$scope.allspeakers = [];
		};

		// put all unique tags into the array
		$scope.initAllTags = function(entri) {
			for (var i = 0; i < entri.length; i++) {
				if ($scope.alltags.indexOf(entri[i]) < 0) {
					$scope.alltags.push(entri[i]);
				}
			}
		};

		// put all unique speakers into the array
		$scope.initAllSpeakers = function(entri) {
			if ($scope.allspeakers.indexOf(entri) < 0) {
				$scope.allspeakers.push(entri);	
			}
		};

		// clean the filter which will displayed all seminars
		$scope.showall = function(){
			$scope.filterstring = [];
			$scope.showallentries = true;
		};

		// add a new filter to the filterstring
		$scope.addfilter =function(tag) {
			if ($scope.filterstring.indexOf(tag) < 0) {
				$scope.filterstring.push(tag);
			}
			$scope.showallentries = false;
			// clean the text in the search text box
			$scope.searchWord = null;
			$scope.searchword_speaker = null;
		};

		// remove a new filter from the filterstring
		$scope.removefilter =function(tag) {
			var index = $scope.filterstring.indexOf(tag);

			if (index > -1) {
				$scope.filterstring.splice(index, 1);
			}

			// if no filter, then need to display all seminars
			if ($scope.filterstring.length == 0) {
				$scope.showallentries = true;
				$scope.filterstring = [];
			}
		};

		// judge if patern is a substring of target, case insensitive
		$scope.containSearchWord = function(target, pattern) {
			if (pattern == undefined)
				return true;

			target = target.toLowerCase();
			pattern = pattern.toLowerCase();

			target = target.trim();
			pattern = pattern.trim();
			if (target.indexOf(pattern) > -1)
				return true;
			else
				return false;
		}

		// determine a item should be displayed or not based on the tags and speaker, and the filterstring
		// if filterstring is a subset of (tags U speaker), which means the item satisfied the search criteria,
		// then it should return true. Otherwise, return false.
		$scope.displayflag = function(tags, speaker) {
			for (var i = 0; i < $scope.filterstring.length; i++) {
				if ($scope.filterstring[i] === undefined)
					continue;
				if (tags.indexOf($scope.filterstring[i]) < 0 && speaker.indexOf($scope.filterstring[i])) {
					return false;
				}
			}
			
			return true;
		};
	}
);

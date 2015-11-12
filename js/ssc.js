var app = angular.module('myapp', []);

app.controller('customersCtrl', function($scope, $http) {
	$http.get("_data/alltalks.json")
	.success(
		function(response) {
			$scope.names = response.records;
		}
		);

		$scope.init = function() {
			$scope.showallentries = true;
			$scope.filterstring = [];
			$scope.alltags = [];
			$scope.allspeakers = [];
		};

		$scope.initAllTags = function(entri) {
			for (var i = 0; i < entri.length; i++) {
				if ($scope.alltags.indexOf(entri[i]) < 0) {
					$scope.alltags.push(entri[i]);
				}
			}
		};

		$scope.initAllSpeakers = function(entri) {
			if ($scope.allspeakers.indexOf(entri) < 0) {
				$scope.allspeakers.push(entri);	
			}
		};

		$scope.showall = function(){
			$scope.filterstring = [];
			$scope.showallentries = true;
		};

		$scope.addfilter =function(tag) {
			if ($scope.filterstring.indexOf(tag) < 0) {
				$scope.filterstring.push(tag);
			}
			$scope.showallentries = false;
			$scope.searchWord = null;

			console.log($scope.filterstring);
		};

		$scope.removefilter =function(tag) {
			var index = $scope.filterstring.indexOf(tag);

			if (index > -1) {
				$scope.filterstring.splice(index, 1);
			}

			if ($scope.filterstring.length == 0) {
				$scope.showallentries = true;
				$scope.filterstring = [];
			}
		};

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

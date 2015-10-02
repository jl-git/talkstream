var app = angular.module('myapp', []);

app.controller('customersCtrl', ['$scope', '$http', function($scope, $http) {
    $http.get("http://localhost/talkstream/_data/alltalks.json")
    .success(
    	function(response) {
    		$scope.names = response.records;
    	}
    	);
	}
]
);


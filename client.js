var app = angular.module("uasApp", []);
var count = 0;

// Video Controller
getFrame = app.controller("videoCtrl",
    function($scope, $http, $interval) {
        $interval(function() {
            if ($scope.isConnected) {
                var img;

                // Design Request
                var request = {
                    method: "GET",
                    url: "http://127.0.0.1:5000/get_image/" + count.toString()
                }

                // Send Request
                $http(request).then(
                    // Success
                    function(response) {
                        $scope.imgUrl = "http://127.0.0.1:5000/get_image/" + count.toString();
                    },
                    // Failure
                    function(response) {
                        $scope.imgUrl = "http://127.0.0.1:5000/get_image/" + count.toString();
                    }
                );
                count = count + 1;
            }
        }, 100);
    }
);

app.controller("testCtrl",
    function($scope, $http) {
        $scope.test_connection = function() {
            var request = {
                method: "GET",
                url: "http://127.0.0.1:5000/test_connection/"
            }

            $http(request).then(
                // Success
                function(response) {
                    alert("Connection Test Passed")
                },
                function(response) {
                    alert("Connection Test Failed")
                }
            );
        };
    }
)

var app = angular.module("uasApp", []);
var count = 0;
var host = "http://127.0.0.1:5000/"

// Video Controller
getFrame = app.controller("videoCtrl",
    function($scope, $http, $interval) {
        $interval(function() {
            if ($scope.isConnected) {
                var img;

                // Design Request
                var request = {
                    method: "GET",
                    url: host + "get_image/" + count.toString(),
                    headers: {"Access-Control-Allow-Origin" : "*"}
                }

                // Send Request
                $http(request).then(
                    // Success
                    function(response) {
                        alert(angular.toJson(response.headers()["img-id"]))
                        $scope.imgUrl = host + "get_image/" + count.toString();
                        $scope.cpuTemp = response.headers()["cpu-temp"]
                        $scope.cpuFreq = response.headers()["cpu-freq"]
                    },
                    // Failure
                    function(response) {
                        //$scope.imgUrl = host + "get_image/" + count.toString();
                    }
                );
                count = count + 1;
            }
        }, 200);
    }
);

app.controller("testCtrl",
    function($scope, $http) {
        $scope.test_connection = function() {
            var request = {
                method: "GET",
                url: host + "test_connection/",
                headers: {"Access-Control-Allow-Origin" : "*"}
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

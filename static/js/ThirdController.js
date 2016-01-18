angular.module('myApp').controller('ThirdController',['$scope','$http',function($scope,$http) {

$scope.addd = function() {
	
        data= {
        id:$scope.id,
	author : $scope.author,
	body:$scope.body,
	title:$scope.title
};
   var url="http://127.0.0.1:8000/post/";
    id = $scope.id;
    $http.put(url+id+"/",data).success( function(response){
      $scope.hello = response;

    }).error(function(data, status, headers, config) {
      alert("ERROR " + status + ": " + data);
    });
}

}]);

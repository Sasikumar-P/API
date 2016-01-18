angular.module('myApp').controller('FourController',['$scope','$http',function($scope,$http) {

$scope.adddd = function() {
	
        data= {
        id:$scope.id,
	
};
   var url="http://127.0.0.1:8000/post/";
    id = $scope.id;
    $http.delete(url+id+"/",data).success( function(response){
      $scope.hello = response;

    }).error(function(data, status, headers, config) {
      alert("ERROR " + status + ": " + data);
    });
}

}]);

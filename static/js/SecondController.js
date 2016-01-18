angular.module('myApp').controller('SecondController',['$scope','$http',function($scope,$http) {

$scope.add = function() {
	
        data= {
	author : $scope.author,
	body:$scope.body,
	title:$scope.title
};
   var url="http://127.0.0.1:8000/post/";
    $http.post(url,data).success( function(response){
      $scope.hello = response;

    });
}

}]);

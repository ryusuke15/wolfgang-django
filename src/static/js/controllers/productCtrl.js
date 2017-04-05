app = angular.module('productCtrl', []);

app.controller('productController',function(Products,$stateParams,$scope) {

    id = $stateParams.id;
//Get a single product//    

    Products.detail(id)
        .success(function(data){
            $scope.product = data;
        });
 
});

app = angular.module('shopCtrl', []);

app.controller('shopController',function(Products,$scope) {

//List All Products//
    $scope.style = "display:none"

    Products.all()
        .success(function(data){
            if (Object.keys(data).length == 0) {
                $scope.style="display:block !important;";
                $scope.products = data;
            }else{
                $scope.products = data;
            };
        });
 
});

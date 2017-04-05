app = angular.module('shopCtrl', []);

app.controller('shopController',function(Products, $anchorScroll, $location, $scope) {

    $scope.style = "display:none"

//Scroll back to individual products
    if ($location.hash()){
        $location.hash()
        $anchorScroll()
    } 

//List All Products//
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

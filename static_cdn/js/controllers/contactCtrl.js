app = angular.module('contactCtrl', []);

app.controller('contactController',function(Contacts,$scope) {

//Create a contact//
    $scope.formData = {};
    
    $scope.style = "display:none"

    $scope.submit = function(userForm){
        Contacts.create($scope.formData)
            .success(function(data){
                $scope.formData = {};
                $scope.style="display:block";
           });
        };
});
